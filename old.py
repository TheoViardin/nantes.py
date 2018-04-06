# -*- coding: utf-8 -*-

import csv
import sqlite3
import sys


conn = sqlite3.connect('dataBaseEquipements_Activites.db')
c = conn.cursor()
c.execute('''CREATE TABLE activites (ComInsee real, ComLib text, EquipementId real, EquNbEquIdentique real, ActCode real, ActLib text, EquActivitePraticable text, EquActivitePratique text, EquActiviteSalleSpe text, ActNivLib text)''')
with open('equipements_activites.csv', 'r') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        #print (type(row["ComInsee"]), type(row["ComLib"]))
        u2 = unicode(row["ComLib"], "utf-8")
        u3 = unicode(row["ActLib"], "utf-8")
        u4 = unicode(row["EquActivitePraticable"], "utf-8")
        u5 = unicode(row["EquActivitePratique"], "utf-8")
        u6 = unicode(row["EquActiviteSalleSpe"], "utf-8")
        u7 = unicode(row["ActNivLib"], "utf-8")
        c.execute('INSERT INTO activites VALUES (?,?,?,?,?,?,?,?,?,?)', (row["ComInsee"], u2, row["EquipementId"], row["EquNbEquIdentique"], row["ActCode"], u3, u4, u5, u6, u7))
conn.commit()
conn.close()
