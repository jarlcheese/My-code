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
color_mapping = {
    "A": "red",
    "B": "blue",
    "C": "green",
    "D": "orange",
    "E": "purple"
}

# Create a figure for custom plotting
fig, ax = plt.subplots()

# Custom function to color the branches
def set_clade_colors(clade, color_dict):
    if clade.name in color_dict:
        clade.color = color_dict[clade.name]
    for child in clade.clades:
        set_clade_colors(child, color_dict)

# Apply colors to the tree
set_clade_colors(tree.root, color_mapping)

# Use Phylo's draw function with axes to handle colors
Phylo.draw(tree, axes=ax, branch_labels=lambda c: c.color if hasattr(c, 'color') else None)

# Customize drawing (to handle colors)
for clade in tree.find_clades():
    if hasattr(clade, 'color'):
        color = clade.color
        x = ax.get_position().x0
        y = ax.get_position().y0
        plt.plot([x, y], color=color)

# Display the plot
plt.show()