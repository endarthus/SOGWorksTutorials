##################################################
#           Twitter Analysis Demo
#       July 11, Noli Chew - for SOG Works
#
#   Input:  companies and products of interest
#           file of clean #maker tweets
#           negative and positive sentiment word lists
#
#   Output: .csv file containing total counts and
#           averages of words of interest for each
#           tweet, as well as overall
#
#   Requires pyenchant package.
#
#   Reference:
#           Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on   
#           the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.
#
##################################################

import enchant

d = enchant.Dict("en_US")

with open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\cleantweettext.txt') as f:
    tweetlist = [line.rstrip() for line in f]

with open('C:/Users/Noli/Documents/School/Fall15/ALD/Project/lists/negativewords.txt') as l:
    neglist = [line.rstrip() for line in l]

with open('C:/Users/Noli/Documents/School/Fall15/ALD/Project/lists/positivewords.txt') as g:
    poslist = [line.rstrip() for line in g]

newfile = open(r'C:\Users\Noli\Documents\Shenzhen\Demos\Twitter\tweetmatrix2.csv','w')

print("Please enter company names or product names you would like to identify spearated by spaces\nex. Google Arduino")
yourwords = str(input()).split()

globalwords = {'total':0}

# Counts all proper nouns in the tweet
def tweetnouns(tweet):
    nouncount = 0
    for word in tweet.split():
        if not d.check(word) or not d.check(word.capitalize()):
            nouncount += 1
    return nouncount

# Counts all sentiment words in te tweet
def sentiment(words):
    negwords = 0
    poswords = 0
    for word in words.split():
        if word in neglist:
            negwords += 1
        elif word in poslist:
            poswords += 1
    return (poswords,negwords)

def makecsv(tweetlist):
    print("Calculating...")
    
    header = {} # Dictionary to iterate through 2 lists with associated variables
    header[0] = ['nouns','pos','neg']   # Contains the name of variables for word counts
    [header[0].append(word.lower()) for word in yourwords]
    header[1] = [(word+'avg') for word in header[0]]    # Contains the name of variables for word averages

    print('tweet',end=',',file=newfile) # Print the file header
    for i in range(len(header[0])):
        print(header[0][i]+','+header[1][i],end=',',file=newfile)
    print('total',end=',',file=newfile)

    for tweet in tweetlist:
        tempword = {}   # Maps variable names in header to values
        tempword['total'] = len(tweet.split())  # Count basic words
        tempword['nouns'] = tweetnouns(tweet)
        sentcount = sentiment(tweet)
        tempword['pos'] = sentcount[0]
        tempword['neg'] = sentcount[1]
        for word in header[0][3:len(header[0])]:    # Count words of interest
            tempword[word] = 0
            if word in tweet:
                tempword[word] += 1
        print("\n"+tweet,end=',',file=newfile)  # Begin to print row of information for tweet
        for i in range(len(header[1])): # For each type of word,
            print(tempword[header[0][i]],end=',',file=newfile)  # Print the word count
            tempword[header[1][i]] = float(tempword[header[0][i]]) / tempword['total'] # Calculate the word type average in the tweet
            print(tempword[header[1][i]],end=',',file=newfile)  # Print the word type average
            if header[0][i] not in globalwords: # Add the word count to the global dictionary
                globalwords[header[0][i]] = 0
            globalwords[header[0][i]] += tempword[header[0][i]]
        globalwords['total'] += tempword['total']   # Add the total word count to the global dictionary
        print(tempword['total'],end=',',file=newfile)

    for i in range(len(header[1])): # Calculate the total average for each word type
        globalwords[header[1][i]] = float(globalwords[header[0][i]]) / globalwords['total']

    print("\nTOTALTWEETS",end=',',file=newfile) # Begin to print row of information for total tweets
    for i in range(len(header[1])): # Print the information
        print(str(globalwords[header[0][i]])+','+str(globalwords[header[1][i]]),end=',',file=newfile)
    print(globalwords['total'],end=',',file=newfile)

makecsv(tweetlist)
newfile.close()
print("Done.")

