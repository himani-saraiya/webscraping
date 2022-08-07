import json
from task1 import movie_data
data1=open("task1.json")
movie=json.load(data1)
def group(movie):
    dic1={}
    for index in movie:
        list=[]
        year=index["Year"]
        if year not in dic1:
            for k in movie:
                if year==k["Year"]:
                    list.append(k)
                    dic1[year]=list
            with open("task2.json","w+") as file:
                json.dump(dic1,file,indent=4)
                a=json.dumps(dic1)
year1=group(movie_data)