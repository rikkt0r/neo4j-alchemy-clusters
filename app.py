# -*- coding: utf-8 -*-
__author__ = 'rikkt0r'

from flask import Flask, render_template, jsonify
import py2neo
import igraph
import os
from random import randrange



# TODO
"""
Alchemy.js - clusterization and visualization of neo4j db
http://nicolewhite.github.io/2014/07/24/visualize-subset-neo4j-alchemy.html
http://graphalchemist.github.io/Alchemy/#/examples
http://stackoverflow.com/questions/1545606/python-k-means-algorithm
Dla zbioru 20000x20 zaproponować własny use case, np. w oparciu o metodę klasteryzacji k-means
lub inną z bibliotek pythonowskich.

https://www.cs.ucsb.edu/~xyan/classes/CS595D-2009winter/MCL_Presentation2.pdf
http://jexp.de/blog/2014/03/quickly-create-a-100k-neo4j-graph-data-model-with-cypher-only/
Erdős–Rényi model
"""

app = Flask(__name__)
app.secret_key = os.urandom(24)

py2neo.authenticate('localhost:7474', 'neo4j', 'qwerty')
gph = py2neo.Graph('http://localhost:7474/db/data')


class DrawHelper:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    @property
    def serialize(self):
        return {
            "nodes": [
                {
                    "id": n.properties["id"],
                    "name": n.properties["name"],
                    "cluster": randrange(0, 4, 1)
                } for n in self.nodes],
            "edges": [
                {
                    "source": e.nodes[0].properties["id"],
                    "target": e.nodes[1].properties["id"]
                } for e in self.edges],

        }


@app.route('/')
def index():

    # test = graph.find_one("Person", "born", 1951)  # MATCH (a:Person {born: 1951}) RETURN a
    cars = gph.find("Car", "name", "renault", 150)

    # g = igraph.Graph.Erdos_Renyi(500, 0.05, directed=True, loops=False)

    # igraph.Clustering.membership.
    # igraph.Vertex.betweenness()
    # cypher.
    # print g

    return render_template('index.html')  # , txt=str(g))

@app.route('/data/<string:data_type>')
def data(data_type=None):

    if data_type == "cars":
        # cars = gph.find("Car", "name", "renault", 150)
        # c = gph.cypher.execute("MATCH (p:Part)<-[r:HAS]-(c:Car) WHERE c.id IN
        # [10,15,22,545,346,500,123,54,78,456,345,333,444,222,111] RETURN r LIMIT 100;")
        c = gph.cypher.execute("MATCH (c:Car)-[r:HAS]->(p:Part) RETURN r SKIP 1800 LIMIT 300 ")
        d = c.to_subgraph()
        # print str(dir(cars))
        dh = DrawHelper(d.nodes, d.relationships)
    else:
        dh = DrawHelper([], [])

    return jsonify(dh.serialize)


@app.route('/generate/<int:modifier>')
def generate(modifier=0):

    if modifier:
        pass


if __name__ == '__main__':
    app.run(debug=True)