# Visualization of neo4j clustering #

### What's inside: ###

* Neo4J
* Python: Flask / scipy
* JS: Alchemy.js + Alchemys' dependencies

questions/comments: grzegorz-wojcicki@outlook.com

### Howto run: ###

```bash
# unpack/run neo4j
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