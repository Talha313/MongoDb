import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests

item_list=[]
def getCntent(url):
  url = ("https://www.sotostore.com/en/6/footwear?orderBy=Published")
  response = requests.get(url)
  html = response.content
  soup = BeautifulSoup(html, "html.parser")
  main_cards = soup.find_all("div", attrs={"class": "card"})
  link = "https://www.sotostore.com"
  for card in main_cards:
    # print(card.prettify())
    product_page1 = card.find("a", {"class": "card-image-link"})['href']
    product_page = link + product_page1
    img1 = link + card.find("img", attrs={"class": "card-img"})['data-src']
    h4_brand = str(card.find("h4", attrs={"class": "card-brand"}).text)
    h4_title = str(card.find("h4", attrs={"class": "card-title"}).text)
    active_price = str(card.find("span", attrs={"class": "active-price"}).text)
    original_price = str(card.find("del", attrs={"class": "original-price"}).text)

    # img = card.find("img", src=re.compile("^(/images/)"))
    # img1=img_link+img.get('src')
    item_dic = {}
    item_dic['product_page'] = product_page
    item_dic['img'] = img1
    item_dic['brand'] = h4_brand.strip()
    item_dic['title'] = h4_title.strip()
    item_dic['active_price'] = active_price.strip()
    item_dic['original_price'] = original_price.strip()
    if item_dic not in item_list:
      item_list.append(item_dic)
    # print(item_dic)
  # print(item_list)



def create_database(client):
    mydb=client["mydatabase"]
    return mydb

# create table
# def create_collection(mydb):
#
#     collection=mydb["store"]

def insert(collection,item_list):

  x=collection.insert_many(item_list)
  print(x.inserted_ids)


def find(collection):

  result=collection.find({},{"_id":0})
  for x in result:
    print(x)

def update(collection, values):

    where_query={'brand': 'Nike'}
    newvalues = {"$set": values}

    collection.update_many(where_query, newvalues)

def delete_record(collection):
  query={'brand': 'GulAhmad'}
  collection.delete_many(query)

def drop_collection(collection):
  collection.drop()


if __name__ == '__main__':
  # connection
    client = MongoClient("mongodb://localhost:27017/")
    # print(client)

    # create database

    mydb=create_database(client)
    # print(mydb.list_collection_names())

    # crate collection/table
    collection = mydb["store"]
    # print(collection)

    url = ("https://www.sotostore.com/en/6/footwear?orderBy=Published")
    getCntent(url)

    # insert(collection, item_list)

    # values={"brand": "GulAhmad"}
    # update(collection, values)

    # delete_record(collection)

    drop_collection(collection)

    find(collection)




