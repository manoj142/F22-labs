import requests,json
url = 'https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json'
r = requests.get(url)
data=json.loads(r.content.decode('utf-8'))
print(data)	
	
