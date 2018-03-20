#!/usr/bin/env python

import sqlite3
import sys

class Commune(object):

    def __init__(self, comLib):
        conn = sqlite3.connect('../db.db')
        c = conn.cursor()
        conn.text_factory = str
        self.comLib = comLib
        activite = c.execute("SELECT * FROM 'equipements_activites' WHERE ComLib='"+comLib+"'")
        equipement = c.execute("SELECT * FROM 'equipements' WHERE ComLib='"+comLib+"'")
        tableActivite = activite.fetchall()
        tableEquipement = equipement.fetchall()
        print(tableEquipement)

if __name__ == '__main__':

    commune = Commune('Nantes')
