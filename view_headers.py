import requests

headers = {'Accept-Encoding': 'application/json'}

r = requests.get('http://icanhasdadjoke.com/', headers=headers)
print (r.request.headers)
print()
print (r.request.headers['Accept-Encoding'])
print()
print (r.headers)
print()
print (r.headers['content-type'])



