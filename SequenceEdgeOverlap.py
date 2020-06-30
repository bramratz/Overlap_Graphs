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
from typing import List

# Function for finding pairs of nodes, s and t, that are connected by a direct
#   edge as determined by k number of bases at the end of seq s that match 
#   k number of bases at the beginning of sequence t that are exact matches 
def findDirectEdges(seqIDs: List, seqList: List, k: int) -> List:
    """
    Given a list of sequence ID's and a list of corresponding sequences
    and a value k which determines the overlap between sequence s and t,
    returns an adjacency list of all pairs nodes that share a directed 
    edge. 
    """
    pairs = [] # List to hold pairs of nodes connected by direct edge 
    # Iterate each list item and compare to every other list item excatly once
    for seq1 in range(len(seqList)):
        suffix = seqList[seq1][-k:] # last bases of seq1 trying to match 
        for seq2 in range(seq1 + 1, len(seqList)):
            prefix = seqList[seq2][:k] # first bases of seq2 trying to match 
            if suffix == prefix: # Append pair of IDs if match is found 
                pairs.append(seqIDs[seq1] + " " + seqIDs[seq2])
    return pairs # return list of pairs 
            
# List to hold lines from raw fasta file 
IDs = []
sequence = []

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
                IDs.append(tempList[0][1:]) # Append sequence ID to IDs list. Remove '>'
                sequence.append(tempList[1:]) # Append sequence to sequence list 
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
        IDs.append(tempList[0][1:]) # Append sequence ID to IDs list. Remove '>'
        sequence.append(tempList[1:]) # Append sequence to sequence list 

# k value to determine overlap match allowed
k = int(sys.argv[2])

# Find nodes connected with direct edges
res = findDirectEdges(IDs, sequence, k) 
for x in range(len(res)): 
    print(res[x])