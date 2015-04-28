# Visualization of neo4j clustering #

### What's inside: ###

* Neo4J
* Python: Flask / py2neo / igraph
* JS: Alchemy.js + Alchemys' dependencies

questions/comments/suggestions: grzegorz-wojcicki@outlook.com
Yep, it's an academic project so don't expect clean code or design patterns

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
![screen_menu.png](https://bitbucket.org/repo/ny4eKo/images/3556457875-screen_menu.png)

#### Neo4J Visualization
![screen_neo4j.png](https://bitbucket.org/repo/ny4eKo/images/21534593-screen_neo4j.png)

#### Erdor Renyi (random model)
![screen_erdos_renyi.png](https://bitbucket.org/repo/ny4eKo/images/2983531410-screen_erdos_renyi.png)

#### K-regular (random model)
![screen_k_regular.png](https://bitbucket.org/repo/ny4eKo/images/3519289190-screen_k_regular.png)

#### Forest Fire (random model)
![screen_forest_fire.png](https://bitbucket.org/repo/ny4eKo/images/2869420693-screen_forest_fire.png)