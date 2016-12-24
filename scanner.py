from re import findall

webpage = open('2559_y1_s2.html', 'r').read()
regex = 'faculty_id=\d\d&dept_id=x&curr_id=\d&curr2_id=.&year=\d{4}&semester=\d&class=\d{1,}'
results = findall(regex, webpage) # a function from re module

for i in results:
	print(i)

print("Found", len(results), "results.")
