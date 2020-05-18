
# -*- coding:utf-8 -*-

import re
import json 
import spacy
import requests
import queries_dict_ner as local_file
import funcs as local_func 


def main(tweet='',city=''):
    if city == '':    
        text = local_func.process_tweet(tweet)

        if local_func.main(text) is not None:
            i = local_func.main(text)
            local_func.get_img_id(local_func.my_dict2[i])
            query =  local_file.query_4.replace('_' , str(local_func.get_img_id(local_func.my_dict2[i])))
            return local_func.get_img(query,local_func.pick_loc(local_func.my_dict2[i],text))

        elif local_func.main(tweet) is None:
            text = local_func.process_tweet_second(tweet)

            lis = local_func.detect_loc(text)


            if local_func.check_if_empty(lis):
                return None
            else:
                query =  local_file.query_4.replace('_' , str(  local_func.get_img_id(local_func.pick_loc(lis,text))))
                print(local_func.pick_loc(lis,text))
                if local_func.get_img_id(local_func.pick_loc(lis,text)) is not None:
                    return local_func.get_img(query,local_func.pick_loc(lis,text))
                return None
    else:
        lis = [city]
        if local_func.check_if_empty(lis):
            return None
        else:
            query =  local_file.query_4.replace('_' , str(  local_func.get_img_id(local_func.pick_loc(lis,tweet))))
            if local_func.get_img_id(local_func.pick_loc(lis,tweet)) is not None:
                return local_func.get_img(query,local_func.pick_loc(lis,tweet))
            return None


# print(_main_(txt))



        























# Strasboug 357544

# Lille 355345 
# chercher les artistes qui ont des oevres (art par ville) 



# 152880:Strasboug
# 185187:Auvergne-Rhône-Alpes,
# 185517:Bourgogne-Franche-Comté,
# 223379:Pays de la Loire,
# 364573:Bretagne,
# 205977:Centre-Val de Loire,



