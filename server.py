#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, get, app, hook
from bottle import response
from json import dumps
import sqlite3
import sys


class Equipements_activites(object):

#Retourne un tableau d'activités corresondant à la ville entrée en parametre
    def getActiviteByVille(self, ville):
        try:
            conn = sqlite3.connect('labase.db') # Connexion à la base de donnée
            c = conn.cursor()
            conn.text_factory = str # Le type de donnée en retour de la base est string
            activites = c.execute("SELECT ActLib FROM 'activites' WHERE ComLib='"+ville+"'") # On demande toutes les activités dans la ville demandée
            retour =  activites.fetchall() # On réorganise les valeurs retournées dans un tableau
            conn.commit()
            conn.close() # On termine la connexion avec la base de donnée
            return retour # On retourne le tableau
        except sqlite3.OperationalError as e: # Au cas où le serveur ne trouve pas la table cherchée
            print('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville)) # On affiche l'erreur dans la console du serveur
            return('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville)) # On retourne la meme erreur pour ensuite l'afficher au client

class Equipements(object):

#Retourne un tableau d'equipements corresondant à la ville entrée en parametre
    def getEquipementsByVille(self, ville):
        try:
            conn = sqlite3.connect('labase.db') # Connexion à la base de donnée
            c = conn.cursor()
            conn.text_factory = str # Le type de donnée en retour de la base est string
            activites = c.execute("SELECT EquNom FROM 'equipements' WHERE ComLib='"+ville+"'") # On demande toutes les activités dans la ville demandée
            conn.commit()
            retour = activites.fetchall() # On réorganise les valeurs retournées dans un tableau
            conn.close() # On termine la connexion avec la base de donnée
            return retour # On retourne le tableau
        except sqlite3.OperationalError as e:
            print('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville)) # On affiche l'erreur dans la console du serveur
            return('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville)) # On retourne la meme erreur pour ensuite l'afficher au client

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

# Permet de choisir les headers de les reponses emisent par le serveur
@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''
#Access-Control-Allow-Origin nous permet de pouvoir utiliser l'API qui est sur localhost alors que nous sommes sur un autre domaine
    response.headers['Access-Control-Allow-Origin'] = _allow_origin
#Access-Control-Allow-Methods permet de choisir quelle methode du protocole HTTP sont utilisables
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
#Access-Control-Allow-Headers permet de choisir les headers modifiables
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

# Si le client demande les activités d'une ville
@get('/api/activites/<ville>')
def index(ville):
    activites = Equipements_activites() # Nouvel obet equipement
    liste = activites.getActiviteByVille(ville) # On execute la requete sur la base de donnée
    response.headers['Content-Type'] = 'application/json' # On defini que le type de retour sera du Json
    reussite = "true"
    if (type(liste) is str): # Si le resultat de la requete sur la base est un message
        reussite = "false" # C'est une message d'erreur donc reussite passe à false
        return { "reussite" : reussite, "message" : liste} # On renvoie une reussite false et le message d'erreur au client
    return { "reussite" : reussite, "activites" : liste} # Si tout c'est bien passé on renvoie une reussite true et la table

# Si le client demande les équipements d'une ville
@get('/api/equipements/<ville>')
def index(ville):
    equipements = Equipements() # Nouvel obet equipement
    liste = equipements.getEquipementsByVille(ville) # On execute la requete sur la base de donnée
    response.headers['Content-Type'] = 'application/json' # On defini que le type de retour sera du Json
    reussite = "true"
    if (type(liste) is str): # Si le resultat de la requete sur la base est un message
        reussite = "false" # C'est une message d'erreur donc reussite passe à false
        return { "reussite" : reussite, "message" : liste} # On renvoie une reussite false et le message d'erreur au client
    return { "reussite" : reussite, "equipements" : liste} # Si tout c'est bien passé on renvoie une reussite true et la table



if __name__ == '__main__':

    run(host='localhost', port=2056) # Le serveur écoute sur localhost:2056
