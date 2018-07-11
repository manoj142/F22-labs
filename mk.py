import requests,json
url = 'https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json'
r = requests.get(url)
data=json.loads(r.content.decode('utf-8'))
inv={}
for key in data:
    a=data[key]
    for i in range(0,len(a)):
        if a[i]['investors'] !='':
            word=a[i]['investors']
            if 'and' in word and ',' not in word:
                arr=word.split('and')
                for j in range(0,len(arr)):
                    k=arr[j].strip()
                    if k  not in inv:
                        inv[k]=[]
                        inv[k].append(a[i]['company']['title'])
                    else :
                        inv[k].append(a[i]['company']['title'])
            elif ',' in word and 'and' not in word:
                arr=word.split(',')
                for j in range(0,len(arr)):
                    k=arr[j].strip()
                    if k not in inv:
                        inv[k]=[]
                        inv[k].append(a[i]['company']['title'])
                    else:
                        inv[k].append(a[i]['company']['title'])
            elif ',' in word and 'and' in word:
                arr=word.split('and')
                arr1=arr[0].split(',')
                for j in range(0,len(arr1)-1):
                    k=arr1[j].strip()
                    if k not in inv:
                        inv[k]=[]
                        inv[k].append(a[i]['company']['title'])
                    else:
                        inv[k].append(a[i]['company']['title'])
                k=arr[len(arr)-1].strip()
                if k not in inv:
                    inv[k]=[]
                    inv[k].append(a[i]['company']['title'])
                else:
                    inv[k].append(a[i]['company']['title'])
   
            else:
                if word not in inv:
                    inv[word]=[]
                    inv[word].append(a[i]['company']['title'])
                else:
                    inv[word].append(a[i]['company']['title'])
