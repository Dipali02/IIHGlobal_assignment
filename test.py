import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPONIT='student/'

def get_resource(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    resp=requests.get(BASE_URL+ENDPONIT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource()

# def create_resource():
#     new_stud={
#     'name':'Ram',
#     'email':'ram78@yahoo.com',
#     'dob':'2001-01-05',
#     'profile_pic': None,
#     'fees':10000
#     }
#     resp=requests.post(BASE_URL+ENDPONIT,data=json.dumps(new_stud))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
#
# def update_resource(id):
#     new_stud={
#     'id':id,
#     'fees':'7000',
#     }
#     resp=requests.put(BASE_URL+ENDPONIT,data=json.dumps(new_stud))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(2)
#
# def delete_resource(id):
#     data={
#     'id':id,
#     }
#     resp=requests.delete(BASE_URL+ENDPONIT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(2)
