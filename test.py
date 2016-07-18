

with open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Tweepy\maketweettext1.txt') as f:
    tweetlist = [line.rstrip() for line in f]

new = open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\noURL.txt','w')

def urlremove(tweetlist):
    for tweet in tweetlist:
        pieces = tweet.split()
        newpieces = [p for p in pieces if not (p.startswith("http"))]
        tweet = " ".join(newpieces)
        print(tweet,file = new)

urlremove(tweetlist)

with open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\noURL.txt') as f:
    tweetlist = [line.rstrip() for line in f]

new = open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\nobots.txt','w')

def dupremove(tweetlist):
    unique = set(tweetlist)
    for tweet in unique:
        print(tweet,file = new)

dupremove(tweetlist)

def botremove(tweetlist):
	temp = []
	for tweet in tweetlist:
		pieces = tweet.split()
		newpieces = [p for p in pieces if not (p.startswith("http"))]
		tweet = " ".join(newpieces)
		temp.append(tweet)
	return set(temp)

test = botremove(tweetlist)

test1 = list(test)

def everything(tweetlist):
    temp = []
    for tweet in tweetlist:
        text = tweet.lower()
        text = text.replace('<', ' <')
        text = text.replace('>', '> ')
        pieces = text.split()
        newpieces = [p for p in pieces if not (p.startswith("<"))]
        text = " ".join(newpieces)
        text = text.replace('vs.', 'versus')
        text = text.replace('b/c', 'because')
        text = text.replace('bc', 'because')
        text = text.replace('abt', 'about')
        text = text.replace('w/o', 'without')
        text = text.replace('&gt', ' ')
        text = text.replace('mite', 'might')
        text = text.replace('nite', 'night')
        text = text.replace('pls', 'please')
        text = text.replace('plz', 'please')
        text = text.replace('&amp;', 'and')
        text = text.replace('w/', 'with')
        text = text.replace('fb', 'facebook')
        text = text.replace('re:', 'regarding')
        text = text.replace('chk', 'check')
        text = text.replace('cld', 'could')
        text = text.replace('tmr', 'tomorrow')
        text = text.replace('4u', 'for you')
        text = text.replace('b4', 'before')
        text = text.replace('blieve', 'believe')
        text = text.replace('dnt', 'dont')
        text = text.replace('l8', 'late')
        text = text.replace('l8r', 'later')
        text = text.replace('nvm', 'nevermind')
        text = text.replace('shld', 'should')
        text = text.replace('srsly', 'seriously')
        text = text.replace('srs', 'serious')
        text = text.replace('sux', 'sucks')
        text = text.replace('txt', 'text')
        text = text.replace('wld', 'would')
        text = text.replace('&amp;', 'and')
        text = text.replace('&lt;', ' ')
        text = "".join(p for p in text if not (p.startswith("http")))
        text = text.replace('/', ' ')
        text = text.replace('(',' ')
        text = text.replace(')',' ')
        text = text.replace(':',' ')
        text = text.replace(',', ' ')
        text = "".join(c for c in text if c not in ('»','’','‘','…','—','|','~','[',']','-','!','.',':','\'','?','#','@','$','%','^','&','*','(',')','-','=','+','|',',','/','<','>','_',"\"",";"))
        temp.append(text)
    return temp


test2 = everything(test1)

def writetweets(tweetlist):
	newfile = open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\cleantweettext.txt','w')
	for tweet in tweetlist:
		print(tweet,file = newfile)

def countwords(tweetlist):
	temp = {}
	for tweet in tweetlist:
		for word in tweet.split():
			if word not in temp:
				temp[word] = 0
			temp[word] +=1
	return temp

test4 = countwords(test2)

def listoflists(tweetlist):
	temp = []
	for tweet in tweetlist:
		temp1 = (tweet.split())
		temp.append(temp1)
	return temp

test5 = listoflists(test2)



import enchant 

def checkwords(worddic):
	for key in worddic.keys():
		if not d.check(key):
			print(key)

def tweetnouns(tweetlist):
	temp = {}
	nouncount = 0
	temp1 = []
	for tweet in tweetlist:
		for word in tweet.split():
			if not d.check(word):
				nouncount += 1
		temp1.append(nouncount)
		temp1.append(len(tweet.split()))
		temp[tweet] = temp1

def tweetnouns(tweetlist):
	for tweet in tweetlist:
		nouncount = 0
		for word in tweet.split():
			if not d.check(word):
				nouncount += 1
		print(tweet,nouncount,len(tweet.split()),end="\n")
