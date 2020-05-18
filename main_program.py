
# -*- coding:utf-8 -*-

import re
import json 
import spacy

import requests
import queries_dict_ner as local_file
import funcs as local_func 

# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place PontdIéna Vendôme #allez toi je t'emmène au Toureiffel en zappé le telho reste tranquille t'es sur tn notre dame de paris clavier oussamaid@gmail.com"
# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place Vendôme allez #toi je t'emmène au en zappé le telho reste tranquille t'es #Tour_eiffel"
# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place Dauphine allez toi je t'emmène au en zappé le telho reste tranquille t'es clavier oussamaid@gmail.com"
# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place  Vendôme allez toi je t'emmène au en zappé le telho reste tranquille t'es Tour_eiffel sur tn  clavier oussamaid@gmail.com"
txt = 'je vais aller à paris ou bien #PontDeBezons '

def main(tweet='',city=''):
    if city == '':    
        text = local_func.process_tweet(tweet)

        if local_func.main(text) is not None:
            i = local_func.main(text)
            local_func.get_img_id(local_func.my_dict2[i])
            query =  local_file.query_4.replace('_' , str(local_func.get_img_id(local_func.my_dict2[i])))
            return local_func.get_img(query)

        elif local_func.main(txt) is None:
            text = local_func.process_tweet_second(tweet)

            lis = local_func.detect_loc(text)

            if local_func.check_if_empty(lis):
                return None
            else:
                query =  local_file.query_4.replace('_' , str(  local_func.get_img_id(local_func.pick_loc(lis,text))))
                print(local_func.pick_loc(lis,text))
                if local_func.get_img_id(local_func.pick_loc(lis,text)):
                    return local_func.get_img(query)
                return None
    else:
        lis = [city]
        if local_func.check_if_empty(lis):
            return None
        else:
            query =  local_file.query_4.replace('_' , str(  local_func.get_img_id(local_func.pick_loc(lis,tweet))))
            if local_func.get_img_id(local_func.pick_loc(lis,tweet)):
                return local_func.get_img(query)
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





# http://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da