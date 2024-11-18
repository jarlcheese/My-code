from Bio import Phylo
import json

from matplotlib import pyplot as plt

# Read data from JSON file
with open('phylo.json', 'r') as file:
    data = json.load(file)

# Function to convert JSON data to Newick format
def json_to_newick(data):
    if 'children' in data:
        children = ','.join(json_to_newick(child) for child in data['children'])
        return f"({children}){data['name']}"
    else:
        return data['name']

# Convert JSON data to Newick format
newick_string = json_to_newick(data)

# Write Newick string to a file
with open('tree.newick', 'w') as file:
    file.write(newick_string + ';')

# Read the Newick file using Biopython's Phylo module
tree = Phylo.read('tree.newick', 'newick')


# Customizing colors
for n in tree.find_clades():
    if n.name == "A":
        n.color = "red"
    elif n.name == "B":
        n.color = "blue"
    elif n.name == "C":
        n.color = "green"
    elif n.name == "D":
        n.color = "orange"
    elif n.name == "E":
        n.color = "purple"

# Draw the tree
Phylo.draw(tree)
