# -*- coding:utf-8 -*-
import re
import json 
import spacy
from spacy.matcher import PhraseMatcher
import unidecode
import requests
import random
import queries_dict_ner as local_file


nlp = spacy.load("fr_core_news_sm")
# nlp = spacy.fr_core_news_sm.load()
my_dict2 = {y:x for x,y in local_file.dic_ner.items()}
dict_ = dict(zip(my_dict2.keys(),[ re.sub('\W',' ',unidecode.unidecode(f).lower())  for f in my_dict2.values() ]))
dict_hashtg = dict( zip([ i.replace(' ','') for i in list(dict_.values())],[ i for i in list(dict_.values()) ]))

# print(list( dict_ner.values()))
def process_tweet(txt):
    text = txt.strip()
    text = re.sub('@\S+' , '', txt)
    text = re.sub('_' , '', txt)
    text = re.sub('#','istwichtig',text)
    text = re.sub('\W',' ',text)
    text = re.sub('istwichtig','#',text)
    text = unidecode.unidecode(text)
    text = re.sub('\s+' , ' ', text)
    text = text.lower()
    return text 

def verify_ent_no_sp(txt):
    li = []
    try:
        for i in set(dict_hashtg.keys()):
            if i in txt:
                li.append(i)
        for i in li:
            txt = txt.replace(i,dict_hashtg[i])
        return txt
    except:
        return None

def detect_hashtag_ent(txt):
    l=[]
    if len(re.findall('#(\S+)\s?',txt)) ==1:
            try:
                l.append(dict_hashtg[re.search('#(\S+)\s',txt).group(1)])
                return l[0]
            except:
                return None
    else:
        for a in  re.findall('#(\S+)\s',txt):
            try:
                l.append(dict_hashtg[a])
            except:
                pass         
        try:
            return random.choice(l)
        except:
            return None

def detect_entities(text):
    matcher = PhraseMatcher(nlp.vocab, attr= 'LOWER')
    terms = [ re.sub('\W',' ',unidecode.unidecode(f))  for f in my_dict2.values() ]
    patterns = [nlp.make_doc(text) for text in terms]
    matcher.add("TerminologyList", None, *patterns)

    doc = nlp(text)
    matches = matcher(doc)
    dict_ner = { start:doc[start:end].text for match_id, start, end in matches }
    list_ner = list( dict_ner.values())
        
    matched_id = [ k for k,v in dict_.items() for i in list_ner if v.lower() == i.lower() ]
    try:
        return random.choice(matched_id)
    except:
        return None

def get_id(value):
    return [ k for k,v in dict_.items()  if v.lower() == value.lower()  ][0]

def main(text):
    if  "#" in text:
        if detect_hashtag_ent(text) is not None:
            return get_id(detect_hashtag_ent(text))
        else:
            pass
    if verify_ent_no_sp(text) is not None:
        text = verify_ent_no_sp(text)
    if detect_entities(text) is not None:
        return (detect_entities(text))
    else:
        return None 
    

def process_tweet_second(t):
    t = t.strip()
    t = re.sub('\s+',' ',t)
    t = re.sub('@\S+' , '', t) 
    l = re.findall('[A-Z][a-z]+ ',t)
    s = re.findall('#[A-Z][a-z]+[A-Z][a-z]+[A-Z]*[a-z]*[A-Z]*[a-z]*[A-Z]*[a-z]*',t)
    n = 0 
    for i in s:
        n+=1
        t = t.replace(i,'/'+str(n)+'/')
    s_str = '//'.join(s)

    maj = re.findall('[a-z]([A-Z])',s_str)
    for i in maj:
        s_str = s_str.replace(i,'_'+i)
    n = 0 
    for i in s_str.split('//'):
        n+=1
        t = t.replace('/'+str(n)+'/',i)
    t = re.sub('_+','_',t)
    txt = t.replace('_',' ')
    return txt


def detect_loc(txt):
    txt = txt.replace('#','')
    doc = nlp(process_tweet_second(txt))
    return [X.text for X in doc.ents if X.label_ == 'LOC' ]


def pick_loc(lis_loc,t):
    if len(lis_loc)>1:
        state= True
        for i in lis_loc:
            try:
                if '#'==(t[t.index(i.split(' ')[0])-1]):
                    li_ent=i
                    state=False
                    return li_ent
            except:
                continue
        if state :
            return random.choice(lis_loc)
            
    else:
        return lis_loc[0]


def request_api(X,query_search):
    
    query =  query_search.replace('Whatlookingfor' , str('%')+X.strip()+str('%'))
    # query =  _.replace('Whatlookingfor' , str('%')+'Paris'+str('%'))
    url = 'http://apicollections.parismusees.paris.fr/graphql'
    header = { 'auth-token':'02a60ca6-e0d2-4c32-a2fe-9cdf4fb2186d'}
    r = requests.post(url=url, headers=header, json={ 'query' : query })
    json_data = json.loads(r.text)
    return json_data['data']['nodeQuery']['entities']

def check_if_empty(lis):
    if not lis :
        return True
    else:
        return False
def choose_id(lis):
    l = []
    for f in range(len(lis)):

        try:
            l.append(int(lis[f]['entityId'])) #convert to int to avoid things like '' 
        except:
            continue
    return [str(s) for s in l ]
def get_img_id(li_ent,query_search =local_file.query_search):
    print(li_ent)
    li_ent = li_ent.split(' ')
    if len(li_ent)>1:
        for i in reversed(range(2,len(li_ent)+1)):
            res = request_api("%".join(li_ent[:i]),query_search)
            if check_if_empty(res) == False :
                return  random.choice(choose_id(res))
            elif check_if_empty(res)== True:
                res = request_api("%".join(li_ent[:i]),local_file._)
                if check_if_empty(res)== False:
                    return  random.choice(choose_id(res))
                else:
                    return None
    elif len(li_ent)==1:
        res = request_api(li_ent[0],query_search)
        if check_if_empty(res)== False:
            return  random.choice(choose_id(res))
        else:
            res = request_api(li_ent[0],local_file._)
            if check_if_empty(res)== False:
                return  random.choice(choose_id(res))
        return None
    
    return None

def get_img(query,detected):

    url = 'http://apicollections.parismusees.paris.fr/graphql'
    header = { 'auth-token':'02a60ca6-e0d2-4c32-a2fe-9cdf4fb2186d'}
    r = requests.post(url=url, headers=header, json={ 'query' : query })
    # print(r.status_code)
    json_data = json.loads(r.text)
    try:
        url = json_data['data']['nodeById']['fieldVisuelsPrincipals'][0]['entity']['publicUrl']
    except:
        try:
            url = json_data['data']['nodeById']['fieldVisuelsPrincipals'][0]['entity']['vignette']
        except:
            get_img_id(detected,query_search =local_file.query_search)


    if url is None:
        url = json_data['data']['nodeById']['fieldVisuelsPrincipals'][0]['entity']['vignette']
    try:
        title = json_data['data']['nodeById']['title'] 
        title = title.replace('\n','')
    except:
        title= 'Non renseigné'
    try:
        author = json_data['data']['nodeById']['fieldOeuvreAuteurs'][0]['entity']['fieldAuteurAuteur']['entity']['name']
        author = author.replace('\n','')    
    except:
        author = 'Non renseigné'
    try:
        Museum = json_data['data']['nodeById']['fieldMusee']['entity']['name']
        Museum = Museum.replace('\n','')   
    except:
        Museum = 'Non renseigné'
    try:
        century = json_data['data']['nodeById']['fieldDateProduction']['century']
        century = century.replace('\n','')   
    except:
        century = 'Non renseigné'
    try:
        start_year = json_data['data']['nodeById']['fieldDateProduction']['startYear']
        start_year = start_year.replace('\n','')   
    except:
        start_year  = 'Non renseigné'
    try:
        end_year = json_data['data']['nodeById']['fieldDateProduction']['endYear']
        end_year = end_year.replace('\n','')   
    except:
        end_year  = 'Non renseigné'

    return (url , empty_str(title),empty_str(author),empty_str(Museum),empty_str(century),empty_str(start_year) ,empty_str(end_year),detected)

def empty_str(s):
    if s is None:
        return ''
    return str(s)



