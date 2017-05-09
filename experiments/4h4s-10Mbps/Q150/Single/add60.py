

i=0
with open("owd") as f:
	for line in f:
		line=line.split()
		l=line[0]
		# print l[0]
		# if i<23918:
		# 	print l, line[1]
		# elif i>23918 and i<45914:
		# 	st_l=float(l)+60
		# 	print st_l, line[1]
		# elif i>45914 and i<56306:
		# 	st_l=float(l)+120
		# 	print st_l, line[1]
		# elif i>56306:# and i<59769:
		# 	st_l=float(l)+180
		# 	print st_l, line[1]
		if i>=59768:
			st_l=float(l)-60
			print st_l, line[1]
		i=i+1



# ################################################
# i=0
# with open("s4_iat") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<23850:
# 			print l, line[1]
# 		elif i>23850 and i<45888:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>45888 and i<56284:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>56284:# and i<59741:
# 			st_l=float(l)+180
# 			print st_l, line[1]
# 		# elif i>59741:
# 		# 	st_l=float(l)+240
# 		# 	print st_l, line[1]
# 		i=i+1
# # #