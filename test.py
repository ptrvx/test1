import http.client

conn = http.client.HTTPSConnection("deckofcardsapi.com")
payload = ''
headers = {
  'Cookie': '__cfduid=d2575d61e486c6f79fff404b270f6bf961615830988'
}
conn.request("GET", "/api/deck/nydqb33sezct/draw/?count=2%0A", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))