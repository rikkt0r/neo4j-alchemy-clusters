# -*- coding: utf-8 -*-
__author__ = 'rikkt0r'

from flask import Flask, render_template
from py2neo import Graph, Node, Relationship, authenticate
import os


# TODO
"""
Alchemy.js - clusterization and visualization of neo4j db
http://nicolewhite.github.io/2014/07/24/visualize-subset-neo4j-alchemy.html
http://graphalchemist.github.io/Alchemy/#/examples
http://stackoverflow.com/questions/1545606/python-k-means-algorithm
Dla zbioru 20000x20 zaproponować własny use case, np. w oparciu o metodę klasteryzacji k-means
lub inną z bibliotek pythonowskich.

https://www.cs.ucsb.edu/~xyan/classes/CS595D-2009winter/MCL_Presentation2.pdf
Erdős–Rényi model
"""

app = Flask(__name__)
app.secret_key = os.urandom(24)

authenticate('localhost:7474', 'neo4j', 'qwerty')
graph = Graph('http://localhost:7474/db/data')


@app.route('/')
def index():

    test = graph.find_one("Person", "born", 1951)  # MATCH (a:Person {born: 1951}) RETURN a
    print test

    return render_template('index.html', txt=test)

@app.route('generate/<int:modifier>')
def generate(modifier=0):

    if modifier:
        pass


@app.route('/mockup')
def mockup():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)