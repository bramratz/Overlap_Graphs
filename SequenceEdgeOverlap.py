#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a fasta file returns an adjacency list of strings each representing 
a node where pairs, s and t, are connected with a directed edge when there
is a length k suffix of s that matches a length k prefix of t

Created on Tue Jun 30 10:20:19 2020
@author: bram
"""

# Import modules 
import sys
from typing import List, Dict
from collections import defaultdict
from itertools import combinations

# Function: Checks if suffix of sequence1 matches prefix of sequence2
#   by k-overlapping characters 
def overlap(seq1: str, seq2: str, k: int) -> bool:
    """
    Given two sequences and an integar returns True if the suffix of 
    seq1 overlaps the prefix of seq2 by k. This is equivalent to a 
    directed edge.
    """
    return seq1[-k:] == seq2[:k]

# Function for finding pairs of nodes, s and t, that are connected by a direct
#   edge as determined by k number of bases at the end of seq s that match 
#   k number of bases at the beginning of sequence t that are exact matches 
def findDirectEdges(sequences: Dict, k: int) -> List:
    """
    Given a dictionary of sequence ID's and corresponding sequences
    and a value k which determines the overlap between sequence s and t,
    returns an adjacency list of all pairs nodes that share a directed 
    edge. 
    """
    pairs = [] # List to hold pairs of nodes connected by direct edge 
    # Find all combinations of DNA sequences in the sequence dictionary
    for s, t in combinations(sequences, 2):
        sSeq, tSeq = sequences[s], sequences[t]
        # If suffix of sSeq and prefix of tSeq overlap, or vice versa
        #   append the pair of sequence IDs to pairs list
        if overlap(sSeq, tSeq, k):
            pairs.append(s + " " + t)
        if overlap(tSeq, sSeq, k):
            pairs.append(s + " " + t)
    return pairs # return list of pairs 
            
# List to hold lines from raw fasta file 
seqFromFasta = defaultdict(int)

# Open and parse input file
with open(sys.argv[1]) as f:
    lines = [item.strip() for item in f.readlines() if not item == '']
    tempList = [] # list for sequences associated with each ID. Solves sequences on multiple lines issue.
    for line in lines:
        # All Lines with sequence IDs start with '>'
        if line.startswith('>'):
            # If sequences in temp when new ID reached add sequences to main 
            # list and empty tempList 
            if not len(tempList) == 0:
                seqFromFasta[tempList[0][1:]] = tempList[1:] # ID = key, sequence = value
                tempList = [line,] # Empty List, Add new ID to it 
            # Add seq ID to list if it's the first sequence ID
            else:
                tempList = [line,]
        # Add sequences to the tempList if no ID is encountered
        else:
            for char in line:
                if char == "\n":
                    pass
                else:
                    tempList.append(char)
    # Handles sequence for last ID
    else:
        seqFromFasta[tempList[0][1:]] = tempList[1:] # ID = key, sequence = value

# k value to determine overlap match allowed
k = int(sys.argv[2])

# Find nodes connected with direct edges
res = findDirectEdges(seqFromFasta, k) 
for x in range(len(res)): 
    print(res[x])