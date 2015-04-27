# Visualization of neo4j clustering #

### What's inside: ###

* Neo4J
* Python: Flask / scipy / py2neo
* JS: Alchemy.js + Alchemys' dependencies

questions/comments: grzegorz-wojcicki@outlook.com

### Howto run: ###

```bash
# unpack/run neo4j
aptitude install libblas-dev liblapack-dev gfortran g++ libigraph-dev  
virtualenv alchemy-clustering
cd alchemy-clustering
source bin/activate
git checkout https://YOUR_USER@bitbucket.org/rikkt0r/alchemy-clusters.git
cd alchemy-clusters
pip install -r requirements.txt
# change config however you like
python2 app.py
# done
```

```neo4j

// remove all
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r

// Added 500 labels, created 500 nodes, set 1000 properties, statement executed in 127 ms.
WITH ["audi", "bmw", "ford", "mercedes", "nissan", "opel", "peugeot", "renault", "toyota", "volkswagen"]
AS names FOREACH (r IN range(0,499) | CREATE (:Car {id:r, name:names[r % size(names)]+" "+r}));

// Added 10 labels, created 10 nodes, set 20 properties, statement executed in 41 ms.
WITH ["hybrid engine", "spare wheel", "computer", "digital speedometer", "sunroof", "alarm", "abs", "esp", "asr", "muffler"]
AS names FOREACH (r IN range(0,9) | CREATE (:Part {id:r, name:names[r % size(names)]+" "+r}));

// Created 143 relationships, statement executed in 112 ms.
MATCH (c:Car),(p:Part) WITH c,p
LIMIT 5000 WHERE rand() < 0.1
CREATE (c)-[:HAS]->(p);

create index on :Car(id);
// Added 1 index, statement executed in 36 ms.

create index on :Part(id);
// Added 1 index, statement executed in 22 ms.


MATCH (p:Part)<-[r:HAS]-(c:Car) WHERE p.id = 9 OR c.id = 100 OR c.id = 111 RETURN r; // duzo!
MATCH (p:Part)<-[r:HAS]-(c:Car) WHERE c.id IN [10,15,22,545,346,500,123,54,78,456,345,333,444,222,111] RETURN r LIMIT 100;

MATCH (c)-[b:HAS]->(p) RETURN b, rand() as r ORDER BY r
```

### Links:
* http://arxiv.org/abs/0908.1062
* http://nicolewhite.github.io/2014/07/24/visualize-subset-neo4j-alchemy.html
* http://graphalchemist.github.io/Alchemy/#/examples
* http://stackoverflow.com/questions/1545606/python-k-means-algorithm
* https://www.cs.ucsb.edu/~xyan/classes/CS595D-2009winter/MCL_Presentation2.pdf
* http://jexp.de/blog/2014/03/quickly-create-a-100k-neo4j-graph-data-model-with-cypher-only/