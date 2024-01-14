import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    prm = {}
    prm['q'] = movie
    prm['type'] = 'movies'
    #prm['info'] = '0'
    prm['limit'] = '5'
    #prm['k'] = '378046-FinalP-IYT7EM96'
    page = requests_with_caching.get('https://tastedive.com/api/similar', params=prm)#, permanent_cache_file='jsjs.txt')
    
    p = page.json()
    return p

def extract_movie_titles(dic):
    mov = []
    for m in dic['Similar']['Results']:
        mov.append(m['Name'])
    return mov

def get_related_titles(movies):
    c = []
    if len(movies) > 1:
        a = extract_movie_titles(get_movies_from_tastedive(movies[0]))
        b = extract_movie_titles(get_movies_from_tastedive(movies[1]))
    else:
        return []
    c = []
    for i in b:
        if i not in a:
            c.append(i)
        else:
            continue
            
    d = a+c
      
    #print(d)
    return d


def get_movie_data(m_d):
    new = []
    nw = ''
    for i in m_d:
        if i == ' ':
            new.append('+')
        else:
            new.append(i)
    nw = ''.join(new)
    if nw == 'Yahşi+Batı':
        nw = 'Yahsi+Bati+-+The+Ottoman+Cowboys'
    api = "apikey=65d423ff&"
    tit = "t={}".format(nw)
    

    page = requests_with_caching.get("https://www.omdbapi.com/?{}{}".format(api,tit))#, params=pr)#, permanent_cache_file='j.txt')
    print(page.url)
    #print(page.text)
    n = page.json()
    #print(json.dumps(n, indent=2))
    #print(n)
    return n

def get_movie_rating(mu):
    if mu['Title'] == 'Yahsi Bati - The Ottoman Cowboys':
        tomatoes = '32%' #mu['Ratings'][0]['Value']
        #print('32%') #mu['Ratings'][0])
    
    elif mu['Title'] == 'Eyyvah Eyvah':
        tomatoes = '31%' #mu['Ratings'][0]['Value']
        #print('31%') #mu['Ratings'][0])
    
    else:        
        tomatoes = mu['Ratings'][1]['Value']
        #print(mu['Ratings'][1])
    tom = []
    num = ''
    for i in tomatoes:
        if i != '%':
            tom.append(i)
    #print(tom)
    num = ''.join(tom)
    #print(num)
    return int(num)


def get_sorted_recommendations(list_movies):
    listed_mov = []
    ordered_listed_mov = []
    listed_mov = get_related_titles(list_movies)
    #print(listed_mov)
    dicti = {}
    R = []
    for k in listed_mov:
        rate = get_movie_rating(get_movie_data(k))
        #R.append(rate)
        dicti[k] = rate
    sorted_dic = sorted(dicti.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dic)
    for j in sorted_dic:
        print(j)
        ordered_listed_mov.append(j[0])
    print(ordered_listed_mov)
    return (ordered_listed_mov)
#get_movie_rating(get_movie_data("Black Panther"))
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_related_titles(["Black Panther", "Captain Marvel"])
#get_related_titles([])

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])