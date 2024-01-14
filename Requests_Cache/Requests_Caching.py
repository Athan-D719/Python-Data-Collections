import requests_with_caching
import requests
# it's not found in the permanent cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=hello", permanent_cache_file="datamuse_cache.txt")
print(res) #string
#print(res.text[:150])
#req = requests.get("https://api.datamuse.com/words?rel_rhy=hello")
#print('########################################')
#print(req.text)
# this time it will be found in the temporary cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
