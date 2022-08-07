from task1 import movie_data
from task4 import dict_data
from task5 import get_movie_details_list
import json
# with open("task1.json","r") as b:
#    movies= json.load(b)
# analyse_language_and_directors=get_movie_details_list()
def analyse_language_and_directors(movies):
    dic={}
    director_list=[]
    for i in movies:
        print(i)
        if "Director" in i:
            m=i["Director"]
            for director in m:
                if director not in director_list:
                    director_list.append(director)
    dic={}
    for director in director_list:
        d={}
        for i in movies:
            if director in i["Director"]:
                if "Language" in i:
                    for j in i["Language"]:
                        if j in d:
                            d[j]=d[j]+1                        
                        if j not in d:
                            d[j]=1
        dic[director]=d
        with open("task10.json","w") as a:
            json.dump(dic,a,indent=4)
analyse_language_and_directors(get_movie_details_list)