
with open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\makertweettext1.txt') as f:
    tweetlist = [line.rstrip() for line in f]

new = open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\cleantweettext1.txt','w',encoding='utf-8')


def urlremove(tweetlist):
    temp = []
    for tweet in tweetlist:
        pieces = tweet.split()
        newpieces = [p for p in pieces if not (p.startswith("http"))]
        tweet = " ".join(newpieces)
        temp.append(tweet)
    return temp

def dupremove(tweetlist):
    temp = []
    unique = set(tweetlist)
    for tweet in unique:
        temp.append(tweet)
    return temp

def botremove(tweetlist):
	temp = []
	for tweet in tweetlist:
		pieces = tweet.split()
		newpieces = [p for p in pieces if not (p.startswith("http"))]
		tweet = " ".join(newpieces)
		temp.append(tweet)
	return set(temp)

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

def writetweets(tweetlist):
    newtweets = urlremove(tweetlist)
    newtweets1 = dupremove(newtweets)
    newtweets2 = botremove(newtweets1)
    newtweets3 = list(newtweets2)
    newtweets4 = everything(newtweets3)
    for tweet in newtweets4:
        print(tweet,file = new)

writetweets(tweetlist)

new.close()

