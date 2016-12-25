from re import findall
from codecs import open

file = open("2559_y1_s2.html", "r", "utf-8").read()
regex = 'faculty_id=\d\d&dept_id=x&curr_id=\d&curr2_id=.&year=\d{4}&semester=\d&class=\d{1,}'
raw_results = findall(regex, file) # a function from re module
final_results = []

for i in raw_results:
	if i not in final_results:
		final_results.append(i)

create_text_file = open("results.txt", "w")

for i in final_results:
	create_text_file.write(i + '\n')

create_text_file.close()
print("Found", len(final_results), "results.")
print("Results saved to results.txt")
