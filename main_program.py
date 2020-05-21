
# -*- coding:utf-8 -*-

import re
import json 
import spacy
import requests
import urllib.request
import queries_dict_ner as local_file
import funcs as local_func 



def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")


def main(tweet='',city=''):
    if city == '':    
        text = local_func.process_tweet(tweet)

        if local_func.main(text) is not None:
            i = local_func.main(text)
            detected = local_func.my_dict2[i]

            query =  local_file.query_4.replace('_' , str(local_func.get_img_id(detected)))
            
            return (local_func.get_img(query,detected),local_func.get_img_id(detected))

        elif local_func.main(tweet) is None:
            text = local_func.process_tweet_second(tweet)

            lis = local_func.detect_loc(text)

            if local_func.check_if_empty(lis):
                return None
            else:
                detected = local_func.pick_loc(lis,text)
                query =  local_file.query_4.replace('_' , str(  local_func.get_img_id(detected)))    #move that a line below
                if local_func.get_img_id(detected) is not None:
                    # print('hereweare',local_func.get_img(query,detected))
                    return (local_func.get_img(query,detected),local_func.get_img_id(detected))
                return None
    else:
        lis = [city]
        if local_func.check_if_empty(lis):
            return None
        detected = lis[0]
        # print('hereweare',detected)
        query =  local_file.query_4.replace('_' , str(  local_func.get_img_id(detected))) #move that a line below
        if local_func.get_img_id(detected) is not None:
            
            return (local_func.get_img(query,detected),local_func.get_img_id(detected))
        return None






















