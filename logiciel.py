#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, get, app, hook
from bottle import response
from json import dumps
import sqlite3
import sys


class Equipements_activites(object):


    def getActiviteByVille(self, ville):
        conn = sqlite3.connect('labase.db')
        c = conn.cursor()
        conn.text_factory = str
        activites = c.execute("SELECT ActLib FROM 'activites' WHERE ComLib='"+ville+"'")
        return activites.fetchall()
        conn.commit()
        conn.close()


class Equipements(object):


    def getEquipementsByVille(self, ville):
        conn = sqlite3.connect('labase.db')
        c = conn.cursor()
        conn.text_factory = str
        activites = c.execute("SELECT EquNom FROM 'equipements' WHERE ComLib='"+ville+"'")
        return activites.fetchall()
        conn.commit()
        conn.close()

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
    if (len(liste) == 0):
        reussite = "false"
    return { "reussite" : reussite, "activites" : liste}

@get('/api/equipements/<ville>')
def index(ville):
    equipements = Equipements()
    liste = equipements.getEquipementsByVille(ville)
    print('test')
    response.headers['Content-Type'] = 'application/json'
    reussite = "true"
    if (len(liste) == 0):
        reussite = "false"
    return { "reussite" : reussite, "equipements" : liste}



if __name__ == '__main__':

    run(host='localhost', port=2056)
