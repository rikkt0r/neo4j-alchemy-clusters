__author__ = 'rikkt0r'

from flask import Flask, render_template
from py2neo import Graph, Node, Relationship, authenticate
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

authenticate('localhost:7474', 'neo4j', 'qwerty')
graph = Graph('http://localhost:7474/db/data')


@app.route('/')
def index():

    test = graph.find_one("Person", "born", 1951)  # MATCH (a:Person {born: 1951}) RETURN a
    print test

    return render_template('index.html', txt=test)


@app.route('/mockup')
def mockup():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)