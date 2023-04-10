import requests
import json

url = "http://127.0.0.1:8080/attendance/student_api/"
'''
j1 = {"id":2}

json_data = json.dumps(j1)
r=requests.get(url=url, data=json_data)
print(r)
print(r.json())
'''

def postdata1():
	data = {"stuid":37, "stuname":"maheshbabu", "stumail":"babu@abc.com"}
	json_data = json.dumps(data)
	r = requests.post(url=url, data=json_data)
	data = r.json()
	print(data)


def putdata1():
	#data = {"stuid":556, "stuname":"rajababu", "stumail":"babu@gmail.com"}
	data = {"stuid":556, "stuname":"rajaji"}
	json_data = json.dumps(data)
	r = requests.put(url=url, data=json_data)
	data = r.json()
	print(data)


def deletedata1():
	data = {"stuid":555}
	json_data = json.dumps(data)
	r = requests.delete(url=url, data=json_data)
	data = r.json()
	print(data)


putdata1()


