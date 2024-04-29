import networkx as nx
import pandas as pd
from pyvis.network import Network

# Sample data
data = {
    'source': ['A', 'B', 'C', 'A', 'D', 'B'],
    'target': ['B', 'C', 'A', 'D', 'E', 'E']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Creating a undirected graph (pyvis doesn't support directed graphs)
G = nx.from_pandas_edgelist(df, source='source', target='target')

# Create a pyvis network
net = Network(notebook=True)
net.from_nx(G)

# Show the network
net.show("test.html")
