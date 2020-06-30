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
import collections

# List to hold lines from raw fasta file 
sequencesDict = collections.defaultdict(int)

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
                sequencesDict[tempList[0]] = tempList[1:] # ID = key, sequence = value
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
        sequencesDict[tempList[0]] = tempList[1:] # ID = key, sequence = value

# k value to determine overlap match allowed
k = sys.argv[2]

# 