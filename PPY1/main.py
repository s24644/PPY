import webbrowser
import requests

# pageurl = 'https://github.com'
# date = 20150101
pageurl = input("podaj adres strony: ")

date1 = input("podaj pierwszy punkt w czasie (rrrrmmdd): ")
date2 = input("podaj drugi punkt w czasie (rrrrmmdd): ")
date3 = input("podaj trzeci punkt w czasie (rrrrmmdd): ")

url1 = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date1)
url2 = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date2)
url3 = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date3)

response = requests.get(url1)
d1 = response.json()
print(d1)
page1 = d1["archived_snapshots"]["closest"]["url"]

response = requests.get(url2)
d2 = response.json()
print(d2)
page2 = d2["archived_snapshots"]["closest"]["url"]

response = requests.get(url3)
d3 = response.json()
print(d3)
page3 = d3["archived_snapshots"]["closest"]["url"]

webbrowser.open(page1)
webbrowser.open(page2)
webbrowser.open(page3)