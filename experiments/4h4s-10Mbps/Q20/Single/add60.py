

# i=0
# with open("owd") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<33982:
# 			print l, line[1]
# 		elif i>33982 and i<50586:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>50586 and i<58439:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>58439:# and i<59769:
# 			st_l=float(l)+180
# 			print st_l, line[1]
# 		# elif i>59769:
# 		# 	st_l=float(l)+240
# 		# 	print st_l, line[1]
# 		i=i+1



################################################
i=0
with open("s4_iat") as f:
	for line in f:
		line=line.split()
		l=line[0]
		# print l[0]
		if i<33973:
			print l, line[1]
		elif i>33973 and i<50583:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>50583 and i<58438:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>58438:# and i<59741:
			st_l=float(l)+180
			print st_l, line[1]
		# elif i>59741:
		# 	st_l=float(l)+240
		# 	print st_l, line[1]
		i=i+1
#