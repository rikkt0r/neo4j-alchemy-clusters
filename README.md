# Visualization of neo4j clustering #

### What's inside: ###

* Neo4J
* Python: Flask / scipy / py2neo
* JS: Alchemy.js + Alchemys' dependencies

questions/comments: grzegorz-wojcicki@outlook.com

### Howto run: ###

```bash
# unpack/run neo4j
aptitude install libblas-dev liblapack-dev gfortran g++
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

WITH ["audi", "bmw", "ford", "mercedes", "nissan", "opel", "peugeot", "renault", "toyota", "volkswagen"]
AS names FOREACH (r IN range(0,20000) | CREATE (:Car {id:r, name:names[r % size(names)]+" "+r}));

// Added 20001 labels, created 20001 nodes, set 40002 properties, statement executed in 632 ms.

WITH ["hybrid engine", "spare wheel", "computer", "digital speedometer", "sunroof", "alarm", "abs", "esp", "asr", "muffler"]
AS names FOREACH (r IN range(0,9) | CREATE (:Part {id:r, name:names[r % size(names)]+" "+r}));

// Added 101 labels, created 101 nodes, set 202 properties, statement executed in 65 ms.

MATCH (c:Car),(p:Part) WITH c,p
LIMIT 150000 WHERE rand() < 0.1
CREATE (c)-[:HAS]->(p);

// Created 15136 relationships, statement executed in 659 ms.

create index on :Car(id);
// Added 1 index, statement executed in 36 ms.

create index on :Part(id);
// Added 1 index, statement executed in 22 ms.


MATCH (p:Part)<-[r:HAS]-(c:Car) WHERE p.id = 9 OR c.id = 100 OR c.id = 111 RETURN r; // duzo!
MATCH (p:Part)<-[r:HAS]-(c:Car) WHERE c.id IN [10,15,22,545,346,500,123,54,78,456,345,333,444,222,111] RETURN r LIMIT 100;


```