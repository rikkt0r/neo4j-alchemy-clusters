# -*- coding: utf-8 -*-
__author__ = 'rikkt0r'

from flask import Flask, render_template, jsonify, url_for, redirect
import py2neo
import igraph
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

py2neo.authenticate('localhost:7474', 'neo4j', 'qwerty')
gph = py2neo.Graph('http://localhost:7474/db/data')


class DrawHelper:

    # @input VertexClustering object
    # @output JSON
    def __init__(self, clusters, edges):
        self.nodes = []
        self.edges = edges

        for idx, cluster in enumerate(clusters):
            for node in cluster:
                # print node.attributes()
                self.nodes.append({
                    'id': node,
                    'name': 'node',
                    'cluster': idx
                })

    @property
    def serialize(self):
        return {
            "nodes": [
                {
                    "id": n['id'],
                    "name": n['name'],
                    "cluster": n['cluster']
                } for n in self.nodes],
            "edges": [
                {
                    "source": e[0],
                    "target": e[1]
                } for e in self.edges],
        }


def reset_neo4j():
    # remove all
    gph.cypher.execute("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")

    # Added 500 labels, created 500 nodes, set 1000 properties, statement executed in 127 ms.
    gph.cypher.execute(
        """WITH ["audi", "bmw", "ford", "mercedes", "nissan", "opel", "peugeot", "renault", "toyota", "volkswagen"]
         AS names FOREACH (r IN range(0,100) | CREATE (:Car {id:r, name:names[r % size(names)]+" "+r}));"""
    )

    # Added 10 labels, created 10 nodes, set 20 properties, statement executed in 41 ms.
    gph.cypher.execute(
        """WITH ["hybrid engine", "spare wheel", "computer", "digital speedometer", "sunroof",
         "alarm", "abs", "esp", "asr", "muffler"] AS names FOREACH
         (r IN range(0,9) | CREATE (:Part {id:r, name:names[r % size(names)]+" "+r}));"""
    )

    # Created 143 relationships, statement executed in 112 ms.
    gph.cypher.execute("MATCH (c:Car),(p:Part) WITH c,p LIMIT 800 WHERE rand() < 0.1 CREATE (c)-[:HAS]->(p);")

    # Added 1 index, statement executed in 36 ms.
    gph.cypher.execute("create index on :Car(id);")

    # Added 1 index, statement executed in 22 ms.
    gph.cypher.execute("create index on :Part(id);")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph/<string:data_type>/<int:case>')
def graph(data_type=None, case=None):

    if data_type == "neo4j":
        if case == 0:
            data_source = "/data/neo4j/0"
        elif case == 1534234:
            reset_neo4j()
            return redirect(url_for('index'))
    elif data_type == "igraph":
        data_source = '/data/igraph/'+str(case)

    return render_template('graph.html', data_source=data_source)


# data and graph is divided into two routes (instead of request.method modifier)
# coz alchemy uses only GET :/
@app.route('/data/<string:data_type>/<int:case>')
def data(data_type=None, case=0):

    if data_type == "neo4j":

        if case == 0:
            query_n = "MATCH (c:Car)-[:HAS]->(:Part) RETURN DISTINCT ID(c) AS id, c.name AS name"
            query_e = "MATCH (c1:Car)-[:HAS]->(:Part)<-[:HAS]-(c2:Car) RETURN ID(c1) AS source, ID(c2) AS target"

            nodes = gph.cypher.execute(query_n)
            edges = gph.cypher.execute(query_e)

            g = igraph.Graph()
            for node in nodes:
                g.add_vertex(name=str(node.id))
            for edge in edges:
                g.add_edge(str(edge.source), str(edge.target))

            g = g.as_undirected()

        else:
            pass  # no other cases yet

    elif data_type == "igraph":
        if case == 0:
            g = igraph.Graph.Erdos_Renyi(50, 0.05, directed=False, loops=False)
        elif case == 1:
            g = igraph.Graph.K_Regular(50, 6, directed=False, multiple=False)
        elif case == 2:
            g = igraph.Graph.Full(40, directed=False, loops=False)
        elif case == 3:
            g = igraph.Graph.Forest_Fire(80, 0.1, bw_factor=0.0, ambs=1, directed=False)
        elif case == 4:
            g = igraph.Graph.Barabasi(80, 2)

    # communities = g.community_multilevel()
    clusters = g.community_edge_betweenness().as_clustering()

    # membership vector
    # membership = clusters.membership

    if not g:
        dh = {
            "nodes": [],
            "edges": []
        }
    else:
        dh = DrawHelper(clusters, g.get_edgelist())

    return jsonify(dh.serialize)



if __name__ == '__main__':
    app.run(debug=True)