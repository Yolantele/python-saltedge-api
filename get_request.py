from saltedge import SaltEdge
import keys

app = SaltEdge(keys.APP_ID, keys.SECRET, 'private.pem')

url = 'https://www.saltedge.com/api/v4/countries'
response = app.get(url)
data = response.json()
print(data)
