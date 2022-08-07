import json
from task1 import movie_data
from task4 import movie_details
# all_movie=movie_data()
with open("task1.json","r")as file:
    data=json.load(file)# top_movies=all_movie[:10]
    # print(data)
def get_movie_details_list():
    list1=[]
    for i in data:
        # print(i)
        k=i["moviceurl"]
        # print(k)
        a=movie_details(k)
        # print(a)
        list1.append(a)
        print(list1)

    with open("task5.json","w") as file:
        json.dump(list1,file,indent = 4)
    # file.close()
    return list1
get_movie_details_list()