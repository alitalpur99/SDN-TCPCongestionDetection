

i=0
with open("s4_iat") as f:
	for line in f:
		line=line.split()
		l=line[0]
		# print l[0]
		if i<7943:
			print l, line[1]
		elif i>7943 and i<38691:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>38691 and i<52925:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>52925 and i<59769:
			st_l=float(l)+180
			print st_l, line[1]
		elif i>59769:
			st_l=float(l)+240
			print st_l, line[1]
		i=i+1



# ################################################
# i=0
# with open("s4_iat") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<9094:
# 			print l, line[1]
# 		elif i>9094 and i<39088:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>39088 and i<52990:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>52990 and i<59741:
# 			st_l=float(l)+180
# 			print st_l, line[1]
# 		elif i>59741:
# 			st_l=float(l)+240
# 			print st_l, line[1]
# 		i=i+1
# #