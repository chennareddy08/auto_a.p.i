import requests, json

#r = requests.get('https://stage.handstandapp.com/api/gymlocations')
r1 = requests.post("http://httpbin.org/post")
r2= requests.put("http://httpbin.org/put")
r3=requests.delete("http://httpbin.org/delete")
r4= requests.head("http://httpbin.org/get")
r5= requests.options("http://httpbin.org/get")
# print(r.status_code)
# print r.content
#
# data = r.json()
data1=r1.json()
data2=r2.json()
data3=r3.json()

# print(type(data))
# print(data)
# print(r.headers)
# print(r.headers["content-type"])
# print(data["number"])
# print(data)
print (data1)

print(data2)
print (data3)
print (r4)
print (r5)