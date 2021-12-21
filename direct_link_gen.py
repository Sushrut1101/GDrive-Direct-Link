#!/bin/env python3

SHARED_LINK = input("Enter the GDrive View or Share URL: ")

tmp = SHARED_LINK.split(sep="/")

possible_ids = []

for i in tmp:
    if i in ["https:","http:","drive.google.com","drive","google","view"]:
        continue
    else:
        possible_ids.append(i)
