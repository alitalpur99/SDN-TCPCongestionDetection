

# i=0
# with open("owd") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<17548:
# 			print l, line[1]
# 		elif i>17548 and i<43236:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>43236 and i<55098:#:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>55098:# and i<59769:
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
		if i<17508:
			print l, line[1]
		elif i>17508 and i<43200:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>43200 and i<55087:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>55087:#and i<59741:
			st_l=float(l)+180
			print st_l, line[1]
		# elif i>59741:
		# 	st_l=float(l)+240
		# 	print st_l, line[1]
		i=i+1
#