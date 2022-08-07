import json
from bs4 import BeautifulSoup
from task5 import get_movies_details_list

director=get_movies_details_list()
def analyse_movies_directors():
    d={}
    for i in director:
        # print(i)
        dir_name=i["Director"]
        # print(dir_name)
        for j in dir_name:
            if j not in d:
                dir_name=j
                d[j]=1
            else:
                d[j]+=1
    print(d)
    with open("task7.json","w+") as file7:
        json.dump(d,file7,indent=4)
        return d
analyse_movies_directors()