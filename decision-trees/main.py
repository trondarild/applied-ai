from readarff import *
from tree import *
from visualize import *
from decisiontree import *
from importance import *
from utils import argmax
from math import log
from prune import *

examples, attributes, classes = read_arff('restaurant-domain.arff')

tsttree = decision_tree_learning(examples, attributes, [], classes)
print 'before pruning'
visualize(tsttree)
expected = get_expected_values(examples, attributes, classes)
tsttree = prune(tsttree, examples, attributes, classes, expected)
print;print
print 'after pruning'
visualize(tsttree)
