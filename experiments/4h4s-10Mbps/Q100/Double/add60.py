

# i=0
# with open("owd") as f:
# 	for line in f:
# 		line=line.split()
# 		l=line[0]
# 		# print l[0]
# 		if i<9168:
# 			print l, line[1]
# 		elif i>9168 and i<37084:
# 			st_l=float(l)+60
# 			print st_l, line[1]
# 		elif i>37084 and i<51385:
# 			st_l=float(l)+120
# 			print st_l, line[1]
# 		elif i>51385 and i<58497:
# 			st_l=float(l)+180
# 			print st_l, line[1]
# 		elif i>58497:
# 			st_l=float(l)+240
# 			print st_l, line[1]
# 		i=i+1



# ################################################
i=0
with open("s4_iat") as f:
	for line in f:
		line=line.split()
		l=line[0]
		# print l[0]
		if i<9082:
			print l, line[1]
		elif i>9082 and i<37056:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>37056 and i<51367:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>51367 and i<58492:
			st_l=float(l)+180
			print st_l, line[1]
		elif i>58492:
			st_l=float(l)+240
			print st_l, line[1]
		i=i+1
#