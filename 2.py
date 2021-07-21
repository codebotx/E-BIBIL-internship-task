import requests
import json
l=[]
for i in range(1,6):
	response = requests.get(("https://jsonplaceholder.typicode.com/todos/"+str(i)))
	data=response.json()
	l.append(data['title'])
print(l)