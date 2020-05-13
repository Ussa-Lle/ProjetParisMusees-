# -*- coding:utf-8 -*-
import re
import json 
import spacy
import pandas as pd
from spacy import displacy
from spacy.matcher import PhraseMatcher
import unidecode
import webbrowser
import requests
import random
import queries_dict_ner as local_file

nlp = spacy.load("fr_core_news_sm")

my_dict2 = {y:x for x,y in local_file.dic_ner.items()}
dict_ = dict(zip(my_dict2.keys(),[ re.sub('\W',' ',unidecode.unidecode(f).lower())  for f in my_dict2.values() ]))
dict_hashtg = dict( zip([ i.replace(' ','') for i in list(dict_.values())],[ i for i in list(dict_.values()) ]))


def process_tweet(txt):

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
    if len(re.findall('#(\S+)\s',txt)) ==1:
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
    return random.choice(matched_id)

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
    