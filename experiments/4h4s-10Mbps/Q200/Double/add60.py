

# i=0
# with open("owd") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<21051:
# 			print l, line[1]
# 		elif i>21051 and i<35890:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>35890 and i<44619:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>44619:# and i<59769:
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
		if i<21019:
			print l, line[1]
		elif i>21019 and i<35862:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>35862 and i<44600:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>44600:# and i<59741:
			st_l=float(l)+180
			print st_l, line[1]
		# elif i>59741:
		# 	st_l=float(l)+240
		# 	print st_l, line[1]
		i=i+1
#