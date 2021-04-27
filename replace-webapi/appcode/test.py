import requests
BASE = "http://127.0.0.1:5000/"

data = [
        {"name": "rest api","likes": 1000,"views": 22},
        {"name": "demo api","likes": 1001,"views": 32},
        {"name": "test api","likes": 1002,"views": 42}
        ]

for i in range(len(data)):
    #response = requests.get(BASE + "replace/Microsoft")
    response = requests.put(BASE + "video/"+ str(i), data[i])
    print(response.json())

#response = requests.delete(BASE + "video/0")
#print(response)
input()

response = requests.patch(BASE + "video/2",{"views": 99,"likes":11})
print(response.json())
response = requests.get(BASE + "video/2")
print(response.json())
