import os
import re
import subprocess

repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Knowledge-Graph-Platform"
os.chdir(repo_dir)

def git_commit(msg):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", msg])

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Added github stars and sorted the opensource based on that
opensource_section = """## Open-Source GitHub Projects

- **[Dgraph](https://github.com/dgraph-io/dgraph)** [![Stars](https://img.shields.io/github/stars/dgraph-io/dgraph?style=social&color=white)](https://github.com/dgraph-io/dgraph/stargazers)
  Native distributed graph database with GraphQL-native interface, high performance, and horizontal scalability (now fully Apache 2.0).

- **[ArangoDB](https://github.com/arangodb/arangodb)** [![Stars](https://img.shields.io/github/stars/arangodb/arangodb?style=social&color=white)](https://github.com/arangodb/arangodb/stargazers)
  Multi-model open-source database supporting graphs, documents, and key-value with a unified query language (AQL); Community Edition available.

- **[Memgraph](https://github.com/memgraph/memgraph)** [![Stars](https://img.shields.io/github/stars/memgraph/memgraph?style=social&color=white)](https://github.com/memgraph/memgraph/stargazers)
  High-performance open-source (BSL) in-memory graph database with Cypher, built-in algorithms (MAGE), vector search, and strong real-time/GraphRAG focus.

- **[JanusGraph](https://github.com/JanusGraph/janusgraph)** [![Stars](https://img.shields.io/github/stars/JanusGraph/janusgraph?style=social&color=white)](https://github.com/JanusGraph/janusgraph/stargazers)
  Highly scalable, distributed open-source property graph database (Apache TinkerPop/Gremlin) with pluggable storage (Cassandra, HBase, etc.) and indexing backends.

- **[TerminusDB](https://github.com/terminusdb/terminusdb)** [![Stars](https://img.shields.io/github/stars/terminusdb/terminusdb?style=social&color=white)](https://github.com/terminusdb/terminusdb/stargazers)
  Open-source document + knowledge graph database with Git-like versioning (branch, diff, merge, time-travel), GraphQL, and WOQL (Datalog-style) query language.

- **[Apache Jena / Fuseki](https://github.com/apache/jena)** [![Stars](https://img.shields.io/github/stars/apache/jena?style=social&color=white)](https://github.com/apache/jena/stargazers)
  Comprehensive open-source Java framework for Semantic Web and Linked Data applications, including TDB storage, SPARQL engine, and Fuseki SPARQL server.

- **[Oxigraph](https://github.com/oxigraph/oxigraph)** [![Stars](https://img.shields.io/github/stars/oxigraph/oxigraph?style=social&color=white)](https://github.com/oxigraph/oxigraph/stargazers)
  Fast, standards-compliant RDF graph database and SPARQL toolkit written in Rust (RocksDB-backed), with Python and JavaScript bindings.

- **[ArcadeDB](https://github.com/ArcadeData/arcadedb)** [![Stars](https://img.shields.io/github/stars/ArcadeData/arcadedb?style=social&color=white)](https://github.com/ArcadeData/arcadedb/stargazers)
  Fully open-source (Apache 2.0) multi-model database supporting graphs, documents, key-value, time-series, and vectors with SQL, Cypher, Gremlin, and GraphQL.

- **[Protégé](https://github.com/protegeproject/protege)** [![Stars](https://img.shields.io/github/stars/protegeproject/protege?style=social&color=white)](https://github.com/protegeproject/protege/stargazers)
  The leading free, open-source ontology editor supporting OWL 2, with desktop and collaborative WebProtégé versions for ontology engineering.

- **[Blazegraph](https://github.com/blazegraph/database)** [![Stars](https://img.shields.io/github/stars/blazegraph/database?style=social&color=white)](https://github.com/blazegraph/database/stargazers)
  High-performance open-source RDF/SPARQL and property graph database (powers Wikidata Query Service); note: development largely paused after AWS acquisition of the team.

- **[OpenLink Virtuoso (Open Source Edition)](https://github.com/openlink/virtuoso-opensource)** [![Stars](https://img.shields.io/github/stars/openlink/virtuoso-opensource?style=social&color=white)](https://github.com/openlink/virtuoso-opensource/stargazers)
  High-performance multi-model RDBMS and RDF triple store with SPARQL, Linked Data deployment, and data integration capabilities.

- **[Eclipse RDF4J](https://github.com/eclipse-rdf4j/rdf4j)** [![Stars](https://img.shields.io/github/stars/eclipse-rdf4j/rdf4j?style=social&color=white)](https://github.com/eclipse-rdf4j/rdf4j/stargazers)
  Scalable Java framework for RDF processing, storage, reasoning, and querying with a vendor-neutral Repository API and SPARQL support.

- **[QLever](https://github.com/ad-freiburg/qlever)** [![Stars](https://img.shields.io/github/stars/ad-freiburg/qlever?style=social&color=white)](https://github.com/ad-freiburg/qlever/stargazers)
  Extremely fast SPARQL engine and RDF triplestore that scales to hundreds of billions (and beyond) of triples on a single commodity machine, with full-text and GeoSPARQL support."""

content = re.sub(r'## Open-Source GitHub Projects.*?### Additional Strong Open-Source Options', opensource_section + '\n\n### Additional Strong Open-Source Options', content, flags=re.DOTALL)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("Added github stars and sorted the opensource based on that")

# 2. Add banner
os.makedirs("assets", exist_ok=True)
svg_banner = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#2a0845" />
            <stop offset="100%" stop-color="#6441A5" />
        </linearGradient>
    </defs>
    <rect width="800" height="200" fill="url(#bg)" rx="15" ry="15"/>
    <text x="400" y="100" font-family="Arial, sans-serif" font-size="42" font-weight="bold" fill="#ffffff" text-anchor="middle" dominant-baseline="middle">
        Awesome Knowledge Graph Platform
        <animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite" />
    </text>
    <text x="400" y="150" font-family="Arial, sans-serif" font-size="18" fill="#e0e0e0" text-anchor="middle" dominant-baseline="middle">
        Curated list of Semantic, GraphRAG, and Enterprise Data Tools
    </text>
</svg>'''
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_banner)

content = "![Banner](assets/banner.svg)\n" + content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("added banner")

# 3. Add Emojis
content = content.replace("## Top Knowledge Graph Platforms Ecosystem", "## 🌟 Top Knowledge Graph Platforms Ecosystem")
content = content.replace("## Table of Contents", "## 📚 Table of Contents")
content = content.replace("## SaaS/Hosted Platforms", "## ☁️ SaaS/Hosted Platforms")
content = content.replace("## Open-Source GitHub Projects", "## 💻 Open-Source GitHub Projects")
content = content.replace("## How to Contribute", "## 🤝 How to Contribute")
content = content.replace("## Disclaimer", "## ⚠️ Disclaimer")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("added emojis")

# 4. SEO Optimised
# Add meta keywords in a comment at the top for some SEO, or expand title
content = "<!-- Keywords: Knowledge Graph, Graph Database, Semantic Web, Ontology, GraphRAG, Neo4j, RDF, SPARQL, SaaS, Open Source -->\n" + content
content = content.replace("# Awesome-Knowledge-Graph-Platform", "# Awesome Knowledge Graph Platform - The Ultimate Graph Database Guide")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("seo optimised")

# 5. Badges to left added
badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a> '
content = content.replace("# Awesome Knowledge Graph Platform", badges_left + "# Awesome Knowledge Graph Platform")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("badges to left added")

# 6. Badges to right added
badge_right = ' <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
content = content.replace("Awesome Knowledge Graph Platform - The Ultimate Graph Database Guide", "Awesome Knowledge Graph Platform - The Ultimate Graph Database Guide" + badge_right)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("badges to right added")

# 7. Star history added
star_history = """

## 📈 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Knowledge-Graph-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Knowledge-Graph-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Knowledge-Graph-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Knowledge-Graph-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("star history added")

# 8. Fixed star plot
content = content.replace("chartrepos", "chart?repos")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("fixed star plot")

# 9. Invalid awesome link fixed
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
git_commit("invalid awesome link fixed")

print("Done with script")
