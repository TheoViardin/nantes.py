#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, get, app, hook
from bottle import response
from json import dumps
import sqlite3
import sys


class Equipements_activites(object):


    def getActiviteByVille(self, ville):
        try:
            conn = sqlite3.connect('labase.db')
            c = conn.cursor()
            conn.text_factory = str
            activites = c.execute("SELECT ActLib FROM 'activites' WHERE ComLib='"+ville+"'")
            retour =  activites.fetchall()
            conn.commit()
            conn.close()
            return retour
        except sqlite3.OperationalError as e:
            print('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville))
            return('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville))

class Equipements(object):


    def getEquipementsByVille(self, ville):
        try:
            conn = sqlite3.connect('labase.db')
            c = conn.cursor()
            conn.text_factory = str
            activites = c.execute("SELECT EquNom FROM 'equipements' WHERE ComLib='"+ville+"'")
            conn.commit()
            retour = activites.fetchall()
            conn.close()
            return retour
        except sqlite3.OperationalError as e:
            print('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville))
            return('[-] Sqlite operational error: {}, ville: {}, Abandon'.format(e, ville))

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

@get('/api/activites/<ville>')
def index(ville):
    activites = Equipements_activites()
    liste = activites.getActiviteByVille(ville)
    response.headers['Content-Type'] = 'application/json'
    reussite = "true"
    if (type(liste) is str):
        reussite = "false"
        return { "reussite" : reussite, "message" : liste}
    return { "reussite" : reussite, "activites" : liste}

@get('/api/equipements/<ville>')
def index(ville):
    equipements = Equipements()
    liste = equipements.getEquipementsByVille(ville)
    response.headers['Content-Type'] = 'application/json'
    reussite = "true"
    if (type(liste) is str):
        reussite = "false"
        return { "reussite" : reussite, "message" : liste}
    return { "reussite" : reussite, "equipements" : liste}



if __name__ == '__main__':

    run(host='localhost', port=2056)
