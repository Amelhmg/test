#!/usr/bin/python3
import sqlite3
import unittest
import json
import requests

class TestBD(unittest.TestCase):
    def test_18_15(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('select age from utilisateurs where age<18 or age>50')
        print(len(cur.fetchall()))
        self.assertEqual(len(cur.fetchall()), 0, msg="il ya des ages inf a 30 et supp a 50!!!!!")
        cur.close()


    def test_ville_no_fr(self):
        ville_fr=[]
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('select distinct ville from utilisateurs')
        rows=cur.fetchall()
        r=requests.get("https://eo.api.gouv.fr/communes?codeDepartement=15")

        j=r.json()
        for i in range(len(j)):
           ville_fr.append(j[i]["nom"])
           for v in range(len(rows)):
                 self.assertNotIn(rows[v], ville_fr, msg="La commune {} est une ville franaise!!!".format(rows[v]))


