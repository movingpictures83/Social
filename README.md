# Social
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy_1.16.0

PluMA plugin that outputs all edge weights for a series of social clubs
in a network, their mean edge weight, along with standard deviation.

The plugin accepts as input a parameter file of keyword-value pairs:
clusterfile: Cluster CSV file
corfile: CSV file of network where entry (i, j) is the weight of edge (i, j)

Data on social clubs will be output as a TXT file
