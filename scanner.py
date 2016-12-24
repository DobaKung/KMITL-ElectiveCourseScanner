#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import findall
import codecs

file = codecs.open("2559_y1_s2.html", "r", "utf-8")
webpage = file.read()
regex = 'faculty_id=\d\d&dept_id=x&curr_id=\d&curr2_id=.&year=\d{4}&semester=\d&class=\d{1,}'
results = findall(regex, webpage) # a function from re module
create_text_file = open("results.txt", "w")
for i in results:
	create_text_file.write(i)
create_text_file.close()
print("Found", len(results), "results.")
