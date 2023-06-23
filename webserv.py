#!/usr/bin/python3
import sqlite3, random
from flask import Flask, jsonify, request
from flask_cors import CORS

prenom = ['ali','said','dasdas','dsadasgg','dsadwtrt']
ville = ['tizi','alger','oran','tirmitin']
nom = ['zid','aaa','bbb','ccc','ddd']

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS utilisateurs(nom TEXT, prenom TEXT, age INTERGER, Ville TEXT)')
conn.commit()
conn.close()

app=Flask(__name__)
CORS(app)


@app.route('/<nb_rows>')
def index(nb_rows): 
    sqlw(nb_rows)
    return jsonify ({"message": "repose ok"})

def sqlw(rows):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    for i in range(int(rows)):
        cur.execute('INSERT INTO utilisateurs VALUES("{}","{}","{}","{}")'.format(random.choice(nom), random.choice(prenom), random.randrange(10,70),random.choice(ville)))
    conn.commit()
    conn.close()
    return 'ok',200
    

@app.route('/select')
def sqlr ():
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute("select * from utilisateurs")
    rows = cur.fetchall()
    for row in rows :
        print (row)
    conn.commit()
    conn.close()
    return jsonify({"row":rows})

@app.route('/groupby')
def sqlg():
	conn=sqlite3.connect('database.db')
	cur=conn.cursor()
	cur.execute('select ville, count(*) as num from utilisateurs group by ville')
	rows=cur.fetchall()
	conn.close()
	return jsonify({"result": rows})

	
@app.route('/delete')
def sqldel():
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute('delete from utilisateurs')
    nbbb=cur.rowcount
    conn.commit()
    conn.close()
    return jsonify({"result": "{} lignes supprimées".format(nbbb)})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081)