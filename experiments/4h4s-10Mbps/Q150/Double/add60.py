

# i=0
# with open("owd") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<20200:
# 			print l, line[1]
# 		elif i>20200 and i<41959:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>41959 and i<53701:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>53701:# and i<59769:
# 			st_l=float(l)+180
# 			print st_l, line[1]
# 		# elif i>59769:
# 		# 	st_l=float(l)+240
# 		# 	print st_l, line[1]
# 		i=i+1



# ################################################
i=0
with open("s4_iat") as f:
	for line in f:
		line=line.split()
		l=line[0]
		# print l[0]
		if i<20126:
			print l, line[1]
		elif i>20126 and i<41931:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>41931 and i<53667:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>53667:# and i<59741:
			st_l=float(l)+180
			print st_l, line[1]
		# elif i>59741:
		# 	st_l=float(l)+240
		# 	print st_l, line[1]
		i=i+1
#