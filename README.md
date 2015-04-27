# Visualization of neo4j clustering #

### What's inside: ###

* Neo4J
* Python: Flask / py2neo / igraph
* JS: Alchemy.js + Alchemys' dependencies

questions/comments: grzegorz-wojcicki@outlook.com

### Howto run: ###

```bash
# first of all unpack/run neo4j, then
aptitude install libigraph-dev
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
MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r

// create cars/parts nodes
WITH ["audi", "bmw", "ford", "mercedes", "nissan", "opel", "peugeot", "renault", "toyota", "volkswagen"]
AS names FOREACH (r IN range(0,100) | CREATE (:Car {id:r, name:names[r % size(names)]+" "+r}));

// Added 10 labels, created 10 nodes, set 20 properties, statement executed in 41 ms.
WITH ["hybrid engine", "spare wheel", "computer", "digital speedometer", "sunroof", "alarm", "abs", "esp", "asr", "muffler"]
AS names FOREACH (r IN range(0,9) | CREATE (:Part {id:r, name:names[r % size(names)]+" "+r}));

// create some relationships
MATCH (c:Car),(p:Part) WITH c,p
LIMIT 800 WHERE rand() < 0.1
CREATE (c)-[:HAS]->(p);

// create indexes
create index on :Car(id);
create index on :Part(id);

```

### Links:
* http://arxiv.org/abs/0908.1062
* http://nicolewhite.github.io/2014/07/24/visualize-subset-neo4j-alchemy.html
* http://graphalchemist.github.io/Alchemy/#/examples
* http://stackoverflow.com/questions/1545606/python-k-means-algorithm
* https://www.cs.ucsb.edu/~xyan/classes/CS595D-2009winter/MCL_Presentation2.pdf
* http://jexp.de/blog/2014/03/quickly-create-a-100k-neo4j-graph-data-model-with-cypher-only/
* http://py2neo.org/2.0/cypher.html