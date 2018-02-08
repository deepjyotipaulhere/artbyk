from flask import Flask,jsonify
import MySQLdb as mdb

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/art/<artid>",methods=['GET'])
def getArt(artid):
    con=mdb.connect("localhost","root","1234","artbyk")
    cur=con.cursor()
    cur.execute("""SELECT * FROM arts WHERE id= %s""",(artid))
    rows=cur.fetchall()
    res=[]
    for c in rows:
        d={}
        d["id"]=c[0]
        d["title"]=c[1]
        d["subtitle"]=c[2]
        d["price"]=c[3]
        d["size"]=c[4]
        res.append(d)
    j=jsonify(res)
    con.close()
    j.headers.add('Access-Control-Allow-Origin','*')
    return j

@app.route("/art/all/<atype>",methods=['GET'])
def getArtType(atype):
    con=mdb.connect("localhost","root","1234","artbyk")
    cur=con.cursor()
    cur.execute("SELECT * FROM arts WHERE type= '"+atype+"'")
    rows=cur.fetchall()
    res=[]
    for c in rows:
        d={}
        d["id"]=c[0]
        d["title"]=c[1]
        d["subtitle"]=c[2]
        d["price"]=c[3]
        d["size"]=c[4]
        res.append(d)
    j=jsonify(res)
    con.close()
    j.headers.add('Access-Control-Allow-Origin','*')
    return j

if __name__=="__main__":
    app.run()