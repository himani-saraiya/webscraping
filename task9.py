import os
import json
import time
import random
import requests
with open("task5.json","r+") as file:
    a=json.load(file)
def fun():
    b=random.randint(1,3)
    for i in a:
        path="/home/admin123/Desktop/task9/task99"+i["Name"]+".json"
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w")
            json.dump(i,create,indent=4)
        time.sleep(b)
fun()