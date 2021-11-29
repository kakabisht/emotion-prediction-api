import requests 
import json

url="your_url" #pass url where you've hosted your api
playload=json.dumps([
     {
       "data":"Enter your phrases for emotion prediction"
     }
  ])
headers={
  'Content-Type':'application/json'
}
response=requests.request("POST",url,data=payload,headers=headers)
print(response.json)
