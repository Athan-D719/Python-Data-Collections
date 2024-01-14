import requests
#import urllib.error, urllib.parse, urllib.request
import json

#page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
#page = urllib.request.urlopen("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy':'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
# Additional parameter to add the arguments, keys...
#Sometimest the requests for security means wont work.
print(type(page))
print(page.text[:150]) #print the first 150 characters
print(page.url) #print the url that was fetched
print('-------')
print('STATUS')
print(page.status_code)
print('-------')
print('STATUS = OK?')
print(page.status_code == requests.codes.ok)
print("-------")
print(page.headers['Content-Type'])
#print(page.headers.get['content-type'])
x = page.json() #turn page.text into python object (json.loads)
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) #pretty print the results
###############################################################
#http://www.datamuse.com/api/      #documentation
###############################################################
#print(p.headers.keys())  #printing the headers
##.history #contains a list of previous responses

d = {'q': '"violins and guitars"', 'tbm': 'isch'} #isch for images
results = requests.get("https://google.com/search", params=d)
print(results.url) 


######################################################################
#WORDS THAT RYMH
# import statements for necessary Python modules
import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    print(resp.url)
    #print(rasp.text[:100])
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))


####################################################################
#CHACHING RESPONSE OBJECT
####################################################################

