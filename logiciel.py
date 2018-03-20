#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template
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


if __name__ == '__main__':

    @route('/api/activites/<ville>')
    def index(ville):
        activites = Equipements_activites()
        liste = activites.getActiviteByVille(ville)
        return { "activites" : liste}

    @route('/api/equipements/<ville>')
    def index(ville):
        equipements = Equipements()
        liste = equipements.getEquipementsByVille(ville)
        print('test')
        return { "equipements" : liste}

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
