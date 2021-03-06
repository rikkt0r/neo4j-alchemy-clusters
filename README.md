# Clustering and Visualization of Neo4j #

### What's inside: ###

* Neo4J
* Python: Flask / py2neo / igraph
* JS: Alchemy.js + Alchemys' dependencies

Yep, it's an old academic project so don't expect clean code or design patterns

### Howto run: ###

```bash
# first of all unpack/run neo4j, then
aptitude install libigraph-dev
pip2 install virtualenv
> clone this repo
cd neo4j-alchemy-clusters
virtualenv -p /usr/bin/python2 env
source env/bin/activate
pip install -r requirements.txt
# change config however you like
python app.py
# done
```

### Neo4J Initialization (within code) ###
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
* http://jexp.de/blog/2014/03/quickly-create-a-100k-neo4j-graph-data-model-with-cypher-only/
* http://igraph.org/python/doc/igraph-module.html
* http://graphalchemist.github.io/Alchemy/#/examples
* https://www.cs.ucsb.edu/~xyan/classes/CS595D-2009winter/MCL_Presentation2.pdf
* http://py2neo.org/2.0/cypher.html

### Screens:

#### Choices
![Menu](readme/screen_menu.png)

#### Neo4J Visualization
![Neo4J](readme/screen_neo4j.png)

#### Erdor Renyi (random model)
![Erdos Renyi](readme/screen_erdos_renyi.png)

#### K-regular (random model)
![K-regular](readme/screen_k_regular.png)

#### Forest Fire (random model)
![Forest Fire](readme/screen_forest_fire.png)
