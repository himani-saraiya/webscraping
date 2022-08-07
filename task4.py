from bs4 import BeautifulSoup
import requests
import json
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
# print(url)

def movie_details(movie_url):
    res=requests.get(movie_url)
    # print(res)
    soup = BeautifulSoup(res.text,"html.parser")
    # print(soup) 
    h1=soup.find("h1", class_="scoreboard__title").get_text()
    # print(h1)
    li=soup.find_all("li",class_="meta-row clearfix")
    # print(li)
    dic={}
    dic["Name"]=h1
    # print(dic)
    for k in li:
        # print(k)
        f=k.text
        # print(f)
        b=f.split()
        # print(b)
        if "Rating:" in b:
            dic["Rating"]=b[1]
            # print(dic)
        
        elif "Genre:" in b:
            k=b[1:]
            g=" "
            for i in k:
                g+=i
            g=g.strip()
            g=g.split(",")
            # print(g)
            
            dic["Genre"]=g
            # print(dic)
        elif "Language:" in b:
            dic['Language']=b[2]
            # print(dic)
        elif "Director:" in b:
            w=b[1:]
            # print(w)
            h=" "
            i=0
            while i<len(w):
                # print(w[i])
                h=h+w[i]
                # print(h)
                i+=1
            l=h.split(",")
            # print(l)
            k=" "
            r={}
            l1=[]
            for i in l:
                # print(i)
                str1=""
                for j in i:
                    if j!=k:
                        str1+=j
                        # print(str1)
                l1.append(str1)
                # print(l1)
            dic["Director"]=l1
            # print(dic)
        elif "Producer:" in b:
            dic["Producer"]=b[1:]
            # print(dic)
        elif "Runtime:" in b:
            s=b[1:]
            # print(s)
            for i in s:
                # print(i)
                if "h" in i:
                    first=int(i[0:-1])*60
                    # print(first)
                elif "m" in i:
                    sec=int(i[:-1])
                    # print(sec)
            dic["Runtime"]=first+sec
            # print(dic)
    with open("task4.json","w+") as file:
        json.dump(dic,file,indent = 4)
        b=json.dumps(dic)
    return dic
print(movie_details(url))