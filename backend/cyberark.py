import requests
import base64
username="jakob.holst"
password="Nice2Know2!"
url="https://priv.emea.dsv.com/PasswordVault/ObjectDetails.aspx?Data=RE1aLUpBS09CLUhPTFNUXkBeUm9vdF5AXmpha2hvbF9zc2hrZXlfZG16XkBeMF5AXkZhbHNlXkBeRmFsc2VeQF5eQF5CYWNrVVJMPU1zZ0Vycj1Nc2dJbmZvPQ%3D%3D"

id_secret_bytes = bytes(username + ':' + password, 'UTF-7')
basictoken = base64.b64encode(id_secret_bytes)
headers = {
     "Content-Type": "application/json",
     "Authorization": f"Basic {basictoken}"
}

session = requests()
response = session.get(url, headers=headers)
print(response.text)




