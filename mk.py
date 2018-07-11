import requests,json
url = 'https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json'
res= requests.get(url)
sharktank=json.loads(res.content.decode('utf-8'))
investors={}
for episode in sharktank:
    edetails=sharktank[episode]
    for i in range(0,len(edetails)):
        if edetails[i]['investors'] !='': #checking if investor is null
            invnames=edetails[i]['investors']
            if 'and' in invnames and ',' not in invnames:#if only two investors are in investor 
                inames=invnames.split('and')
                for j in range(0,len(inames)):
                    iname=inames[j].strip()
                    if iname  not in investors:
                        investors[iname]=[]
                        investors[iname].append(edetails[i]['company']['title'])
                    else :
                        investors[iname].append(edetails[i]['company']['title'])
            elif ',' in invnames and 'and' not in invnames: #if more than two investors
                inames=invnames.split(',')
                for j in range(0,len(inames)):
                    iname=inames[j].strip()
                    if iname not in investors:
                        investors[iname]=[]
                        investors[iname].append(edetails[i]['company']['title'])
                    else:
                        investors[iname].append(edetails[i]['company']['title'])
            elif ',' in invnames and 'and' in invnames:#more than two investors and ending with and
                inames=invnames.split('and')
                investorname=inames[0].split(',')
                for j in range(0,len(investorname)-1):
                    iname=investorname[j].strip()
                    if iname not in investors:
                        investors[iname]=[]
                        investors[iname].append(edetails[i]['company']['title'])
                    else:
                        investors[iname].append(edetails[i]['company']['title'])
                iname=inames[len(inames)-1].strip()
                if iname not in investors:
                    investors[iname]=[]
                    investors[iname].append(edetails[i]['company']['title'])
                else:
                    investors[iname].append(edetails[i]['company']['title'])
   
            else: #only one investor
                if invnames not in investors:
                    investors[invnames]=[]
                    investors[invnames].append(edetails[i]['company']['title'])
                else:
                    investors[invnames].append(edetails[i]['company']['title'])

#printing investors and their companies in sorting order
for investorname in sorted(investors,key=lambda investorname:len(investors[investorname])):
    print(investorname+":")
    print(investors[investorname])
