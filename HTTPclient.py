import http.client
x=http.client.HTTPConnection('www.google.com',80)
x.connect()
x.request('GET','/index.html')
y=x.getresponse()
z=y.read().decode()
print(z)
x.close()
