import pymongo
from pymongo import MongoClient
# from pymongo import Connection
if __name__ == '__main__':

    client=pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=client["mydatabase"]
    print(client)
    db_list=client.list_database_names()
    print(db_list)

    table=mydb["customer"]

    list=[
        {'name':'talha', 'father':'mobin'},
        {'name': 'talha1', 'father': 'mobin1'}
    ]

    # x=table.find_one()
    # print(x)
    # table.drop()

    # table.insert_many(list)
    # first=table.find_one()
    # print(first)

    # query={"name": "talha1"}
    #
    # result=table.find(query)
    # for x in result:
    #     print(x)


    # x=table.find({},{"name":0})
    # for y in x:
    #     print(y)
    # if("mydatabase" in db_list):
    #     print("data base exites")
    # else:
    #     print("not found")
