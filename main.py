
# -*- coding:utf-8 -*-

import re
import json 
import spacy
import webbrowser
import requests
import queries_dict_ner as local_file
import funcs as local_func 

# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place PontdIéna Vendôme #allez toi je t'emmène au Toureiffel en zappé le telho reste tranquille t'es sur tn notre dame de paris clavier oussamaid@gmail.com"
# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place Vendôme allez #toi je t'emmène au en zappé le telho reste tranquille t'es #Tour_eiffel sur tn  clavier oussamaid@gmail.com"
# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place Dauphine allez toi je t'emmène au en zappé le telho reste tranquille t'es clavier oussamaid@gmail.com"
# txt = "@ss8ToutLesnews @MyriamOr8 @NanaPOUCAVE mais Place  Vendôme allez toi je t'emmène au en zappé le telho reste tranquille t'es Tour_eiffel sur tn  clavier oussamaid@gmail.com"
text = local_func.process_tweet(txt)
print(text)

if local_func.main(text) is not None:
    i = local_func.main(text)
    query =  local_file.query_4.replace('_' , str(i))
    url = 'http://apicollections.parismusees.paris.fr/graphql'
    header = { 'auth-token':'02a60ca6-e0d2-4c32-a2fe-9cdf4fb2186d'}
    r = requests.post(url=url, headers=header, json={ 'query' : query })
    print(r.status_code)
    json_data = json.loads(r.text)
    df_data = json_data['data']['nodeById']['fieldVisuelsPrincipals'][0]['entity']['publicUrl']
    print(json_data['data']['nodeById']['title'])
    print(json_data['data']['nodeById']['fieldOeuvreAuteurs'][0]['entity']['fieldAuteurAuteur']['entity']['name'])
    
    if df_data is None:
        df_data = json_data['data']['nodeById']['fieldVisuelsPrincipals'][0]['entity']['vignette']
    # print(df_data)
    webbrowser.open(df_data, new=1, autoraise=True)
else:
    pass 


# Strasboug 357544

# Lille 355345 
# chercher les artistes qui ont des oevres (art par ville) 



# 152880:Strasboug
# 185187:Auvergne-Rhône-Alpes,
# 185517:Bourgogne-Franche-Comté,
# 223379:Pays de la Loire,
# 364573:Bretagne,
# 205977:Centre-Val de Loire,
