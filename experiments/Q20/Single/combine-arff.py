"""This script combines all of the result file, and generates a single .arff file"""
l1=[]
l2=[]
l3=[]
l4=[]


## Open and append owd loss result file
with open("owd-loss-results") as f1:
	for line1 in f1:
		l1.append(line1)


# print l1[1]
# print l1[1][:-3]

## Open and append iat loss result file
with open("iat-loss-results") as f2:
	for line2 in f2:
		l2.append(line2)


## Open and append owd no-loss result file
with open("owd-noloss-results") as f3:
	for line3 in f3:
		
		# line3.strip()
		l3.append(line3)	

## Open and append iat no-loss result file
with open("iat-noloss-results") as f4:
	for line4 in f4:
		# line4.strip()
		l4.append(line4)


## write to a new file
open("all.arff","w").close()

with open("all.arff","w") as wf:
	for i in range(len(l1)):
		# print l1[i]+l2[i]
		wf.write(l1[i][:-2]+l2[i])
with open("all.arff","a") as wf:
	# wf.write("\n")
	for i in range(len(l3)):
		# print l3[i]+l4[i]
		wf.write(l3[i][:-2]+l4[i])
# print len(l1), len(l2), len(l3), len(l4)