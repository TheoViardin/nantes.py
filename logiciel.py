#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, get, app, hook
from bottle import response
from json import dumps
import sqlite3
import sys


class Equipements_activites(object):


    def getActiviteByVille(self, ville):
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        conn.text_factory = str
        activites = c.execute("SELECT ActLib FROM 'equipements_activites' WHERE ComLib='"+ville+"'")
        return activites.fetchall()
        conn.commit()
        conn.close()


class Equipements(object):


    def getEquipementsByVille(self, ville):
        conn = sqlite3.connect('db.db')
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
    return { "activites" : liste}

@get('/api/equipements/<ville>')
def index(ville):
    equipements = Equipements()
    liste = equipements.getEquipementsByVille(ville)
    print('test')
    response.headers['Content-Type'] = 'application/json'
    return { "equipements" : liste}



if __name__ == '__main__':

    run(host='localhost', port=2056)

    '''print('Que voulez-vous savoir ?')
    choix = input('1 - Activites d\'une ville\n2 - Equipements d\'une ville\n')
    if (choix == 1):
        equipement = Equipements_activites()
        choix = raw_input('Entrer le nom d\'une ville\n')
        print(equipement.getActiviteByVille(choix))
    elif (choix == 2):
        equipement = Equipements()
        choix = raw_input('Entrer le nom d\'une ville\n')
        print(equipement.getEquipementsByVille(choix))
    else:
        print('Choix invalide')'''
