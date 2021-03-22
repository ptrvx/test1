import http.client

conn = http.client.HTTPSConnection("deckofcardsapi.com")
payload = ''
headers = {}
conn.request("GET", "/api/deck/nydqb33sezct/draw/?count=2%0A", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))