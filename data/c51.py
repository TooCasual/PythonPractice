with open ('james.txt') as jaf:
	data = jaf.readline()
	james = data.strip().split(',')
with open ('julie.txt') as juf:
	data = juf.readline()
	julie = data.strip().split(',')
print(sorted(julie))
print(sorted(james))


def sanitize(time_string):
	if '-' in time_string:
		spliter = '-'
	elif ':' in time_string:
		spliter = ':'
	else: 
		return(time_string)
	(min, secs) = time_string.split(spliter)
	return(min + '.' + secs)

clean_james = []
clean_julie = []

for each_t in james:
	clean_james.append(sanitize(each_t))
for each_t in julie:
	clean_julie.append(sanitize(each_t))
print(sorted(clean_julie))
print(sorted(clean_james))

test = sorted(set(clean_julie))[0:3]
print(test)
