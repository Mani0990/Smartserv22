import requests
import json
response_API = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
print(response_API.status_code)
data = response_API.text
parse_json=json.loads(data)
parse_json_ordered=json.dumps(parse_json,indent=4)
#print(parse_json_ordered)
prod_list=[]
#print(parse_json["products"].keys())
indices=parse_json["products"].keys()

for i in indices:
    subcategory=parse_json["products"][str(i)]["subcategory"]
    title=parse_json["products"][str(i)]["title"]
    price=parse_json["products"][str(i)]["price"]
    popularity=parse_json["products"][str(i)]["popularity"]
    lst1=[subcategory,title,price,popularity]
    prod_list.append(lst1)
print("subcategory"+" "*3,"title"+" "*20,"price"+" "*8,"popularity")
for i in prod_list:
    print(i[0]+" "*8+i[1]+" "*8+i[2]+" "*8+i[3])
