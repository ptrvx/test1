import http.client

conn = http.client.HTTPSConnection("deckofcardsapi.com")
payload = ''
headers = {}
conn.request("GET", "/api/deck/new/shuffle/?deck_count=1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
