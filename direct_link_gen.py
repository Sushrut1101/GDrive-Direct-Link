#!/bin/env python3

SHARED_LINK = input("Enter the GDrive View or Share URL: ")

tmp = SHARED_LINK.split(sep="/")

possible_ids = []

for i in tmp:
    if i in ["https:","http:","drive.google.com","drive","google","view","file","d"]:
        continue
    else:
        possible_ids.append(i)

for i in possible_ids:
    if "view" in i:
        possible_ids.remove(i)

if len(possible_ids)==1:
    ID = possible_ids[0]
