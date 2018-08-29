#!/usr/bin/python
#################################################
#Python Code
#@Author 		Sina Boroumand
#@Date			Aug 29, 2018
#@Affilation	CAS, Imperial College London
#################################################
#PCNF to WCNF parser
#@params	input_t:	*.aaig 	(AAIG output)
#			input_dot:	*.dot 	(aiger dot output)
#@return
#################################################

import sys
import os.path

# if len(sys.argv) == 1:
# 	print "Usage: dotFlag.py <aig> <dot>"
# 	quit()

# input_PCNF  = sys.argv[1]
input_PCNF  = "input.pcnf"

output_path = input_PCNF.split(".")[0]+".wcnf"

pyCNF_clauses = []
varibales_set = set()
variables = []

number_of_variables = 0
number_of_clauses = 0

#######################################################
print "------------------------------"
print "Opening PyCNF file..."

print "Reading PyCNF clauses..."
with open(input_PCNF, "rt") as fin_t:
	pyCNF_clauses = fin_t.readlines()

number_of_clauses = len(pyCNF_clauses)

#######################################################
# Finding Variables
print "Finding Variables..."
print "------------------------------"
temp_clauses = []

for clause in pyCNF_clauses:
	temp_clauses.append(clause.strip().split(" "))

# Removing duplicates
for clause in temp_clauses:
	for var in clause:
		varibales_set.add(var.strip("~"))

# Removing & character
varibales_set.remove("&")

# Sort the set
varibales_set = sorted(varibales_set)

# Convert to list
variables = list(varibales_set)

number_of_variables = len(variables)

#######################################################

print variables