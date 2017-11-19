"""This script is used to automatically take the values of Oneway delay (loss and no-loss cases) from a file"""


import numpy
import numpy as np
import peakutils
from peakutils.plot import plot as pplot
import matplotlib.pyplot as plt
from matplotlib import pyplot

d=[]
t=[]

"""Open the One-way delay file and append time and delay values"""

with open("owd-new") as f:
	for l in f:
		l=l.split()
		t.append(float(l[0]))
		d.append(float(l[1]))

""" Convert into np arrays"""
delay=np.array(d)
t=np.array(t)

""" For Smoothing the curve (not using)"""
# #def smooth(y, box_pts):
# #    box = np.ones(box_pts)/box_pts
# #    # print box
# #    y_smooth = np.convolve(y, box, mode='same')
# #    # print "ysmooth",y_smooth
# #    return y_smooth

""" Find the peak values, (tweak to find the approx peak value)"""

indexes = peakutils.indexes(delay, thres=0.855, min_dist=500)
# ii=indexes
print "Total peaks found: \n", len(indexes)
print "Peaks found at (indexed values): \n",indexes
time=t[indexes]
values=delay[indexes]
print "\n time:",t[indexes],"\n values", delay[indexes]

"""TAKING THE VALUES OF WINDOW INDEXES THAT HAVE LARGE GAPS"""

win_index=[]

""" Diff of the windows: take window if the gap is large enough"""

diff= [j-i for i, j in zip(indexes[:-1], indexes[1:])]
print "differences between indexed values: \n",diff
for i in range(len(diff)):
	if values[i]>=0.024 and diff[i]>=700:
		# print indexes[i+1]
		win_index.append(indexes[i+1])

"""LIST OF SELECTED PEAK INDEXES"""

print "\n selected number of peaks", len(win_index)
print "\n selected Window Peaks at (indexes): \n",win_index
# plt.plot(t, delay,'ko')
# pplot(t, delay, indexes)
# plt.show()

"""to randomize the index selection for noloss"""
win11=int((win_index[0]+win_index[1])*0.5)
win21=int((win_index[1]+win_index[2])*0.5)
win31=int((win_index[2]+win_index[3])*0.5)
win41=int((win_index[3]+win_index[4])*0.5)
win51=int((win_index[4]+win_index[5])*0.5)
win61=int((win_index[5]+win_index[6])*0.5)
win71=int((win_index[6]+win_index[7])*0.5)
win81=int((win_index[7]+win_index[8])*0.5)
win91=int((win_index[8]+win_index[9])*0.5)
win101=int((win_index[9]+win_index[10])*0.5)
win111=int((win_index[10]+win_index[11])*0.5)
win121=int((win_index[11]+win_index[12])*0.5)
win131=int((win_index[12]+win_index[13])*0.5)

win141=int((win_index[13]+win_index[14])*0.5)
win151=int((win_index[14]+win_index[15])*0.5)
win161=int((win_index[15]+win_index[16])*0.5)
win171=int((win_index[16]+win_index[17])*0.5)
win181=int((win_index[17]+win_index[18])*0.5)

win191=int((win_index[18]+win_index[19])*0.5)
win201=int((win_index[19]+win_index[20])*0.5)

win211=int((win_index[20]+win_index[21])*0.5)
win221=int((win_index[21]+win_index[22])*0.5)
win231=int((win_index[22]+win_index[23])*0.5)
win241=int((win_index[23]+win_index[24])*0.5)
win251=int((win_index[24]+win_index[25])*0.5)
win261=int((win_index[25]+win_index[26])*0.5)
win271=int((win_index[26]+win_index[27])*0.5)
win281=int(0.7*(win_index[1]-win_index[0]))


# print "win101",win101
"""Since onlyTake diff, and the 2/3 of it, and then add it to first window"""
# win111_1= 0.35*(win_index[1]-win_index[0])
# print "win111", int(win111_1)
# win=int(win111_1)

"""adding no loss ploting"""
nolosswin=[win11, win21, win31, win41, win51, win61, win71, win81, win91, win101, win111]#,win121]#, win131, win141]#, win151, win161, win171, win181]
print "\n selected NoLoss points at (nolosswin): \n",len(nolosswin),nolosswin
print "index-val \t Diff \t Time \t Delay  "
for i in range(len(indexes)):
	if i > 0:
		print str(i)+" "+str(indexes[i])+" \t\t"+str(diff[i-1]) +"  "+str(time[i])+"  "+str(values[i])
	else:
		print str(i)+" "+str(indexes[i])+" \t\t "+str("000") +"  "+str(time[i])+"  "+str(values[i])

#####################################################################

#####################################################################
"""Open the IAT file and append the values of IAT values to a list"""
iat=[]
tt=[]
with open("s4_iat-new") as f:
	for l in f:
		l=l.split()
		tt.append(float(l[0]))
		iat.append(float(l[1]))
#########################################################################
""" CALCULATION FOR WINDOWS"""
"""LOSS # 1"""
print "Loss # 1"

"""TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind11=win11-300
ind12=win11-150
ind13=win11

print "\n index number for Loss 1", ind11, ind12, ind13

""" CALCULATION FOR FIRST PEAK PARAMETERS (WIN 1,2,3)"""
owd11=[]
owd12=[]
owd13=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind11 and nn<ind12:
		owd11.append(iat[nn])
	elif nn>=ind12 and nn<ind13:
		owd12.append(iat[nn])
	elif nn>=ind13 and nn<ind13+150:
		owd13.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd11"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd11))
""" owd11 avg"""
print 'mean11 = {}'.format(numpy.mean(owd11))
"""owd11 min"""
print 'min11 = {}'.format(min(owd11))
"""owd11 max"""
print 'max11 = {}'.format(max(owd11))
""" owd11 std"""
print 'std11 = {}'.format(numpy.std(owd11))

"""for owd12"""
print "number of packets included = {}".format(len(owd12))
print 'mean12 = {}'.format(numpy.mean(owd12))
print 'min12 = {}'.format(min(owd12))
print 'max12 = {}'.format(max(owd12))
print 'std12 = {}'.format(numpy.std(owd12))

""" for owd13"""
print "number of packets included = {}".format(len(owd13))
print 'mean13 = {}'.format(numpy.mean(owd13))
print 'min13 = {}'.format(min(owd13))
print 'max13 = {}'.format(max(owd13))
print 'std13 = {}'.format(numpy.std(owd13))


""" next take the Window3/Window1""" 
a1 = numpy.mean(owd13)/numpy.mean(owd11)
a2 = numpy.mean(owd13)/numpy.min(owd11)
a3 = numpy.mean(owd13)/numpy.max(owd11)

a4 = numpy.min(owd13)/numpy.mean(owd11)
a5 = numpy.min(owd13)/numpy.min(owd11)
a6 = numpy.min(owd13)/numpy.max(owd11)

a7 = numpy.max(owd13)/numpy.mean(owd11)
a8 = numpy.max(owd13)/numpy.min(owd11)
a9 = numpy.max(owd13)/numpy.max(owd11)

"""next take the Window3/Window2"""
a10 = numpy.mean(owd13)/numpy.mean(owd12)
a11 = numpy.mean(owd13)/numpy.min(owd12)
a12 = numpy.mean(owd13)/numpy.max(owd12)

a13 = numpy.min(owd13)/numpy.mean(owd12)
a14 = numpy.min(owd13)/numpy.min(owd12)
a15 = numpy.min(owd13)/numpy.max(owd12)

a16 = numpy.max(owd13)/numpy.mean(owd12)
a17 = numpy.max(owd13)/numpy.min(owd12)
a18 = numpy.max(owd13)/numpy.max(owd12)

""" min/max window 3"""
a19 = numpy.min(owd13)/numpy.max(owd13)

"""standard dev values"""
a20 = numpy.std(owd13)/numpy.std(owd11)
a21 = numpy.std(owd13)/numpy.std(owd12)
a22 = numpy.std(owd11)/numpy.std(owd12)

"""next window1 / window2"""
a23 = numpy.mean(owd11)/numpy.mean(owd12)
a24 = numpy.mean(owd11)/numpy.min(owd12)
a25 = numpy.mean(owd11)/numpy.max(owd12)

a26 = numpy.min(owd11)/numpy.mean(owd12)
a27 = numpy.min(owd11)/numpy.min(owd12)
a28 = numpy.min(owd11)/numpy.max(owd12)

a29 = numpy.max(owd11)/numpy.mean(owd12)
a30 = numpy.max(owd11)/numpy.min(owd12)
a31 = numpy.max(owd11)/numpy.max(owd12)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(a1)+"\n"
print "avg-win3 / min-win1 = "+ str(a2)+"\n"
print "avg-win3 / max-win1 = "+ str(a3)+"\n"

print "min-win3 / avg-win1 = "+ str(a4)+"\n"
print "min-win3 / min-win1 = "+ str(a5)+"\n"
print "min-win3 / max-win1 = "+ str(a6)+"\n"

print "max-win3 / avg-win1 = "+ str(a7)+"\n"
print "max-win3 / min-win1 = "+ str(a8)+"\n"
print "max-win3 / max-win1 = "+ str(a9)+"\n"

"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(a10)+"\n"
print "avg-win3 / min-win2 = "+ str(a11)+"\n"
print "avg-win3 / max-win2 = "+ str(a12)+"\n"

print "min-win3 / avg-win2 = "+ str(a13)+"\n"
print "min-win3 / min-win2 = "+ str(a14)+"\n"
print "min-win3 / max-win2 = "+ str(a15)+"\n"

print "max-win3 / avg-win2 = "+ str(a16)+"\n"
print "max-win3 / min-win2 = "+ str(a17)+"\n"
print "max-win3 / max-win2 = "+ str(a18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(a19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(a20)+"\n"
print "std-win3 / std-win2 = "+ str(a21)+"\n"
print "std-win1 / std-win2 = "+ str(a22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(a23)+"\n"
print "avg-win1 / min-win2 = "+ str(a24)+"\n"
print "avg-win1 / max-win2 = "+ str(a25)+"\n"

print "min-win1 / avg-win2 = "+ str(a26)+"\n"
print "min-win1 / min-win2 = "+ str(a27)+"\n"
print "min-win1 / max-win2 = "+ str(a28)+"\n"

print "max-win1 / avg-win2 = "+ str(a29)+"\n"
print "max-win1 / min-win2 = "+ str(a30)+"\n"
print "max-win1 / max-win2 = "+ str(a31)+"\n"

print "##################################################"


"""LOSS # 2"""
print "Loss # 2"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind21=win21-300
ind22=win21-150
ind23=win21

print "\n index number for Loss 2", ind21, ind22, ind23

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd21=[]
owd22=[]
owd23=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind21 and nn<ind22:
		owd21.append(iat[nn])
	elif nn>=ind22 and nn<ind23:
		owd22.append(iat[nn])
	elif nn>=ind23 and nn<ind23+150:
		owd23.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd21"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd21))
""" owd21 avg"""
print 'mean21 = {}'.format(numpy.mean(owd21))
"""owd21 min"""
print 'min21 = {}'.format(min(owd21))
"""owd21 max"""
print 'max21 = {}'.format(max(owd21))
""" owd21 std"""
print 'std21 = {}'.format(numpy.std(owd21))

"""for owd22"""
print "number of packets included = {}".format(len(owd22))
print 'mean22 = {}'.format(numpy.mean(owd22))
print 'min22 = {}'.format(min(owd22))
print 'max22 = {}'.format(max(owd22))
print 'std22 = {}'.format(numpy.std(owd22))

""" for owd23"""
print "number of packets included = {}".format(len(owd23))
print 'mean23 = {}'.format(numpy.mean(owd23))
print 'min23 = {}'.format(min(owd23))
print 'max23 = {}'.format(max(owd23))
print 'std23 = {}'.format(numpy.std(owd23))


""" next take the Window3/Window1""" 
b1 = numpy.mean(owd23)/numpy.mean(owd21)
b2 = numpy.mean(owd23)/numpy.min(owd21)
b3 = numpy.mean(owd23)/numpy.max(owd21)

b4 = numpy.min(owd23)/numpy.mean(owd21)
b5 = numpy.min(owd23)/numpy.min(owd21)
b6 = numpy.min(owd23)/numpy.max(owd21)

b7 = numpy.max(owd23)/numpy.mean(owd21)
b8 = numpy.max(owd23)/numpy.min(owd21)
b9 = numpy.max(owd23)/numpy.max(owd21)

"""next take the Window3/Window2"""
b10 = numpy.mean(owd23)/numpy.mean(owd22)
b11 = numpy.mean(owd23)/numpy.min(owd22)
b12 = numpy.mean(owd23)/numpy.max(owd22)

b13 = numpy.min(owd23)/numpy.mean(owd22)
b14 = numpy.min(owd23)/numpy.min(owd22)
b15 = numpy.min(owd23)/numpy.max(owd22)

b16 = numpy.max(owd23)/numpy.mean(owd22)
b17 = numpy.max(owd23)/numpy.min(owd22)
b18 = numpy.max(owd23)/numpy.max(owd22)

""" min/max window 3"""
b19 = numpy.min(owd23)/numpy.max(owd23)

"""standard dev values"""
b20 = numpy.std(owd23)/numpy.std(owd21)
b21 = numpy.std(owd23)/numpy.std(owd22)
b22 = numpy.std(owd21)/numpy.std(owd22)

"""next window1 / window2"""
b23 = numpy.mean(owd21)/numpy.mean(owd22)
b24 = numpy.mean(owd21)/numpy.min(owd22)
b25 = numpy.mean(owd21)/numpy.max(owd22)

b26 = numpy.min(owd21)/numpy.mean(owd22)
b27 = numpy.min(owd21)/numpy.min(owd22)
b28 = numpy.min(owd21)/numpy.max(owd22)

b29 = numpy.max(owd21)/numpy.mean(owd22)
b30 = numpy.max(owd21)/numpy.min(owd22)
b31 = numpy.max(owd21)/numpy.max(owd22)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(b1)+"\n"
print "avg-win3 / min-win1 = "+ str(b2)+"\n"
print "avg-win3 / max-win1 = "+ str(b3)+"\n"

print "min-win3 / avg-win1 = "+ str(b4)+"\n"
print "min-win3 / min-win1 = "+ str(b5)+"\n"
print "min-win3 / max-win1 = "+ str(b6)+"\n"

print "max-win3 / avg-win1 = "+ str(b7)+"\n"
print "max-win3 / min-win1 = "+ str(b8)+"\n"
print "max-win3 / max-win1 = "+ str(b9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(b10)+"\n"
print "avg-win3 / min-win2 = "+ str(b11)+"\n"
print "avg-win3 / max-win2 = "+ str(b12)+"\n"

print "min-win3 / avg-win2 = "+ str(b13)+"\n"
print "min-win3 / min-win2 = "+ str(b14)+"\n"
print "min-win3 / max-win2 = "+ str(b15)+"\n"

print "max-win3 / avg-win2 = "+ str(b16)+"\n"
print "max-win3 / min-win2 = "+ str(b17)+"\n"
print "max-win3 / max-win2 = "+ str(b18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(b19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(b20)+"\n"
print "std-win3 / std-win2 = "+ str(b21)+"\n"
print "std-win1 / std-win2 = "+ str(b22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(b23)+"\n"
print "avg-win1 / min-win2 = "+ str(b24)+"\n"
print "avg-win1 / max-win2 = "+ str(b25)+"\n"

print "min-win1 / avg-win2 = "+ str(b26)+"\n"
print "min-win1 / min-win2 = "+ str(b27)+"\n"
print "min-win1 / max-win2 = "+ str(b28)+"\n"

print "max-win1 / avg-win2 = "+ str(b29)+"\n"
print "max-win1 / min-win2 = "+ str(b30)+"\n"
print "max-win1 / max-win2 = "+ str(b31)+"\n"

print "##################################################"


"""LOSS # 3"""
print "Loss # 3"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind31=win31-300
ind32=win31-150
ind33=win31

print "\n index number for Loss 3", ind31, ind32, ind33

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd31=[]
owd32=[]
owd33=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind31 and nn<ind32:
		owd31.append(iat[nn])
	elif nn>=ind32 and nn<ind33:
		owd32.append(iat[nn])
	elif nn>=ind33 and nn<ind33+150:
		owd33.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd31"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd31))
""" owd31 avg"""
print 'mean31 = {}'.format(numpy.mean(owd31))
"""owd31 min"""
print 'min31 = {}'.format(min(owd31))
"""owd31 max"""
print 'max31 = {}'.format(max(owd31))
""" owd31 std"""
print 'std31 = {}'.format(numpy.std(owd31))

"""for owd32"""
print "number of packets included = {}".format(len(owd32))
print 'mean32 = {}'.format(numpy.mean(owd32))
print 'min32 = {}'.format(min(owd32))
print 'max32 = {}'.format(max(owd32))
print 'std32 = {}'.format(numpy.std(owd32))

""" for owd33"""
print "number of packets included = {}".format(len(owd33))
print 'mean33 = {}'.format(numpy.mean(owd33))
print 'min33 = {}'.format(min(owd33))
print 'max33 = {}'.format(max(owd33))
print 'std33 = {}'.format(numpy.std(owd33))


""" next take the Window3/Window1""" 
c1 = numpy.mean(owd33)/numpy.mean(owd31)
c2 = numpy.mean(owd33)/numpy.min(owd31)
c3 = numpy.mean(owd33)/numpy.max(owd31)

c4 = numpy.min(owd33)/numpy.mean(owd31)
c5 = numpy.min(owd33)/numpy.min(owd31)
c6 = numpy.min(owd33)/numpy.max(owd31)

c7 = numpy.max(owd33)/numpy.mean(owd31)
c8 = numpy.max(owd33)/numpy.min(owd31)
c9 = numpy.max(owd33)/numpy.max(owd31)

"""next take the Window3/Window2"""
c10 = numpy.mean(owd33)/numpy.mean(owd32)
c11 = numpy.mean(owd33)/numpy.min(owd32)
c12 = numpy.mean(owd33)/numpy.max(owd32)

c13 = numpy.min(owd33)/numpy.mean(owd32)
c14 = numpy.min(owd33)/numpy.min(owd32)
c15 = numpy.min(owd33)/numpy.max(owd32)

c16 = numpy.max(owd33)/numpy.mean(owd32)
c17 = numpy.max(owd33)/numpy.min(owd32)
c18 = numpy.max(owd33)/numpy.max(owd32)

""" min/max window 3"""
c19 = numpy.min(owd33)/numpy.max(owd33)

"""standard dev values"""
c20 = numpy.std(owd33)/numpy.std(owd31)
c21 = numpy.std(owd33)/numpy.std(owd32)
c22 = numpy.std(owd31)/numpy.std(owd32)

"""next window1 / window2"""
c23 = numpy.mean(owd31)/numpy.mean(owd32)
c24 = numpy.mean(owd31)/numpy.min(owd32)
c25 = numpy.mean(owd31)/numpy.max(owd32)

c26 = numpy.min(owd31)/numpy.mean(owd32)
c27 = numpy.min(owd31)/numpy.min(owd32)
c28 = numpy.min(owd31)/numpy.max(owd32)

c29 = numpy.max(owd31)/numpy.mean(owd32)
c30 = numpy.max(owd31)/numpy.min(owd32)
c31 = numpy.max(owd31)/numpy.max(owd32)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(c1)+"\n"
print "avg-win3 / min-win1 = "+ str(c2)+"\n"
print "avg-win3 / max-win1 = "+ str(c3)+"\n"

print "min-win3 / avg-win1 = "+ str(c4)+"\n"
print "min-win3 / min-win1 = "+ str(c5)+"\n"
print "min-win3 / max-win1 = "+ str(c6)+"\n"

print "max-win3 / avg-win1 = "+ str(c7)+"\n"
print "max-win3 / min-win1 = "+ str(c8)+"\n"
print "max-win3 / max-win1 = "+ str(c9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(c10)+"\n"
print "avg-win3 / min-win2 = "+ str(c11)+"\n"
print "avg-win3 / max-win2 = "+ str(c12)+"\n"

print "min-win3 / avg-win2 = "+ str(c13)+"\n"
print "min-win3 / min-win2 = "+ str(c14)+"\n"
print "min-win3 / max-win2 = "+ str(c15)+"\n"

print "max-win3 / avg-win2 = "+ str(c16)+"\n"
print "max-win3 / min-win2 = "+ str(c17)+"\n"
print "max-win3 / max-win2 = "+ str(c18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(c19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(c20)+"\n"
print "std-win3 / std-win2 = "+ str(c21)+"\n"
print "std-win1 / std-win2 = "+ str(c22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(c23)+"\n"
print "avg-win1 / min-win2 = "+ str(c24)+"\n"
print "avg-win1 / max-win2 = "+ str(c25)+"\n"

print "min-win1 / avg-win2 = "+ str(c26)+"\n"
print "min-win1 / min-win2 = "+ str(c27)+"\n"
print "min-win1 / max-win2 = "+ str(c28)+"\n"

print "max-win1 / avg-win2 = "+ str(c29)+"\n"
print "max-win1 / min-win2 = "+ str(c30)+"\n"
print "max-win1 / max-win2 = "+ str(c31)+"\n"

print "##################################################"

"""LOSS # 4"""
print "Loss # 4"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind41=win41-300
ind42=win41-150
ind43=win41

print "\n index number for loss 4", ind41, ind42, ind43

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd41=[]
owd42=[]
owd43=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind41 and nn<ind42:
		owd41.append(iat[nn])
	elif nn>=ind42 and nn<ind43:
		owd42.append(iat[nn])
	elif nn>=ind43 and nn<ind43+150:
		owd43.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd41"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd41))
""" owd41 avg"""
print 'mean11 = {}'.format(numpy.mean(owd41))
"""owd41 min"""
print 'min11 = {}'.format(min(owd41))
"""owd41 max"""
print 'max11 = {}'.format(max(owd41))
""" owd41 std"""
print 'std11 = {}'.format(numpy.std(owd41))

"""for owd42"""
print "number of packets included = {}".format(len(owd42))
print 'mean12 = {}'.format(numpy.mean(owd42))
print 'min12 = {}'.format(min(owd42))
print 'max12 = {}'.format(max(owd42))
print 'std12 = {}'.format(numpy.std(owd42))

""" for owd43"""
print "number of packets included = {}".format(len(owd43))
print 'mean13 = {}'.format(numpy.mean(owd43))
print 'min13 = {}'.format(min(owd43))
print 'max13 = {}'.format(max(owd43))
print 'std13 = {}'.format(numpy.std(owd43))


""" next take the Window3/Window1""" 
d1 = numpy.mean(owd43)/numpy.mean(owd41)
d2 = numpy.mean(owd43)/numpy.min(owd41)
d3 = numpy.mean(owd43)/numpy.max(owd41)

d4 = numpy.min(owd43)/numpy.mean(owd41)
d5 = numpy.min(owd43)/numpy.min(owd41)
d6 = numpy.min(owd43)/numpy.max(owd41)

d7 = numpy.max(owd43)/numpy.mean(owd41)
d8 = numpy.max(owd43)/numpy.min(owd41)
d9 = numpy.max(owd43)/numpy.max(owd41)

"""next take the Window3/Window2"""
d10 = numpy.mean(owd43)/numpy.mean(owd42)
d11 = numpy.mean(owd43)/numpy.min(owd42)
d12 = numpy.mean(owd43)/numpy.max(owd42)

d13 = numpy.min(owd43)/numpy.mean(owd42)
d14 = numpy.min(owd43)/numpy.min(owd42)
d15 = numpy.min(owd43)/numpy.max(owd42)

d16 = numpy.max(owd43)/numpy.mean(owd42)
d17 = numpy.max(owd43)/numpy.min(owd42)
d18 = numpy.max(owd43)/numpy.max(owd42)

""" min/max window 3"""
d19 = numpy.min(owd43)/numpy.max(owd43)

"""standard dev values"""
d20 = numpy.std(owd43)/numpy.std(owd41)
d21 = numpy.std(owd43)/numpy.std(owd42)
d22 = numpy.std(owd41)/numpy.std(owd42)

"""next window1 / window2"""
d23 = numpy.mean(owd41)/numpy.mean(owd42)
d24 = numpy.mean(owd41)/numpy.min(owd42)
d25 = numpy.mean(owd41)/numpy.max(owd42)

d26 = numpy.min(owd41)/numpy.mean(owd42)
d27 = numpy.min(owd41)/numpy.min(owd42)
d28 = numpy.min(owd41)/numpy.max(owd42)

d29 = numpy.max(owd41)/numpy.mean(owd42)
d30 = numpy.max(owd41)/numpy.min(owd42)
d31 = numpy.max(owd41)/numpy.max(owd42)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(d1)+"\n"
print "avg-win3 / min-win1 = "+ str(d2)+"\n"
print "avg-win3 / max-win1 = "+ str(d3)+"\n"

print "min-win3 / avg-win1 = "+ str(d4)+"\n"
print "min-win3 / min-win1 = "+ str(d5)+"\n"
print "min-win3 / max-win1 = "+ str(d6)+"\n"

print "max-win3 / avg-win1 = "+ str(d7)+"\n"
print "max-win3 / min-win1 = "+ str(d8)+"\n"
print "max-win3 / max-win1 = "+ str(d9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(d10)+"\n"
print "avg-win3 / min-win2 = "+ str(d11)+"\n"
print "avg-win3 / max-win2 = "+ str(d12)+"\n"

print "min-win3 / avg-win2 = "+ str(d13)+"\n"
print "min-win3 / min-win2 = "+ str(d14)+"\n"
print "min-win3 / max-win2 = "+ str(d15)+"\n"

print "max-win3 / avg-win2 = "+ str(d16)+"\n"
print "max-win3 / min-win2 = "+ str(d17)+"\n"
print "max-win3 / max-win2 = "+ str(d18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(d19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(d20)+"\n"
print "std-win3 / std-win2 = "+ str(d21)+"\n"
print "std-win1 / std-win2 = "+ str(d22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(d23)+"\n"
print "avg-win1 / min-win2 = "+ str(d24)+"\n"
print "avg-win1 / max-win2 = "+ str(d25)+"\n"

print "min-win1 / avg-win2 = "+ str(d26)+"\n"
print "min-win1 / min-win2 = "+ str(d27)+"\n"
print "min-win1 / max-win2 = "+ str(d28)+"\n"

print "max-win1 / avg-win2 = "+ str(d29)+"\n"
print "max-win1 / min-win2 = "+ str(d30)+"\n"
print "max-win1 / max-win2 = "+ str(d31)+"\n"

print "##################################################"



"""LOSS # 5"""
print "Loss # 5"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind51=win51-300
ind52=win51-150
ind53=win51

print "\n index number for Loss 5", ind51, ind52, ind53

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd51=[]
owd52=[]
owd53=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind51 and nn<ind52:
		owd51.append(iat[nn])
	elif nn>=ind52 and nn<ind53:
		owd52.append(iat[nn])
	elif nn>=ind53 and nn<ind53+150:
		owd53.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd51"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd51))
""" owd51 avg"""
print 'mean11 = {}'.format(numpy.mean(owd51))
"""owd51 min"""
print 'min11 = {}'.format(min(owd51))
"""owd51 max"""
print 'max11 = {}'.format(max(owd51))
""" owd51 std"""
print 'std11 = {}'.format(numpy.std(owd51))

"""for owd52"""
print "number of packets included = {}".format(len(owd52))
print 'mean12 = {}'.format(numpy.mean(owd52))
print 'min12 = {}'.format(min(owd52))
print 'max12 = {}'.format(max(owd52))
print 'std12 = {}'.format(numpy.std(owd52))

""" for owd53"""
print "number of packets included = {}".format(len(owd53))
print 'mean13 = {}'.format(numpy.mean(owd53))
print 'min13 = {}'.format(min(owd53))
print 'max13 = {}'.format(max(owd53))
print 'std13 = {}'.format(numpy.std(owd53))


""" next take the Window3/Window1""" 
e1 = numpy.mean(owd53)/numpy.mean(owd51)
e2 = numpy.mean(owd53)/numpy.min(owd51)
e3 = numpy.mean(owd53)/numpy.max(owd51)

e4 = numpy.min(owd53)/numpy.mean(owd51)
e5 = numpy.min(owd53)/numpy.min(owd51)
e6 = numpy.min(owd53)/numpy.max(owd51)

e7 = numpy.max(owd53)/numpy.mean(owd51)
e8 = numpy.max(owd53)/numpy.min(owd51)
e9 = numpy.max(owd53)/numpy.max(owd51)

"""next take the Window3/Window2"""
e10 = numpy.mean(owd53)/numpy.mean(owd52)
e11 = numpy.mean(owd53)/numpy.min(owd52)
e12 = numpy.mean(owd53)/numpy.max(owd52)

e13 = numpy.min(owd53)/numpy.mean(owd52)
e14 = numpy.min(owd53)/numpy.min(owd52)
e15 = numpy.min(owd53)/numpy.max(owd52)

e16 = numpy.max(owd53)/numpy.mean(owd52)
e17 = numpy.max(owd53)/numpy.min(owd52)
e18 = numpy.max(owd53)/numpy.max(owd52)

""" min/max window 3"""
e19 = numpy.min(owd53)/numpy.max(owd53)

"""standard dev values"""
e20 = numpy.std(owd53)/numpy.std(owd51)
e21 = numpy.std(owd53)/numpy.std(owd52)
e22 = numpy.std(owd51)/numpy.std(owd52)

"""next window1 / window2"""
e23 = numpy.mean(owd51)/numpy.mean(owd52)
e24 = numpy.mean(owd51)/numpy.min(owd52)
e25 = numpy.mean(owd51)/numpy.max(owd52)

e26 = numpy.min(owd51)/numpy.mean(owd52)
e27 = numpy.min(owd51)/numpy.min(owd52)
e28 = numpy.min(owd51)/numpy.max(owd52)

e29 = numpy.max(owd51)/numpy.mean(owd52)
e30 = numpy.max(owd51)/numpy.min(owd52)
e31 = numpy.max(owd51)/numpy.max(owd52)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(e1)+"\n"
print "avg-win3 / min-win1 = "+ str(e2)+"\n"
print "avg-win3 / max-win1 = "+ str(e3)+"\n"

print "min-win3 / avg-win1 = "+ str(e4)+"\n"
print "min-win3 / min-win1 = "+ str(e5)+"\n"
print "min-win3 / max-win1 = "+ str(e6)+"\n"

print "max-win3 / avg-win1 = "+ str(e7)+"\n"
print "max-win3 / min-win1 = "+ str(e8)+"\n"
print "max-win3 / max-win1 = "+ str(e9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(e10)+"\n"
print "avg-win3 / min-win2 = "+ str(e11)+"\n"
print "avg-win3 / max-win2 = "+ str(e12)+"\n"

print "min-win3 / avg-win2 = "+ str(e13)+"\n"
print "min-win3 / min-win2 = "+ str(e14)+"\n"
print "min-win3 / max-win2 = "+ str(e15)+"\n"

print "max-win3 / avg-win2 = "+ str(e16)+"\n"
print "max-win3 / min-win2 = "+ str(e17)+"\n"
print "max-win3 / max-win2 = "+ str(e18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(e19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(e20)+"\n"
print "std-win3 / std-win2 = "+ str(e21)+"\n"
print "std-win1 / std-win2 = "+ str(e22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(e23)+"\n"
print "avg-win1 / min-win2 = "+ str(e24)+"\n"
print "avg-win1 / max-win2 = "+ str(e25)+"\n"

print "min-win1 / avg-win2 = "+ str(e26)+"\n"
print "min-win1 / min-win2 = "+ str(e27)+"\n"
print "min-win1 / max-win2 = "+ str(e28)+"\n"

print "max-win1 / avg-win2 = "+ str(e29)+"\n"
print "max-win1 / min-win2 = "+ str(e30)+"\n"
print "max-win1 / max-win2 = "+ str(e31)+"\n"

print "##################################################"




"""LOSS # 6"""
print "Loss # 6"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind61=win61-300
ind62=win61-150
ind63=win61

print "\n index number for window1", ind61, ind62, ind63

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd61=[]
owd62=[]
owd63=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind61 and nn<ind62:
		owd61.append(iat[nn])
	elif nn>=ind62 and nn<ind63:
		owd62.append(iat[nn])
	elif nn>=ind63 and nn<ind63+150:
		owd63.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd61"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd61))
""" owd61 avg"""
print 'mean11 = {}'.format(numpy.mean(owd61))
"""owd61 min"""
print 'min11 = {}'.format(min(owd61))
"""owd61 max"""
print 'max11 = {}'.format(max(owd61))
""" owd61 std"""
print 'std11 = {}'.format(numpy.std(owd61))

"""for owd62"""
print "number of packets included = {}".format(len(owd62))
print 'mean12 = {}'.format(numpy.mean(owd62))
print 'min12 = {}'.format(min(owd62))
print 'max12 = {}'.format(max(owd62))
print 'std12 = {}'.format(numpy.std(owd62))

""" for owd63"""
print "number of packets included = {}".format(len(owd63))
print 'mean13 = {}'.format(numpy.mean(owd63))
print 'min13 = {}'.format(min(owd63))
print 'max13 = {}'.format(max(owd63))
print 'std13 = {}'.format(numpy.std(owd63))


""" next take the Window3/Window1""" 
f1 = numpy.mean(owd63)/numpy.mean(owd61)
f2 = numpy.mean(owd63)/numpy.min(owd61)
f3 = numpy.mean(owd63)/numpy.max(owd61)

f4 = numpy.min(owd63)/numpy.mean(owd61)
f5 = numpy.min(owd63)/numpy.min(owd61)
f6 = numpy.min(owd63)/numpy.max(owd61)

f7 = numpy.max(owd63)/numpy.mean(owd61)
f8 = numpy.max(owd63)/numpy.min(owd61)
f9 = numpy.max(owd63)/numpy.max(owd61)

"""next take the Window3/Window2"""
f10 = numpy.mean(owd63)/numpy.mean(owd62)
f11 = numpy.mean(owd63)/numpy.min(owd62)
f12 = numpy.mean(owd63)/numpy.max(owd62)

f13 = numpy.min(owd63)/numpy.mean(owd62)
f14 = numpy.min(owd63)/numpy.min(owd62)
f15 = numpy.min(owd63)/numpy.max(owd62)

f16 = numpy.max(owd63)/numpy.mean(owd62)
f17 = numpy.max(owd63)/numpy.min(owd62)
f18 = numpy.max(owd63)/numpy.max(owd62)

""" min/max window 3"""
f19 = numpy.min(owd63)/numpy.max(owd63)

"""standard dev values"""
f20 = numpy.std(owd63)/numpy.std(owd61)
f21 = numpy.std(owd63)/numpy.std(owd62)
f22 = numpy.std(owd61)/numpy.std(owd62)

"""next window1 / window2"""
f23 = numpy.mean(owd61)/numpy.mean(owd62)
f24 = numpy.mean(owd61)/numpy.min(owd62)
f25 = numpy.mean(owd61)/numpy.max(owd62)

f26 = numpy.min(owd61)/numpy.mean(owd62)
f27 = numpy.min(owd61)/numpy.min(owd62)
f28 = numpy.min(owd61)/numpy.max(owd62)

f29 = numpy.max(owd61)/numpy.mean(owd62)
f30 = numpy.max(owd61)/numpy.min(owd62)
f31 = numpy.max(owd61)/numpy.max(owd62)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(f1)+"\n"
print "avg-win3 / min-win1 = "+ str(f2)+"\n"
print "avg-win3 / max-win1 = "+ str(f3)+"\n"

print "min-win3 / avg-win1 = "+ str(f4)+"\n"
print "min-win3 / min-win1 = "+ str(f5)+"\n"
print "min-win3 / max-win1 = "+ str(f6)+"\n"

print "max-win3 / avg-win1 = "+ str(f7)+"\n"
print "max-win3 / min-win1 = "+ str(f8)+"\n"
print "max-win3 / max-win1 = "+ str(f9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(f10)+"\n"
print "avg-win3 / min-win2 = "+ str(f11)+"\n"
print "avg-win3 / max-win2 = "+ str(f12)+"\n"

print "min-win3 / avg-win2 = "+ str(f13)+"\n"
print "min-win3 / min-win2 = "+ str(f14)+"\n"
print "min-win3 / max-win2 = "+ str(f15)+"\n"

print "max-win3 / avg-win2 = "+ str(f16)+"\n"
print "max-win3 / min-win2 = "+ str(f17)+"\n"
print "max-win3 / max-win2 = "+ str(f18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(f19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(f20)+"\n"
print "std-win3 / std-win2 = "+ str(f21)+"\n"
print "std-win1 / std-win2 = "+ str(f22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(f23)+"\n"
print "avg-win1 / min-win2 = "+ str(f24)+"\n"
print "avg-win1 / max-win2 = "+ str(f25)+"\n"

print "min-win1 / avg-win2 = "+ str(f26)+"\n"
print "min-win1 / min-win2 = "+ str(f27)+"\n"
print "min-win1 / max-win2 = "+ str(f28)+"\n"

print "max-win1 / avg-win2 = "+ str(f29)+"\n"
print "max-win1 / min-win2 = "+ str(f30)+"\n"
print "max-win1 / max-win2 = "+ str(f31)+"\n"

print "##################################################"



"""LOSS # 7"""
print "Loss # 7"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind71=win71-300
ind72=win71-150
ind73=win71

print "\n index number for Loss 7", ind71, ind72, ind73

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd71=[]
owd72=[]
owd73=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind71 and nn<ind72:
		owd71.append(iat[nn])
	elif nn>=ind72 and nn<ind73:
		owd72.append(iat[nn])
	elif nn>=ind73 and nn<ind73+150:
		owd73.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd71"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd71))
""" owd71 avg"""
print 'mean11 = {}'.format(numpy.mean(owd71))
"""owd71 min"""
print 'min11 = {}'.format(min(owd71))
"""owd71 max"""
print 'max11 = {}'.format(max(owd71))
""" owd71 std"""
print 'std11 = {}'.format(numpy.std(owd71))

"""for owd72"""
print "number of packets included = {}".format(len(owd72))
print 'mean12 = {}'.format(numpy.mean(owd72))
print 'min12 = {}'.format(min(owd72))
print 'max12 = {}'.format(max(owd72))
print 'std12 = {}'.format(numpy.std(owd72))

""" for owd73"""
print "number of packets included = {}".format(len(owd73))
print 'mean13 = {}'.format(numpy.mean(owd73))
print 'min13 = {}'.format(min(owd73))
print 'max13 = {}'.format(max(owd73))
print 'std13 = {}'.format(numpy.std(owd73))


""" next take the Window3/Window1""" 
g1 = numpy.mean(owd73)/numpy.mean(owd71)
g2 = numpy.mean(owd73)/numpy.min(owd71)
g3 = numpy.mean(owd73)/numpy.max(owd71)

g4 = numpy.min(owd73)/numpy.mean(owd71)
g5 = numpy.min(owd73)/numpy.min(owd71)
g6 = numpy.min(owd73)/numpy.max(owd71)

g7 = numpy.max(owd73)/numpy.mean(owd71)
g8 = numpy.max(owd73)/numpy.min(owd71)
g9 = numpy.max(owd73)/numpy.max(owd71)

"""next take the Window3/Window2"""
g10 = numpy.mean(owd73)/numpy.mean(owd72)
g11 = numpy.mean(owd73)/numpy.min(owd72)
g12 = numpy.mean(owd73)/numpy.max(owd72)

g13 = numpy.min(owd73)/numpy.mean(owd72)
g14 = numpy.min(owd73)/numpy.min(owd72)
g15 = numpy.min(owd73)/numpy.max(owd72)

g16 = numpy.max(owd73)/numpy.mean(owd72)
g17 = numpy.max(owd73)/numpy.min(owd72)
g18 = numpy.max(owd73)/numpy.max(owd72)

""" min/max window 3"""
g19 = numpy.min(owd73)/numpy.max(owd73)

"""standard dev values"""
g20 = numpy.std(owd73)/numpy.std(owd71)
g21 = numpy.std(owd73)/numpy.std(owd72)
g22 = numpy.std(owd71)/numpy.std(owd72)

"""next window1 / window2"""
g23 = numpy.mean(owd71)/numpy.mean(owd72)
g24 = numpy.mean(owd71)/numpy.min(owd72)
g25 = numpy.mean(owd71)/numpy.max(owd72)

g26 = numpy.min(owd71)/numpy.mean(owd72)
g27 = numpy.min(owd71)/numpy.min(owd72)
g28 = numpy.min(owd71)/numpy.max(owd72)

g29 = numpy.max(owd71)/numpy.mean(owd72)
g30 = numpy.max(owd71)/numpy.min(owd72)
g31 = numpy.max(owd71)/numpy.max(owd72)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(g1)+"\n"
print "avg-win3 / min-win1 = "+ str(g2)+"\n"
print "avg-win3 / max-win1 = "+ str(g3)+"\n"

print "min-win3 / avg-win1 = "+ str(g4)+"\n"
print "min-win3 / min-win1 = "+ str(g5)+"\n"
print "min-win3 / max-win1 = "+ str(g6)+"\n"

print "max-win3 / avg-win1 = "+ str(g7)+"\n"
print "max-win3 / min-win1 = "+ str(g8)+"\n"
print "max-win3 / max-win1 = "+ str(g9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(g10)+"\n"
print "avg-win3 / min-win2 = "+ str(g11)+"\n"
print "avg-win3 / max-win2 = "+ str(g12)+"\n"

print "min-win3 / avg-win2 = "+ str(g13)+"\n"
print "min-win3 / min-win2 = "+ str(g14)+"\n"
print "min-win3 / max-win2 = "+ str(g15)+"\n"

print "max-win3 / avg-win2 = "+ str(g16)+"\n"
print "max-win3 / min-win2 = "+ str(g17)+"\n"
print "max-win3 / max-win2 = "+ str(g18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(g19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(g20)+"\n"
print "std-win3 / std-win2 = "+ str(g21)+"\n"
print "std-win1 / std-win2 = "+ str(g22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(g23)+"\n"
print "avg-win1 / min-win2 = "+ str(g24)+"\n"
print "avg-win1 / max-win2 = "+ str(g25)+"\n"

print "min-win1 / avg-win2 = "+ str(g26)+"\n"
print "min-win1 / min-win2 = "+ str(g27)+"\n"
print "min-win1 / max-win2 = "+ str(g28)+"\n"

print "max-win1 / avg-win2 = "+ str(g29)+"\n"
print "max-win1 / min-win2 = "+ str(g30)+"\n"
print "max-win1 / max-win2 = "+ str(g31)+"\n"

print "##################################################"



"""LOSS # 8"""
print "Loss # 8"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind81=win81-300
ind82=win81-150
ind83=win81

print "\n index number for window1", ind81, ind82, ind83

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd81=[]
owd82=[]
owd83=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind81 and nn<ind82:
		owd81.append(iat[nn])
	elif nn>=ind82 and nn<ind83:
		owd82.append(iat[nn])
	elif nn>=ind83 and nn<ind83+150:
		owd83.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd81"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd81))
""" owd81 avg"""
print 'mean11 = {}'.format(numpy.mean(owd81))
"""owd81 min"""
print 'min11 = {}'.format(min(owd81))
"""owd81 max"""
print 'max11 = {}'.format(max(owd81))
""" owd81 std"""
print 'std11 = {}'.format(numpy.std(owd81))

"""for owd82"""
print "number of packets included = {}".format(len(owd82))
print 'mean12 = {}'.format(numpy.mean(owd82))
print 'min12 = {}'.format(min(owd82))
print 'max12 = {}'.format(max(owd82))
print 'std12 = {}'.format(numpy.std(owd82))

""" for owd83"""
print "number of packets included = {}".format(len(owd83))
print 'mean13 = {}'.format(numpy.mean(owd83))
print 'min13 = {}'.format(min(owd83))
print 'max13 = {}'.format(max(owd83))
print 'std13 = {}'.format(numpy.std(owd83))


""" next take the Window3/Window1""" 
h1 = numpy.mean(owd83)/numpy.mean(owd81)
h2 = numpy.mean(owd83)/numpy.min(owd81)
h3 = numpy.mean(owd83)/numpy.max(owd81)

h4 = numpy.min(owd83)/numpy.mean(owd81)
h5 = numpy.min(owd83)/numpy.min(owd81)
h6 = numpy.min(owd83)/numpy.max(owd81)

h7 = numpy.max(owd83)/numpy.mean(owd81)
h8 = numpy.max(owd83)/numpy.min(owd81)
h9 = numpy.max(owd83)/numpy.max(owd81)

"""next take the Window3/Window2"""
h10 = numpy.mean(owd83)/numpy.mean(owd82)
h11 = numpy.mean(owd83)/numpy.min(owd82)
h12 = numpy.mean(owd83)/numpy.max(owd82)

h13 = numpy.min(owd83)/numpy.mean(owd82)
h14 = numpy.min(owd83)/numpy.min(owd82)
h15 = numpy.min(owd83)/numpy.max(owd82)

h16 = numpy.max(owd83)/numpy.mean(owd82)
h17 = numpy.max(owd83)/numpy.min(owd82)
h18 = numpy.max(owd83)/numpy.max(owd82)

""" min/max window 3"""
h19 = numpy.min(owd83)/numpy.max(owd83)

"""standard dev values"""
h20 = numpy.std(owd83)/numpy.std(owd81)
h21 = numpy.std(owd83)/numpy.std(owd82)
h22 = numpy.std(owd81)/numpy.std(owd82)

"""next window1 / window2"""
h23 = numpy.mean(owd81)/numpy.mean(owd82)
h24 = numpy.mean(owd81)/numpy.min(owd82)
h25 = numpy.mean(owd81)/numpy.max(owd82)

h26 = numpy.min(owd81)/numpy.mean(owd82)
h27 = numpy.min(owd81)/numpy.min(owd82)
h28 = numpy.min(owd81)/numpy.max(owd82)

h29 = numpy.max(owd81)/numpy.mean(owd82)
h30 = numpy.max(owd81)/numpy.min(owd82)
h31 = numpy.max(owd81)/numpy.max(owd82)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(h1)+"\n"
print "avg-win3 / min-win1 = "+ str(h2)+"\n"
print "avg-win3 / max-win1 = "+ str(h3)+"\n"

print "min-win3 / avg-win1 = "+ str(h4)+"\n"
print "min-win3 / min-win1 = "+ str(h5)+"\n"
print "min-win3 / max-win1 = "+ str(h6)+"\n"

print "max-win3 / avg-win1 = "+ str(h7)+"\n"
print "max-win3 / min-win1 = "+ str(h8)+"\n"
print "max-win3 / max-win1 = "+ str(h9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(h10)+"\n"
print "avg-win3 / min-win2 = "+ str(h11)+"\n"
print "avg-win3 / max-win2 = "+ str(h12)+"\n"

print "min-win3 / avg-win2 = "+ str(h13)+"\n"
print "min-win3 / min-win2 = "+ str(h14)+"\n"
print "min-win3 / max-win2 = "+ str(h15)+"\n"

print "max-win3 / avg-win2 = "+ str(h16)+"\n"
print "max-win3 / min-win2 = "+ str(h17)+"\n"
print "max-win3 / max-win2 = "+ str(h18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(h19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(h20)+"\n"
print "std-win3 / std-win2 = "+ str(h21)+"\n"
print "std-win1 / std-win2 = "+ str(h22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(h23)+"\n"
print "avg-win1 / min-win2 = "+ str(h24)+"\n"
print "avg-win1 / max-win2 = "+ str(h25)+"\n"

print "min-win1 / avg-win2 = "+ str(h26)+"\n"
print "min-win1 / min-win2 = "+ str(h27)+"\n"
print "min-win1 / max-win2 = "+ str(h28)+"\n"

print "max-win1 / avg-win2 = "+ str(h29)+"\n"
print "max-win1 / min-win2 = "+ str(h30)+"\n"
print "max-win1 / max-win2 = "+ str(h31)+"\n"

print "##################################################"



"""LOSS # 9"""
print "Loss # 9"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind91=win91-300
ind92=win91-150
ind93=win91

print "\n index number for Loss 9", ind91, ind92, ind93

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd91=[]
owd92=[]
owd93=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind91 and nn<ind92:
		owd91.append(iat[nn])
	elif nn>=ind92 and nn<ind93:
		owd92.append(iat[nn])
	elif nn>=ind93 and nn<ind93+150:
		owd93.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd91"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd91))
""" owd91 avg"""
print 'mean11 = {}'.format(numpy.mean(owd91))
"""owd91 min"""
print 'min11 = {}'.format(min(owd91))
"""owd91 max"""
print 'max11 = {}'.format(max(owd91))
""" owd91 std"""
print 'std11 = {}'.format(numpy.std(owd91))

"""for owd92"""
print "number of packets included = {}".format(len(owd92))
print 'mean12 = {}'.format(numpy.mean(owd92))
print 'min12 = {}'.format(min(owd92))
print 'max12 = {}'.format(max(owd92))
print 'std12 = {}'.format(numpy.std(owd92))

""" for owd93"""
print "number of packets included = {}".format(len(owd93))
print 'mean13 = {}'.format(numpy.mean(owd93))
print 'min13 = {}'.format(min(owd93))
print 'max13 = {}'.format(max(owd93))
print 'std13 = {}'.format(numpy.std(owd93))


""" next take the Window3/Window1""" 
i1 = numpy.mean(owd93)/numpy.mean(owd91)
i2 = numpy.mean(owd93)/numpy.min(owd91)
i3 = numpy.mean(owd93)/numpy.max(owd91)

i4 = numpy.min(owd93)/numpy.mean(owd91)
i5 = numpy.min(owd93)/numpy.min(owd91)
i6 = numpy.min(owd93)/numpy.max(owd91)

i7 = numpy.max(owd93)/numpy.mean(owd91)
i8 = numpy.max(owd93)/numpy.min(owd91)
i9 = numpy.max(owd93)/numpy.max(owd91)

"""next take the Window3/Window2"""
i10 = numpy.mean(owd93)/numpy.mean(owd92)
i11 = numpy.mean(owd93)/numpy.min(owd92)
i12 = numpy.mean(owd93)/numpy.max(owd92)

i13 = numpy.min(owd93)/numpy.mean(owd92)
i14 = numpy.min(owd93)/numpy.min(owd92)
i15 = numpy.min(owd93)/numpy.max(owd92)

i16 = numpy.max(owd93)/numpy.mean(owd92)
i17 = numpy.max(owd93)/numpy.min(owd92)
i18 = numpy.max(owd93)/numpy.max(owd92)

""" min/max window 3"""
i19 = numpy.min(owd93)/numpy.max(owd93)

"""standard dev values"""
i20 = numpy.std(owd93)/numpy.std(owd91)
i21 = numpy.std(owd93)/numpy.std(owd92)
i22 = numpy.std(owd91)/numpy.std(owd92)

"""next window1 / window2"""
i23 = numpy.mean(owd91)/numpy.mean(owd92)
i24 = numpy.mean(owd91)/numpy.min(owd92)
i25 = numpy.mean(owd91)/numpy.max(owd92)

i26 = numpy.min(owd91)/numpy.mean(owd92)
i27 = numpy.min(owd91)/numpy.min(owd92)
i28 = numpy.min(owd91)/numpy.max(owd92)

i29 = numpy.max(owd91)/numpy.mean(owd92)
i30 = numpy.max(owd91)/numpy.min(owd92)
i31 = numpy.max(owd91)/numpy.max(owd92)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(i1)+"\n"
print "avg-win3 / min-win1 = "+ str(i2)+"\n"
print "avg-win3 / max-win1 = "+ str(i3)+"\n"

print "min-win3 / avg-win1 = "+ str(i4)+"\n"
print "min-win3 / min-win1 = "+ str(i5)+"\n"
print "min-win3 / max-win1 = "+ str(i6)+"\n"

print "max-win3 / avg-win1 = "+ str(i7)+"\n"
print "max-win3 / min-win1 = "+ str(i8)+"\n"
print "max-win3 / max-win1 = "+ str(i9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(i10)+"\n"
print "avg-win3 / min-win2 = "+ str(i11)+"\n"
print "avg-win3 / max-win2 = "+ str(i12)+"\n"

print "min-win3 / avg-win2 = "+ str(i13)+"\n"
print "min-win3 / min-win2 = "+ str(i14)+"\n"
print "min-win3 / max-win2 = "+ str(i15)+"\n"

print "max-win3 / avg-win2 = "+ str(i16)+"\n"
print "max-win3 / min-win2 = "+ str(i17)+"\n"
print "max-win3 / max-win2 = "+ str(i18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(i19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(i20)+"\n"
print "std-win3 / std-win2 = "+ str(i21)+"\n"
print "std-win1 / std-win2 = "+ str(i22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(i23)+"\n"
print "avg-win1 / min-win2 = "+ str(i24)+"\n"
print "avg-win1 / max-win2 = "+ str(i25)+"\n"

print "min-win1 / avg-win2 = "+ str(i26)+"\n"
print "min-win1 / min-win2 = "+ str(i27)+"\n"
print "min-win1 / max-win2 = "+ str(i28)+"\n"

print "max-win1 / avg-win2 = "+ str(i29)+"\n"
print "max-win1 / min-win2 = "+ str(i30)+"\n"
print "max-win1 / max-win2 = "+ str(i31)+"\n"

print "##################################################"



"""LOSS # 10"""
print "Loss # 10"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind101=win101-300
ind102=win101-150
ind103=win101

print "\n index number for Loss 10", ind101, ind102, ind103

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd101=[]
owd102=[]
owd103=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind101 and nn<ind102:
		owd101.append(iat[nn])
	elif nn>=ind102 and nn<ind103:
		owd102.append(iat[nn])
	elif nn>=ind103 and nn<ind103+150:
		owd103.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd101"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd101))
""" owd101 avg"""
print 'mean11 = {}'.format(numpy.mean(owd101))
"""owd101 min"""
print 'min11 = {}'.format(min(owd101))
"""owd101 max"""
print 'max11 = {}'.format(max(owd101))
""" owd101 std"""
print 'std11 = {}'.format(numpy.std(owd101))

"""for owd102"""
print "number of packets included = {}".format(len(owd102))
print 'mean12 = {}'.format(numpy.mean(owd102))
print 'min12 = {}'.format(min(owd102))
print 'max12 = {}'.format(max(owd102))
print 'std12 = {}'.format(numpy.std(owd102))

""" for owd103"""
print "number of packets included = {}".format(len(owd103))
print 'mean13 = {}'.format(numpy.mean(owd103))
print 'min13 = {}'.format(min(owd103))
print 'max13 = {}'.format(max(owd103))
print 'std13 = {}'.format(numpy.std(owd103))


""" next take the Window3/Window1""" 
j1 = numpy.mean(owd103)/numpy.mean(owd101)
j2 = numpy.mean(owd103)/numpy.min(owd101)
j3 = numpy.mean(owd103)/numpy.max(owd101)

j4 = numpy.min(owd103)/numpy.mean(owd101)
j5 = numpy.min(owd103)/numpy.min(owd101)
j6 = numpy.min(owd103)/numpy.max(owd101)

j7 = numpy.max(owd103)/numpy.mean(owd101)
j8 = numpy.max(owd103)/numpy.min(owd101)
j9 = numpy.max(owd103)/numpy.max(owd101)

"""next take the Window3/Window2"""
j10 = numpy.mean(owd103)/numpy.mean(owd102)
j11 = numpy.mean(owd103)/numpy.min(owd102)
j12 = numpy.mean(owd103)/numpy.max(owd102)

j13 = numpy.min(owd103)/numpy.mean(owd102)
j14 = numpy.min(owd103)/numpy.min(owd102)
j15 = numpy.min(owd103)/numpy.max(owd102)

j16 = numpy.max(owd103)/numpy.mean(owd102)
j17 = numpy.max(owd103)/numpy.min(owd102)
j18 = numpy.max(owd103)/numpy.max(owd102)

""" min/max window 3"""
j19 = numpy.min(owd103)/numpy.max(owd103)

"""standard dev values"""
j20 = numpy.std(owd103)/numpy.std(owd101)
j21 = numpy.std(owd103)/numpy.std(owd102)
j22 = numpy.std(owd101)/numpy.std(owd102)

"""next window1 / window2"""
j23 = numpy.mean(owd101)/numpy.mean(owd102)
j24 = numpy.mean(owd101)/numpy.min(owd102)
j25 = numpy.mean(owd101)/numpy.max(owd102)

j26 = numpy.min(owd101)/numpy.mean(owd102)
j27 = numpy.min(owd101)/numpy.min(owd102)
j28 = numpy.min(owd101)/numpy.max(owd102)

j29 = numpy.max(owd101)/numpy.mean(owd102)
j30 = numpy.max(owd101)/numpy.min(owd102)
j31 = numpy.max(owd101)/numpy.max(owd102)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(j1)+"\n"
print "avg-win3 / min-win1 = "+ str(j2)+"\n"
print "avg-win3 / max-win1 = "+ str(j3)+"\n"

print "min-win3 / avg-win1 = "+ str(j4)+"\n"
print "min-win3 / min-win1 = "+ str(j5)+"\n"
print "min-win3 / max-win1 = "+ str(j6)+"\n"

print "max-win3 / avg-win1 = "+ str(j7)+"\n"
print "max-win3 / min-win1 = "+ str(j8)+"\n"
print "max-win3 / max-win1 = "+ str(j9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(j10)+"\n"
print "avg-win3 / min-win2 = "+ str(j11)+"\n"
print "avg-win3 / max-win2 = "+ str(j12)+"\n"

print "min-win3 / avg-win2 = "+ str(j13)+"\n"
print "min-win3 / min-win2 = "+ str(j14)+"\n"
print "min-win3 / max-win2 = "+ str(j15)+"\n"

print "max-win3 / avg-win2 = "+ str(j16)+"\n"
print "max-win3 / min-win2 = "+ str(j17)+"\n"
print "max-win3 / max-win2 = "+ str(j18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(j19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(j20)+"\n"
print "std-win3 / std-win2 = "+ str(j21)+"\n"
print "std-win1 / std-win2 = "+ str(j22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(j23)+"\n"
print "avg-win1 / min-win2 = "+ str(j24)+"\n"
print "avg-win1 / max-win2 = "+ str(j25)+"\n"

print "min-win1 / avg-win2 = "+ str(j26)+"\n"
print "min-win1 / min-win2 = "+ str(j27)+"\n"
print "min-win1 / max-win2 = "+ str(j28)+"\n"

print "max-win1 / avg-win2 = "+ str(j29)+"\n"
print "max-win1 / min-win2 = "+ str(j30)+"\n"
print "max-win1 / max-win2 = "+ str(j31)+"\n"

print "##################################################"



"""LOSS # 11"""
print "Loss # 11"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind111=win111-300
ind112=win111-150
ind113=win111

print "\n index number for loss 11", ind111, ind112, ind113

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd111=[]
owd112=[]
owd113=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind111 and nn<ind112:
		owd111.append(iat[nn])
	elif nn>=ind112 and nn<ind113:
		owd112.append(iat[nn])
	elif nn>=ind113 and nn<ind113+150:
		owd113.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd111"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd111))
""" owd111 avg"""
print 'mean11 = {}'.format(numpy.mean(owd111))
"""owd111 min"""
print 'min11 = {}'.format(min(owd111))
"""owd111 max"""
print 'max11 = {}'.format(max(owd111))
""" owd111 std"""
print 'std11 = {}'.format(numpy.std(owd111))

"""for owd112"""
print "number of packets included = {}".format(len(owd112))
print 'mean12 = {}'.format(numpy.mean(owd112))
print 'min12 = {}'.format(min(owd112))
print 'max12 = {}'.format(max(owd112))
print 'std12 = {}'.format(numpy.std(owd112))

""" for owd113"""
print "number of packets included = {}".format(len(owd113))
print 'mean13 = {}'.format(numpy.mean(owd113))
print 'min13 = {}'.format(min(owd113))
print 'max13 = {}'.format(max(owd113))
print 'std13 = {}'.format(numpy.std(owd113))


""" next take the Window3/Window1""" 
k1 = numpy.mean(owd113)/numpy.mean(owd111)
k2 = numpy.mean(owd113)/numpy.min(owd111)
k3 = numpy.mean(owd113)/numpy.max(owd111)

k4 = numpy.min(owd113)/numpy.mean(owd111)
k5 = numpy.min(owd113)/numpy.min(owd111)
k6 = numpy.min(owd113)/numpy.max(owd111)

k7 = numpy.max(owd113)/numpy.mean(owd111)
k8 = numpy.max(owd113)/numpy.min(owd111)
k9 = numpy.max(owd113)/numpy.max(owd111)

"""next take the Window3/Window2"""
k10 = numpy.mean(owd113)/numpy.mean(owd112)
k11 = numpy.mean(owd113)/numpy.min(owd112)
k12 = numpy.mean(owd113)/numpy.max(owd112)

k13 = numpy.min(owd113)/numpy.mean(owd112)
k14 = numpy.min(owd113)/numpy.min(owd112)
k15 = numpy.min(owd113)/numpy.max(owd112)

k16 = numpy.max(owd113)/numpy.mean(owd112)
k17 = numpy.max(owd113)/numpy.min(owd112)
k18 = numpy.max(owd113)/numpy.max(owd112)

""" min/max window 3"""
k19 = numpy.min(owd113)/numpy.max(owd113)

"""standard dev values"""
k20 = numpy.std(owd113)/numpy.std(owd111)
k21 = numpy.std(owd113)/numpy.std(owd112)
k22 = numpy.std(owd111)/numpy.std(owd112)

"""next window1 / window2"""
k23 = numpy.mean(owd111)/numpy.mean(owd112)
k24 = numpy.mean(owd111)/numpy.min(owd112)
k25 = numpy.mean(owd111)/numpy.max(owd112)

k26 = numpy.min(owd111)/numpy.mean(owd112)
k27 = numpy.min(owd111)/numpy.min(owd112)
k28 = numpy.min(owd111)/numpy.max(owd112)

k29 = numpy.max(owd111)/numpy.mean(owd112)
k30 = numpy.max(owd111)/numpy.min(owd112)
k31 = numpy.max(owd111)/numpy.max(owd112)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(k1)+"\n"
print "avg-win3 / min-win1 = "+ str(k2)+"\n"
print "avg-win3 / max-win1 = "+ str(k3)+"\n"

print "min-win3 / avg-win1 = "+ str(k4)+"\n"
print "min-win3 / min-win1 = "+ str(k5)+"\n"
print "min-win3 / max-win1 = "+ str(k6)+"\n"

print "max-win3 / avg-win1 = "+ str(k7)+"\n"
print "max-win3 / min-win1 = "+ str(k8)+"\n"
print "max-win3 / max-win1 = "+ str(k9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(k10)+"\n"
print "avg-win3 / min-win2 = "+ str(k11)+"\n"
print "avg-win3 / max-win2 = "+ str(k12)+"\n"

print "min-win3 / avg-win2 = "+ str(k13)+"\n"
print "min-win3 / min-win2 = "+ str(k14)+"\n"
print "min-win3 / max-win2 = "+ str(k15)+"\n"

print "max-win3 / avg-win2 = "+ str(k16)+"\n"
print "max-win3 / min-win2 = "+ str(k17)+"\n"
print "max-win3 / max-win2 = "+ str(k18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(k19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(k20)+"\n"
print "std-win3 / std-win2 = "+ str(k21)+"\n"
print "std-win1 / std-win2 = "+ str(k22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(k23)+"\n"
print "avg-win1 / min-win2 = "+ str(k24)+"\n"
print "avg-win1 / max-win2 = "+ str(k25)+"\n"

print "min-win1 / avg-win2 = "+ str(k26)+"\n"
print "min-win1 / min-win2 = "+ str(k27)+"\n"
print "min-win1 / max-win2 = "+ str(k28)+"\n"

print "max-win1 / avg-win2 = "+ str(k29)+"\n"
print "max-win1 / min-win2 = "+ str(k30)+"\n"
print "max-win1 / max-win2 = "+ str(k31)+"\n"

print "############################################"


# ""LOSS # 12"""
print "Loss # 12"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind121=win121-300
ind122=win121-150
ind123=win121

print "\n index number for loss 12", ind121, ind122, ind123

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd121=[]
owd122=[]
owd123=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind121 and nn<ind122:
		owd121.append(iat[nn])
	elif nn>=ind122 and nn<ind123:
		owd122.append(iat[nn])
	elif nn>=ind123 and nn<ind123+150:
		owd123.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd121"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd121))
""" owd121 avg"""
print 'mean11 = {}'.format(numpy.mean(owd121))
"""owd121 min"""
print 'min11 = {}'.format(min(owd121))
"""owd121 max"""
print 'max11 = {}'.format(max(owd121))
""" owd121 std"""
print 'std11 = {}'.format(numpy.std(owd121))

"""for owd122"""
print "number of packets included = {}".format(len(owd122))
print 'mean12 = {}'.format(numpy.mean(owd122))
print 'min12 = {}'.format(min(owd122))
print 'max12 = {}'.format(max(owd122))
print 'std12 = {}'.format(numpy.std(owd122))

""" for owd123"""
print "number of packets included = {}".format(len(owd123))
print 'mean13 = {}'.format(numpy.mean(owd123))
print 'min13 = {}'.format(min(owd123))
print 'max13 = {}'.format(max(owd123))
print 'std13 = {}'.format(numpy.std(owd123))


""" next take the Window3/Window1""" 
l1 = numpy.mean(owd123)/numpy.mean(owd121)
l2 = numpy.mean(owd123)/numpy.min(owd121)
l3 = numpy.mean(owd123)/numpy.max(owd121)

l4 = numpy.min(owd123)/numpy.mean(owd121)
l5 = numpy.min(owd123)/numpy.min(owd121)
l6 = numpy.min(owd123)/numpy.max(owd121)

l7 = numpy.max(owd123)/numpy.mean(owd121)
l8 = numpy.max(owd123)/numpy.min(owd121)
l9 = numpy.max(owd123)/numpy.max(owd121)

"""next take the Window3/Window2"""
l10 = numpy.mean(owd123)/numpy.mean(owd122)
l11 = numpy.mean(owd123)/numpy.min(owd122)
l12 = numpy.mean(owd123)/numpy.max(owd122)

l13 = numpy.min(owd123)/numpy.mean(owd122)
l14 = numpy.min(owd123)/numpy.min(owd122)
l15 = numpy.min(owd123)/numpy.max(owd122)

l16 = numpy.max(owd123)/numpy.mean(owd122)
l17 = numpy.max(owd123)/numpy.min(owd122)
l18 = numpy.max(owd123)/numpy.max(owd122)

""" min/max window 3"""
l19 = numpy.min(owd123)/numpy.max(owd123)

"""standard dev values"""
l20 = numpy.std(owd123)/numpy.std(owd121)
l21 = numpy.std(owd123)/numpy.std(owd122)
l22 = numpy.std(owd121)/numpy.std(owd122)

"""next window1 / window2"""
l23 = numpy.mean(owd121)/numpy.mean(owd122)
l24 = numpy.mean(owd121)/numpy.min(owd122)
l25 = numpy.mean(owd121)/numpy.max(owd122)

l26 = numpy.min(owd121)/numpy.mean(owd122)
l27 = numpy.min(owd121)/numpy.min(owd122)
l28 = numpy.min(owd121)/numpy.max(owd122)

l29 = numpy.max(owd121)/numpy.mean(owd122)
l30 = numpy.max(owd121)/numpy.min(owd122)
l31 = numpy.max(owd121)/numpy.max(owd122)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(l1)+"\n"
print "avg-win3 / min-win1 = "+ str(l2)+"\n"
print "avg-win3 / max-win1 = "+ str(l3)+"\n"

print "min-win3 / avg-win1 = "+ str(l4)+"\n"
print "min-win3 / min-win1 = "+ str(l5)+"\n"
print "min-win3 / max-win1 = "+ str(l6)+"\n"

print "max-win3 / avg-win1 = "+ str(l7)+"\n"
print "max-win3 / min-win1 = "+ str(l8)+"\n"
print "max-win3 / max-win1 = "+ str(l9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(l10)+"\n"
print "avg-win3 / min-win2 = "+ str(l11)+"\n"
print "avg-win3 / max-win2 = "+ str(l12)+"\n"

print "min-win3 / avg-win2 = "+ str(l13)+"\n"
print "min-win3 / min-win2 = "+ str(l14)+"\n"
print "min-win3 / max-win2 = "+ str(l15)+"\n"

print "max-win3 / avg-win2 = "+ str(l16)+"\n"
print "max-win3 / min-win2 = "+ str(l17)+"\n"
print "max-win3 / max-win2 = "+ str(l18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(l19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(l20)+"\n"
print "std-win3 / std-win2 = "+ str(l21)+"\n"
print "std-win1 / std-win2 = "+ str(l22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(l23)+"\n"
print "avg-win1 / min-win2 = "+ str(l24)+"\n"
print "avg-win1 / max-win2 = "+ str(l25)+"\n"

print "min-win1 / avg-win2 = "+ str(l26)+"\n"
print "min-win1 / min-win2 = "+ str(l27)+"\n"
print "min-win1 / max-win2 = "+ str(l28)+"\n"

print "max-win1 / avg-win2 = "+ str(l29)+"\n"
print "max-win1 / min-win2 = "+ str(l30)+"\n"
print "max-win1 / max-win2 = "+ str(l31)+"\n"

print "##################################################"


"""LOSS # 13"""
print "Loss # 13"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind131=win131-300
ind132=win131-150
ind133=win131

print "\n index number for window1", ind131, ind132, ind133

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd131=[]
owd132=[]
owd133=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind131 and nn<ind132:
		owd131.append(iat[nn])
	elif nn>=ind132 and nn<ind133:
		owd132.append(iat[nn])
	elif nn>=ind133 and nn<ind133+150:
		owd133.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd131"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd131))
""" owd131 avg"""
print 'mean11 = {}'.format(numpy.mean(owd131))
"""owd131 min"""
print 'min11 = {}'.format(min(owd131))
"""owd131 max"""
print 'max11 = {}'.format(max(owd131))
""" owd131 std"""
print 'std11 = {}'.format(numpy.std(owd131))

"""for owd132"""
print "number of packets included = {}".format(len(owd132))
print 'mean12 = {}'.format(numpy.mean(owd132))
print 'min12 = {}'.format(min(owd132))
print 'max12 = {}'.format(max(owd132))
print 'std12 = {}'.format(numpy.std(owd132))

""" for owd133"""
print "number of packets included = {}".format(len(owd133))
print 'mean13 = {}'.format(numpy.mean(owd133))
print 'min13 = {}'.format(min(owd133))
print 'max13 = {}'.format(max(owd133))
print 'std13 = {}'.format(numpy.std(owd133))


""" next take the Window3/Window1""" 
m1 = numpy.mean(owd133)/numpy.mean(owd131)
m2 = numpy.mean(owd133)/numpy.min(owd131)
m3 = numpy.mean(owd133)/numpy.max(owd131)

m4 = numpy.min(owd133)/numpy.mean(owd131)
m5 = numpy.min(owd133)/numpy.min(owd131)
m6 = numpy.min(owd133)/numpy.max(owd131)

m7 = numpy.max(owd133)/numpy.mean(owd131)
m8 = numpy.max(owd133)/numpy.min(owd131)
m9 = numpy.max(owd133)/numpy.max(owd131)

"""next take the Window3/Window2"""
m10 = numpy.mean(owd133)/numpy.mean(owd132)
m11 = numpy.mean(owd133)/numpy.min(owd132)
m12 = numpy.mean(owd133)/numpy.max(owd132)

m13 = numpy.min(owd133)/numpy.mean(owd132)
m14 = numpy.min(owd133)/numpy.min(owd132)
m15 = numpy.min(owd133)/numpy.max(owd132)

m16 = numpy.max(owd133)/numpy.mean(owd132)
m17 = numpy.max(owd133)/numpy.min(owd132)
m18 = numpy.max(owd133)/numpy.max(owd132)

""" min/max window 3"""
m19 = numpy.min(owd133)/numpy.max(owd133)

"""standard dev values"""
m20 = numpy.std(owd133)/numpy.std(owd131)
m21 = numpy.std(owd133)/numpy.std(owd132)
m22 = numpy.std(owd131)/numpy.std(owd132)

"""next window1 / window2"""
m23 = numpy.mean(owd131)/numpy.mean(owd132)
m24 = numpy.mean(owd131)/numpy.min(owd132)
m25 = numpy.mean(owd131)/numpy.max(owd132)

m26 = numpy.min(owd131)/numpy.mean(owd132)
m27 = numpy.min(owd131)/numpy.min(owd132)
m28 = numpy.min(owd131)/numpy.max(owd132)

m29 = numpy.max(owd131)/numpy.mean(owd132)
m30 = numpy.max(owd131)/numpy.min(owd132)
m31 = numpy.max(owd131)/numpy.max(owd132)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(m1)+"\n"
print "avg-win3 / min-win1 = "+ str(m2)+"\n"
print "avg-win3 / max-win1 = "+ str(m3)+"\n"

print "min-win3 / avg-win1 = "+ str(m4)+"\n"
print "min-win3 / min-win1 = "+ str(m5)+"\n"
print "min-win3 / max-win1 = "+ str(m6)+"\n"

print "max-win3 / avg-win1 = "+ str(m7)+"\n"
print "max-win3 / min-win1 = "+ str(m8)+"\n"
print "max-win3 / max-win1 = "+ str(m9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(m10)+"\n"
print "avg-win3 / min-win2 = "+ str(m11)+"\n"
print "avg-win3 / max-win2 = "+ str(m12)+"\n"

print "min-win3 / avg-win2 = "+ str(m13)+"\n"
print "min-win3 / min-win2 = "+ str(m14)+"\n"
print "min-win3 / max-win2 = "+ str(m15)+"\n"

print "max-win3 / avg-win2 = "+ str(m16)+"\n"
print "max-win3 / min-win2 = "+ str(m17)+"\n"
print "max-win3 / max-win2 = "+ str(m18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(m19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(m20)+"\n"
print "std-win3 / std-win2 = "+ str(m21)+"\n"
print "std-win1 / std-win2 = "+ str(m22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(m23)+"\n"
print "avg-win1 / min-win2 = "+ str(m24)+"\n"
print "avg-win1 / max-win2 = "+ str(m25)+"\n"

print "min-win1 / avg-win2 = "+ str(m26)+"\n"
print "min-win1 / min-win2 = "+ str(m27)+"\n"
print "min-win1 / max-win2 = "+ str(m28)+"\n"

print "max-win1 / avg-win2 = "+ str(m29)+"\n"
print "max-win1 / min-win2 = "+ str(m30)+"\n"
print "max-win1 / max-win2 = "+ str(m31)+"\n"

print "#################################################"





"""8OSS # 14"""
print "Loss # 14"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind141=win141-300
ind142=win141-150
ind143=win141

print "\n index number for loss 14", ind141, ind142, ind143

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd141=[]
owd142=[]
owd143=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind141 and nn<ind142:
		owd141.append(iat[nn])
	elif nn>=ind142 and nn<ind143:
		owd142.append(iat[nn])
	elif nn>=ind143 and nn<ind143+150:
		owd143.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd141"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd141))
""" owd141 avg"""
print 'mean11 = {}'.format(numpy.mean(owd141))
"""owd141 min"""
print 'min11 = {}'.format(min(owd141))
"""owd141 max"""
print 'max11 = {}'.format(max(owd141))
""" owd141 std"""
print 'std11 = {}'.format(numpy.std(owd141))

"""for owd142"""
print "number of packets included = {}".format(len(owd142))
print 'mean12 = {}'.format(numpy.mean(owd142))
print 'min12 = {}'.format(min(owd142))
print 'max12 = {}'.format(max(owd142))
print 'std12 = {}'.format(numpy.std(owd142))

""" for owd143"""
print "number of packets included = {}".format(len(owd143))
print 'mean13 = {}'.format(numpy.mean(owd143))
print 'min13 = {}'.format(min(owd143))
print 'max13 = {}'.format(max(owd143))
print 'std13 = {}'.format(numpy.std(owd143))


""" next take the Window3/Window1""" 
n1 = numpy.mean(owd143)/numpy.mean(owd141)
n2 = numpy.mean(owd143)/numpy.min(owd141)
n3 = numpy.mean(owd143)/numpy.max(owd141)

n4 = numpy.min(owd143)/numpy.mean(owd141)
n5 = numpy.min(owd143)/numpy.min(owd141)
n6 = numpy.min(owd143)/numpy.max(owd141)

n7 = numpy.max(owd143)/numpy.mean(owd141)
n8 = numpy.max(owd143)/numpy.min(owd141)
n9 = numpy.max(owd143)/numpy.max(owd141)

"""next take the Window3/Window2"""
n10 = numpy.mean(owd143)/numpy.mean(owd142)
n11 = numpy.mean(owd143)/numpy.min(owd142)
n12 = numpy.mean(owd143)/numpy.max(owd142)

n13 = numpy.min(owd143)/numpy.mean(owd142)
n14 = numpy.min(owd143)/numpy.min(owd142)
n15 = numpy.min(owd143)/numpy.max(owd142)

n16 = numpy.max(owd143)/numpy.mean(owd142)
n17 = numpy.max(owd143)/numpy.min(owd142)
n18 = numpy.max(owd143)/numpy.max(owd142)

""" min/max window 3"""
n19 = numpy.min(owd143)/numpy.max(owd143)

"""standard dev values"""
n20 = numpy.std(owd143)/numpy.std(owd141)
n21 = numpy.std(owd143)/numpy.std(owd142)
n22 = numpy.std(owd141)/numpy.std(owd142)

"""next window1 / window2"""
n23 = numpy.mean(owd141)/numpy.mean(owd142)
n24 = numpy.mean(owd141)/numpy.min(owd142)
n25 = numpy.mean(owd141)/numpy.max(owd142)

n26 = numpy.min(owd141)/numpy.mean(owd142)
n27 = numpy.min(owd141)/numpy.min(owd142)
n28 = numpy.min(owd141)/numpy.max(owd142)

n29 = numpy.max(owd141)/numpy.mean(owd142)
n30 = numpy.max(owd141)/numpy.min(owd142)
n31 = numpy.max(owd141)/numpy.max(owd142)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(n1)+"\n"
print "avg-win3 / min-win1 = "+ str(n2)+"\n"
print "avg-win3 / max-win1 = "+ str(n3)+"\n"

print "min-win3 / avg-win1 = "+ str(n4)+"\n"
print "min-win3 / min-win1 = "+ str(n5)+"\n"
print "min-win3 / max-win1 = "+ str(n6)+"\n"

print "max-win3 / avg-win1 = "+ str(n7)+"\n"
print "max-win3 / min-win1 = "+ str(n8)+"\n"
print "max-win3 / max-win1 = "+ str(n9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(n10)+"\n"
print "avg-win3 / min-win2 = "+ str(n11)+"\n"
print "avg-win3 / max-win2 = "+ str(n12)+"\n"

print "min-win3 / avg-win2 = "+ str(n13)+"\n"
print "min-win3 / min-win2 = "+ str(n14)+"\n"
print "min-win3 / max-win2 = "+ str(n15)+"\n"

print "max-win3 / avg-win2 = "+ str(n16)+"\n"
print "max-win3 / min-win2 = "+ str(n17)+"\n"
print "max-win3 / max-win2 = "+ str(n18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(n19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(n20)+"\n"
print "std-win3 / std-win2 = "+ str(n21)+"\n"
print "std-win1 / std-win2 = "+ str(n22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(n23)+"\n"
print "avg-win1 / min-win2 = "+ str(n24)+"\n"
print "avg-win1 / max-win2 = "+ str(n25)+"\n"

print "min-win1 / avg-win2 = "+ str(n26)+"\n"
print "min-win1 / min-win2 = "+ str(n27)+"\n"
print "min-win1 / max-win2 = "+ str(n28)+"\n"

print "max-win1 / avg-win2 = "+ str(n29)+"\n"
print "max-win1 / min-win2 = "+ str(n30)+"\n"
print "max-win1 / max-win2 = "+ str(n31)+"\n"

print "#################################################"





"""LOSS # 15"""
print "Loss # 15"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind151=win151-300
ind152=win151-150
ind153=win151

print "\n index number for loss 15", ind151, ind152, ind153

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd151=[]
owd152=[]
owd153=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind151 and nn<ind152:
		owd151.append(iat[nn])
	elif nn>=ind152 and nn<ind153:
		owd152.append(iat[nn])
	elif nn>=ind153 and nn<ind153+150:
		owd153.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd151"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd151))
""" owd151 avg"""
print 'mean11 = {}'.format(numpy.mean(owd151))
"""owd151 min"""
print 'min11 = {}'.format(min(owd151))
"""owd151 max"""
print 'max11 = {}'.format(max(owd151))
""" owd151 std"""
print 'std11 = {}'.format(numpy.std(owd151))

"""for owd152"""
print "number of packets included = {}".format(len(owd152))
print 'mean12 = {}'.format(numpy.mean(owd152))
print 'min12 = {}'.format(min(owd152))
print 'max12 = {}'.format(max(owd152))
print 'std12 = {}'.format(numpy.std(owd152))

""" for owd153"""
print "number of packets included = {}".format(len(owd153))
print 'mean13 = {}'.format(numpy.mean(owd153))
print 'min13 = {}'.format(min(owd153))
print 'max13 = {}'.format(max(owd153))
print 'std13 = {}'.format(numpy.std(owd153))


""" next take the Window3/Window1""" 
o1 = numpy.mean(owd153)/numpy.mean(owd151)
o2 = numpy.mean(owd153)/numpy.min(owd151)
o3 = numpy.mean(owd153)/numpy.max(owd151)

o4 = numpy.min(owd153)/numpy.mean(owd151)
o5 = numpy.min(owd153)/numpy.min(owd151)
o6 = numpy.min(owd153)/numpy.max(owd151)

o7 = numpy.max(owd153)/numpy.mean(owd151)
o8 = numpy.max(owd153)/numpy.min(owd151)
o9 = numpy.max(owd153)/numpy.max(owd151)

"""next take the Window3/Window2"""
o10 = numpy.mean(owd153)/numpy.mean(owd152)
o11 = numpy.mean(owd153)/numpy.min(owd152)
o12 = numpy.mean(owd153)/numpy.max(owd152)

o13 = numpy.min(owd153)/numpy.mean(owd152)
o14 = numpy.min(owd153)/numpy.min(owd152)
o15 = numpy.min(owd153)/numpy.max(owd152)

o16 = numpy.max(owd153)/numpy.mean(owd152)
o17 = numpy.max(owd153)/numpy.min(owd152)
o18 = numpy.max(owd153)/numpy.max(owd152)

""" min/max window 3"""
o19 = numpy.min(owd153)/numpy.max(owd153)

"""standard dev values"""
o20 = numpy.std(owd153)/numpy.std(owd151)
o21 = numpy.std(owd153)/numpy.std(owd152)
o22 = numpy.std(owd151)/numpy.std(owd152)

"""next window1 / window2"""
o23 = numpy.mean(owd151)/numpy.mean(owd152)
o24 = numpy.mean(owd151)/numpy.min(owd152)
o25 = numpy.mean(owd151)/numpy.max(owd152)

o26 = numpy.min(owd151)/numpy.mean(owd152)
o27 = numpy.min(owd151)/numpy.min(owd152)
o28 = numpy.min(owd151)/numpy.max(owd152)

o29 = numpy.max(owd151)/numpy.mean(owd152)
o30 = numpy.max(owd151)/numpy.min(owd152)
o31 = numpy.max(owd151)/numpy.max(owd152)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(o1)+"\n"
print "avg-win3 / min-win1 = "+ str(o2)+"\n"
print "avg-win3 / max-win1 = "+ str(o3)+"\n"

print "min-win3 / avg-win1 = "+ str(o4)+"\n"
print "min-win3 / min-win1 = "+ str(o5)+"\n"
print "min-win3 / max-win1 = "+ str(o6)+"\n"

print "max-win3 / avg-win1 = "+ str(o7)+"\n"
print "max-win3 / min-win1 = "+ str(o8)+"\n"
print "max-win3 / max-win1 = "+ str(o9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(o10)+"\n"
print "avg-win3 / min-win2 = "+ str(o11)+"\n"
print "avg-win3 / max-win2 = "+ str(o12)+"\n"

print "min-win3 / avg-win2 = "+ str(o13)+"\n"
print "min-win3 / min-win2 = "+ str(o14)+"\n"
print "min-win3 / max-win2 = "+ str(o15)+"\n"

print "max-win3 / avg-win2 = "+ str(o16)+"\n"
print "max-win3 / min-win2 = "+ str(o17)+"\n"
print "max-win3 / max-win2 = "+ str(o18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(o19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(o20)+"\n"
print "std-win3 / std-win2 = "+ str(o21)+"\n"
print "std-win1 / std-win2 = "+ str(o22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(o23)+"\n"
print "avg-win1 / min-win2 = "+ str(o24)+"\n"
print "avg-win1 / max-win2 = "+ str(o25)+"\n"

print "min-win1 / avg-win2 = "+ str(o26)+"\n"
print "min-win1 / min-win2 = "+ str(o27)+"\n"
print "min-win1 / max-win2 = "+ str(o28)+"\n"

print "max-win1 / avg-win2 = "+ str(o29)+"\n"
print "max-win1 / min-win2 = "+ str(o30)+"\n"
print "max-win1 / max-win2 = "+ str(o31)+"\n"

print "#################################################"



"""LOSS # 16"""
print "Loss # 16"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind161=win161-300
ind162=win161-150
ind163=win161

print "\n index number for loss ", ind161, ind162, ind163

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd161=[]
owd162=[]
owd163=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind161 and nn<ind162:
		owd161.append(iat[nn])
	elif nn>=ind162 and nn<ind163:
		owd162.append(iat[nn])
	elif nn>=ind163 and nn<ind163+150:
		owd163.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd161"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd161))
""" owd161 avg"""
print 'mean11 = {}'.format(numpy.mean(owd161))
"""owd161 min"""
print 'min11 = {}'.format(min(owd161))
"""owd161 max"""
print 'max11 = {}'.format(max(owd161))
""" owd161 std"""
print 'std11 = {}'.format(numpy.std(owd161))

"""for owd162"""
print "number of packets included = {}".format(len(owd162))
print 'mean12 = {}'.format(numpy.mean(owd162))
print 'min12 = {}'.format(min(owd162))
print 'max12 = {}'.format(max(owd162))
print 'std12 = {}'.format(numpy.std(owd162))

""" for owd163"""
print "number of packets included = {}".format(len(owd163))
print 'mean13 = {}'.format(numpy.mean(owd163))
print 'min13 = {}'.format(min(owd163))
print 'max13 = {}'.format(max(owd163))
print 'std13 = {}'.format(numpy.std(owd163))


""" next take the Window3/Window1""" 
p1 = numpy.mean(owd163)/numpy.mean(owd161)
p2 = numpy.mean(owd163)/numpy.min(owd161)
p3 = numpy.mean(owd163)/numpy.max(owd161)

p4 = numpy.min(owd163)/numpy.mean(owd161)
p5 = numpy.min(owd163)/numpy.min(owd161)
p6 = numpy.min(owd163)/numpy.max(owd161)

p7 = numpy.max(owd163)/numpy.mean(owd161)
p8 = numpy.max(owd163)/numpy.min(owd161)
p9 = numpy.max(owd163)/numpy.max(owd161)

"""next take the Window3/Window2"""
p10 = numpy.mean(owd163)/numpy.mean(owd162)
p11 = numpy.mean(owd163)/numpy.min(owd162)
p12 = numpy.mean(owd163)/numpy.max(owd162)

p13 = numpy.min(owd163)/numpy.mean(owd162)
p14 = numpy.min(owd163)/numpy.min(owd162)
p15 = numpy.min(owd163)/numpy.max(owd162)

p16 = numpy.max(owd163)/numpy.mean(owd162)
p17 = numpy.max(owd163)/numpy.min(owd162)
p18 = numpy.max(owd163)/numpy.max(owd162)

""" min/max window 3"""
p19 = numpy.min(owd163)/numpy.max(owd163)

"""standard dev values"""
p20 = numpy.std(owd163)/numpy.std(owd161)
p21 = numpy.std(owd163)/numpy.std(owd162)
p22 = numpy.std(owd161)/numpy.std(owd162)

"""next window1 / window2"""
p23 = numpy.mean(owd161)/numpy.mean(owd162)
p24 = numpy.mean(owd161)/numpy.min(owd162)
p25 = numpy.mean(owd161)/numpy.max(owd162)

p26 = numpy.min(owd161)/numpy.mean(owd162)
p27 = numpy.min(owd161)/numpy.min(owd162)
p28 = numpy.min(owd161)/numpy.max(owd162)

p29 = numpy.max(owd161)/numpy.mean(owd162)
p30 = numpy.max(owd161)/numpy.min(owd162)
p31 = numpy.max(owd161)/numpy.max(owd162)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(p1)+"\n"
print "avg-win3 / min-win1 = "+ str(p2)+"\n"
print "avg-win3 / max-win1 = "+ str(p3)+"\n"

print "min-win3 / avg-win1 = "+ str(p4)+"\n"
print "min-win3 / min-win1 = "+ str(p5)+"\n"
print "min-win3 / max-win1 = "+ str(p6)+"\n"

print "max-win3 / avg-win1 = "+ str(p7)+"\n"
print "max-win3 / min-win1 = "+ str(p8)+"\n"
print "max-win3 / max-win1 = "+ str(p9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(p10)+"\n"
print "avg-win3 / min-win2 = "+ str(p11)+"\n"
print "avg-win3 / max-win2 = "+ str(p12)+"\n"

print "min-win3 / avg-win2 = "+ str(p13)+"\n"
print "min-win3 / min-win2 = "+ str(p14)+"\n"
print "min-win3 / max-win2 = "+ str(p15)+"\n"

print "max-win3 / avg-win2 = "+ str(p16)+"\n"
print "max-win3 / min-win2 = "+ str(p17)+"\n"
print "max-win3 / max-win2 = "+ str(p18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(p19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(p20)+"\n"
print "std-win3 / std-win2 = "+ str(p21)+"\n"
print "std-win1 / std-win2 = "+ str(p22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(p23)+"\n"
print "avg-win1 / min-win2 = "+ str(p24)+"\n"
print "avg-win1 / max-win2 = "+ str(p25)+"\n"

print "min-win1 / avg-win2 = "+ str(p26)+"\n"
print "min-win1 / min-win2 = "+ str(p27)+"\n"
print "min-win1 / max-win2 = "+ str(p28)+"\n"

print "max-win1 / avg-win2 = "+ str(p29)+"\n"
print "max-win1 / min-win2 = "+ str(p30)+"\n"
print "max-win1 / max-win2 = "+ str(p31)+"\n"

print "#################################################"






"""LOSS # 17"""
print "Loss # 17"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind171=win171-300
ind172=win171-150
ind173=win171

print "\n index number for loss ", ind171, ind172, ind173

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd171=[]
owd172=[]
owd173=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind171 and nn<ind172:
		owd171.append(iat[nn])
	elif nn>=ind172 and nn<ind173:
		owd172.append(iat[nn])
	elif nn>=ind173 and nn<ind173+150:
		owd173.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd171"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd171))
""" owd171 avg"""
print 'mean11 = {}'.format(numpy.mean(owd171))
"""owd171 min"""
print 'min11 = {}'.format(min(owd171))
"""owd171 max"""
print 'max11 = {}'.format(max(owd171))
""" owd171 std"""
print 'std11 = {}'.format(numpy.std(owd171))

"""for owd172"""
print "number of packets included = {}".format(len(owd172))
print 'mean12 = {}'.format(numpy.mean(owd172))
print 'min12 = {}'.format(min(owd172))
print 'max12 = {}'.format(max(owd172))
print 'std12 = {}'.format(numpy.std(owd172))

""" for owd173"""
print "number of packets included = {}".format(len(owd173))
print 'mean13 = {}'.format(numpy.mean(owd173))
print 'min13 = {}'.format(min(owd173))
print 'max13 = {}'.format(max(owd173))
print 'std13 = {}'.format(numpy.std(owd173))


""" next take the Window3/Window1""" 
q1 = numpy.mean(owd173)/numpy.mean(owd171)
q2 = numpy.mean(owd173)/numpy.min(owd171)
q3 = numpy.mean(owd173)/numpy.max(owd171)

q4 = numpy.min(owd173)/numpy.mean(owd171)
q5 = numpy.min(owd173)/numpy.min(owd171)
q6 = numpy.min(owd173)/numpy.max(owd171)

q7 = numpy.max(owd173)/numpy.mean(owd171)
q8 = numpy.max(owd173)/numpy.min(owd171)
q9 = numpy.max(owd173)/numpy.max(owd171)

"""next take the Window3/Window2"""
q10 = numpy.mean(owd173)/numpy.mean(owd172)
q11 = numpy.mean(owd173)/numpy.min(owd172)
q12 = numpy.mean(owd173)/numpy.max(owd172)

q13 = numpy.min(owd173)/numpy.mean(owd172)
q14 = numpy.min(owd173)/numpy.min(owd172)
q15 = numpy.min(owd173)/numpy.max(owd172)

q16 = numpy.max(owd173)/numpy.mean(owd172)
q17 = numpy.max(owd173)/numpy.min(owd172)
q18 = numpy.max(owd173)/numpy.max(owd172)

""" min/max window 3"""
q19 = numpy.min(owd173)/numpy.max(owd173)

"""standard dev values"""
q20 = numpy.std(owd173)/numpy.std(owd171)
q21 = numpy.std(owd173)/numpy.std(owd172)
q22 = numpy.std(owd171)/numpy.std(owd172)

"""next window1 / window2"""
q23 = numpy.mean(owd171)/numpy.mean(owd172)
q24 = numpy.mean(owd171)/numpy.min(owd172)
q25 = numpy.mean(owd171)/numpy.max(owd172)

q26 = numpy.min(owd171)/numpy.mean(owd172)
q27 = numpy.min(owd171)/numpy.min(owd172)
q28 = numpy.min(owd171)/numpy.max(owd172)

q29 = numpy.max(owd171)/numpy.mean(owd172)
q30 = numpy.max(owd171)/numpy.min(owd172)
q31 = numpy.max(owd171)/numpy.max(owd172)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(q1)+"\n"
print "avg-win3 / min-win1 = "+ str(q2)+"\n"
print "avg-win3 / max-win1 = "+ str(q3)+"\n"

print "min-win3 / avg-win1 = "+ str(q4)+"\n"
print "min-win3 / min-win1 = "+ str(q5)+"\n"
print "min-win3 / max-win1 = "+ str(q6)+"\n"

print "max-win3 / avg-win1 = "+ str(q7)+"\n"
print "max-win3 / min-win1 = "+ str(q8)+"\n"
print "max-win3 / max-win1 = "+ str(q9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(q10)+"\n"
print "avg-win3 / min-win2 = "+ str(q11)+"\n"
print "avg-win3 / max-win2 = "+ str(q12)+"\n"

print "min-win3 / avg-win2 = "+ str(q13)+"\n"
print "min-win3 / min-win2 = "+ str(q14)+"\n"
print "min-win3 / max-win2 = "+ str(q15)+"\n"

print "max-win3 / avg-win2 = "+ str(q16)+"\n"
print "max-win3 / min-win2 = "+ str(q17)+"\n"
print "max-win3 / max-win2 = "+ str(q18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(q19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(q20)+"\n"
print "std-win3 / std-win2 = "+ str(q21)+"\n"
print "std-win1 / std-win2 = "+ str(q22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(q23)+"\n"
print "avg-win1 / min-win2 = "+ str(q24)+"\n"
print "avg-win1 / max-win2 = "+ str(q25)+"\n"

print "min-win1 / avg-win2 = "+ str(q26)+"\n"
print "min-win1 / min-win2 = "+ str(q27)+"\n"
print "min-win1 / max-win2 = "+ str(q28)+"\n"

print "max-win1 / avg-win2 = "+ str(q29)+"\n"
print "max-win1 / min-win2 = "+ str(q30)+"\n"
print "max-win1 / max-win2 = "+ str(q31)+"\n"

print "#################################################"







"""LOSS # 18"""
print "Loss # 18"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind181=win181-300
ind182=win181-150
ind183=win181

print "\n index number for loss ", ind181, ind182, ind183

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd181=[]
owd182=[]
owd183=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind181 and nn<ind182:
		owd181.append(iat[nn])
	elif nn>=ind182 and nn<ind183:
		owd182.append(iat[nn])
	elif nn>=ind183 and nn<ind183+150:
		owd183.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd181"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd181))
""" owd181 avg"""
print 'mean11 = {}'.format(numpy.mean(owd181))
"""owd181 min"""
print 'min11 = {}'.format(min(owd181))
"""owd181 max"""
print 'max11 = {}'.format(max(owd181))
""" owd181 std"""
print 'std11 = {}'.format(numpy.std(owd181))

"""for owd182"""
print "number of packets included = {}".format(len(owd182))
print 'mean12 = {}'.format(numpy.mean(owd182))
print 'min12 = {}'.format(min(owd182))
print 'max12 = {}'.format(max(owd182))
print 'std12 = {}'.format(numpy.std(owd182))

""" for owd183"""
print "number of packets included = {}".format(len(owd183))
print 'mean13 = {}'.format(numpy.mean(owd183))
print 'min13 = {}'.format(min(owd183))
print 'max13 = {}'.format(max(owd183))
print 'std13 = {}'.format(numpy.std(owd183))


""" next take the Window3/Window1""" 
r1 = numpy.mean(owd183)/numpy.mean(owd181)
r2 = numpy.mean(owd183)/numpy.min(owd181)
r3 = numpy.mean(owd183)/numpy.max(owd181)

r4 = numpy.min(owd183)/numpy.mean(owd181)
r5 = numpy.min(owd183)/numpy.min(owd181)
r6 = numpy.min(owd183)/numpy.max(owd181)

r7 = numpy.max(owd183)/numpy.mean(owd181)
r8 = numpy.max(owd183)/numpy.min(owd181)
r9 = numpy.max(owd183)/numpy.max(owd181)

"""next take the Window3/Window2"""
r10 = numpy.mean(owd183)/numpy.mean(owd182)
r11 = numpy.mean(owd183)/numpy.min(owd182)
r12 = numpy.mean(owd183)/numpy.max(owd182)

r13 = numpy.min(owd183)/numpy.mean(owd182)
r14 = numpy.min(owd183)/numpy.min(owd182)
r15 = numpy.min(owd183)/numpy.max(owd182)

r16 = numpy.max(owd183)/numpy.mean(owd182)
r17 = numpy.max(owd183)/numpy.min(owd182)
r18 = numpy.max(owd183)/numpy.max(owd182)

""" min/max window 3"""
r19 = numpy.min(owd183)/numpy.max(owd183)

"""standard dev values"""
r20 = numpy.std(owd183)/numpy.std(owd181)
r21 = numpy.std(owd183)/numpy.std(owd182)
r22 = numpy.std(owd181)/numpy.std(owd182)

"""next window1 / window2"""
r23 = numpy.mean(owd181)/numpy.mean(owd182)
r24 = numpy.mean(owd181)/numpy.min(owd182)
r25 = numpy.mean(owd181)/numpy.max(owd182)

r26 = numpy.min(owd181)/numpy.mean(owd182)
r27 = numpy.min(owd181)/numpy.min(owd182)
r28 = numpy.min(owd181)/numpy.max(owd182)

r29 = numpy.max(owd181)/numpy.mean(owd182)
r30 = numpy.max(owd181)/numpy.min(owd182)
r31 = numpy.max(owd181)/numpy.max(owd182)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(r1)+"\n"
print "avg-win3 / min-win1 = "+ str(r2)+"\n"
print "avg-win3 / max-win1 = "+ str(r3)+"\n"

print "min-win3 / avg-win1 = "+ str(r4)+"\n"
print "min-win3 / min-win1 = "+ str(r5)+"\n"
print "min-win3 / max-win1 = "+ str(r6)+"\n"

print "max-win3 / avg-win1 = "+ str(r7)+"\n"
print "max-win3 / min-win1 = "+ str(r8)+"\n"
print "max-win3 / max-win1 = "+ str(r9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(r10)+"\n"
print "avg-win3 / min-win2 = "+ str(r11)+"\n"
print "avg-win3 / max-win2 = "+ str(r12)+"\n"

print "min-win3 / avg-win2 = "+ str(r13)+"\n"
print "min-win3 / min-win2 = "+ str(r14)+"\n"
print "min-win3 / max-win2 = "+ str(r15)+"\n"

print "max-win3 / avg-win2 = "+ str(r16)+"\n"
print "max-win3 / min-win2 = "+ str(r17)+"\n"
print "max-win3 / max-win2 = "+ str(r18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(r19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(r20)+"\n"
print "std-win3 / std-win2 = "+ str(r21)+"\n"
print "std-win1 / std-win2 = "+ str(r22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(r23)+"\n"
print "avg-win1 / min-win2 = "+ str(r24)+"\n"
print "avg-win1 / max-win2 = "+ str(r25)+"\n"

print "min-win1 / avg-win2 = "+ str(r26)+"\n"
print "min-win1 / min-win2 = "+ str(r27)+"\n"
print "min-win1 / max-win2 = "+ str(r28)+"\n"

print "max-win1 / avg-win2 = "+ str(r29)+"\n"
print "max-win1 / min-win2 = "+ str(r30)+"\n"
print "max-win1 / max-win2 = "+ str(r31)+"\n"

print "#################################################"



"""LOSS # 19"""
print "Loss # 19"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind191=win191-300
ind192=win191-150
ind193=win191

print "\n index number for loss 19 ", ind191, ind192, ind193

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd191=[]
owd192=[]
owd193=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind191 and nn<ind192:
		owd191.append(iat[nn])
	elif nn>=ind192 and nn<ind193:
		owd192.append(iat[nn])
	elif nn>=ind193 and nn<ind193+150:
		owd193.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd191"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd191))
""" owd191 avg"""
print 'mean11 = {}'.format(numpy.mean(owd191))
"""owd191 min"""
print 'min11 = {}'.format(min(owd191))
"""owd191 max"""
print 'max11 = {}'.format(max(owd191))
""" owd191 std"""
print 'std11 = {}'.format(numpy.std(owd191))

"""for owd192"""
print "number of packets included = {}".format(len(owd192))
print 'mean12 = {}'.format(numpy.mean(owd192))
print 'min12 = {}'.format(min(owd192))
print 'max12 = {}'.format(max(owd192))
print 'std12 = {}'.format(numpy.std(owd192))

""" for owd193"""
print "number of packets included = {}".format(len(owd193))
print 'mean13 = {}'.format(numpy.mean(owd193))
print 'min13 = {}'.format(min(owd193))
print 'max13 = {}'.format(max(owd193))
print 'std13 = {}'.format(numpy.std(owd193))


""" next take the Window3/Window1""" 
s1 = numpy.mean(owd193)/numpy.mean(owd191)
s2 = numpy.mean(owd193)/numpy.min(owd191)
s3 = numpy.mean(owd193)/numpy.max(owd191)

s4 = numpy.min(owd193)/numpy.mean(owd191)
s5 = numpy.min(owd193)/numpy.min(owd191)
s6 = numpy.min(owd193)/numpy.max(owd191)

s7 = numpy.max(owd193)/numpy.mean(owd191)
s8 = numpy.max(owd193)/numpy.min(owd191)
s9 = numpy.max(owd193)/numpy.max(owd191)

"""next take the Window3/Window2"""
s10 = numpy.mean(owd193)/numpy.mean(owd192)
s11 = numpy.mean(owd193)/numpy.min(owd192)
s12 = numpy.mean(owd193)/numpy.max(owd192)

s13 = numpy.min(owd193)/numpy.mean(owd192)
s14 = numpy.min(owd193)/numpy.min(owd192)
s15 = numpy.min(owd193)/numpy.max(owd192)

s16 = numpy.max(owd193)/numpy.mean(owd192)
s17 = numpy.max(owd193)/numpy.min(owd192)
s18 = numpy.max(owd193)/numpy.max(owd192)

""" min/max window 3"""
s19 = numpy.min(owd193)/numpy.max(owd193)

"""standard dev values"""
s20 = numpy.std(owd193)/numpy.std(owd191)
s21 = numpy.std(owd193)/numpy.std(owd192)
s22 = numpy.std(owd191)/numpy.std(owd192)

"""next window1 / window2"""
s23 = numpy.mean(owd191)/numpy.mean(owd192)
s24 = numpy.mean(owd191)/numpy.min(owd192)
s25 = numpy.mean(owd191)/numpy.max(owd192)

s26 = numpy.min(owd191)/numpy.mean(owd192)
s27 = numpy.min(owd191)/numpy.min(owd192)
s28 = numpy.min(owd191)/numpy.max(owd192)

s29 = numpy.max(owd191)/numpy.mean(owd192)
s30 = numpy.max(owd191)/numpy.min(owd192)
s31 = numpy.max(owd191)/numpy.max(owd192)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(s1)+"\n"
print "avg-win3 / min-win1 = "+ str(s2)+"\n"
print "avg-win3 / max-win1 = "+ str(s3)+"\n"

print "min-win3 / avg-win1 = "+ str(s4)+"\n"
print "min-win3 / min-win1 = "+ str(s5)+"\n"
print "min-win3 / max-win1 = "+ str(s6)+"\n"

print "max-win3 / avg-win1 = "+ str(s7)+"\n"
print "max-win3 / min-win1 = "+ str(s8)+"\n"
print "max-win3 / max-win1 = "+ str(s9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(s10)+"\n"
print "avg-win3 / min-win2 = "+ str(s11)+"\n"
print "avg-win3 / max-win2 = "+ str(s12)+"\n"

print "min-win3 / avg-win2 = "+ str(s13)+"\n"
print "min-win3 / min-win2 = "+ str(s14)+"\n"
print "min-win3 / max-win2 = "+ str(s15)+"\n"

print "max-win3 / avg-win2 = "+ str(s16)+"\n"
print "max-win3 / min-win2 = "+ str(s17)+"\n"
print "max-win3 / max-win2 = "+ str(s18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(s19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(s20)+"\n"
print "std-win3 / std-win2 = "+ str(s21)+"\n"
print "std-win1 / std-win2 = "+ str(s22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(s23)+"\n"
print "avg-win1 / min-win2 = "+ str(s24)+"\n"
print "avg-win1 / max-win2 = "+ str(s25)+"\n"

print "min-win1 / avg-win2 = "+ str(s26)+"\n"
print "min-win1 / min-win2 = "+ str(s27)+"\n"
print "min-win1 / max-win2 = "+ str(s28)+"\n"

print "max-win1 / avg-win2 = "+ str(s29)+"\n"
print "max-win1 / min-win2 = "+ str(s30)+"\n"
print "max-win1 / max-win2 = "+ str(s31)+"\n"

print "#################################################"






"""LOSS # 20"""
print "Loss # 20"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind201=win201-300
ind202=win201-150
ind203=win201

print "\n index number for loss 19 ", ind201, ind202, ind203

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd201=[]
owd202=[]
owd203=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind201 and nn<ind202:
		owd201.append(iat[nn])
	elif nn>=ind202 and nn<ind203:
		owd202.append(iat[nn])
	elif nn>=ind203 and nn<ind203+150:
		owd203.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd201"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd201))
""" owd201 avg"""
print 'mean11 = {}'.format(numpy.mean(owd201))
"""owd201 min"""
print 'min11 = {}'.format(min(owd201))
"""owd201 max"""
print 'max11 = {}'.format(max(owd201))
""" owd201 std"""
print 'std11 = {}'.format(numpy.std(owd201))

"""for owd202"""
print "number of packets included = {}".format(len(owd202))
print 'mean12 = {}'.format(numpy.mean(owd202))
print 'min12 = {}'.format(min(owd202))
print 'max12 = {}'.format(max(owd202))
print 'std12 = {}'.format(numpy.std(owd202))

""" for owd203"""
print "number of packets included = {}".format(len(owd203))
print 'mean13 = {}'.format(numpy.mean(owd203))
print 'min13 = {}'.format(min(owd203))
print 'max13 = {}'.format(max(owd203))
print 'std13 = {}'.format(numpy.std(owd203))


""" next take the Window3/Window1""" 
t1 = numpy.mean(owd203)/numpy.mean(owd201)
t2 = numpy.mean(owd203)/numpy.min(owd201)
t3 = numpy.mean(owd203)/numpy.max(owd201)

t4 = numpy.min(owd203)/numpy.mean(owd201)
t5 = numpy.min(owd203)/numpy.min(owd201)
t6 = numpy.min(owd203)/numpy.max(owd201)

t7 = numpy.max(owd203)/numpy.mean(owd201)
t8 = numpy.max(owd203)/numpy.min(owd201)
t9 = numpy.max(owd203)/numpy.max(owd201)

"""next take the Window3/Window2"""
t10 = numpy.mean(owd203)/numpy.mean(owd202)
t11 = numpy.mean(owd203)/numpy.min(owd202)
t12 = numpy.mean(owd203)/numpy.max(owd202)

t13 = numpy.min(owd203)/numpy.mean(owd202)
t14 = numpy.min(owd203)/numpy.min(owd202)
t15 = numpy.min(owd203)/numpy.max(owd202)

t16 = numpy.max(owd203)/numpy.mean(owd202)
t17 = numpy.max(owd203)/numpy.min(owd202)
t18 = numpy.max(owd203)/numpy.max(owd202)

""" min/max window 3"""
t19 = numpy.min(owd203)/numpy.max(owd203)

"""standard dev values"""
t20 = numpy.std(owd203)/numpy.std(owd201)
t21 = numpy.std(owd203)/numpy.std(owd202)
t22 = numpy.std(owd201)/numpy.std(owd202)

"""next window1 / window2"""
t23 = numpy.mean(owd201)/numpy.mean(owd202)
t24 = numpy.mean(owd201)/numpy.min(owd202)
t25 = numpy.mean(owd201)/numpy.max(owd202)

t26 = numpy.min(owd201)/numpy.mean(owd202)
t27 = numpy.min(owd201)/numpy.min(owd202)
t28 = numpy.min(owd201)/numpy.max(owd202)

t29 = numpy.max(owd201)/numpy.mean(owd202)
t30 = numpy.max(owd201)/numpy.min(owd202)
t31 = numpy.max(owd201)/numpy.max(owd202)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(t1)+"\n"
print "avg-win3 / min-win1 = "+ str(t2)+"\n"
print "avg-win3 / max-win1 = "+ str(t3)+"\n"

print "min-win3 / avg-win1 = "+ str(t4)+"\n"
print "min-win3 / min-win1 = "+ str(t5)+"\n"
print "min-win3 / max-win1 = "+ str(t6)+"\n"

print "max-win3 / avg-win1 = "+ str(t7)+"\n"
print "max-win3 / min-win1 = "+ str(t8)+"\n"
print "max-win3 / max-win1 = "+ str(t9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(t10)+"\n"
print "avg-win3 / min-win2 = "+ str(t11)+"\n"
print "avg-win3 / max-win2 = "+ str(t12)+"\n"

print "min-win3 / avg-win2 = "+ str(t13)+"\n"
print "min-win3 / min-win2 = "+ str(t14)+"\n"
print "min-win3 / max-win2 = "+ str(t15)+"\n"

print "max-win3 / avg-win2 = "+ str(t16)+"\n"
print "max-win3 / min-win2 = "+ str(t17)+"\n"
print "max-win3 / max-win2 = "+ str(t18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(t19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(t20)+"\n"
print "std-win3 / std-win2 = "+ str(t21)+"\n"
print "std-win1 / std-win2 = "+ str(t22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(t23)+"\n"
print "avg-win1 / min-win2 = "+ str(t24)+"\n"
print "avg-win1 / max-win2 = "+ str(t25)+"\n"

print "min-win1 / avg-win2 = "+ str(t26)+"\n"
print "min-win1 / min-win2 = "+ str(t27)+"\n"
print "min-win1 / max-win2 = "+ str(t28)+"\n"

print "max-win1 / avg-win2 = "+ str(t29)+"\n"
print "max-win1 / min-win2 = "+ str(t30)+"\n"
print "max-win1 / max-win2 = "+ str(t31)+"\n"

print "#################################################"








"""LOSS # 21"""
print "Loss # 21"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind211=win211-300
ind212=win211-150
ind213=win211

print "\n index number for loss 21", ind211, ind212, ind213

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd211=[]
owd212=[]
owd213=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind211 and nn<ind212:
		owd211.append(iat[nn])
	elif nn>=ind212 and nn<ind213:
		owd212.append(iat[nn])
	elif nn>=ind213 and nn<ind213+150:
		owd213.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd211"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd211))
""" owd211 avg"""
print 'mean11 = {}'.format(numpy.mean(owd211))
"""owd211 min"""
print 'min11 = {}'.format(min(owd211))
"""owd211 max"""
print 'max11 = {}'.format(max(owd211))
""" owd211 std"""
print 'std11 = {}'.format(numpy.std(owd211))

"""for owd212"""
print "number of packets included = {}".format(len(owd212))
print 'mean12 = {}'.format(numpy.mean(owd212))
print 'min12 = {}'.format(min(owd212))
print 'max12 = {}'.format(max(owd212))
print 'std12 = {}'.format(numpy.std(owd212))

""" for owd213"""
print "number of packets included = {}".format(len(owd213))
print 'mean13 = {}'.format(numpy.mean(owd213))
print 'min13 = {}'.format(min(owd213))
print 'max13 = {}'.format(max(owd213))
print 'std13 = {}'.format(numpy.std(owd213))


""" next take the Window3/Window1""" 
u1 = numpy.mean(owd213)/numpy.mean(owd211)
u2 = numpy.mean(owd213)/numpy.min(owd211)
u3 = numpy.mean(owd213)/numpy.max(owd211)

u4 = numpy.min(owd213)/numpy.mean(owd211)
u5 = numpy.min(owd213)/numpy.min(owd211)
u6 = numpy.min(owd213)/numpy.max(owd211)

u7 = numpy.max(owd213)/numpy.mean(owd211)
u8 = numpy.max(owd213)/numpy.min(owd211)
u9 = numpy.max(owd213)/numpy.max(owd211)

"""next take the Window3/Window2"""
u10 = numpy.mean(owd213)/numpy.mean(owd212)
u11 = numpy.mean(owd213)/numpy.min(owd212)
u12 = numpy.mean(owd213)/numpy.max(owd212)

u13 = numpy.min(owd213)/numpy.mean(owd212)
u14 = numpy.min(owd213)/numpy.min(owd212)
u15 = numpy.min(owd213)/numpy.max(owd212)

u16 = numpy.max(owd213)/numpy.mean(owd212)
u17 = numpy.max(owd213)/numpy.min(owd212)
u18 = numpy.max(owd213)/numpy.max(owd212)

""" min/max window 3"""
u19 = numpy.min(owd213)/numpy.max(owd213)

"""standard dev values"""
u20 = numpy.std(owd213)/numpy.std(owd211)
u21 = numpy.std(owd213)/numpy.std(owd212)
u22 = numpy.std(owd211)/numpy.std(owd212)

"""next window1 / window2"""
u23 = numpy.mean(owd211)/numpy.mean(owd212)
u24 = numpy.mean(owd211)/numpy.min(owd212)
u25 = numpy.mean(owd211)/numpy.max(owd212)

u26 = numpy.min(owd211)/numpy.mean(owd212)
u27 = numpy.min(owd211)/numpy.min(owd212)
u28 = numpy.min(owd211)/numpy.max(owd212)

u29 = numpy.max(owd211)/numpy.mean(owd212)
u30 = numpy.max(owd211)/numpy.min(owd212)
u31 = numpy.max(owd211)/numpy.max(owd212)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(u1)+"\n"
print "avg-win3 / min-win1 = "+ str(u2)+"\n"
print "avg-win3 / max-win1 = "+ str(u3)+"\n"

print "min-win3 / avg-win1 = "+ str(u4)+"\n"
print "min-win3 / min-win1 = "+ str(u5)+"\n"
print "min-win3 / max-win1 = "+ str(u6)+"\n"

print "max-win3 / avg-win1 = "+ str(u7)+"\n"
print "max-win3 / min-win1 = "+ str(u8)+"\n"
print "max-win3 / max-win1 = "+ str(u9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(u10)+"\n"
print "avg-win3 / min-win2 = "+ str(u11)+"\n"
print "avg-win3 / max-win2 = "+ str(u12)+"\n"

print "min-win3 / avg-win2 = "+ str(u13)+"\n"
print "min-win3 / min-win2 = "+ str(u14)+"\n"
print "min-win3 / max-win2 = "+ str(u15)+"\n"

print "max-win3 / avg-win2 = "+ str(u16)+"\n"
print "max-win3 / min-win2 = "+ str(u17)+"\n"
print "max-win3 / max-win2 = "+ str(u18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(u19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(u20)+"\n"
print "std-win3 / std-win2 = "+ str(u21)+"\n"
print "std-win1 / std-win2 = "+ str(u22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(u23)+"\n"
print "avg-win1 / min-win2 = "+ str(u24)+"\n"
print "avg-win1 / max-win2 = "+ str(u25)+"\n"

print "min-win1 / avg-win2 = "+ str(u26)+"\n"
print "min-win1 / min-win2 = "+ str(u27)+"\n"
print "min-win1 / max-win2 = "+ str(u28)+"\n"

print "max-win1 / avg-win2 = "+ str(u29)+"\n"
print "max-win1 / min-win2 = "+ str(u30)+"\n"
print "max-win1 / max-win2 = "+ str(u31)+"\n"

print "#################################################"








"""LOSS # 22"""
print "Loss # 22"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind221=win221-300
ind222=win221-150
ind223=win221

print "\n index number for loss 22", ind221, ind222, ind223

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd221=[]
owd222=[]
owd223=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind221 and nn<ind222:
		owd221.append(iat[nn])
	elif nn>=ind222 and nn<ind223:
		owd222.append(iat[nn])
	elif nn>=ind223 and nn<ind223+150:
		owd223.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd221"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd221))
""" owd221 avg"""
print 'mean11 = {}'.format(numpy.mean(owd221))
"""owd221 min"""
print 'min11 = {}'.format(min(owd221))
"""owd221 max"""
print 'max11 = {}'.format(max(owd221))
""" owd221 std"""
print 'std11 = {}'.format(numpy.std(owd221))

"""for owd222"""
print "number of packets included = {}".format(len(owd222))
print 'mean12 = {}'.format(numpy.mean(owd222))
print 'min12 = {}'.format(min(owd222))
print 'max12 = {}'.format(max(owd222))
print 'std12 = {}'.format(numpy.std(owd222))

""" for owd223"""
print "number of packets included = {}".format(len(owd223))
print 'mean13 = {}'.format(numpy.mean(owd223))
print 'min13 = {}'.format(min(owd223))
print 'max13 = {}'.format(max(owd223))
print 'std13 = {}'.format(numpy.std(owd223))


""" next take the Window3/Window1""" 
v1 = numpy.mean(owd223)/numpy.mean(owd221)
v2 = numpy.mean(owd223)/numpy.min(owd221)
v3 = numpy.mean(owd223)/numpy.max(owd221)

v4 = numpy.min(owd223)/numpy.mean(owd221)
v5 = numpy.min(owd223)/numpy.min(owd221)
v6 = numpy.min(owd223)/numpy.max(owd221)

v7 = numpy.max(owd223)/numpy.mean(owd221)
v8 = numpy.max(owd223)/numpy.min(owd221)
v9 = numpy.max(owd223)/numpy.max(owd221)

"""next take the Window3/Window2"""
v10 = numpy.mean(owd223)/numpy.mean(owd222)
v11 = numpy.mean(owd223)/numpy.min(owd222)
v12 = numpy.mean(owd223)/numpy.max(owd222)

v13 = numpy.min(owd223)/numpy.mean(owd222)
v14 = numpy.min(owd223)/numpy.min(owd222)
v15 = numpy.min(owd223)/numpy.max(owd222)

v16 = numpy.max(owd223)/numpy.mean(owd222)
v17 = numpy.max(owd223)/numpy.min(owd222)
v18 = numpy.max(owd223)/numpy.max(owd222)

""" min/max window 3"""
v19 = numpy.min(owd223)/numpy.max(owd223)

"""standard dev values"""
v20 = numpy.std(owd223)/numpy.std(owd221)
v21 = numpy.std(owd223)/numpy.std(owd222)
v22 = numpy.std(owd221)/numpy.std(owd222)

"""next window1 / window2"""
v23 = numpy.mean(owd221)/numpy.mean(owd222)
v24 = numpy.mean(owd221)/numpy.min(owd222)
v25 = numpy.mean(owd221)/numpy.max(owd222)

v26 = numpy.min(owd221)/numpy.mean(owd222)
v27 = numpy.min(owd221)/numpy.min(owd222)
v28 = numpy.min(owd221)/numpy.max(owd222)

v29 = numpy.max(owd221)/numpy.mean(owd222)
v30 = numpy.max(owd221)/numpy.min(owd222)
v31 = numpy.max(owd221)/numpy.max(owd222)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(v1)+"\n"
print "avg-win3 / min-win1 = "+ str(v2)+"\n"
print "avg-win3 / max-win1 = "+ str(v3)+"\n"

print "min-win3 / avg-win1 = "+ str(v4)+"\n"
print "min-win3 / min-win1 = "+ str(v5)+"\n"
print "min-win3 / max-win1 = "+ str(v6)+"\n"

print "max-win3 / avg-win1 = "+ str(v7)+"\n"
print "max-win3 / min-win1 = "+ str(v8)+"\n"
print "max-win3 / max-win1 = "+ str(v9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(v10)+"\n"
print "avg-win3 / min-win2 = "+ str(v11)+"\n"
print "avg-win3 / max-win2 = "+ str(v12)+"\n"

print "min-win3 / avg-win2 = "+ str(v13)+"\n"
print "min-win3 / min-win2 = "+ str(v14)+"\n"
print "min-win3 / max-win2 = "+ str(v15)+"\n"

print "max-win3 / avg-win2 = "+ str(v16)+"\n"
print "max-win3 / min-win2 = "+ str(v17)+"\n"
print "max-win3 / max-win2 = "+ str(v18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(v19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(v20)+"\n"
print "std-win3 / std-win2 = "+ str(v21)+"\n"
print "std-win1 / std-win2 = "+ str(v22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(v23)+"\n"
print "avg-win1 / min-win2 = "+ str(v24)+"\n"
print "avg-win1 / max-win2 = "+ str(v25)+"\n"

print "min-win1 / avg-win2 = "+ str(v26)+"\n"
print "min-win1 / min-win2 = "+ str(v27)+"\n"
print "min-win1 / max-win2 = "+ str(v28)+"\n"

print "max-win1 / avg-win2 = "+ str(v29)+"\n"
print "max-win1 / min-win2 = "+ str(v30)+"\n"
print "max-win1 / max-win2 = "+ str(v31)+"\n"

print "#################################################"








"""LOSS # 23"""
print "Loss # 23"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind231=win231-300
ind232=win231-150
ind233=win231

print "\n index number for loss 23", ind231, ind232, ind233

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd231=[]
owd232=[]
owd233=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind231 and nn<ind232:
		owd231.append(iat[nn])
	elif nn>=ind232 and nn<ind233:
		owd232.append(iat[nn])
	elif nn>=ind233 and nn<ind233+150:
		owd233.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd231"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd231))
""" owd231 avg"""
print 'mean11 = {}'.format(numpy.mean(owd231))
"""owd231 min"""
print 'min11 = {}'.format(min(owd231))
"""owd231 max"""
print 'max11 = {}'.format(max(owd231))
""" owd231 std"""
print 'std11 = {}'.format(numpy.std(owd231))

"""for owd232"""
print "number of packets included = {}".format(len(owd232))
print 'mean12 = {}'.format(numpy.mean(owd232))
print 'min12 = {}'.format(min(owd232))
print 'max12 = {}'.format(max(owd232))
print 'std12 = {}'.format(numpy.std(owd232))

""" for owd233"""
print "number of packets included = {}".format(len(owd233))
print 'mean13 = {}'.format(numpy.mean(owd233))
print 'min13 = {}'.format(min(owd233))
print 'max13 = {}'.format(max(owd233))
print 'std13 = {}'.format(numpy.std(owd233))


""" next take the Window3/Window1""" 
w1 = numpy.mean(owd233)/numpy.mean(owd231)
w2 = numpy.mean(owd233)/numpy.min(owd231)
w3 = numpy.mean(owd233)/numpy.max(owd231)

w4 = numpy.min(owd233)/numpy.mean(owd231)
w5 = numpy.min(owd233)/numpy.min(owd231)
w6 = numpy.min(owd233)/numpy.max(owd231)

w7 = numpy.max(owd233)/numpy.mean(owd231)
w8 = numpy.max(owd233)/numpy.min(owd231)
w9 = numpy.max(owd233)/numpy.max(owd231)

"""next take the Window3/Window2"""
w10 = numpy.mean(owd233)/numpy.mean(owd232)
w11 = numpy.mean(owd233)/numpy.min(owd232)
w12 = numpy.mean(owd233)/numpy.max(owd232)

w13 = numpy.min(owd233)/numpy.mean(owd232)
w14 = numpy.min(owd233)/numpy.min(owd232)
w15 = numpy.min(owd233)/numpy.max(owd232)

w16 = numpy.max(owd233)/numpy.mean(owd232)
w17 = numpy.max(owd233)/numpy.min(owd232)
w18 = numpy.max(owd233)/numpy.max(owd232)

""" min/max window 3"""
w19 = numpy.min(owd233)/numpy.max(owd233)

"""standard dev values"""
w20 = numpy.std(owd233)/numpy.std(owd231)
w21 = numpy.std(owd233)/numpy.std(owd232)
w22 = numpy.std(owd231)/numpy.std(owd232)

"""next window1 / window2"""
w23 = numpy.mean(owd231)/numpy.mean(owd232)
w24 = numpy.mean(owd231)/numpy.min(owd232)
w25 = numpy.mean(owd231)/numpy.max(owd232)

w26 = numpy.min(owd231)/numpy.mean(owd232)
w27 = numpy.min(owd231)/numpy.min(owd232)
w28 = numpy.min(owd231)/numpy.max(owd232)

w29 = numpy.max(owd231)/numpy.mean(owd232)
w30 = numpy.max(owd231)/numpy.min(owd232)
w31 = numpy.max(owd231)/numpy.max(owd232)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(w1)+"\n"
print "avg-win3 / min-win1 = "+ str(w2)+"\n"
print "avg-win3 / max-win1 = "+ str(w3)+"\n"

print "min-win3 / avg-win1 = "+ str(w4)+"\n"
print "min-win3 / min-win1 = "+ str(w5)+"\n"
print "min-win3 / max-win1 = "+ str(w6)+"\n"

print "max-win3 / avg-win1 = "+ str(w7)+"\n"
print "max-win3 / min-win1 = "+ str(w8)+"\n"
print "max-win3 / max-win1 = "+ str(w9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(w10)+"\n"
print "avg-win3 / min-win2 = "+ str(w11)+"\n"
print "avg-win3 / max-win2 = "+ str(w12)+"\n"

print "min-win3 / avg-win2 = "+ str(w13)+"\n"
print "min-win3 / min-win2 = "+ str(w14)+"\n"
print "min-win3 / max-win2 = "+ str(w15)+"\n"

print "max-win3 / avg-win2 = "+ str(w16)+"\n"
print "max-win3 / min-win2 = "+ str(w17)+"\n"
print "max-win3 / max-win2 = "+ str(w18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(w19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(w20)+"\n"
print "std-win3 / std-win2 = "+ str(w21)+"\n"
print "std-win1 / std-win2 = "+ str(w22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(w23)+"\n"
print "avg-win1 / min-win2 = "+ str(w24)+"\n"
print "avg-win1 / max-win2 = "+ str(w25)+"\n"

print "min-win1 / avg-win2 = "+ str(w26)+"\n"
print "min-win1 / min-win2 = "+ str(w27)+"\n"
print "min-win1 / max-win2 = "+ str(w28)+"\n"

print "max-win1 / avg-win2 = "+ str(w29)+"\n"
print "max-win1 / min-win2 = "+ str(w30)+"\n"
print "max-win1 / max-win2 = "+ str(w31)+"\n"

print "#################################################"








"""LOSS # 24"""
print "Loss # 24"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind241=win241-300
ind242=win241-150
ind243=win241

print "\n index number for loss 24 ", ind241, ind242, ind243

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd241=[]
owd242=[]
owd243=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind241 and nn<ind242:
		owd241.append(iat[nn])
	elif nn>=ind242 and nn<ind243:
		owd242.append(iat[nn])
	elif nn>=ind243 and nn<ind243+150:
		owd243.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd241"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd241))
""" owd241 avg"""
print 'mean11 = {}'.format(numpy.mean(owd241))
"""owd241 min"""
print 'min11 = {}'.format(min(owd241))
"""owd241 max"""
print 'max11 = {}'.format(max(owd241))
""" owd241 std"""
print 'std11 = {}'.format(numpy.std(owd241))

"""for owd242"""
print "number of packets included = {}".format(len(owd242))
print 'mean12 = {}'.format(numpy.mean(owd242))
print 'min12 = {}'.format(min(owd242))
print 'max12 = {}'.format(max(owd242))
print 'std12 = {}'.format(numpy.std(owd242))

""" for owd243"""
print "number of packets included = {}".format(len(owd243))
print 'mean13 = {}'.format(numpy.mean(owd243))
print 'min13 = {}'.format(min(owd243))
print 'max13 = {}'.format(max(owd243))
print 'std13 = {}'.format(numpy.std(owd243))


""" next take the Window3/Window1""" 
x1 = numpy.mean(owd243)/numpy.mean(owd241)
x2 = numpy.mean(owd243)/numpy.min(owd241)
x3 = numpy.mean(owd243)/numpy.max(owd241)

x4 = numpy.min(owd243)/numpy.mean(owd241)
x5 = numpy.min(owd243)/numpy.min(owd241)
x6 = numpy.min(owd243)/numpy.max(owd241)

x7 = numpy.max(owd243)/numpy.mean(owd241)
x8 = numpy.max(owd243)/numpy.min(owd241)
x9 = numpy.max(owd243)/numpy.max(owd241)

"""next take the Window3/Window2"""
x10 = numpy.mean(owd243)/numpy.mean(owd242)
x11 = numpy.mean(owd243)/numpy.min(owd242)
x12 = numpy.mean(owd243)/numpy.max(owd242)

x13 = numpy.min(owd243)/numpy.mean(owd242)
x14 = numpy.min(owd243)/numpy.min(owd242)
x15 = numpy.min(owd243)/numpy.max(owd242)

x16 = numpy.max(owd243)/numpy.mean(owd242)
x17 = numpy.max(owd243)/numpy.min(owd242)
x18 = numpy.max(owd243)/numpy.max(owd242)

""" min/max window 3"""
x19 = numpy.min(owd243)/numpy.max(owd243)

"""standard dev values"""
x20 = numpy.std(owd243)/numpy.std(owd241)
x21 = numpy.std(owd243)/numpy.std(owd242)
x22 = numpy.std(owd241)/numpy.std(owd242)

"""next window1 / window2"""
x23 = numpy.mean(owd241)/numpy.mean(owd242)
x24 = numpy.mean(owd241)/numpy.min(owd242)
x25 = numpy.mean(owd241)/numpy.max(owd242)

x26 = numpy.min(owd241)/numpy.mean(owd242)
x27 = numpy.min(owd241)/numpy.min(owd242)
x28 = numpy.min(owd241)/numpy.max(owd242)

x29 = numpy.max(owd241)/numpy.mean(owd242)
x30 = numpy.max(owd241)/numpy.min(owd242)
x31 = numpy.max(owd241)/numpy.max(owd242)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(x1)+"\n"
print "avg-win3 / min-win1 = "+ str(x2)+"\n"
print "avg-win3 / max-win1 = "+ str(x3)+"\n"

print "min-win3 / avg-win1 = "+ str(x4)+"\n"
print "min-win3 / min-win1 = "+ str(x5)+"\n"
print "min-win3 / max-win1 = "+ str(x6)+"\n"

print "max-win3 / avg-win1 = "+ str(x7)+"\n"
print "max-win3 / min-win1 = "+ str(x8)+"\n"
print "max-win3 / max-win1 = "+ str(x9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(x10)+"\n"
print "avg-win3 / min-win2 = "+ str(x11)+"\n"
print "avg-win3 / max-win2 = "+ str(x12)+"\n"

print "min-win3 / avg-win2 = "+ str(x13)+"\n"
print "min-win3 / min-win2 = "+ str(x14)+"\n"
print "min-win3 / max-win2 = "+ str(x15)+"\n"

print "max-win3 / avg-win2 = "+ str(x16)+"\n"
print "max-win3 / min-win2 = "+ str(x17)+"\n"
print "max-win3 / max-win2 = "+ str(x18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(x19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(x20)+"\n"
print "std-win3 / std-win2 = "+ str(x21)+"\n"
print "std-win1 / std-win2 = "+ str(x22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(x23)+"\n"
print "avg-win1 / min-win2 = "+ str(x24)+"\n"
print "avg-win1 / max-win2 = "+ str(x25)+"\n"

print "min-win1 / avg-win2 = "+ str(x26)+"\n"
print "min-win1 / min-win2 = "+ str(x27)+"\n"
print "min-win1 / max-win2 = "+ str(x28)+"\n"

print "max-win1 / avg-win2 = "+ str(x29)+"\n"
print "max-win1 / min-win2 = "+ str(x30)+"\n"
print "max-win1 / max-win2 = "+ str(x31)+"\n"

print "#################################################"








"""LOSS # 25"""
print "Loss # 25"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind251=win251-300
ind252=win251-150
ind253=win251

print "\n index number for loss ", ind251, ind252, ind253

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd251=[]
owd252=[]
owd253=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind251 and nn<ind252:
		owd251.append(iat[nn])
	elif nn>=ind252 and nn<ind253:
		owd252.append(iat[nn])
	elif nn>=ind253 and nn<ind253+150:
		owd253.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd251"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd251))
""" owd251 avg"""
print 'mean11 = {}'.format(numpy.mean(owd251))
"""owd251 min"""
print 'min11 = {}'.format(min(owd251))
"""owd251 max"""
print 'max11 = {}'.format(max(owd251))
""" owd251 std"""
print 'std11 = {}'.format(numpy.std(owd251))

"""for owd252"""
print "number of packets included = {}".format(len(owd252))
print 'mean12 = {}'.format(numpy.mean(owd252))
print 'min12 = {}'.format(min(owd252))
print 'max12 = {}'.format(max(owd252))
print 'std12 = {}'.format(numpy.std(owd252))

""" for owd253"""
print "number of packets included = {}".format(len(owd253))
print 'mean13 = {}'.format(numpy.mean(owd253))
print 'min13 = {}'.format(min(owd253))
print 'max13 = {}'.format(max(owd253))
print 'std13 = {}'.format(numpy.std(owd253))


""" next take the Window3/Window1""" 
y1 = numpy.mean(owd253)/numpy.mean(owd251)
y2 = numpy.mean(owd253)/numpy.min(owd251)
y3 = numpy.mean(owd253)/numpy.max(owd251)

y4 = numpy.min(owd253)/numpy.mean(owd251)
y5 = numpy.min(owd253)/numpy.min(owd251)
y6 = numpy.min(owd253)/numpy.max(owd251)

y7 = numpy.max(owd253)/numpy.mean(owd251)
y8 = numpy.max(owd253)/numpy.min(owd251)
y9 = numpy.max(owd253)/numpy.max(owd251)

"""next take the Window3/Window2"""
y10 = numpy.mean(owd253)/numpy.mean(owd252)
y11 = numpy.mean(owd253)/numpy.min(owd252)
y12 = numpy.mean(owd253)/numpy.max(owd252)

y13 = numpy.min(owd253)/numpy.mean(owd252)
y14 = numpy.min(owd253)/numpy.min(owd252)
y15 = numpy.min(owd253)/numpy.max(owd252)

y16 = numpy.max(owd253)/numpy.mean(owd252)
y17 = numpy.max(owd253)/numpy.min(owd252)
y18 = numpy.max(owd253)/numpy.max(owd252)

""" min/max window 3"""
y19 = numpy.min(owd253)/numpy.max(owd253)

"""standard dev values"""
y20 = numpy.std(owd253)/numpy.std(owd251)
y21 = numpy.std(owd253)/numpy.std(owd252)
y22 = numpy.std(owd251)/numpy.std(owd252)

"""next window1 / window2"""
y23 = numpy.mean(owd251)/numpy.mean(owd252)
y24 = numpy.mean(owd251)/numpy.min(owd252)
y25 = numpy.mean(owd251)/numpy.max(owd252)

y26 = numpy.min(owd251)/numpy.mean(owd252)
y27 = numpy.min(owd251)/numpy.min(owd252)
y28 = numpy.min(owd251)/numpy.max(owd252)

y29 = numpy.max(owd251)/numpy.mean(owd252)
y30 = numpy.max(owd251)/numpy.min(owd252)
y31 = numpy.max(owd251)/numpy.max(owd252)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(y1)+"\n"
print "avg-win3 / min-win1 = "+ str(y2)+"\n"
print "avg-win3 / max-win1 = "+ str(y3)+"\n"

print "min-win3 / avg-win1 = "+ str(y4)+"\n"
print "min-win3 / min-win1 = "+ str(y5)+"\n"
print "min-win3 / max-win1 = "+ str(y6)+"\n"

print "max-win3 / avg-win1 = "+ str(y7)+"\n"
print "max-win3 / min-win1 = "+ str(y8)+"\n"
print "max-win3 / max-win1 = "+ str(y9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(y10)+"\n"
print "avg-win3 / min-win2 = "+ str(y11)+"\n"
print "avg-win3 / max-win2 = "+ str(y12)+"\n"

print "min-win3 / avg-win2 = "+ str(y13)+"\n"
print "min-win3 / min-win2 = "+ str(y14)+"\n"
print "min-win3 / max-win2 = "+ str(y15)+"\n"

print "max-win3 / avg-win2 = "+ str(y16)+"\n"
print "max-win3 / min-win2 = "+ str(y17)+"\n"
print "max-win3 / max-win2 = "+ str(y18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(y19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(y20)+"\n"
print "std-win3 / std-win2 = "+ str(y21)+"\n"
print "std-win1 / std-win2 = "+ str(y22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(y23)+"\n"
print "avg-win1 / min-win2 = "+ str(y24)+"\n"
print "avg-win1 / max-win2 = "+ str(y25)+"\n"

print "min-win1 / avg-win2 = "+ str(y26)+"\n"
print "min-win1 / min-win2 = "+ str(y27)+"\n"
print "min-win1 / max-win2 = "+ str(y28)+"\n"

print "max-win1 / avg-win2 = "+ str(y29)+"\n"
print "max-win1 / min-win2 = "+ str(y30)+"\n"
print "max-win1 / max-win2 = "+ str(y31)+"\n"

print "#################################################"








"""LOSS # 26"""
print "Loss # 26"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind261=win261-300
ind262=win261-150
ind263=win261

print "\n index number for loss 26 ", ind261, ind262, ind263

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd261=[]
owd262=[]
owd263=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind261 and nn<ind262:
		owd261.append(iat[nn])
	elif nn>=ind262 and nn<ind263:
		owd262.append(iat[nn])
	elif nn>=ind263 and nn<ind263+150:
		owd263.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd261"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd261))
""" owd261 avg"""
print 'mean11 = {}'.format(numpy.mean(owd261))
"""owd261 min"""
print 'min11 = {}'.format(min(owd261))
"""owd261 max"""
print 'max11 = {}'.format(max(owd261))
""" owd261 std"""
print 'std11 = {}'.format(numpy.std(owd261))

"""for owd262"""
print "number of packets included = {}".format(len(owd262))
print 'mean12 = {}'.format(numpy.mean(owd262))
print 'min12 = {}'.format(min(owd262))
print 'max12 = {}'.format(max(owd262))
print 'std12 = {}'.format(numpy.std(owd262))

""" for owd263"""
print "number of packets included = {}".format(len(owd263))
print 'mean13 = {}'.format(numpy.mean(owd263))
print 'min13 = {}'.format(min(owd263))
print 'max13 = {}'.format(max(owd263))
print 'std13 = {}'.format(numpy.std(owd263))


""" next take the Window3/Window1""" 
z1 = numpy.mean(owd263)/numpy.mean(owd261)
z2 = numpy.mean(owd263)/numpy.min(owd261)
z3 = numpy.mean(owd263)/numpy.max(owd261)

z4 = numpy.min(owd263)/numpy.mean(owd261)
z5 = numpy.min(owd263)/numpy.min(owd261)
z6 = numpy.min(owd263)/numpy.max(owd261)

z7 = numpy.max(owd263)/numpy.mean(owd261)
z8 = numpy.max(owd263)/numpy.min(owd261)
z9 = numpy.max(owd263)/numpy.max(owd261)

"""next take the Window3/Window2"""
z10 = numpy.mean(owd263)/numpy.mean(owd262)
z11 = numpy.mean(owd263)/numpy.min(owd262)
z12 = numpy.mean(owd263)/numpy.max(owd262)

z13 = numpy.min(owd263)/numpy.mean(owd262)
z14 = numpy.min(owd263)/numpy.min(owd262)
z15 = numpy.min(owd263)/numpy.max(owd262)

z16 = numpy.max(owd263)/numpy.mean(owd262)
z17 = numpy.max(owd263)/numpy.min(owd262)
z18 = numpy.max(owd263)/numpy.max(owd262)

""" min/max window 3"""
z19 = numpy.min(owd263)/numpy.max(owd263)

"""standard dev values"""
z20 = numpy.std(owd263)/numpy.std(owd261)
z21 = numpy.std(owd263)/numpy.std(owd262)
z22 = numpy.std(owd261)/numpy.std(owd262)

"""next window1 / window2"""
z23 = numpy.mean(owd261)/numpy.mean(owd262)
z24 = numpy.mean(owd261)/numpy.min(owd262)
z25 = numpy.mean(owd261)/numpy.max(owd262)

z26 = numpy.min(owd261)/numpy.mean(owd262)
z27 = numpy.min(owd261)/numpy.min(owd262)
z28 = numpy.min(owd261)/numpy.max(owd262)

z29 = numpy.max(owd261)/numpy.mean(owd262)
z30 = numpy.max(owd261)/numpy.min(owd262)
z31 = numpy.max(owd261)/numpy.max(owd262)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(z1)+"\n"
print "avg-win3 / min-win1 = "+ str(z2)+"\n"
print "avg-win3 / max-win1 = "+ str(z3)+"\n"

print "min-win3 / avg-win1 = "+ str(z4)+"\n"
print "min-win3 / min-win1 = "+ str(z5)+"\n"
print "min-win3 / max-win1 = "+ str(z6)+"\n"

print "max-win3 / avg-win1 = "+ str(z7)+"\n"
print "max-win3 / min-win1 = "+ str(z8)+"\n"
print "max-win3 / max-win1 = "+ str(z9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(z10)+"\n"
print "avg-win3 / min-win2 = "+ str(z11)+"\n"
print "avg-win3 / max-win2 = "+ str(z12)+"\n"

print "min-win3 / avg-win2 = "+ str(z13)+"\n"
print "min-win3 / min-win2 = "+ str(z14)+"\n"
print "min-win3 / max-win2 = "+ str(z15)+"\n"

print "max-win3 / avg-win2 = "+ str(z16)+"\n"
print "max-win3 / min-win2 = "+ str(z17)+"\n"
print "max-win3 / max-win2 = "+ str(z18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(z19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(z20)+"\n"
print "std-win3 / std-win2 = "+ str(z21)+"\n"
print "std-win1 / std-win2 = "+ str(z22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(z23)+"\n"
print "avg-win1 / min-win2 = "+ str(z24)+"\n"
print "avg-win1 / max-win2 = "+ str(z25)+"\n"

print "min-win1 / avg-win2 = "+ str(z26)+"\n"
print "min-win1 / min-win2 = "+ str(z27)+"\n"
print "min-win1 / max-win2 = "+ str(z28)+"\n"

print "max-win1 / avg-win2 = "+ str(z29)+"\n"
print "max-win1 / min-win2 = "+ str(z30)+"\n"
print "max-win1 / max-win2 = "+ str(z31)+"\n"

print "#################################################"








"""LOSS # 27"""
print "Loss # 27"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind271=win271-300
ind272=win271-150
ind273=win271

print "\n index number for loss 27 ", ind271, ind272, ind273

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd271=[]
owd272=[]
owd273=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind271 and nn<ind272:
		owd271.append(iat[nn])
	elif nn>=ind272 and nn<ind273:
		owd272.append(iat[nn])
	elif nn>=ind273 and nn<ind273+150:
		owd273.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd271"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd271))
""" owd271 avg"""
print 'mean11 = {}'.format(numpy.mean(owd271))
"""owd271 min"""
print 'min11 = {}'.format(min(owd271))
"""owd271 max"""
print 'max11 = {}'.format(max(owd271))
""" owd271 std"""
print 'std11 = {}'.format(numpy.std(owd271))

"""for owd272"""
print "number of packets included = {}".format(len(owd272))
print 'mean12 = {}'.format(numpy.mean(owd272))
print 'min12 = {}'.format(min(owd272))
print 'max12 = {}'.format(max(owd272))
print 'std12 = {}'.format(numpy.std(owd272))

""" for owd273"""
print "number of packets included = {}".format(len(owd273))
print 'mean13 = {}'.format(numpy.mean(owd273))
print 'min13 = {}'.format(min(owd273))
print 'max13 = {}'.format(max(owd273))
print 'std13 = {}'.format(numpy.std(owd273))


""" next take the Window3/Window1""" 
aa1 = numpy.mean(owd273)/numpy.mean(owd271)
aa2 = numpy.mean(owd273)/numpy.min(owd271)
aa3 = numpy.mean(owd273)/numpy.max(owd271)

aa4 = numpy.min(owd273)/numpy.mean(owd271)
aa5 = numpy.min(owd273)/numpy.min(owd271)
aa6 = numpy.min(owd273)/numpy.max(owd271)

aa7 = numpy.max(owd273)/numpy.mean(owd271)
aa8 = numpy.max(owd273)/numpy.min(owd271)
aa9 = numpy.max(owd273)/numpy.max(owd271)

"""next take the Window3/Window2"""
aa10 = numpy.mean(owd273)/numpy.mean(owd272)
aa11 = numpy.mean(owd273)/numpy.min(owd272)
aa12 = numpy.mean(owd273)/numpy.max(owd272)

aa13 = numpy.min(owd273)/numpy.mean(owd272)
aa14 = numpy.min(owd273)/numpy.min(owd272)
aa15 = numpy.min(owd273)/numpy.max(owd272)

aa16 = numpy.max(owd273)/numpy.mean(owd272)
aa17 = numpy.max(owd273)/numpy.min(owd272)
aa18 = numpy.max(owd273)/numpy.max(owd272)

""" min/max window 3"""
aa19 = numpy.min(owd273)/numpy.max(owd273)

"""standard dev values"""
aa20 = numpy.std(owd273)/numpy.std(owd271)
aa21 = numpy.std(owd273)/numpy.std(owd272)
aa22 = numpy.std(owd271)/numpy.std(owd272)

"""next window1 / window2"""
aa23 = numpy.mean(owd271)/numpy.mean(owd272)
aa24 = numpy.mean(owd271)/numpy.min(owd272)
aa25 = numpy.mean(owd271)/numpy.max(owd272)

aa26 = numpy.min(owd271)/numpy.mean(owd272)
aa27 = numpy.min(owd271)/numpy.min(owd272)
aa28 = numpy.min(owd271)/numpy.max(owd272)

aa29 = numpy.max(owd271)/numpy.mean(owd272)
aa30 = numpy.max(owd271)/numpy.min(owd272)
aa31 = numpy.max(owd271)/numpy.max(owd272)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(aa1)+"\n"
print "avg-win3 / min-win1 = "+ str(aa2)+"\n"
print "avg-win3 / max-win1 = "+ str(aa3)+"\n"

print "min-win3 / avg-win1 = "+ str(aa4)+"\n"
print "min-win3 / min-win1 = "+ str(aa5)+"\n"
print "min-win3 / max-win1 = "+ str(aa6)+"\n"

print "max-win3 / avg-win1 = "+ str(aa7)+"\n"
print "max-win3 / min-win1 = "+ str(aa8)+"\n"
print "max-win3 / max-win1 = "+ str(aa9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(aa10)+"\n"
print "avg-win3 / min-win2 = "+ str(aa11)+"\n"
print "avg-win3 / max-win2 = "+ str(aa12)+"\n"

print "min-win3 / avg-win2 = "+ str(aa13)+"\n"
print "min-win3 / min-win2 = "+ str(aa14)+"\n"
print "min-win3 / max-win2 = "+ str(aa15)+"\n"

print "max-win3 / avg-win2 = "+ str(aa16)+"\n"
print "max-win3 / min-win2 = "+ str(aa17)+"\n"
print "max-win3 / max-win2 = "+ str(aa18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(aa19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(aa20)+"\n"
print "std-win3 / std-win2 = "+ str(aa21)+"\n"
print "std-win1 / std-win2 = "+ str(aa22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(aa23)+"\n"
print "avg-win1 / min-win2 = "+ str(aa24)+"\n"
print "avg-win1 / max-win2 = "+ str(aa25)+"\n"

print "min-win1 / avg-win2 = "+ str(aa26)+"\n"
print "min-win1 / min-win2 = "+ str(aa27)+"\n"
print "min-win1 / max-win2 = "+ str(aa28)+"\n"

print "max-win1 / avg-win2 = "+ str(aa29)+"\n"
print "max-win1 / min-win2 = "+ str(aa30)+"\n"
print "max-win1 / max-win2 = "+ str(aa31)+"\n"

print "#################################################"


"""LOSS # 28"""
print "Loss # 28"

"""SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
ind281=win281-300
ind282=win281-150
ind283=win281

print "\n index number for loss 28", ind281, ind282, ind283

""" CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
owd281=[]
owd282=[]
owd283=[]

"""APPENDING THE DELAYS INTO OWD VARIABLES"""
for nn in range(len(iat)):
	if nn>=ind281 and nn<ind282:
		owd281.append(iat[nn])
	elif nn>=ind282 and nn<ind283:
		owd282.append(iat[nn])
	elif nn>=ind283 and nn<ind283+150:
		owd283.append(iat[nn])
		# print tt[nn], iat[nn]
		

""" TAKE THE AVG, MAX MIN OF EACH WINDOW"""

""" for owd281"""

""" Number of packet in a window"""
print "number of packets included = {}".format(len(owd281))
""" owd281 avg"""
print 'mean11 = {}'.format(numpy.mean(owd281))
"""owd281 min"""
print 'min11 = {}'.format(min(owd281))
"""owd281 max"""
print 'max11 = {}'.format(max(owd281))
""" owd281 std"""
print 'std11 = {}'.format(numpy.std(owd281))

"""for owd282"""
print "number of packets included = {}".format(len(owd282))
print 'mean12 = {}'.format(numpy.mean(owd282))
print 'min12 = {}'.format(min(owd282))
print 'max12 = {}'.format(max(owd282))
print 'std12 = {}'.format(numpy.std(owd282))

""" for owd283"""
print "number of packets included = {}".format(len(owd283))
print 'mean13 = {}'.format(numpy.mean(owd283))
print 'min13 = {}'.format(min(owd283))
print 'max13 = {}'.format(max(owd283))
print 'std13 = {}'.format(numpy.std(owd283))


""" next take the Window3/Window1""" 
ab1 = numpy.mean(owd283)/numpy.mean(owd281)
ab2 = numpy.mean(owd283)/numpy.min(owd281)
ab3 = numpy.mean(owd283)/numpy.max(owd281)

ab4 = numpy.min(owd283)/numpy.mean(owd281)
ab5 = numpy.min(owd283)/numpy.min(owd281)
ab6 = numpy.min(owd283)/numpy.max(owd281)

ab7 = numpy.max(owd283)/numpy.mean(owd281)
ab8 = numpy.max(owd283)/numpy.min(owd281)
ab9 = numpy.max(owd283)/numpy.max(owd281)

"""next take the Window3/Window2"""
ab10 = numpy.mean(owd283)/numpy.mean(owd282)
ab11 = numpy.mean(owd283)/numpy.min(owd282)
ab12 = numpy.mean(owd283)/numpy.max(owd282)

ab13 = numpy.min(owd283)/numpy.mean(owd282)
ab14 = numpy.min(owd283)/numpy.min(owd282)
ab15 = numpy.min(owd283)/numpy.max(owd282)

ab16 = numpy.max(owd283)/numpy.mean(owd282)
ab17 = numpy.max(owd283)/numpy.min(owd282)
ab18 = numpy.max(owd283)/numpy.max(owd282)

""" min/max window 3"""
ab19 = numpy.min(owd283)/numpy.max(owd283)

"""standard dev values"""
ab20 = numpy.std(owd283)/numpy.std(owd281)
ab21 = numpy.std(owd283)/numpy.std(owd282)
ab22 = numpy.std(owd281)/numpy.std(owd282)

"""next window1 / window2"""
ab23 = numpy.mean(owd281)/numpy.mean(owd282)
ab24 = numpy.mean(owd281)/numpy.min(owd282)
ab25 = numpy.mean(owd281)/numpy.max(owd282)

ab26 = numpy.min(owd281)/numpy.mean(owd282)
ab27 = numpy.min(owd281)/numpy.min(owd282)
ab28 = numpy.min(owd281)/numpy.max(owd282)

ab29 = numpy.max(owd281)/numpy.mean(owd282)
ab30 = numpy.max(owd281)/numpy.min(owd282)
ab31 = numpy.max(owd281)/numpy.max(owd282)

"""PRINTING THE VALUES Window3/Window1"""
"""Win3 / Win 1"""
print "avg-win3 / avg-win1 = "+ str(ab1)+"\n"
print "avg-win3 / min-win1 = "+ str(ab2)+"\n"
print "avg-win3 / max-win1 = "+ str(ab3)+"\n"

print "min-win3 / avg-win1 = "+ str(ab4)+"\n"
print "min-win3 / min-win1 = "+ str(ab5)+"\n"
print "min-win3 / max-win1 = "+ str(ab6)+"\n"

print "max-win3 / avg-win1 = "+ str(ab7)+"\n"
print "max-win3 / min-win1 = "+ str(ab8)+"\n"
print "max-win3 / max-win1 = "+ str(ab9)+"\n"


"""Window3/Window2"""
print "avg-win3 / avg-win2 = "+ str(ab10)+"\n"
print "avg-win3 / min-win2 = "+ str(ab11)+"\n"
print "avg-win3 / max-win2 = "+ str(ab12)+"\n"

print "min-win3 / avg-win2 = "+ str(ab13)+"\n"
print "min-win3 / min-win2 = "+ str(ab14)+"\n"
print "min-win3 / max-win2 = "+ str(ab15)+"\n"

print "max-win3 / avg-win2 = "+ str(ab16)+"\n"
print "max-win3 / min-win2 = "+ str(ab17)+"\n"
print "max-win3 / max-win2 = "+ str(ab18)+"\n"

""" min/max of window3"""
print "min-win3 / max-win3 = "+ str(ab19)+"\n"

""" Standar dev values"""
print "std-win3 / std-win1 = "+ str(ab20)+"\n"
print "std-win3 / std-win2 = "+ str(ab21)+"\n"
print "std-win1 / std-win2 = "+ str(ab22)+"\n"

""" window1 / window2"""
print "avg-win1 / avg-win2 = "+ str(ab23)+"\n"
print "avg-win1 / min-win2 = "+ str(ab24)+"\n"
print "avg-win1 / max-win2 = "+ str(ab25)+"\n"

print "min-win1 / avg-win2 = "+ str(ab26)+"\n"
print "min-win1 / min-win2 = "+ str(ab27)+"\n"
print "min-win1 / max-win2 = "+ str(ab28)+"\n"

print "max-win1 / avg-win2 = "+ str(ab29)+"\n"
print "max-win1 / min-win2 = "+ str(ab30)+"\n"
print "max-win1 / max-win2 = "+ str(ab31)+"\n"

print "#################################################"





# # # ""LOSS # 2"""
# # # print "Loss # 2"

# # # """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# # # ind21=win_index[1]-300
# # # ind22=win_index[1]-150
# # # ind23=win_index[1]

# # # print "\n index number for loss ", ind21, ind22, ind23

# # # """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# # # owd21=[]
# # # owd22=[]
# # # owd23=[]

# # # """APPENDING THE DELAYS INTO OWD VARIABLES"""
# # # for nn in range(len(iat)):
# # # 	if nn>=ind21 and nn<ind22:
# # # 		owd21.append(iat[nn])
# # # 	elif nn>=ind22 and nn<ind23:
# # # 		owd22.append(iat[nn])
# # # 	elif nn>=ind23 and nn<ind23+150:
# # # 		owd23.append(iat[nn])
# # # 		# print tt[nn], iat[nn]
		

# # # """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# # # """ for owd21"""

# # # """ Number of packet in a window"""
# # # print "number of packets included = {}".format(len(owd21))
# # # """ owd21 avg"""
# # # print 'mean11 = {}'.format(numpy.mean(owd21))
# # # """owd21 min"""
# # # print 'min11 = {}'.format(min(owd21))
# # # """owd21 max"""
# # # print 'max11 = {}'.format(max(owd21))
# # # """ owd21 std"""
# # # print 'std11 = {}'.format(numpy.std(owd21))

# # # """for owd22"""
# # # print "number of packets included = {}".format(len(owd22))
# # # print 'mean12 = {}'.format(numpy.mean(owd22))
# # # print 'min12 = {}'.format(min(owd22))
# # # print 'max12 = {}'.format(max(owd22))
# # # print 'std12 = {}'.format(numpy.std(owd22))

# # # """ for owd23"""
# # # print "number of packets included = {}".format(len(owd23))
# # # print 'mean13 = {}'.format(numpy.mean(owd23))
# # # print 'min13 = {}'.format(min(owd23))
# # # print 'max13 = {}'.format(max(owd23))
# # # print 'std13 = {}'.format(numpy.std(owd23))


# # # """ next take the Window3/Window1""" 
# # # b1 = numpy.mean(owd23)/numpy.mean(owd21)
# # # b2 = numpy.mean(owd23)/numpy.min(owd21)
# # # b3 = numpy.mean(owd23)/numpy.max(owd21)

# # # b4 = numpy.min(owd23)/numpy.mean(owd21)
# # # b5 = numpy.min(owd23)/numpy.min(owd21)
# # # b6 = numpy.min(owd23)/numpy.max(owd21)

# # # b7 = numpy.max(owd23)/numpy.mean(owd21)
# # # b8 = numpy.max(owd23)/numpy.min(owd21)
# # # b9 = numpy.max(owd23)/numpy.max(owd21)

# # # """next take the Window3/Window2"""
# # # b10 = numpy.mean(owd23)/numpy.mean(owd22)
# # # b11 = numpy.mean(owd23)/numpy.min(owd22)
# # # b12 = numpy.mean(owd23)/numpy.max(owd22)

# # # b13 = numpy.min(owd23)/numpy.mean(owd22)
# # # b14 = numpy.min(owd23)/numpy.min(owd22)
# # # b15 = numpy.min(owd23)/numpy.max(owd22)

# # # b16 = numpy.max(owd23)/numpy.mean(owd22)
# # # b17 = numpy.max(owd23)/numpy.min(owd22)
# # # b18 = numpy.max(owd23)/numpy.max(owd22)

# # # """ min/max window 3"""
# # # b19 = numpy.min(owd23)/numpy.max(owd23)

# # # """standard dev values"""
# # # b20 = numpy.std(owd23)/numpy.std(owd21)
# # # b21 = numpy.std(owd23)/numpy.std(owd22)
# # # b22 = numpy.std(owd21)/numpy.std(owd22)

# # # """next window1 / window2"""
# # # b23 = numpy.mean(owd21)/numpy.mean(owd22)
# # # b24 = numpy.mean(owd21)/numpy.min(owd22)
# # # b25 = numpy.mean(owd21)/numpy.max(owd22)

# # # b26 = numpy.min(owd21)/numpy.mean(owd22)
# # # b27 = numpy.min(owd21)/numpy.min(owd22)
# # # b28 = numpy.min(owd21)/numpy.max(owd22)

# # # b29 = numpy.max(owd21)/numpy.mean(owd22)
# # # b30 = numpy.max(owd21)/numpy.min(owd22)
# # # b31 = numpy.max(owd21)/numpy.max(owd22)

# # # """PRINTING THE VALUES Window3/Window1"""
# # # """Win3 / Win 1"""
# # # print "avg-win3 / avg-win1 = "+ str(b1)+"\n"
# # # print "avg-win3 / min-win1 = "+ str(b2)+"\n"
# # # print "avg-win3 / max-win1 = "+ str(b3)+"\n"

# # # print "min-win3 / avg-win1 = "+ str(b4)+"\n"
# # # print "min-win3 / min-win1 = "+ str(b5)+"\n"
# # # print "min-win3 / max-win1 = "+ str(b6)+"\n"

# # # print "max-win3 / avg-win1 = "+ str(b7)+"\n"
# # # print "max-win3 / min-win1 = "+ str(b8)+"\n"
# # # print "max-win3 / max-win1 = "+ str(b9)+"\n"


# # # """Window3/Window2"""
# # # print "avg-win3 / avg-win2 = "+ str(b10)+"\n"
# # # print "avg-win3 / min-win2 = "+ str(b11)+"\n"
# # # print "avg-win3 / max-win2 = "+ str(b12)+"\n"

# # # print "min-win3 / avg-win2 = "+ str(b13)+"\n"
# # # print "min-win3 / min-win2 = "+ str(b14)+"\n"
# # # print "min-win3 / max-win2 = "+ str(b15)+"\n"

# # # print "max-win3 / avg-win2 = "+ str(b16)+"\n"
# # # print "max-win3 / min-win2 = "+ str(b17)+"\n"
# # # print "max-win3 / max-win2 = "+ str(b18)+"\n"

# # # """ min/max of window3"""
# # # print "min-win3 / max-win3 = "+ str(b19)+"\n"

# # # """ Standar dev values"""
# # # print "std-win3 / std-win1 = "+ str(b20)+"\n"
# # # print "std-win3 / std-win2 = "+ str(b21)+"\n"
# # # print "std-win1 / std-win2 = "+ str(b22)+"\n"

# # # """ window1 / window2"""
# # # print "avg-win1 / avg-win2 = "+ str(b23)+"\n"
# # # print "avg-win1 / min-win2 = "+ str(b24)+"\n"
# # # print "avg-win1 / max-win2 = "+ str(b25)+"\n"

# # # print "min-win1 / avg-win2 = "+ str(b26)+"\n"
# # # print "min-win1 / min-win2 = "+ str(b27)+"\n"
# # # print "min-win1 / max-win2 = "+ str(b28)+"\n"

# # # print "max-win1 / avg-win2 = "+ str(b29)+"\n"
# # # print "max-win1 / min-win2 = "+ str(b30)+"\n"
# # # print "max-win1 / max-win2 = "+ str(b31)+"\n"

# # # print "#################################################"

# #########################################################################################

"""Saving the results to a File name owd-results"""

open("iat-noloss-results","w").close()
with open("iat-noloss-results","w") as f:
	f.write(str(a1)+","+str(a2)+","+str(a3)+","+str(a4)+","+str(a5)+","+str(a6)+","+str(a7)+","+str(a8)+","+
		str(a9)+","+str(a10)+","+str(a11)+","+str(a12)+","+str(a13)+","+str(a14)+","+str(a15)+","+str(a16)+","+
		str(a17)+","+str(a18)+","+str(a19)+","+str(a20)+","+str(a21)+","+str(a22)+","+str(a23)+","+str(a24)+","+
		str(a25)+","+str(a26)+","+str(a27)+","+str(a28)+","+str(a29)+","+str(a30)+","+str(a31)+","+"n"+"\n"
		+str(b1)+","+str(b2)+","+str(b3)+","+str(b4)+","+str(b5)+","+str(b6)+","+str(b7)+","+str(b8)+","+
		str(b9)+","+str(b10)+","+str(b11)+","+str(b12)+","+str(b13)+","+str(b14)+","+str(b15)+","+str(b16)+","+
		str(b17)+","+str(b18)+","+str(b19)+","+str(b20)+","+str(b21)+","+str(b22)+","+str(b23)+","+str(b24)+","+
		str(b25)+","+str(b26)+","+str(b27)+","+str(b28)+","+str(b29)+","+str(b30)+","+str(b31)+","+"n""\n"
		+str(c1)+","+str(c2)+","+str(c3)+","+str(c4)+","+str(c5)+","+str(c6)+","+str(c7)+","+str(c8)+","+
		str(c9)+","+str(c10)+","+str(c11)+","+str(c12)+","+str(c13)+","+str(c14)+","+str(c15)+","+str(c16)+","+
		str(c17)+","+str(c18)+","+str(c19)+","+str(c20)+","+str(c21)+","+str(c22)+","+str(c23)+","+str(c24)+","+
		str(c25)+","+str(c26)+","+str(c27)+","+str(c28)+","+str(c29)+","+str(c30)+","+str(c31)+","+"n""\n"
		+str(d1)+","+str(d2)+","+str(d3)+","+str(d4)+","+str(d5)+","+str(d6)+","+str(d7)+","+str(d8)+","+
		str(d9)+","+str(d10)+","+str(d11)+","+str(d12)+","+str(d13)+","+str(d14)+","+str(d15)+","+str(d16)+","+
		str(d17)+","+str(d18)+","+str(d19)+","+str(d20)+","+str(d21)+","+str(d22)+","+str(d23)+","+str(d24)+","+
		str(d25)+","+str(d26)+","+str(d27)+","+str(d28)+","+str(d29)+","+str(d30)+","+str(d31)+","+"n""\n"
		+str(e1)+","+str(e2)+","+str(e3)+","+str(e4)+","+str(e5)+","+str(e6)+","+str(e7)+","+str(e8)+","+
		str(e9)+","+str(e10)+","+str(e11)+","+str(e12)+","+str(e13)+","+str(e14)+","+str(e15)+","+str(e16)+","+
		str(e17)+","+str(e18)+","+str(e19)+","+str(e20)+","+str(e21)+","+str(e22)+","+str(e23)+","+str(e24)+","+
		str(e25)+","+str(e26)+","+str(e27)+","+str(e28)+","+str(e29)+","+str(e30)+","+str(e31)+","+"n""\n"
		+str(f1)+","+str(f2)+","+str(f3)+","+str(f4)+","+str(f5)+","+str(f6)+","+str(f7)+","+str(f8)+","+
		str(f9)+","+str(f10)+","+str(f11)+","+str(f12)+","+str(f13)+","+str(f14)+","+str(f15)+","+str(f16)+","+
		str(f17)+","+str(f18)+","+str(f19)+","+str(f20)+","+str(f21)+","+str(f22)+","+str(f23)+","+str(f24)+","+
		str(f25)+","+str(f26)+","+str(f27)+","+str(f28)+","+str(f29)+","+str(f30)+","+str(f31)+","+"n""\n"
		+str(g1)+","+str(g2)+","+str(g3)+","+str(g4)+","+str(g5)+","+str(g6)+","+str(g7)+","+str(g8)+","+
		str(g9)+","+str(g10)+","+str(g11)+","+str(g12)+","+str(g13)+","+str(g14)+","+str(g15)+","+str(g16)+","+
		str(g17)+","+str(g18)+","+str(g19)+","+str(g20)+","+str(g21)+","+str(g22)+","+str(g23)+","+str(g24)+","+
		str(g25)+","+str(g26)+","+str(g27)+","+str(g28)+","+str(g29)+","+str(g30)+","+str(g31)+","+"n""\n"
		+str(h1)+","+str(h2)+","+str(h3)+","+str(h4)+","+str(h5)+","+str(h6)+","+str(h7)+","+str(h8)+","+
		str(h9)+","+str(h10)+","+str(h11)+","+str(h12)+","+str(h13)+","+str(h14)+","+str(h15)+","+str(h16)+","+
		str(h17)+","+str(h18)+","+str(h19)+","+str(h20)+","+str(h21)+","+str(h22)+","+str(h23)+","+str(h24)+","+
		str(h25)+","+str(h26)+","+str(h27)+","+str(h28)+","+str(h29)+","+str(h30)+","+str(h31)+","+"n""\n"
		+str(i1)+","+str(i2)+","+str(i3)+","+str(i4)+","+str(i5)+","+str(i6)+","+str(i7)+","+str(i8)+","+
		str(i9)+","+str(i10)+","+str(i11)+","+str(i12)+","+str(i13)+","+str(i14)+","+str(i15)+","+str(i16)+","+
		str(i17)+","+str(i18)+","+str(i19)+","+str(i20)+","+str(i21)+","+str(i22)+","+str(i23)+","+str(i24)+","+
		str(i25)+","+str(i26)+","+str(i27)+","+str(i28)+","+str(i29)+","+str(i30)+","+str(i31)+","+"n""\n"
		+str(j1)+","+str(j2)+","+str(j3)+","+str(j4)+","+str(j5)+","+str(j6)+","+str(j7)+","+str(j8)+","+
		str(j9)+","+str(j10)+","+str(j11)+","+str(j12)+","+str(j13)+","+str(j14)+","+str(j15)+","+str(j16)+","+
		str(j17)+","+str(j18)+","+str(j19)+","+str(j20)+","+str(j21)+","+str(j22)+","+str(j23)+","+str(j24)+","+
		str(j25)+","+str(j26)+","+str(j27)+","+str(j28)+","+str(j29)+","+str(j30)+","+str(j31)+","+"n""\n"
		+str(k1)+","+str(k2)+","+str(k3)+","+str(k4)+","+str(k5)+","+str(k6)+","+str(k7)+","+str(k8)+","+
		str(k9)+","+str(k10)+","+str(k11)+","+str(k12)+","+str(k13)+","+str(k14)+","+str(k15)+","+str(k16)+","+
		str(k17)+","+str(k18)+","+str(k19)+","+str(k20)+","+str(k21)+","+str(k22)+","+str(k23)+","+str(k24)+","+
		str(k25)+","+str(k26)+","+str(k27)+","+str(k28)+","+str(k29)+","+str(k30)+","+str(k31)+","+"n""\n"
		+str(l1)+","+str(l2)+","+str(l3)+","+str(l4)+","+str(l5)+","+str(l6)+","+str(l7)+","+str(l8)+","+
		str(l9)+","+str(l10)+","+str(l11)+","+str(l12)+","+str(l13)+","+str(l14)+","+str(l15)+","+str(l16)+","+
		str(l17)+","+str(l18)+","+str(l19)+","+str(l20)+","+str(l21)+","+str(l22)+","+str(l23)+","+str(l24)+","+
		str(l25)+","+str(l26)+","+str(l27)+","+str(l28)+","+str(l29)+","+str(l30)+","+str(l31)+","+"n""\n"
		+str(m1)+","+str(m2)+","+str(m3)+","+str(m4)+","+str(m5)+","+str(m6)+","+str(m7)+","+str(m8)+","+
		str(m9)+","+str(m10)+","+str(m11)+","+str(m12)+","+str(m13)+","+str(m14)+","+str(m15)+","+str(m16)+","+
		str(m17)+","+str(m18)+","+str(m19)+","+str(m20)+","+str(m21)+","+str(m22)+","+str(m23)+","+str(m24)+","+
		str(m25)+","+str(m26)+","+str(m27)+","+str(m28)+","+str(m29)+","+str(m30)+","+str(m31)+","+"n""\n"
		+str(n1)+","+str(n2)+","+str(n3)+","+str(n4)+","+str(n5)+","+str(n6)+","+str(n7)+","+str(n8)+","+
		str(n9)+","+str(n10)+","+str(n11)+","+str(n12)+","+str(n13)+","+str(n14)+","+str(n15)+","+str(n16)+","+
		str(n17)+","+str(n18)+","+str(n19)+","+str(n20)+","+str(n21)+","+str(n22)+","+str(n23)+","+str(n24)+","+
		str(n25)+","+str(n26)+","+str(n27)+","+str(n28)+","+str(n29)+","+str(n30)+","+str(n31)+","+"n""\n"
		+str(o1)+","+str(o2)+","+str(o3)+","+str(o4)+","+str(o5)+","+str(o6)+","+str(o7)+","+str(o8)+","+
		str(o9)+","+str(o10)+","+str(o11)+","+str(o12)+","+str(o13)+","+str(o14)+","+str(o15)+","+str(o16)+","+
		str(o17)+","+str(o18)+","+str(o19)+","+str(o20)+","+str(o21)+","+str(o22)+","+str(o23)+","+str(o24)+","+
		str(o25)+","+str(o26)+","+str(o27)+","+str(o28)+","+str(o29)+","+str(o30)+","+str(o31)+","+"n""\n"
		+str(p1)+","+str(p2)+","+str(p3)+","+str(p4)+","+str(p5)+","+str(p6)+","+str(p7)+","+str(p8)+","+
		str(p9)+","+str(p10)+","+str(p11)+","+str(p12)+","+str(p13)+","+str(p14)+","+str(p15)+","+str(p16)+","+
		str(p17)+","+str(p18)+","+str(p19)+","+str(p20)+","+str(p21)+","+str(p22)+","+str(p23)+","+str(p24)+","+
		str(p25)+","+str(p26)+","+str(p27)+","+str(p28)+","+str(p29)+","+str(p30)+","+str(p31)+","+"n""\n"
		+str(q1)+","+str(q2)+","+str(q3)+","+str(q4)+","+str(q5)+","+str(q6)+","+str(q7)+","+str(q8)+","+
		str(q9)+","+str(q10)+","+str(q11)+","+str(q12)+","+str(q13)+","+str(q14)+","+str(q15)+","+str(q16)+","+
		str(q17)+","+str(q18)+","+str(q19)+","+str(q20)+","+str(q21)+","+str(q22)+","+str(q23)+","+str(q24)+","+
		str(q25)+","+str(q26)+","+str(q27)+","+str(q28)+","+str(q29)+","+str(q30)+","+str(q31)+","+"n""\n"
		+str(r1)+","+str(r2)+","+str(r3)+","+str(r4)+","+str(r5)+","+str(r6)+","+str(r7)+","+str(r8)+","+
		str(r9)+","+str(r10)+","+str(r11)+","+str(r12)+","+str(r13)+","+str(r14)+","+str(r15)+","+str(r16)+","+
		str(r17)+","+str(r18)+","+str(r19)+","+str(r20)+","+str(r21)+","+str(r22)+","+str(r23)+","+str(r24)+","+
		str(r25)+","+str(r26)+","+str(r27)+","+str(r28)+","+str(r29)+","+str(r30)+","+str(r31)+","+"n""\n"
		+str(s1)+","+str(s2)+","+str(s3)+","+str(s4)+","+str(s5)+","+str(s6)+","+str(s7)+","+str(s8)+","+
		str(s9)+","+str(s10)+","+str(s11)+","+str(s12)+","+str(s13)+","+str(s14)+","+str(s15)+","+str(s16)+","+
		str(s17)+","+str(s18)+","+str(s19)+","+str(s20)+","+str(s21)+","+str(s22)+","+str(s23)+","+str(s24)+","+
		str(s25)+","+str(s26)+","+str(s27)+","+str(s28)+","+str(s29)+","+str(s30)+","+str(s31)+","+"n""\n"
		+str(t1)+","+str(t2)+","+str(t3)+","+str(t4)+","+str(t5)+","+str(t6)+","+str(t7)+","+str(t8)+","+
		str(t9)+","+str(t10)+","+str(t11)+","+str(t12)+","+str(t13)+","+str(t14)+","+str(t15)+","+str(t16)+","+
		str(t17)+","+str(t18)+","+str(t19)+","+str(t20)+","+str(t21)+","+str(t22)+","+str(t23)+","+str(t24)+","+
		str(t25)+","+str(t26)+","+str(t27)+","+str(t28)+","+str(t29)+","+str(t30)+","+str(t31)+","+"n""\n"
		+str(u1)+","+str(u2)+","+str(u3)+","+str(u4)+","+str(u5)+","+str(u6)+","+str(u7)+","+str(u8)+","+
		str(u9)+","+str(u10)+","+str(u11)+","+str(u12)+","+str(u13)+","+str(u14)+","+str(u15)+","+str(u16)+","+
		str(u17)+","+str(u18)+","+str(u19)+","+str(u20)+","+str(u21)+","+str(u22)+","+str(u23)+","+str(u24)+","+
		str(u25)+","+str(u26)+","+str(u27)+","+str(u28)+","+str(u29)+","+str(u30)+","+str(u31)+","+"n""\n"
		+str(v1)+","+str(v2)+","+str(v3)+","+str(v4)+","+str(v5)+","+str(v6)+","+str(v7)+","+str(v8)+","+
		str(v9)+","+str(v10)+","+str(v11)+","+str(v12)+","+str(v13)+","+str(v14)+","+str(v15)+","+str(v16)+","+
		str(v17)+","+str(v18)+","+str(v19)+","+str(v20)+","+str(v21)+","+str(v22)+","+str(v23)+","+str(v24)+","+
		str(v25)+","+str(v26)+","+str(v27)+","+str(v28)+","+str(v29)+","+str(v30)+","+str(v31)+","+"n""\n"
		+str(w1)+","+str(w2)+","+str(w3)+","+str(w4)+","+str(w5)+","+str(w6)+","+str(w7)+","+str(w8)+","+
		str(w9)+","+str(w10)+","+str(w11)+","+str(w12)+","+str(w13)+","+str(w14)+","+str(w15)+","+str(w16)+","+
		str(w17)+","+str(w18)+","+str(w19)+","+str(w20)+","+str(w21)+","+str(w22)+","+str(w23)+","+str(w24)+","+
		str(w25)+","+str(w26)+","+str(w27)+","+str(w28)+","+str(w29)+","+str(w30)+","+str(w31)+","+"n""\n"
		+str(x1)+","+str(x2)+","+str(x3)+","+str(x4)+","+str(x5)+","+str(x6)+","+str(x7)+","+str(x8)+","+
		str(x9)+","+str(x10)+","+str(x11)+","+str(x12)+","+str(x13)+","+str(x14)+","+str(x15)+","+str(x16)+","+
		str(x17)+","+str(x18)+","+str(x19)+","+str(x20)+","+str(x21)+","+str(x22)+","+str(x23)+","+str(x24)+","+
		str(x25)+","+str(x26)+","+str(x27)+","+str(x28)+","+str(x29)+","+str(x30)+","+str(x31)+","+"n""\n"
		+str(y1)+","+str(y2)+","+str(y3)+","+str(y4)+","+str(y5)+","+str(y6)+","+str(y7)+","+str(y8)+","+
		str(y9)+","+str(y10)+","+str(y11)+","+str(y12)+","+str(y13)+","+str(y14)+","+str(y15)+","+str(y16)+","+
		str(y17)+","+str(y18)+","+str(y19)+","+str(y20)+","+str(y21)+","+str(y22)+","+str(y23)+","+str(y24)+","+
		str(y25)+","+str(y26)+","+str(y27)+","+str(y28)+","+str(y29)+","+str(y30)+","+str(y31)+","+"n""\n"
		+str(z1)+","+str(z2)+","+str(z3)+","+str(z4)+","+str(z5)+","+str(z6)+","+str(z7)+","+str(z8)+","+
		str(z9)+","+str(z10)+","+str(z11)+","+str(z12)+","+str(z13)+","+str(z14)+","+str(z15)+","+str(z16)+","+
		str(z17)+","+str(z18)+","+str(z19)+","+str(z20)+","+str(z21)+","+str(z22)+","+str(z23)+","+str(z24)+","+
		str(z25)+","+str(z26)+","+str(z27)+","+str(z28)+","+str(z29)+","+str(z30)+","+str(z31)+","+"n""\n"
		+str(aa1)+","+str(aa2)+","+str(aa3)+","+str(aa4)+","+str(aa5)+","+str(aa6)+","+str(aa7)+","+str(aa8)+","+
		str(aa9)+","+str(aa10)+","+str(aa11)+","+str(aa12)+","+str(aa13)+","+str(aa14)+","+str(aa15)+","+str(aa16)+","+
		str(aa17)+","+str(aa18)+","+str(aa19)+","+str(aa20)+","+str(aa21)+","+str(aa22)+","+str(aa23)+","+str(aa24)+","+
		str(aa25)+","+str(aa26)+","+str(aa27)+","+str(aa28)+","+str(aa29)+","+str(aa30)+","+str(aa31)+","+"n""\n"
		+str(ab1)+","+str(ab2)+","+str(ab3)+","+str(ab4)+","+str(ab5)+","+str(ab6)+","+str(ab7)+","+str(ab8)+","+
		str(ab9)+","+str(ab10)+","+str(ab11)+","+str(ab12)+","+str(ab13)+","+str(ab14)+","+str(ab15)+","+str(ab16)+","+
		str(ab17)+","+str(ab18)+","+str(ab19)+","+str(ab20)+","+str(ab21)+","+str(ab22)+","+str(ab23)+","+str(ab24)+","+
		str(ab25)+","+str(ab26)+","+str(ab27)+","+str(ab28)+","+str(ab29)+","+str(ab30)+","+str(ab31)+","+"n""\n")



# ########################################################################################

"""Removing the 'NAN' & 'INF' words from the file"""

replacements = {'inf':'0','nan':'0'}

lines = []
with open('iat-noloss-results') as infile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        lines.append(line)
print lines
with open('iat-noloss-results', 'w') as outfile:
    for line in lines:
        outfile.write(line)

 # ########################################################################################
 

# # """ Plotting the Peaks on original delay curve"""
# # # plt.plot(x, delay,'ko')


# time1=np.array(t[win_index]).tolist()
# data1=np.array(delay[win_index]).tolist()
# # # print time1, data1
# # marker_list=zip(time1,data1)
# # plt.plot(t,delay,color='black')
# for i in range(len(data1)):
# 	plt.plot(time1[i], data1[i],'go', markersize=10)
# plt.plot(time1[0],data1[0],'go', markersize=10,label='Selected 28 Loss Peaks')
# plt.legend()
# plt.title("Two Flows, Queue=50, BW=10Mbps, RTT=40ms")
# plt.xlabel('Time (sec)')
# plt.ylabel('One-way Delay (msec)')
# pplot(t, delay, indexes)
# pyplot.show()
# ########################################################################################

# """ Plotting the Peaks on original delay curve"""


# pplot(t, delay, indexes)
# # pplot(t, delay, nolosswin) #enabel if required

# # plt.plot(t,delay, color='black')

# """Take the location and value for each point"""
# d1=d[win11]
# t1=t[win11]
# # print t1, d1, win11
# d2=d[win21]
# t2=t[win21]
# d3=d[win31]
# t3=t[win31]
# d4=d[win41]
# t4=t[win41]
# d5=d[win51]
# t5=t[win51]
# d6=d[win61]
# t6=t[win61]
# d7=d[win71]
# t7=t[win71]
# d8=d[win81]
# t8=t[win81]
# d9=d[win91]
# t9=t[win91]
# d10=d[win101]
# t10=t[win101]
# d11=d[win111]
# t11=t[win111]

# d12=d[win121]
# t12=t[win121]
# d13=d[win131]
# t13=t[win131]
# d14=d[win141]
# t14=t[win141]
# d15=d[win151]
# t15=t[win151]
# d16=d[win161]
# t16=t[win161]
# d17=d[win171]
# t17=t[win171]
# d18=d[win181]
# t18=t[win181]
# d19=d[win191]
# t19=t[win191]
# d20=d[win201]
# t20=t[win201]
# d21=d[win211]
# t21=t[win211]
# d22=d[win221]
# t22=t[win221]
# d23=d[win231]
# t23=t[win231]
# d24=d[win241]
# t24=t[win241]
# d25=d[win251]
# t25=t[win251]
# d26=d[win261]
# t26=t[win261]
# d27=d[win271]
# t27=t[win271]
# d28=d[win281]
# t28=t[win281]

# plt.plot(t1,d1,'ro', markersize=10)
# plt.plot(t2,d2,'ro', markersize=10)
# plt.plot(t3,d3,'ro', markersize=10)
# plt.plot(t4,d4,'ro', markersize=10)
# plt.plot(t5,d5,'ro', markersize=10)
# plt.plot(t6,d6,'ro', markersize=10)
# plt.plot(t7,d7,'ro', markersize=10)
# plt.plot(t8,d8,'ro', markersize=10)
# plt.plot(t9,d9,'ro', markersize=10)
# plt.plot(t10,d10,'ro', markersize=10)

# plt.plot(t11,d11,'ro', markersize=10)
# plt.plot(t12,d12,'ro', markersize=10)
# plt.plot(t13,d13,'ro', markersize=10)
# plt.plot(t14,d14,'ro', markersize=10)
# plt.plot(t15,d15,'ro', markersize=10)
# plt.plot(t16,d16,'ro', markersize=10)
# plt.plot(t17,d17,'ro', markersize=10)
# plt.plot(t18,d18,'ro', markersize=10)
# plt.plot(t19,d19,'ro', markersize=10)
# plt.plot(t20,d20,'ro', markersize=10)
# plt.plot(t20,d20,'ro', markersize=10)
# plt.plot(t21,d21,'ro', markersize=10)
# plt.plot(t22,d22,'ro', markersize=10)
# plt.plot(t23,d23,'ro', markersize=10)
# plt.plot(t24,d24,'ro', markersize=10)
# plt.plot(t25,d25,'ro', markersize=10)
# plt.plot(t26,d26,'ro', markersize=10)
# plt.plot(t27,d27,'ro', markersize=10)

# plt.plot(t28,d28,'ro', markersize=10, label='No-loss window points')

# plt.title("Two Flows, Queue=50, BW=10Mbps, RTT=40ms")
# plt.xlabel("Time (sec)")
# plt.ylabel("One-way Delay (msec)")
# plt.legend()
# pyplot.show()
