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

WITH ["audi", "bmw", "form", "mercedes", "nissan", "opel", "peugeot", "renault", "toyota", "wolksvagen"]
AS names FOREACH (r IN range(0,20000) | CREATE (:Car {id:r, name:names[r % size(names)]+" "+r}));

WITH ["engine", "wheels", "dashboard", "speedometer", "sunroof", "alarm", "abs", "esp", "asr", "muffler"]
AS names FOREACH (r IN range(0,100) | CREATE (:Part {id:r, name:names[r % size(names)]+" "+r}));

// Added 20001 labels, created 20001 nodes, set 40002 properties, statement executed in 20211 ms.
```