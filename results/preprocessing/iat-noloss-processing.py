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

indexes = peakutils.indexes(delay, thres=0.91, min_dist=1000)
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
	if values[i]>=0.12 and diff[i]>=800:
		# print indexes[i+1]
		win_index.append(indexes[i+1])

"""LIST OF SELECTED PEAK INDEXES"""

print "\n selected number of peaks", len(win_index)
print "\n selected Window Peaks at (indexes): \n",win_index
# plt.plot(t, delay,'ko')
# pplot(t, delay, indexes)
# plt.show()

"""to randomize the index selection for noloss"""
win11=int((win_index[0]+win_index[1])*0.285)
win21=int((win_index[1]+win_index[2])*0.53)
win31=int((win_index[2]+win_index[3])*0.52)
win41=int((win_index[3]+win_index[4])*0.5)
win51=int((win_index[4]+win_index[5])*0.5)
win61=int((win_index[5]+win_index[6])*0.5)
win71=int((win_index[6]+win_index[7])*0.5)
win81=int((win_index[7]+win_index[8])*0.5)
win91=int((win_index[8]+win_index[9])*0.5)
win101=int((win_index[9]+win_index[10])*0.5)
win111=int((win_index[10]-win_index[8])*0.05)
win121=int((win_index[10]-win_index[5])*1.5)
# win211=int((win_index[20]+win_index[21])*0.5)
# win221=int((win_index[21]+win_index[22])*0.5)
# win231=int((win_index[22]+win_index[23])*0.5)
# win241=int((win_index[23]+win_index[24])*0.5)
# win251=int((win_index[24]+win_index[25])*0.5)
# win261=int((win_index[25]+win_index[26])*0.5)
# win271=int((win_index[26]+win_index[27])*0.5)
# win281=int(0.7*(win_index[1]-win_index[0]))

# win291=int((win_index[28]+win_index[29])*0.5)
# win301=int((win_index[29]+win_index[30])*0.5)

# win311=int((win_index[30]+win_index[31])*0.5)
# win321=int((win_index[31]+win_index[32])*0.5)
# win331=int((win_index[32]+win_index[33])*0.5)
# win341=int((win_index[33]+win_index[34])*0.5)
# win351=int(0.7*(win_index[1]-win_index[0]))
# win361=int((win_index[35]+win_index[36])*0.5)
# win371=int((win_index[36]+win_index[37])*0.5)
# win381=int((win_index[37]+win_index[38])*0.5)
# win391=int((win_index[38]+win_index[39])*0.5)
# win401=int((win_index[39]+win_index[40])*0.5)

# win411=int((win_index[40]+win_index[41])*0.5)
# win421=int((win_index[41]+win_index[42])*0.5)
# win431=int((win_index[42]+win_index[43])*0.501)
# win441=int((win_index[43]+win_index[44])*0.5)
# win451=int((win_index[44]+win_index[45])*0.5)
# win461=int((win_index[45]+win_index[46])*0.5)
# win471=int((win_index[46]+win_index[47])*0.501)
# win481=int((win_index[47]+win_index[48])*0.5)
# win491=int((win_index[48]+win_index[49])*0.5)
# win501=int(0.7*(win_index[1]-win_index[0]))

# print "win101",win101
"""Since onlyTake diff, and the 2/3 of it, and then add it to first window"""
# win111_1= 0.35*(win_index[1]-win_index[0])
# print "win111", int(win111_1)
# win=int(win111_1)

"""adding no loss ploting"""
# nolosswin=[win11, win21, win31, win41, win51, win61, win71, win81, win91, win101]#, win111,win121, win131, win141, win151, win161, win171, win181, win191]
# print "\n selected NoLoss points at (nolosswin): \n",len(nolosswin),nolosswin
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


# """LOSS # 13"""
# print "Loss # 13"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind131=win131-300
# ind132=win131-150
# ind133=win131

# print "\n index number for window1", ind131, ind132, ind133

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd131=[]
# owd132=[]
# owd133=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind131 and nn<ind132:
# 		owd131.append(iat[nn])
# 	elif nn>=ind132 and nn<ind133:
# 		owd132.append(iat[nn])
# 	elif nn>=ind133 and nn<ind133+150:
# 		owd133.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd131"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd131))
# """ owd131 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd131))
# """owd131 min"""
# print 'min11 = {}'.format(min(owd131))
# """owd131 max"""
# print 'max11 = {}'.format(max(owd131))
# """ owd131 std"""
# print 'std11 = {}'.format(numpy.std(owd131))

# """for owd132"""
# print "number of packets included = {}".format(len(owd132))
# print 'mean12 = {}'.format(numpy.mean(owd132))
# print 'min12 = {}'.format(min(owd132))
# print 'max12 = {}'.format(max(owd132))
# print 'std12 = {}'.format(numpy.std(owd132))

# """ for owd133"""
# print "number of packets included = {}".format(len(owd133))
# print 'mean13 = {}'.format(numpy.mean(owd133))
# print 'min13 = {}'.format(min(owd133))
# print 'max13 = {}'.format(max(owd133))
# print 'std13 = {}'.format(numpy.std(owd133))


# """ next take the Window3/Window1""" 
# m1 = numpy.mean(owd133)/numpy.mean(owd131)
# m2 = numpy.mean(owd133)/numpy.min(owd131)
# m3 = numpy.mean(owd133)/numpy.max(owd131)

# m4 = numpy.min(owd133)/numpy.mean(owd131)
# m5 = numpy.min(owd133)/numpy.min(owd131)
# m6 = numpy.min(owd133)/numpy.max(owd131)

# m7 = numpy.max(owd133)/numpy.mean(owd131)
# m8 = numpy.max(owd133)/numpy.min(owd131)
# m9 = numpy.max(owd133)/numpy.max(owd131)

# """next take the Window3/Window2"""
# m10 = numpy.mean(owd133)/numpy.mean(owd132)
# m11 = numpy.mean(owd133)/numpy.min(owd132)
# m12 = numpy.mean(owd133)/numpy.max(owd132)

# m13 = numpy.min(owd133)/numpy.mean(owd132)
# m14 = numpy.min(owd133)/numpy.min(owd132)
# m15 = numpy.min(owd133)/numpy.max(owd132)

# m16 = numpy.max(owd133)/numpy.mean(owd132)
# m17 = numpy.max(owd133)/numpy.min(owd132)
# m18 = numpy.max(owd133)/numpy.max(owd132)

# """ min/max window 3"""
# m19 = numpy.min(owd133)/numpy.max(owd133)

# """standard dev values"""
# m20 = numpy.std(owd133)/numpy.std(owd131)
# m21 = numpy.std(owd133)/numpy.std(owd132)
# m22 = numpy.std(owd131)/numpy.std(owd132)

# """next window1 / window2"""
# m23 = numpy.mean(owd131)/numpy.mean(owd132)
# m24 = numpy.mean(owd131)/numpy.min(owd132)
# m25 = numpy.mean(owd131)/numpy.max(owd132)

# m26 = numpy.min(owd131)/numpy.mean(owd132)
# m27 = numpy.min(owd131)/numpy.min(owd132)
# m28 = numpy.min(owd131)/numpy.max(owd132)

# m29 = numpy.max(owd131)/numpy.mean(owd132)
# m30 = numpy.max(owd131)/numpy.min(owd132)
# m31 = numpy.max(owd131)/numpy.max(owd132)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(m1)+"\n"
# print "avg-win3 / min-win1 = "+ str(m2)+"\n"
# print "avg-win3 / max-win1 = "+ str(m3)+"\n"

# print "min-win3 / avg-win1 = "+ str(m4)+"\n"
# print "min-win3 / min-win1 = "+ str(m5)+"\n"
# print "min-win3 / max-win1 = "+ str(m6)+"\n"

# print "max-win3 / avg-win1 = "+ str(m7)+"\n"
# print "max-win3 / min-win1 = "+ str(m8)+"\n"
# print "max-win3 / max-win1 = "+ str(m9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(m10)+"\n"
# print "avg-win3 / min-win2 = "+ str(m11)+"\n"
# print "avg-win3 / max-win2 = "+ str(m12)+"\n"

# print "min-win3 / avg-win2 = "+ str(m13)+"\n"
# print "min-win3 / min-win2 = "+ str(m14)+"\n"
# print "min-win3 / max-win2 = "+ str(m15)+"\n"

# print "max-win3 / avg-win2 = "+ str(m16)+"\n"
# print "max-win3 / min-win2 = "+ str(m17)+"\n"
# print "max-win3 / max-win2 = "+ str(m18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(m19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(m20)+"\n"
# print "std-win3 / std-win2 = "+ str(m21)+"\n"
# print "std-win1 / std-win2 = "+ str(m22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(m23)+"\n"
# print "avg-win1 / min-win2 = "+ str(m24)+"\n"
# print "avg-win1 / max-win2 = "+ str(m25)+"\n"

# print "min-win1 / avg-win2 = "+ str(m26)+"\n"
# print "min-win1 / min-win2 = "+ str(m27)+"\n"
# print "min-win1 / max-win2 = "+ str(m28)+"\n"

# print "max-win1 / avg-win2 = "+ str(m29)+"\n"
# print "max-win1 / min-win2 = "+ str(m30)+"\n"
# print "max-win1 / max-win2 = "+ str(m31)+"\n"

# print "#################################################"





# """LOSS # 14"""
# print "Loss # 14"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind141=win141-300
# ind142=win141-150
# ind143=win141

# print "\n index number for loss 14", ind141, ind142, ind143

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd141=[]
# owd142=[]
# owd143=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind141 and nn<ind142:
# 		owd141.append(iat[nn])
# 	elif nn>=ind142 and nn<ind143:
# 		owd142.append(iat[nn])
# 	elif nn>=ind143 and nn<ind143+150:
# 		owd143.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd141"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd141))
# """ owd141 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd141))
# """owd141 min"""
# print 'min11 = {}'.format(min(owd141))
# """owd141 max"""
# print 'max11 = {}'.format(max(owd141))
# """ owd141 std"""
# print 'std11 = {}'.format(numpy.std(owd141))

# """for owd142"""
# print "number of packets included = {}".format(len(owd142))
# print 'mean12 = {}'.format(numpy.mean(owd142))
# print 'min12 = {}'.format(min(owd142))
# print 'max12 = {}'.format(max(owd142))
# print 'std12 = {}'.format(numpy.std(owd142))

# """ for owd143"""
# print "number of packets included = {}".format(len(owd143))
# print 'mean13 = {}'.format(numpy.mean(owd143))
# print 'min13 = {}'.format(min(owd143))
# print 'max13 = {}'.format(max(owd143))
# print 'std13 = {}'.format(numpy.std(owd143))


# """ next take the Window3/Window1""" 
# n1 = numpy.mean(owd143)/numpy.mean(owd141)
# n2 = numpy.mean(owd143)/numpy.min(owd141)
# n3 = numpy.mean(owd143)/numpy.max(owd141)

# n4 = numpy.min(owd143)/numpy.mean(owd141)
# n5 = numpy.min(owd143)/numpy.min(owd141)
# n6 = numpy.min(owd143)/numpy.max(owd141)

# n7 = numpy.max(owd143)/numpy.mean(owd141)
# n8 = numpy.max(owd143)/numpy.min(owd141)
# n9 = numpy.max(owd143)/numpy.max(owd141)

# """next take the Window3/Window2"""
# n10 = numpy.mean(owd143)/numpy.mean(owd142)
# n11 = numpy.mean(owd143)/numpy.min(owd142)
# n12 = numpy.mean(owd143)/numpy.max(owd142)

# n13 = numpy.min(owd143)/numpy.mean(owd142)
# n14 = numpy.min(owd143)/numpy.min(owd142)
# n15 = numpy.min(owd143)/numpy.max(owd142)

# n16 = numpy.max(owd143)/numpy.mean(owd142)
# n17 = numpy.max(owd143)/numpy.min(owd142)
# n18 = numpy.max(owd143)/numpy.max(owd142)

# """ min/max window 3"""
# n19 = numpy.min(owd143)/numpy.max(owd143)

# """standard dev values"""
# n20 = numpy.std(owd143)/numpy.std(owd141)
# n21 = numpy.std(owd143)/numpy.std(owd142)
# n22 = numpy.std(owd141)/numpy.std(owd142)

# """next window1 / window2"""
# n23 = numpy.mean(owd141)/numpy.mean(owd142)
# n24 = numpy.mean(owd141)/numpy.min(owd142)
# n25 = numpy.mean(owd141)/numpy.max(owd142)

# n26 = numpy.min(owd141)/numpy.mean(owd142)
# n27 = numpy.min(owd141)/numpy.min(owd142)
# n28 = numpy.min(owd141)/numpy.max(owd142)

# n29 = numpy.max(owd141)/numpy.mean(owd142)
# n30 = numpy.max(owd141)/numpy.min(owd142)
# n31 = numpy.max(owd141)/numpy.max(owd142)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(n1)+"\n"
# print "avg-win3 / min-win1 = "+ str(n2)+"\n"
# print "avg-win3 / max-win1 = "+ str(n3)+"\n"

# print "min-win3 / avg-win1 = "+ str(n4)+"\n"
# print "min-win3 / min-win1 = "+ str(n5)+"\n"
# print "min-win3 / max-win1 = "+ str(n6)+"\n"

# print "max-win3 / avg-win1 = "+ str(n7)+"\n"
# print "max-win3 / min-win1 = "+ str(n8)+"\n"
# print "max-win3 / max-win1 = "+ str(n9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(n10)+"\n"
# print "avg-win3 / min-win2 = "+ str(n11)+"\n"
# print "avg-win3 / max-win2 = "+ str(n12)+"\n"

# print "min-win3 / avg-win2 = "+ str(n13)+"\n"
# print "min-win3 / min-win2 = "+ str(n14)+"\n"
# print "min-win3 / max-win2 = "+ str(n15)+"\n"

# print "max-win3 / avg-win2 = "+ str(n16)+"\n"
# print "max-win3 / min-win2 = "+ str(n17)+"\n"
# print "max-win3 / max-win2 = "+ str(n18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(n19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(n20)+"\n"
# print "std-win3 / std-win2 = "+ str(n21)+"\n"
# print "std-win1 / std-win2 = "+ str(n22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(n23)+"\n"
# print "avg-win1 / min-win2 = "+ str(n24)+"\n"
# print "avg-win1 / max-win2 = "+ str(n25)+"\n"

# print "min-win1 / avg-win2 = "+ str(n26)+"\n"
# print "min-win1 / min-win2 = "+ str(n27)+"\n"
# print "min-win1 / max-win2 = "+ str(n28)+"\n"

# print "max-win1 / avg-win2 = "+ str(n29)+"\n"
# print "max-win1 / min-win2 = "+ str(n30)+"\n"
# print "max-win1 / max-win2 = "+ str(n31)+"\n"

# print "#################################################"





# """LOSS # 15"""
# print "Loss # 15"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind151=win151-300
# ind152=win151-150
# ind153=win151

# print "\n index number for loss 15", ind151, ind152, ind153

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd151=[]
# owd152=[]
# owd153=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind151 and nn<ind152:
# 		owd151.append(iat[nn])
# 	elif nn>=ind152 and nn<ind153:
# 		owd152.append(iat[nn])
# 	elif nn>=ind153 and nn<ind153+150:
# 		owd153.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd151"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd151))
# """ owd151 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd151))
# """owd151 min"""
# print 'min11 = {}'.format(min(owd151))
# """owd151 max"""
# print 'max11 = {}'.format(max(owd151))
# """ owd151 std"""
# print 'std11 = {}'.format(numpy.std(owd151))

# """for owd152"""
# print "number of packets included = {}".format(len(owd152))
# print 'mean12 = {}'.format(numpy.mean(owd152))
# print 'min12 = {}'.format(min(owd152))
# print 'max12 = {}'.format(max(owd152))
# print 'std12 = {}'.format(numpy.std(owd152))

# """ for owd153"""
# print "number of packets included = {}".format(len(owd153))
# print 'mean13 = {}'.format(numpy.mean(owd153))
# print 'min13 = {}'.format(min(owd153))
# print 'max13 = {}'.format(max(owd153))
# print 'std13 = {}'.format(numpy.std(owd153))


# """ next take the Window3/Window1""" 
# o1 = numpy.mean(owd153)/numpy.mean(owd151)
# o2 = numpy.mean(owd153)/numpy.min(owd151)
# o3 = numpy.mean(owd153)/numpy.max(owd151)

# o4 = numpy.min(owd153)/numpy.mean(owd151)
# o5 = numpy.min(owd153)/numpy.min(owd151)
# o6 = numpy.min(owd153)/numpy.max(owd151)

# o7 = numpy.max(owd153)/numpy.mean(owd151)
# o8 = numpy.max(owd153)/numpy.min(owd151)
# o9 = numpy.max(owd153)/numpy.max(owd151)

# """next take the Window3/Window2"""
# o10 = numpy.mean(owd153)/numpy.mean(owd152)
# o11 = numpy.mean(owd153)/numpy.min(owd152)
# o12 = numpy.mean(owd153)/numpy.max(owd152)

# o13 = numpy.min(owd153)/numpy.mean(owd152)
# o14 = numpy.min(owd153)/numpy.min(owd152)
# o15 = numpy.min(owd153)/numpy.max(owd152)

# o16 = numpy.max(owd153)/numpy.mean(owd152)
# o17 = numpy.max(owd153)/numpy.min(owd152)
# o18 = numpy.max(owd153)/numpy.max(owd152)

# """ min/max window 3"""
# o19 = numpy.min(owd153)/numpy.max(owd153)

# """standard dev values"""
# o20 = numpy.std(owd153)/numpy.std(owd151)
# o21 = numpy.std(owd153)/numpy.std(owd152)
# o22 = numpy.std(owd151)/numpy.std(owd152)

# """next window1 / window2"""
# o23 = numpy.mean(owd151)/numpy.mean(owd152)
# o24 = numpy.mean(owd151)/numpy.min(owd152)
# o25 = numpy.mean(owd151)/numpy.max(owd152)

# o26 = numpy.min(owd151)/numpy.mean(owd152)
# o27 = numpy.min(owd151)/numpy.min(owd152)
# o28 = numpy.min(owd151)/numpy.max(owd152)

# o29 = numpy.max(owd151)/numpy.mean(owd152)
# o30 = numpy.max(owd151)/numpy.min(owd152)
# o31 = numpy.max(owd151)/numpy.max(owd152)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(o1)+"\n"
# print "avg-win3 / min-win1 = "+ str(o2)+"\n"
# print "avg-win3 / max-win1 = "+ str(o3)+"\n"

# print "min-win3 / avg-win1 = "+ str(o4)+"\n"
# print "min-win3 / min-win1 = "+ str(o5)+"\n"
# print "min-win3 / max-win1 = "+ str(o6)+"\n"

# print "max-win3 / avg-win1 = "+ str(o7)+"\n"
# print "max-win3 / min-win1 = "+ str(o8)+"\n"
# print "max-win3 / max-win1 = "+ str(o9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(o10)+"\n"
# print "avg-win3 / min-win2 = "+ str(o11)+"\n"
# print "avg-win3 / max-win2 = "+ str(o12)+"\n"

# print "min-win3 / avg-win2 = "+ str(o13)+"\n"
# print "min-win3 / min-win2 = "+ str(o14)+"\n"
# print "min-win3 / max-win2 = "+ str(o15)+"\n"

# print "max-win3 / avg-win2 = "+ str(o16)+"\n"
# print "max-win3 / min-win2 = "+ str(o17)+"\n"
# print "max-win3 / max-win2 = "+ str(o18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(o19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(o20)+"\n"
# print "std-win3 / std-win2 = "+ str(o21)+"\n"
# print "std-win1 / std-win2 = "+ str(o22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(o23)+"\n"
# print "avg-win1 / min-win2 = "+ str(o24)+"\n"
# print "avg-win1 / max-win2 = "+ str(o25)+"\n"

# print "min-win1 / avg-win2 = "+ str(o26)+"\n"
# print "min-win1 / min-win2 = "+ str(o27)+"\n"
# print "min-win1 / max-win2 = "+ str(o28)+"\n"

# print "max-win1 / avg-win2 = "+ str(o29)+"\n"
# print "max-win1 / min-win2 = "+ str(o30)+"\n"
# print "max-win1 / max-win2 = "+ str(o31)+"\n"

# print "#################################################"



# """LOSS # 16"""
# print "Loss # 16"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind161=win161-300
# ind162=win161-150
# ind163=win161

# print "\n index number for loss ", ind161, ind162, ind163

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd161=[]
# owd162=[]
# owd163=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind161 and nn<ind162:
# 		owd161.append(iat[nn])
# 	elif nn>=ind162 and nn<ind163:
# 		owd162.append(iat[nn])
# 	elif nn>=ind163 and nn<ind163+150:
# 		owd163.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd161"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd161))
# """ owd161 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd161))
# """owd161 min"""
# print 'min11 = {}'.format(min(owd161))
# """owd161 max"""
# print 'max11 = {}'.format(max(owd161))
# """ owd161 std"""
# print 'std11 = {}'.format(numpy.std(owd161))

# """for owd162"""
# print "number of packets included = {}".format(len(owd162))
# print 'mean12 = {}'.format(numpy.mean(owd162))
# print 'min12 = {}'.format(min(owd162))
# print 'max12 = {}'.format(max(owd162))
# print 'std12 = {}'.format(numpy.std(owd162))

# """ for owd163"""
# print "number of packets included = {}".format(len(owd163))
# print 'mean13 = {}'.format(numpy.mean(owd163))
# print 'min13 = {}'.format(min(owd163))
# print 'max13 = {}'.format(max(owd163))
# print 'std13 = {}'.format(numpy.std(owd163))


# """ next take the Window3/Window1""" 
# p1 = numpy.mean(owd163)/numpy.mean(owd161)
# p2 = numpy.mean(owd163)/numpy.min(owd161)
# p3 = numpy.mean(owd163)/numpy.max(owd161)

# p4 = numpy.min(owd163)/numpy.mean(owd161)
# p5 = numpy.min(owd163)/numpy.min(owd161)
# p6 = numpy.min(owd163)/numpy.max(owd161)

# p7 = numpy.max(owd163)/numpy.mean(owd161)
# p8 = numpy.max(owd163)/numpy.min(owd161)
# p9 = numpy.max(owd163)/numpy.max(owd161)

# """next take the Window3/Window2"""
# p10 = numpy.mean(owd163)/numpy.mean(owd162)
# p11 = numpy.mean(owd163)/numpy.min(owd162)
# p12 = numpy.mean(owd163)/numpy.max(owd162)

# p13 = numpy.min(owd163)/numpy.mean(owd162)
# p14 = numpy.min(owd163)/numpy.min(owd162)
# p15 = numpy.min(owd163)/numpy.max(owd162)

# p16 = numpy.max(owd163)/numpy.mean(owd162)
# p17 = numpy.max(owd163)/numpy.min(owd162)
# p18 = numpy.max(owd163)/numpy.max(owd162)

# """ min/max window 3"""
# p19 = numpy.min(owd163)/numpy.max(owd163)

# """standard dev values"""
# p20 = numpy.std(owd163)/numpy.std(owd161)
# p21 = numpy.std(owd163)/numpy.std(owd162)
# p22 = numpy.std(owd161)/numpy.std(owd162)

# """next window1 / window2"""
# p23 = numpy.mean(owd161)/numpy.mean(owd162)
# p24 = numpy.mean(owd161)/numpy.min(owd162)
# p25 = numpy.mean(owd161)/numpy.max(owd162)

# p26 = numpy.min(owd161)/numpy.mean(owd162)
# p27 = numpy.min(owd161)/numpy.min(owd162)
# p28 = numpy.min(owd161)/numpy.max(owd162)

# p29 = numpy.max(owd161)/numpy.mean(owd162)
# p30 = numpy.max(owd161)/numpy.min(owd162)
# p31 = numpy.max(owd161)/numpy.max(owd162)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(p1)+"\n"
# print "avg-win3 / min-win1 = "+ str(p2)+"\n"
# print "avg-win3 / max-win1 = "+ str(p3)+"\n"

# print "min-win3 / avg-win1 = "+ str(p4)+"\n"
# print "min-win3 / min-win1 = "+ str(p5)+"\n"
# print "min-win3 / max-win1 = "+ str(p6)+"\n"

# print "max-win3 / avg-win1 = "+ str(p7)+"\n"
# print "max-win3 / min-win1 = "+ str(p8)+"\n"
# print "max-win3 / max-win1 = "+ str(p9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(p10)+"\n"
# print "avg-win3 / min-win2 = "+ str(p11)+"\n"
# print "avg-win3 / max-win2 = "+ str(p12)+"\n"

# print "min-win3 / avg-win2 = "+ str(p13)+"\n"
# print "min-win3 / min-win2 = "+ str(p14)+"\n"
# print "min-win3 / max-win2 = "+ str(p15)+"\n"

# print "max-win3 / avg-win2 = "+ str(p16)+"\n"
# print "max-win3 / min-win2 = "+ str(p17)+"\n"
# print "max-win3 / max-win2 = "+ str(p18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(p19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(p20)+"\n"
# print "std-win3 / std-win2 = "+ str(p21)+"\n"
# print "std-win1 / std-win2 = "+ str(p22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(p23)+"\n"
# print "avg-win1 / min-win2 = "+ str(p24)+"\n"
# print "avg-win1 / max-win2 = "+ str(p25)+"\n"

# print "min-win1 / avg-win2 = "+ str(p26)+"\n"
# print "min-win1 / min-win2 = "+ str(p27)+"\n"
# print "min-win1 / max-win2 = "+ str(p28)+"\n"

# print "max-win1 / avg-win2 = "+ str(p29)+"\n"
# print "max-win1 / min-win2 = "+ str(p30)+"\n"
# print "max-win1 / max-win2 = "+ str(p31)+"\n"

# print "#################################################"



# """LOSS # 17"""
# print "Loss # 17"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind171=win171-300
# ind172=win171-150
# ind173=win171

# print "\n index number for loss ", ind171, ind172, ind173

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd171=[]
# owd172=[]
# owd173=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind171 and nn<ind172:
# 		owd171.append(iat[nn])
# 	elif nn>=ind172 and nn<ind173:
# 		owd172.append(iat[nn])
# 	elif nn>=ind173 and nn<ind173+150:
# 		owd173.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd171"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd171))
# """ owd171 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd171))
# """owd171 min"""
# print 'min11 = {}'.format(min(owd171))
# """owd171 max"""
# print 'max11 = {}'.format(max(owd171))
# """ owd171 std"""
# print 'std11 = {}'.format(numpy.std(owd171))

# """for owd172"""
# print "number of packets included = {}".format(len(owd172))
# print 'mean12 = {}'.format(numpy.mean(owd172))
# print 'min12 = {}'.format(min(owd172))
# print 'max12 = {}'.format(max(owd172))
# print 'std12 = {}'.format(numpy.std(owd172))

# """ for owd173"""
# print "number of packets included = {}".format(len(owd173))
# print 'mean13 = {}'.format(numpy.mean(owd173))
# print 'min13 = {}'.format(min(owd173))
# print 'max13 = {}'.format(max(owd173))
# print 'std13 = {}'.format(numpy.std(owd173))


# """ next take the Window3/Window1""" 
# q1 = numpy.mean(owd173)/numpy.mean(owd171)
# q2 = numpy.mean(owd173)/numpy.min(owd171)
# q3 = numpy.mean(owd173)/numpy.max(owd171)

# q4 = numpy.min(owd173)/numpy.mean(owd171)
# q5 = numpy.min(owd173)/numpy.min(owd171)
# q6 = numpy.min(owd173)/numpy.max(owd171)

# q7 = numpy.max(owd173)/numpy.mean(owd171)
# q8 = numpy.max(owd173)/numpy.min(owd171)
# q9 = numpy.max(owd173)/numpy.max(owd171)

# """next take the Window3/Window2"""
# q10 = numpy.mean(owd173)/numpy.mean(owd172)
# q11 = numpy.mean(owd173)/numpy.min(owd172)
# q12 = numpy.mean(owd173)/numpy.max(owd172)

# q13 = numpy.min(owd173)/numpy.mean(owd172)
# q14 = numpy.min(owd173)/numpy.min(owd172)
# q15 = numpy.min(owd173)/numpy.max(owd172)

# q16 = numpy.max(owd173)/numpy.mean(owd172)
# q17 = numpy.max(owd173)/numpy.min(owd172)
# q18 = numpy.max(owd173)/numpy.max(owd172)

# """ min/max window 3"""
# q19 = numpy.min(owd173)/numpy.max(owd173)

# """standard dev values"""
# q20 = numpy.std(owd173)/numpy.std(owd171)
# q21 = numpy.std(owd173)/numpy.std(owd172)
# q22 = numpy.std(owd171)/numpy.std(owd172)

# """next window1 / window2"""
# q23 = numpy.mean(owd171)/numpy.mean(owd172)
# q24 = numpy.mean(owd171)/numpy.min(owd172)
# q25 = numpy.mean(owd171)/numpy.max(owd172)

# q26 = numpy.min(owd171)/numpy.mean(owd172)
# q27 = numpy.min(owd171)/numpy.min(owd172)
# q28 = numpy.min(owd171)/numpy.max(owd172)

# q29 = numpy.max(owd171)/numpy.mean(owd172)
# q30 = numpy.max(owd171)/numpy.min(owd172)
# q31 = numpy.max(owd171)/numpy.max(owd172)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(q1)+"\n"
# print "avg-win3 / min-win1 = "+ str(q2)+"\n"
# print "avg-win3 / max-win1 = "+ str(q3)+"\n"

# print "min-win3 / avg-win1 = "+ str(q4)+"\n"
# print "min-win3 / min-win1 = "+ str(q5)+"\n"
# print "min-win3 / max-win1 = "+ str(q6)+"\n"

# print "max-win3 / avg-win1 = "+ str(q7)+"\n"
# print "max-win3 / min-win1 = "+ str(q8)+"\n"
# print "max-win3 / max-win1 = "+ str(q9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(q10)+"\n"
# print "avg-win3 / min-win2 = "+ str(q11)+"\n"
# print "avg-win3 / max-win2 = "+ str(q12)+"\n"

# print "min-win3 / avg-win2 = "+ str(q13)+"\n"
# print "min-win3 / min-win2 = "+ str(q14)+"\n"
# print "min-win3 / max-win2 = "+ str(q15)+"\n"

# print "max-win3 / avg-win2 = "+ str(q16)+"\n"
# print "max-win3 / min-win2 = "+ str(q17)+"\n"
# print "max-win3 / max-win2 = "+ str(q18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(q19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(q20)+"\n"
# print "std-win3 / std-win2 = "+ str(q21)+"\n"
# print "std-win1 / std-win2 = "+ str(q22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(q23)+"\n"
# print "avg-win1 / min-win2 = "+ str(q24)+"\n"
# print "avg-win1 / max-win2 = "+ str(q25)+"\n"

# print "min-win1 / avg-win2 = "+ str(q26)+"\n"
# print "min-win1 / min-win2 = "+ str(q27)+"\n"
# print "min-win1 / max-win2 = "+ str(q28)+"\n"

# print "max-win1 / avg-win2 = "+ str(q29)+"\n"
# print "max-win1 / min-win2 = "+ str(q30)+"\n"
# print "max-win1 / max-win2 = "+ str(q31)+"\n"

# print "#################################################"







# """LOSS # 18"""
# print "Loss # 18"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind181=win181-300
# ind182=win181-150
# ind183=win181

# print "\n index number for loss ", ind181, ind182, ind183

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd181=[]
# owd182=[]
# owd183=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind181 and nn<ind182:
# 		owd181.append(iat[nn])
# 	elif nn>=ind182 and nn<ind183:
# 		owd182.append(iat[nn])
# 	elif nn>=ind183 and nn<ind183+150:
# 		owd183.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd181"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd181))
# """ owd181 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd181))
# """owd181 min"""
# print 'min11 = {}'.format(min(owd181))
# """owd181 max"""
# print 'max11 = {}'.format(max(owd181))
# """ owd181 std"""
# print 'std11 = {}'.format(numpy.std(owd181))

# """for owd182"""
# print "number of packets included = {}".format(len(owd182))
# print 'mean12 = {}'.format(numpy.mean(owd182))
# print 'min12 = {}'.format(min(owd182))
# print 'max12 = {}'.format(max(owd182))
# print 'std12 = {}'.format(numpy.std(owd182))

# """ for owd183"""
# print "number of packets included = {}".format(len(owd183))
# print 'mean13 = {}'.format(numpy.mean(owd183))
# print 'min13 = {}'.format(min(owd183))
# print 'max13 = {}'.format(max(owd183))
# print 'std13 = {}'.format(numpy.std(owd183))


# """ next take the Window3/Window1""" 
# r1 = numpy.mean(owd183)/numpy.mean(owd181)
# r2 = numpy.mean(owd183)/numpy.min(owd181)
# r3 = numpy.mean(owd183)/numpy.max(owd181)

# r4 = numpy.min(owd183)/numpy.mean(owd181)
# r5 = numpy.min(owd183)/numpy.min(owd181)
# r6 = numpy.min(owd183)/numpy.max(owd181)

# r7 = numpy.max(owd183)/numpy.mean(owd181)
# r8 = numpy.max(owd183)/numpy.min(owd181)
# r9 = numpy.max(owd183)/numpy.max(owd181)

# """next take the Window3/Window2"""
# r10 = numpy.mean(owd183)/numpy.mean(owd182)
# r11 = numpy.mean(owd183)/numpy.min(owd182)
# r12 = numpy.mean(owd183)/numpy.max(owd182)

# r13 = numpy.min(owd183)/numpy.mean(owd182)
# r14 = numpy.min(owd183)/numpy.min(owd182)
# r15 = numpy.min(owd183)/numpy.max(owd182)

# r16 = numpy.max(owd183)/numpy.mean(owd182)
# r17 = numpy.max(owd183)/numpy.min(owd182)
# r18 = numpy.max(owd183)/numpy.max(owd182)

# """ min/max window 3"""
# r19 = numpy.min(owd183)/numpy.max(owd183)

# """standard dev values"""
# r20 = numpy.std(owd183)/numpy.std(owd181)
# r21 = numpy.std(owd183)/numpy.std(owd182)
# r22 = numpy.std(owd181)/numpy.std(owd182)

# """next window1 / window2"""
# r23 = numpy.mean(owd181)/numpy.mean(owd182)
# r24 = numpy.mean(owd181)/numpy.min(owd182)
# r25 = numpy.mean(owd181)/numpy.max(owd182)

# r26 = numpy.min(owd181)/numpy.mean(owd182)
# r27 = numpy.min(owd181)/numpy.min(owd182)
# r28 = numpy.min(owd181)/numpy.max(owd182)

# r29 = numpy.max(owd181)/numpy.mean(owd182)
# r30 = numpy.max(owd181)/numpy.min(owd182)
# r31 = numpy.max(owd181)/numpy.max(owd182)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(r1)+"\n"
# print "avg-win3 / min-win1 = "+ str(r2)+"\n"
# print "avg-win3 / max-win1 = "+ str(r3)+"\n"

# print "min-win3 / avg-win1 = "+ str(r4)+"\n"
# print "min-win3 / min-win1 = "+ str(r5)+"\n"
# print "min-win3 / max-win1 = "+ str(r6)+"\n"

# print "max-win3 / avg-win1 = "+ str(r7)+"\n"
# print "max-win3 / min-win1 = "+ str(r8)+"\n"
# print "max-win3 / max-win1 = "+ str(r9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(r10)+"\n"
# print "avg-win3 / min-win2 = "+ str(r11)+"\n"
# print "avg-win3 / max-win2 = "+ str(r12)+"\n"

# print "min-win3 / avg-win2 = "+ str(r13)+"\n"
# print "min-win3 / min-win2 = "+ str(r14)+"\n"
# print "min-win3 / max-win2 = "+ str(r15)+"\n"

# print "max-win3 / avg-win2 = "+ str(r16)+"\n"
# print "max-win3 / min-win2 = "+ str(r17)+"\n"
# print "max-win3 / max-win2 = "+ str(r18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(r19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(r20)+"\n"
# print "std-win3 / std-win2 = "+ str(r21)+"\n"
# print "std-win1 / std-win2 = "+ str(r22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(r23)+"\n"
# print "avg-win1 / min-win2 = "+ str(r24)+"\n"
# print "avg-win1 / max-win2 = "+ str(r25)+"\n"

# print "min-win1 / avg-win2 = "+ str(r26)+"\n"
# print "min-win1 / min-win2 = "+ str(r27)+"\n"
# print "min-win1 / max-win2 = "+ str(r28)+"\n"

# print "max-win1 / avg-win2 = "+ str(r29)+"\n"
# print "max-win1 / min-win2 = "+ str(r30)+"\n"
# print "max-win1 / max-win2 = "+ str(r31)+"\n"

# print "#################################################"



# """LOSS # 19"""
# print "Loss # 19"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind191=win191-300
# ind192=win191-150
# ind193=win191

# print "\n index number for loss 19 ", ind191, ind192, ind193

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd191=[]
# owd192=[]
# owd193=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind191 and nn<ind192:
# 		owd191.append(iat[nn])
# 	elif nn>=ind192 and nn<ind193:
# 		owd192.append(iat[nn])
# 	elif nn>=ind193 and nn<ind193+150:
# 		owd193.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd191"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd191))
# """ owd191 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd191))
# """owd191 min"""
# print 'min11 = {}'.format(min(owd191))
# """owd191 max"""
# print 'max11 = {}'.format(max(owd191))
# """ owd191 std"""
# print 'std11 = {}'.format(numpy.std(owd191))

# """for owd192"""
# print "number of packets included = {}".format(len(owd192))
# print 'mean12 = {}'.format(numpy.mean(owd192))
# print 'min12 = {}'.format(min(owd192))
# print 'max12 = {}'.format(max(owd192))
# print 'std12 = {}'.format(numpy.std(owd192))

# """ for owd193"""
# print "number of packets included = {}".format(len(owd193))
# print 'mean13 = {}'.format(numpy.mean(owd193))
# print 'min13 = {}'.format(min(owd193))
# print 'max13 = {}'.format(max(owd193))
# print 'std13 = {}'.format(numpy.std(owd193))


# """ next take the Window3/Window1""" 
# s1 = numpy.mean(owd193)/numpy.mean(owd191)
# s2 = numpy.mean(owd193)/numpy.min(owd191)
# s3 = numpy.mean(owd193)/numpy.max(owd191)

# s4 = numpy.min(owd193)/numpy.mean(owd191)
# s5 = numpy.min(owd193)/numpy.min(owd191)
# s6 = numpy.min(owd193)/numpy.max(owd191)

# s7 = numpy.max(owd193)/numpy.mean(owd191)
# s8 = numpy.max(owd193)/numpy.min(owd191)
# s9 = numpy.max(owd193)/numpy.max(owd191)

# """next take the Window3/Window2"""
# s10 = numpy.mean(owd193)/numpy.mean(owd192)
# s11 = numpy.mean(owd193)/numpy.min(owd192)
# s12 = numpy.mean(owd193)/numpy.max(owd192)

# s13 = numpy.min(owd193)/numpy.mean(owd192)
# s14 = numpy.min(owd193)/numpy.min(owd192)
# s15 = numpy.min(owd193)/numpy.max(owd192)

# s16 = numpy.max(owd193)/numpy.mean(owd192)
# s17 = numpy.max(owd193)/numpy.min(owd192)
# s18 = numpy.max(owd193)/numpy.max(owd192)

# """ min/max window 3"""
# s19 = numpy.min(owd193)/numpy.max(owd193)

# """standard dev values"""
# s20 = numpy.std(owd193)/numpy.std(owd191)
# s21 = numpy.std(owd193)/numpy.std(owd192)
# s22 = numpy.std(owd191)/numpy.std(owd192)

# """next window1 / window2"""
# s23 = numpy.mean(owd191)/numpy.mean(owd192)
# s24 = numpy.mean(owd191)/numpy.min(owd192)
# s25 = numpy.mean(owd191)/numpy.max(owd192)

# s26 = numpy.min(owd191)/numpy.mean(owd192)
# s27 = numpy.min(owd191)/numpy.min(owd192)
# s28 = numpy.min(owd191)/numpy.max(owd192)

# s29 = numpy.max(owd191)/numpy.mean(owd192)
# s30 = numpy.max(owd191)/numpy.min(owd192)
# s31 = numpy.max(owd191)/numpy.max(owd192)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(s1)+"\n"
# print "avg-win3 / min-win1 = "+ str(s2)+"\n"
# print "avg-win3 / max-win1 = "+ str(s3)+"\n"

# print "min-win3 / avg-win1 = "+ str(s4)+"\n"
# print "min-win3 / min-win1 = "+ str(s5)+"\n"
# print "min-win3 / max-win1 = "+ str(s6)+"\n"

# print "max-win3 / avg-win1 = "+ str(s7)+"\n"
# print "max-win3 / min-win1 = "+ str(s8)+"\n"
# print "max-win3 / max-win1 = "+ str(s9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(s10)+"\n"
# print "avg-win3 / min-win2 = "+ str(s11)+"\n"
# print "avg-win3 / max-win2 = "+ str(s12)+"\n"

# print "min-win3 / avg-win2 = "+ str(s13)+"\n"
# print "min-win3 / min-win2 = "+ str(s14)+"\n"
# print "min-win3 / max-win2 = "+ str(s15)+"\n"

# print "max-win3 / avg-win2 = "+ str(s16)+"\n"
# print "max-win3 / min-win2 = "+ str(s17)+"\n"
# print "max-win3 / max-win2 = "+ str(s18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(s19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(s20)+"\n"
# print "std-win3 / std-win2 = "+ str(s21)+"\n"
# print "std-win1 / std-win2 = "+ str(s22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(s23)+"\n"
# print "avg-win1 / min-win2 = "+ str(s24)+"\n"
# print "avg-win1 / max-win2 = "+ str(s25)+"\n"

# print "min-win1 / avg-win2 = "+ str(s26)+"\n"
# print "min-win1 / min-win2 = "+ str(s27)+"\n"
# print "min-win1 / max-win2 = "+ str(s28)+"\n"

# print "max-win1 / avg-win2 = "+ str(s29)+"\n"
# print "max-win1 / min-win2 = "+ str(s30)+"\n"
# print "max-win1 / max-win2 = "+ str(s31)+"\n"

# print "#################################################"






# """LOSS # 20"""
# print "Loss # 20"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind201=win201-300
# ind202=win201-150
# ind203=win201

# print "\n index number for loss 20 ", ind201, ind202, ind203

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd201=[]
# owd202=[]
# owd203=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind201 and nn<ind202:
# 		owd201.append(iat[nn])
# 	elif nn>=ind202 and nn<ind203:
# 		owd202.append(iat[nn])
# 	elif nn>=ind203 and nn<ind203+150:
# 		owd203.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd201"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd201))
# """ owd201 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd201))
# """owd201 min"""
# print 'min11 = {}'.format(min(owd201))
# """owd201 max"""
# print 'max11 = {}'.format(max(owd201))
# """ owd201 std"""
# print 'std11 = {}'.format(numpy.std(owd201))

# """for owd202"""
# print "number of packets included = {}".format(len(owd202))
# print 'mean12 = {}'.format(numpy.mean(owd202))
# print 'min12 = {}'.format(min(owd202))
# print 'max12 = {}'.format(max(owd202))
# print 'std12 = {}'.format(numpy.std(owd202))

# """ for owd203"""
# print "number of packets included = {}".format(len(owd203))
# print 'mean13 = {}'.format(numpy.mean(owd203))
# print 'min13 = {}'.format(min(owd203))
# print 'max13 = {}'.format(max(owd203))
# print 'std13 = {}'.format(numpy.std(owd203))


# """ next take the Window3/Window1""" 
# t1 = numpy.mean(owd203)/numpy.mean(owd201)
# t2 = numpy.mean(owd203)/numpy.min(owd201)
# t3 = numpy.mean(owd203)/numpy.max(owd201)

# t4 = numpy.min(owd203)/numpy.mean(owd201)
# t5 = numpy.min(owd203)/numpy.min(owd201)
# t6 = numpy.min(owd203)/numpy.max(owd201)

# t7 = numpy.max(owd203)/numpy.mean(owd201)
# t8 = numpy.max(owd203)/numpy.min(owd201)
# t9 = numpy.max(owd203)/numpy.max(owd201)

# """next take the Window3/Window2"""
# t10 = numpy.mean(owd203)/numpy.mean(owd202)
# t11 = numpy.mean(owd203)/numpy.min(owd202)
# t12 = numpy.mean(owd203)/numpy.max(owd202)

# t13 = numpy.min(owd203)/numpy.mean(owd202)
# t14 = numpy.min(owd203)/numpy.min(owd202)
# t15 = numpy.min(owd203)/numpy.max(owd202)

# t16 = numpy.max(owd203)/numpy.mean(owd202)
# t17 = numpy.max(owd203)/numpy.min(owd202)
# t18 = numpy.max(owd203)/numpy.max(owd202)

# """ min/max window 3"""
# t19 = numpy.min(owd203)/numpy.max(owd203)

# """standard dev values"""
# t20 = numpy.std(owd203)/numpy.std(owd201)
# t21 = numpy.std(owd203)/numpy.std(owd202)
# t22 = numpy.std(owd201)/numpy.std(owd202)

# """next window1 / window2"""
# t23 = numpy.mean(owd201)/numpy.mean(owd202)
# t24 = numpy.mean(owd201)/numpy.min(owd202)
# t25 = numpy.mean(owd201)/numpy.max(owd202)

# t26 = numpy.min(owd201)/numpy.mean(owd202)
# t27 = numpy.min(owd201)/numpy.min(owd202)
# t28 = numpy.min(owd201)/numpy.max(owd202)

# t29 = numpy.max(owd201)/numpy.mean(owd202)
# t30 = numpy.max(owd201)/numpy.min(owd202)
# t31 = numpy.max(owd201)/numpy.max(owd202)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(t1)+"\n"
# print "avg-win3 / min-win1 = "+ str(t2)+"\n"
# print "avg-win3 / max-win1 = "+ str(t3)+"\n"

# print "min-win3 / avg-win1 = "+ str(t4)+"\n"
# print "min-win3 / min-win1 = "+ str(t5)+"\n"
# print "min-win3 / max-win1 = "+ str(t6)+"\n"

# print "max-win3 / avg-win1 = "+ str(t7)+"\n"
# print "max-win3 / min-win1 = "+ str(t8)+"\n"
# print "max-win3 / max-win1 = "+ str(t9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(t10)+"\n"
# print "avg-win3 / min-win2 = "+ str(t11)+"\n"
# print "avg-win3 / max-win2 = "+ str(t12)+"\n"

# print "min-win3 / avg-win2 = "+ str(t13)+"\n"
# print "min-win3 / min-win2 = "+ str(t14)+"\n"
# print "min-win3 / max-win2 = "+ str(t15)+"\n"

# print "max-win3 / avg-win2 = "+ str(t16)+"\n"
# print "max-win3 / min-win2 = "+ str(t17)+"\n"
# print "max-win3 / max-win2 = "+ str(t18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(t19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(t20)+"\n"
# print "std-win3 / std-win2 = "+ str(t21)+"\n"
# print "std-win1 / std-win2 = "+ str(t22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(t23)+"\n"
# print "avg-win1 / min-win2 = "+ str(t24)+"\n"
# print "avg-win1 / max-win2 = "+ str(t25)+"\n"

# print "min-win1 / avg-win2 = "+ str(t26)+"\n"
# print "min-win1 / min-win2 = "+ str(t27)+"\n"
# print "min-win1 / max-win2 = "+ str(t28)+"\n"

# print "max-win1 / avg-win2 = "+ str(t29)+"\n"
# print "max-win1 / min-win2 = "+ str(t30)+"\n"
# print "max-win1 / max-win2 = "+ str(t31)+"\n"

# print "#################################################"








# """LOSS # 21"""
# print "Loss # 21"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind211=win211-300
# ind212=win211-150
# ind213=win211

# print "\n index number for loss 21", ind211, ind212, ind213

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd211=[]
# owd212=[]
# owd213=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind211 and nn<ind212:
# 		owd211.append(iat[nn])
# 	elif nn>=ind212 and nn<ind213:
# 		owd212.append(iat[nn])
# 	elif nn>=ind213 and nn<ind213+150:
# 		owd213.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd211"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd211))
# """ owd211 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd211))
# """owd211 min"""
# print 'min11 = {}'.format(min(owd211))
# """owd211 max"""
# print 'max11 = {}'.format(max(owd211))
# """ owd211 std"""
# print 'std11 = {}'.format(numpy.std(owd211))

# """for owd212"""
# print "number of packets included = {}".format(len(owd212))
# print 'mean12 = {}'.format(numpy.mean(owd212))
# print 'min12 = {}'.format(min(owd212))
# print 'max12 = {}'.format(max(owd212))
# print 'std12 = {}'.format(numpy.std(owd212))

# """ for owd213"""
# print "number of packets included = {}".format(len(owd213))
# print 'mean13 = {}'.format(numpy.mean(owd213))
# print 'min13 = {}'.format(min(owd213))
# print 'max13 = {}'.format(max(owd213))
# print 'std13 = {}'.format(numpy.std(owd213))


# """ next take the Window3/Window1""" 
# u1 = numpy.mean(owd213)/numpy.mean(owd211)
# u2 = numpy.mean(owd213)/numpy.min(owd211)
# u3 = numpy.mean(owd213)/numpy.max(owd211)

# u4 = numpy.min(owd213)/numpy.mean(owd211)
# u5 = numpy.min(owd213)/numpy.min(owd211)
# u6 = numpy.min(owd213)/numpy.max(owd211)

# u7 = numpy.max(owd213)/numpy.mean(owd211)
# u8 = numpy.max(owd213)/numpy.min(owd211)
# u9 = numpy.max(owd213)/numpy.max(owd211)

# """next take the Window3/Window2"""
# u10 = numpy.mean(owd213)/numpy.mean(owd212)
# u11 = numpy.mean(owd213)/numpy.min(owd212)
# u12 = numpy.mean(owd213)/numpy.max(owd212)

# u13 = numpy.min(owd213)/numpy.mean(owd212)
# u14 = numpy.min(owd213)/numpy.min(owd212)
# u15 = numpy.min(owd213)/numpy.max(owd212)

# u16 = numpy.max(owd213)/numpy.mean(owd212)
# u17 = numpy.max(owd213)/numpy.min(owd212)
# u18 = numpy.max(owd213)/numpy.max(owd212)

# """ min/max window 3"""
# u19 = numpy.min(owd213)/numpy.max(owd213)

# """standard dev values"""
# u20 = numpy.std(owd213)/numpy.std(owd211)
# u21 = numpy.std(owd213)/numpy.std(owd212)
# u22 = numpy.std(owd211)/numpy.std(owd212)

# """next window1 / window2"""
# u23 = numpy.mean(owd211)/numpy.mean(owd212)
# u24 = numpy.mean(owd211)/numpy.min(owd212)
# u25 = numpy.mean(owd211)/numpy.max(owd212)

# u26 = numpy.min(owd211)/numpy.mean(owd212)
# u27 = numpy.min(owd211)/numpy.min(owd212)
# u28 = numpy.min(owd211)/numpy.max(owd212)

# u29 = numpy.max(owd211)/numpy.mean(owd212)
# u30 = numpy.max(owd211)/numpy.min(owd212)
# u31 = numpy.max(owd211)/numpy.max(owd212)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(u1)+"\n"
# print "avg-win3 / min-win1 = "+ str(u2)+"\n"
# print "avg-win3 / max-win1 = "+ str(u3)+"\n"

# print "min-win3 / avg-win1 = "+ str(u4)+"\n"
# print "min-win3 / min-win1 = "+ str(u5)+"\n"
# print "min-win3 / max-win1 = "+ str(u6)+"\n"

# print "max-win3 / avg-win1 = "+ str(u7)+"\n"
# print "max-win3 / min-win1 = "+ str(u8)+"\n"
# print "max-win3 / max-win1 = "+ str(u9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(u10)+"\n"
# print "avg-win3 / min-win2 = "+ str(u11)+"\n"
# print "avg-win3 / max-win2 = "+ str(u12)+"\n"

# print "min-win3 / avg-win2 = "+ str(u13)+"\n"
# print "min-win3 / min-win2 = "+ str(u14)+"\n"
# print "min-win3 / max-win2 = "+ str(u15)+"\n"

# print "max-win3 / avg-win2 = "+ str(u16)+"\n"
# print "max-win3 / min-win2 = "+ str(u17)+"\n"
# print "max-win3 / max-win2 = "+ str(u18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(u19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(u20)+"\n"
# print "std-win3 / std-win2 = "+ str(u21)+"\n"
# print "std-win1 / std-win2 = "+ str(u22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(u23)+"\n"
# print "avg-win1 / min-win2 = "+ str(u24)+"\n"
# print "avg-win1 / max-win2 = "+ str(u25)+"\n"

# print "min-win1 / avg-win2 = "+ str(u26)+"\n"
# print "min-win1 / min-win2 = "+ str(u27)+"\n"
# print "min-win1 / max-win2 = "+ str(u28)+"\n"

# print "max-win1 / avg-win2 = "+ str(u29)+"\n"
# print "max-win1 / min-win2 = "+ str(u30)+"\n"
# print "max-win1 / max-win2 = "+ str(u31)+"\n"

# print "#################################################"








# """LOSS # 22"""
# print "Loss # 22"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind221=win221-300
# ind222=win221-150
# ind223=win221

# print "\n index number for loss 22", ind221, ind222, ind223

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd221=[]
# owd222=[]
# owd223=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind221 and nn<ind222:
# 		owd221.append(iat[nn])
# 	elif nn>=ind222 and nn<ind223:
# 		owd222.append(iat[nn])
# 	elif nn>=ind223 and nn<ind223+150:
# 		owd223.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd221"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd221))
# """ owd221 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd221))
# """owd221 min"""
# print 'min11 = {}'.format(min(owd221))
# """owd221 max"""
# print 'max11 = {}'.format(max(owd221))
# """ owd221 std"""
# print 'std11 = {}'.format(numpy.std(owd221))

# """for owd222"""
# print "number of packets included = {}".format(len(owd222))
# print 'mean12 = {}'.format(numpy.mean(owd222))
# print 'min12 = {}'.format(min(owd222))
# print 'max12 = {}'.format(max(owd222))
# print 'std12 = {}'.format(numpy.std(owd222))

# """ for owd223"""
# print "number of packets included = {}".format(len(owd223))
# print 'mean13 = {}'.format(numpy.mean(owd223))
# print 'min13 = {}'.format(min(owd223))
# print 'max13 = {}'.format(max(owd223))
# print 'std13 = {}'.format(numpy.std(owd223))


# """ next take the Window3/Window1""" 
# v1 = numpy.mean(owd223)/numpy.mean(owd221)
# v2 = numpy.mean(owd223)/numpy.min(owd221)
# v3 = numpy.mean(owd223)/numpy.max(owd221)

# v4 = numpy.min(owd223)/numpy.mean(owd221)
# v5 = numpy.min(owd223)/numpy.min(owd221)
# v6 = numpy.min(owd223)/numpy.max(owd221)

# v7 = numpy.max(owd223)/numpy.mean(owd221)
# v8 = numpy.max(owd223)/numpy.min(owd221)
# v9 = numpy.max(owd223)/numpy.max(owd221)

# """next take the Window3/Window2"""
# v10 = numpy.mean(owd223)/numpy.mean(owd222)
# v11 = numpy.mean(owd223)/numpy.min(owd222)
# v12 = numpy.mean(owd223)/numpy.max(owd222)

# v13 = numpy.min(owd223)/numpy.mean(owd222)
# v14 = numpy.min(owd223)/numpy.min(owd222)
# v15 = numpy.min(owd223)/numpy.max(owd222)

# v16 = numpy.max(owd223)/numpy.mean(owd222)
# v17 = numpy.max(owd223)/numpy.min(owd222)
# v18 = numpy.max(owd223)/numpy.max(owd222)

# """ min/max window 3"""
# v19 = numpy.min(owd223)/numpy.max(owd223)

# """standard dev values"""
# v20 = numpy.std(owd223)/numpy.std(owd221)
# v21 = numpy.std(owd223)/numpy.std(owd222)
# v22 = numpy.std(owd221)/numpy.std(owd222)

# """next window1 / window2"""
# v23 = numpy.mean(owd221)/numpy.mean(owd222)
# v24 = numpy.mean(owd221)/numpy.min(owd222)
# v25 = numpy.mean(owd221)/numpy.max(owd222)

# v26 = numpy.min(owd221)/numpy.mean(owd222)
# v27 = numpy.min(owd221)/numpy.min(owd222)
# v28 = numpy.min(owd221)/numpy.max(owd222)

# v29 = numpy.max(owd221)/numpy.mean(owd222)
# v30 = numpy.max(owd221)/numpy.min(owd222)
# v31 = numpy.max(owd221)/numpy.max(owd222)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(v1)+"\n"
# print "avg-win3 / min-win1 = "+ str(v2)+"\n"
# print "avg-win3 / max-win1 = "+ str(v3)+"\n"

# print "min-win3 / avg-win1 = "+ str(v4)+"\n"
# print "min-win3 / min-win1 = "+ str(v5)+"\n"
# print "min-win3 / max-win1 = "+ str(v6)+"\n"

# print "max-win3 / avg-win1 = "+ str(v7)+"\n"
# print "max-win3 / min-win1 = "+ str(v8)+"\n"
# print "max-win3 / max-win1 = "+ str(v9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(v10)+"\n"
# print "avg-win3 / min-win2 = "+ str(v11)+"\n"
# print "avg-win3 / max-win2 = "+ str(v12)+"\n"

# print "min-win3 / avg-win2 = "+ str(v13)+"\n"
# print "min-win3 / min-win2 = "+ str(v14)+"\n"
# print "min-win3 / max-win2 = "+ str(v15)+"\n"

# print "max-win3 / avg-win2 = "+ str(v16)+"\n"
# print "max-win3 / min-win2 = "+ str(v17)+"\n"
# print "max-win3 / max-win2 = "+ str(v18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(v19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(v20)+"\n"
# print "std-win3 / std-win2 = "+ str(v21)+"\n"
# print "std-win1 / std-win2 = "+ str(v22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(v23)+"\n"
# print "avg-win1 / min-win2 = "+ str(v24)+"\n"
# print "avg-win1 / max-win2 = "+ str(v25)+"\n"

# print "min-win1 / avg-win2 = "+ str(v26)+"\n"
# print "min-win1 / min-win2 = "+ str(v27)+"\n"
# print "min-win1 / max-win2 = "+ str(v28)+"\n"

# print "max-win1 / avg-win2 = "+ str(v29)+"\n"
# print "max-win1 / min-win2 = "+ str(v30)+"\n"
# print "max-win1 / max-win2 = "+ str(v31)+"\n"

# print "#################################################"








# """LOSS # 23"""
# print "Loss # 23"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind231=win231-300
# ind232=win231-150
# ind233=win231

# print "\n index number for loss 23", ind231, ind232, ind233

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd231=[]
# owd232=[]
# owd233=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind231 and nn<ind232:
# 		owd231.append(iat[nn])
# 	elif nn>=ind232 and nn<ind233:
# 		owd232.append(iat[nn])
# 	elif nn>=ind233 and nn<ind233+150:
# 		owd233.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd231"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd231))
# """ owd231 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd231))
# """owd231 min"""
# print 'min11 = {}'.format(min(owd231))
# """owd231 max"""
# print 'max11 = {}'.format(max(owd231))
# """ owd231 std"""
# print 'std11 = {}'.format(numpy.std(owd231))

# """for owd232"""
# print "number of packets included = {}".format(len(owd232))
# print 'mean12 = {}'.format(numpy.mean(owd232))
# print 'min12 = {}'.format(min(owd232))
# print 'max12 = {}'.format(max(owd232))
# print 'std12 = {}'.format(numpy.std(owd232))

# """ for owd233"""
# print "number of packets included = {}".format(len(owd233))
# print 'mean13 = {}'.format(numpy.mean(owd233))
# print 'min13 = {}'.format(min(owd233))
# print 'max13 = {}'.format(max(owd233))
# print 'std13 = {}'.format(numpy.std(owd233))


# """ next take the Window3/Window1""" 
# w1 = numpy.mean(owd233)/numpy.mean(owd231)
# w2 = numpy.mean(owd233)/numpy.min(owd231)
# w3 = numpy.mean(owd233)/numpy.max(owd231)

# w4 = numpy.min(owd233)/numpy.mean(owd231)
# w5 = numpy.min(owd233)/numpy.min(owd231)
# w6 = numpy.min(owd233)/numpy.max(owd231)

# w7 = numpy.max(owd233)/numpy.mean(owd231)
# w8 = numpy.max(owd233)/numpy.min(owd231)
# w9 = numpy.max(owd233)/numpy.max(owd231)

# """next take the Window3/Window2"""
# w10 = numpy.mean(owd233)/numpy.mean(owd232)
# w11 = numpy.mean(owd233)/numpy.min(owd232)
# w12 = numpy.mean(owd233)/numpy.max(owd232)

# w13 = numpy.min(owd233)/numpy.mean(owd232)
# w14 = numpy.min(owd233)/numpy.min(owd232)
# w15 = numpy.min(owd233)/numpy.max(owd232)

# w16 = numpy.max(owd233)/numpy.mean(owd232)
# w17 = numpy.max(owd233)/numpy.min(owd232)
# w18 = numpy.max(owd233)/numpy.max(owd232)

# """ min/max window 3"""
# w19 = numpy.min(owd233)/numpy.max(owd233)

# """standard dev values"""
# w20 = numpy.std(owd233)/numpy.std(owd231)
# w21 = numpy.std(owd233)/numpy.std(owd232)
# w22 = numpy.std(owd231)/numpy.std(owd232)

# """next window1 / window2"""
# w23 = numpy.mean(owd231)/numpy.mean(owd232)
# w24 = numpy.mean(owd231)/numpy.min(owd232)
# w25 = numpy.mean(owd231)/numpy.max(owd232)

# w26 = numpy.min(owd231)/numpy.mean(owd232)
# w27 = numpy.min(owd231)/numpy.min(owd232)
# w28 = numpy.min(owd231)/numpy.max(owd232)

# w29 = numpy.max(owd231)/numpy.mean(owd232)
# w30 = numpy.max(owd231)/numpy.min(owd232)
# w31 = numpy.max(owd231)/numpy.max(owd232)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(w1)+"\n"
# print "avg-win3 / min-win1 = "+ str(w2)+"\n"
# print "avg-win3 / max-win1 = "+ str(w3)+"\n"

# print "min-win3 / avg-win1 = "+ str(w4)+"\n"
# print "min-win3 / min-win1 = "+ str(w5)+"\n"
# print "min-win3 / max-win1 = "+ str(w6)+"\n"

# print "max-win3 / avg-win1 = "+ str(w7)+"\n"
# print "max-win3 / min-win1 = "+ str(w8)+"\n"
# print "max-win3 / max-win1 = "+ str(w9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(w10)+"\n"
# print "avg-win3 / min-win2 = "+ str(w11)+"\n"
# print "avg-win3 / max-win2 = "+ str(w12)+"\n"

# print "min-win3 / avg-win2 = "+ str(w13)+"\n"
# print "min-win3 / min-win2 = "+ str(w14)+"\n"
# print "min-win3 / max-win2 = "+ str(w15)+"\n"

# print "max-win3 / avg-win2 = "+ str(w16)+"\n"
# print "max-win3 / min-win2 = "+ str(w17)+"\n"
# print "max-win3 / max-win2 = "+ str(w18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(w19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(w20)+"\n"
# print "std-win3 / std-win2 = "+ str(w21)+"\n"
# print "std-win1 / std-win2 = "+ str(w22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(w23)+"\n"
# print "avg-win1 / min-win2 = "+ str(w24)+"\n"
# print "avg-win1 / max-win2 = "+ str(w25)+"\n"

# print "min-win1 / avg-win2 = "+ str(w26)+"\n"
# print "min-win1 / min-win2 = "+ str(w27)+"\n"
# print "min-win1 / max-win2 = "+ str(w28)+"\n"

# print "max-win1 / avg-win2 = "+ str(w29)+"\n"
# print "max-win1 / min-win2 = "+ str(w30)+"\n"
# print "max-win1 / max-win2 = "+ str(w31)+"\n"

# print "#################################################"








# """LOSS # 24"""
# print "Loss # 24"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind241=win241-300
# ind242=win241-150
# ind243=win241

# print "\n index number for loss 24 ", ind241, ind242, ind243

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd241=[]
# owd242=[]
# owd243=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind241 and nn<ind242:
# 		owd241.append(iat[nn])
# 	elif nn>=ind242 and nn<ind243:
# 		owd242.append(iat[nn])
# 	elif nn>=ind243 and nn<ind243+150:
# 		owd243.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd241"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd241))
# """ owd241 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd241))
# """owd241 min"""
# print 'min11 = {}'.format(min(owd241))
# """owd241 max"""
# print 'max11 = {}'.format(max(owd241))
# """ owd241 std"""
# print 'std11 = {}'.format(numpy.std(owd241))

# """for owd242"""
# print "number of packets included = {}".format(len(owd242))
# print 'mean12 = {}'.format(numpy.mean(owd242))
# print 'min12 = {}'.format(min(owd242))
# print 'max12 = {}'.format(max(owd242))
# print 'std12 = {}'.format(numpy.std(owd242))

# """ for owd243"""
# print "number of packets included = {}".format(len(owd243))
# print 'mean13 = {}'.format(numpy.mean(owd243))
# print 'min13 = {}'.format(min(owd243))
# print 'max13 = {}'.format(max(owd243))
# print 'std13 = {}'.format(numpy.std(owd243))


# """ next take the Window3/Window1""" 
# x1 = numpy.mean(owd243)/numpy.mean(owd241)
# x2 = numpy.mean(owd243)/numpy.min(owd241)
# x3 = numpy.mean(owd243)/numpy.max(owd241)

# x4 = numpy.min(owd243)/numpy.mean(owd241)
# x5 = numpy.min(owd243)/numpy.min(owd241)
# x6 = numpy.min(owd243)/numpy.max(owd241)

# x7 = numpy.max(owd243)/numpy.mean(owd241)
# x8 = numpy.max(owd243)/numpy.min(owd241)
# x9 = numpy.max(owd243)/numpy.max(owd241)

# """next take the Window3/Window2"""
# x10 = numpy.mean(owd243)/numpy.mean(owd242)
# x11 = numpy.mean(owd243)/numpy.min(owd242)
# x12 = numpy.mean(owd243)/numpy.max(owd242)

# x13 = numpy.min(owd243)/numpy.mean(owd242)
# x14 = numpy.min(owd243)/numpy.min(owd242)
# x15 = numpy.min(owd243)/numpy.max(owd242)

# x16 = numpy.max(owd243)/numpy.mean(owd242)
# x17 = numpy.max(owd243)/numpy.min(owd242)
# x18 = numpy.max(owd243)/numpy.max(owd242)

# """ min/max window 3"""
# x19 = numpy.min(owd243)/numpy.max(owd243)

# """standard dev values"""
# x20 = numpy.std(owd243)/numpy.std(owd241)
# x21 = numpy.std(owd243)/numpy.std(owd242)
# x22 = numpy.std(owd241)/numpy.std(owd242)

# """next window1 / window2"""
# x23 = numpy.mean(owd241)/numpy.mean(owd242)
# x24 = numpy.mean(owd241)/numpy.min(owd242)
# x25 = numpy.mean(owd241)/numpy.max(owd242)

# x26 = numpy.min(owd241)/numpy.mean(owd242)
# x27 = numpy.min(owd241)/numpy.min(owd242)
# x28 = numpy.min(owd241)/numpy.max(owd242)

# x29 = numpy.max(owd241)/numpy.mean(owd242)
# x30 = numpy.max(owd241)/numpy.min(owd242)
# x31 = numpy.max(owd241)/numpy.max(owd242)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(x1)+"\n"
# print "avg-win3 / min-win1 = "+ str(x2)+"\n"
# print "avg-win3 / max-win1 = "+ str(x3)+"\n"

# print "min-win3 / avg-win1 = "+ str(x4)+"\n"
# print "min-win3 / min-win1 = "+ str(x5)+"\n"
# print "min-win3 / max-win1 = "+ str(x6)+"\n"

# print "max-win3 / avg-win1 = "+ str(x7)+"\n"
# print "max-win3 / min-win1 = "+ str(x8)+"\n"
# print "max-win3 / max-win1 = "+ str(x9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(x10)+"\n"
# print "avg-win3 / min-win2 = "+ str(x11)+"\n"
# print "avg-win3 / max-win2 = "+ str(x12)+"\n"

# print "min-win3 / avg-win2 = "+ str(x13)+"\n"
# print "min-win3 / min-win2 = "+ str(x14)+"\n"
# print "min-win3 / max-win2 = "+ str(x15)+"\n"

# print "max-win3 / avg-win2 = "+ str(x16)+"\n"
# print "max-win3 / min-win2 = "+ str(x17)+"\n"
# print "max-win3 / max-win2 = "+ str(x18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(x19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(x20)+"\n"
# print "std-win3 / std-win2 = "+ str(x21)+"\n"
# print "std-win1 / std-win2 = "+ str(x22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(x23)+"\n"
# print "avg-win1 / min-win2 = "+ str(x24)+"\n"
# print "avg-win1 / max-win2 = "+ str(x25)+"\n"

# print "min-win1 / avg-win2 = "+ str(x26)+"\n"
# print "min-win1 / min-win2 = "+ str(x27)+"\n"
# print "min-win1 / max-win2 = "+ str(x28)+"\n"

# print "max-win1 / avg-win2 = "+ str(x29)+"\n"
# print "max-win1 / min-win2 = "+ str(x30)+"\n"
# print "max-win1 / max-win2 = "+ str(x31)+"\n"

# print "#################################################"








# """LOSS # 25"""
# print "Loss # 25"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind251=win251-300
# ind252=win251-150
# ind253=win251

# print "\n index number for loss ", ind251, ind252, ind253

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd251=[]
# owd252=[]
# owd253=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind251 and nn<ind252:
# 		owd251.append(iat[nn])
# 	elif nn>=ind252 and nn<ind253:
# 		owd252.append(iat[nn])
# 	elif nn>=ind253 and nn<ind253+150:
# 		owd253.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd251"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd251))
# """ owd251 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd251))
# """owd251 min"""
# print 'min11 = {}'.format(min(owd251))
# """owd251 max"""
# print 'max11 = {}'.format(max(owd251))
# """ owd251 std"""
# print 'std11 = {}'.format(numpy.std(owd251))

# """for owd252"""
# print "number of packets included = {}".format(len(owd252))
# print 'mean12 = {}'.format(numpy.mean(owd252))
# print 'min12 = {}'.format(min(owd252))
# print 'max12 = {}'.format(max(owd252))
# print 'std12 = {}'.format(numpy.std(owd252))

# """ for owd253"""
# print "number of packets included = {}".format(len(owd253))
# print 'mean13 = {}'.format(numpy.mean(owd253))
# print 'min13 = {}'.format(min(owd253))
# print 'max13 = {}'.format(max(owd253))
# print 'std13 = {}'.format(numpy.std(owd253))


# """ next take the Window3/Window1""" 
# y1 = numpy.mean(owd253)/numpy.mean(owd251)
# y2 = numpy.mean(owd253)/numpy.min(owd251)
# y3 = numpy.mean(owd253)/numpy.max(owd251)

# y4 = numpy.min(owd253)/numpy.mean(owd251)
# y5 = numpy.min(owd253)/numpy.min(owd251)
# y6 = numpy.min(owd253)/numpy.max(owd251)

# y7 = numpy.max(owd253)/numpy.mean(owd251)
# y8 = numpy.max(owd253)/numpy.min(owd251)
# y9 = numpy.max(owd253)/numpy.max(owd251)

# """next take the Window3/Window2"""
# y10 = numpy.mean(owd253)/numpy.mean(owd252)
# y11 = numpy.mean(owd253)/numpy.min(owd252)
# y12 = numpy.mean(owd253)/numpy.max(owd252)

# y13 = numpy.min(owd253)/numpy.mean(owd252)
# y14 = numpy.min(owd253)/numpy.min(owd252)
# y15 = numpy.min(owd253)/numpy.max(owd252)

# y16 = numpy.max(owd253)/numpy.mean(owd252)
# y17 = numpy.max(owd253)/numpy.min(owd252)
# y18 = numpy.max(owd253)/numpy.max(owd252)

# """ min/max window 3"""
# y19 = numpy.min(owd253)/numpy.max(owd253)

# """standard dev values"""
# y20 = numpy.std(owd253)/numpy.std(owd251)
# y21 = numpy.std(owd253)/numpy.std(owd252)
# y22 = numpy.std(owd251)/numpy.std(owd252)

# """next window1 / window2"""
# y23 = numpy.mean(owd251)/numpy.mean(owd252)
# y24 = numpy.mean(owd251)/numpy.min(owd252)
# y25 = numpy.mean(owd251)/numpy.max(owd252)

# y26 = numpy.min(owd251)/numpy.mean(owd252)
# y27 = numpy.min(owd251)/numpy.min(owd252)
# y28 = numpy.min(owd251)/numpy.max(owd252)

# y29 = numpy.max(owd251)/numpy.mean(owd252)
# y30 = numpy.max(owd251)/numpy.min(owd252)
# y31 = numpy.max(owd251)/numpy.max(owd252)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(y1)+"\n"
# print "avg-win3 / min-win1 = "+ str(y2)+"\n"
# print "avg-win3 / max-win1 = "+ str(y3)+"\n"

# print "min-win3 / avg-win1 = "+ str(y4)+"\n"
# print "min-win3 / min-win1 = "+ str(y5)+"\n"
# print "min-win3 / max-win1 = "+ str(y6)+"\n"

# print "max-win3 / avg-win1 = "+ str(y7)+"\n"
# print "max-win3 / min-win1 = "+ str(y8)+"\n"
# print "max-win3 / max-win1 = "+ str(y9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(y10)+"\n"
# print "avg-win3 / min-win2 = "+ str(y11)+"\n"
# print "avg-win3 / max-win2 = "+ str(y12)+"\n"

# print "min-win3 / avg-win2 = "+ str(y13)+"\n"
# print "min-win3 / min-win2 = "+ str(y14)+"\n"
# print "min-win3 / max-win2 = "+ str(y15)+"\n"

# print "max-win3 / avg-win2 = "+ str(y16)+"\n"
# print "max-win3 / min-win2 = "+ str(y17)+"\n"
# print "max-win3 / max-win2 = "+ str(y18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(y19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(y20)+"\n"
# print "std-win3 / std-win2 = "+ str(y21)+"\n"
# print "std-win1 / std-win2 = "+ str(y22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(y23)+"\n"
# print "avg-win1 / min-win2 = "+ str(y24)+"\n"
# print "avg-win1 / max-win2 = "+ str(y25)+"\n"

# print "min-win1 / avg-win2 = "+ str(y26)+"\n"
# print "min-win1 / min-win2 = "+ str(y27)+"\n"
# print "min-win1 / max-win2 = "+ str(y28)+"\n"

# print "max-win1 / avg-win2 = "+ str(y29)+"\n"
# print "max-win1 / min-win2 = "+ str(y30)+"\n"
# print "max-win1 / max-win2 = "+ str(y31)+"\n"

# print "#################################################"








# """LOSS # 26"""
# print "Loss # 26"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind261=win261-300
# ind262=win261-150
# ind263=win261

# print "\n index number for loss 26 ", ind261, ind262, ind263

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd261=[]
# owd262=[]
# owd263=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind261 and nn<ind262:
# 		owd261.append(iat[nn])
# 	elif nn>=ind262 and nn<ind263:
# 		owd262.append(iat[nn])
# 	elif nn>=ind263 and nn<ind263+150:
# 		owd263.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd261"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd261))
# """ owd261 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd261))
# """owd261 min"""
# print 'min11 = {}'.format(min(owd261))
# """owd261 max"""
# print 'max11 = {}'.format(max(owd261))
# """ owd261 std"""
# print 'std11 = {}'.format(numpy.std(owd261))

# """for owd262"""
# print "number of packets included = {}".format(len(owd262))
# print 'mean12 = {}'.format(numpy.mean(owd262))
# print 'min12 = {}'.format(min(owd262))
# print 'max12 = {}'.format(max(owd262))
# print 'std12 = {}'.format(numpy.std(owd262))

# """ for owd263"""
# print "number of packets included = {}".format(len(owd263))
# print 'mean13 = {}'.format(numpy.mean(owd263))
# print 'min13 = {}'.format(min(owd263))
# print 'max13 = {}'.format(max(owd263))
# print 'std13 = {}'.format(numpy.std(owd263))


# """ next take the Window3/Window1""" 
# z1 = numpy.mean(owd263)/numpy.mean(owd261)
# z2 = numpy.mean(owd263)/numpy.min(owd261)
# z3 = numpy.mean(owd263)/numpy.max(owd261)

# z4 = numpy.min(owd263)/numpy.mean(owd261)
# z5 = numpy.min(owd263)/numpy.min(owd261)
# z6 = numpy.min(owd263)/numpy.max(owd261)

# z7 = numpy.max(owd263)/numpy.mean(owd261)
# z8 = numpy.max(owd263)/numpy.min(owd261)
# z9 = numpy.max(owd263)/numpy.max(owd261)

# """next take the Window3/Window2"""
# z10 = numpy.mean(owd263)/numpy.mean(owd262)
# z11 = numpy.mean(owd263)/numpy.min(owd262)
# z12 = numpy.mean(owd263)/numpy.max(owd262)

# z13 = numpy.min(owd263)/numpy.mean(owd262)
# z14 = numpy.min(owd263)/numpy.min(owd262)
# z15 = numpy.min(owd263)/numpy.max(owd262)

# z16 = numpy.max(owd263)/numpy.mean(owd262)
# z17 = numpy.max(owd263)/numpy.min(owd262)
# z18 = numpy.max(owd263)/numpy.max(owd262)

# """ min/max window 3"""
# z19 = numpy.min(owd263)/numpy.max(owd263)

# """standard dev values"""
# z20 = numpy.std(owd263)/numpy.std(owd261)
# z21 = numpy.std(owd263)/numpy.std(owd262)
# z22 = numpy.std(owd261)/numpy.std(owd262)

# """next window1 / window2"""
# z23 = numpy.mean(owd261)/numpy.mean(owd262)
# z24 = numpy.mean(owd261)/numpy.min(owd262)
# z25 = numpy.mean(owd261)/numpy.max(owd262)

# z26 = numpy.min(owd261)/numpy.mean(owd262)
# z27 = numpy.min(owd261)/numpy.min(owd262)
# z28 = numpy.min(owd261)/numpy.max(owd262)

# z29 = numpy.max(owd261)/numpy.mean(owd262)
# z30 = numpy.max(owd261)/numpy.min(owd262)
# z31 = numpy.max(owd261)/numpy.max(owd262)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(z1)+"\n"
# print "avg-win3 / min-win1 = "+ str(z2)+"\n"
# print "avg-win3 / max-win1 = "+ str(z3)+"\n"

# print "min-win3 / avg-win1 = "+ str(z4)+"\n"
# print "min-win3 / min-win1 = "+ str(z5)+"\n"
# print "min-win3 / max-win1 = "+ str(z6)+"\n"

# print "max-win3 / avg-win1 = "+ str(z7)+"\n"
# print "max-win3 / min-win1 = "+ str(z8)+"\n"
# print "max-win3 / max-win1 = "+ str(z9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(z10)+"\n"
# print "avg-win3 / min-win2 = "+ str(z11)+"\n"
# print "avg-win3 / max-win2 = "+ str(z12)+"\n"

# print "min-win3 / avg-win2 = "+ str(z13)+"\n"
# print "min-win3 / min-win2 = "+ str(z14)+"\n"
# print "min-win3 / max-win2 = "+ str(z15)+"\n"

# print "max-win3 / avg-win2 = "+ str(z16)+"\n"
# print "max-win3 / min-win2 = "+ str(z17)+"\n"
# print "max-win3 / max-win2 = "+ str(z18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(z19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(z20)+"\n"
# print "std-win3 / std-win2 = "+ str(z21)+"\n"
# print "std-win1 / std-win2 = "+ str(z22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(z23)+"\n"
# print "avg-win1 / min-win2 = "+ str(z24)+"\n"
# print "avg-win1 / max-win2 = "+ str(z25)+"\n"

# print "min-win1 / avg-win2 = "+ str(z26)+"\n"
# print "min-win1 / min-win2 = "+ str(z27)+"\n"
# print "min-win1 / max-win2 = "+ str(z28)+"\n"

# print "max-win1 / avg-win2 = "+ str(z29)+"\n"
# print "max-win1 / min-win2 = "+ str(z30)+"\n"
# print "max-win1 / max-win2 = "+ str(z31)+"\n"

# print "#################################################"








# """LOSS # 27"""
# print "Loss # 27"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind271=win271-300
# ind272=win271-150
# ind273=win271

# print "\n index number for loss 27 ", ind271, ind272, ind273

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd271=[]
# owd272=[]
# owd273=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind271 and nn<ind272:
# 		owd271.append(iat[nn])
# 	elif nn>=ind272 and nn<ind273:
# 		owd272.append(iat[nn])
# 	elif nn>=ind273 and nn<ind273+150:
# 		owd273.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd271"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd271))
# """ owd271 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd271))
# """owd271 min"""
# print 'min11 = {}'.format(min(owd271))
# """owd271 max"""
# print 'max11 = {}'.format(max(owd271))
# """ owd271 std"""
# print 'std11 = {}'.format(numpy.std(owd271))

# """for owd272"""
# print "number of packets included = {}".format(len(owd272))
# print 'mean12 = {}'.format(numpy.mean(owd272))
# print 'min12 = {}'.format(min(owd272))
# print 'max12 = {}'.format(max(owd272))
# print 'std12 = {}'.format(numpy.std(owd272))

# """ for owd273"""
# print "number of packets included = {}".format(len(owd273))
# print 'mean13 = {}'.format(numpy.mean(owd273))
# print 'min13 = {}'.format(min(owd273))
# print 'max13 = {}'.format(max(owd273))
# print 'std13 = {}'.format(numpy.std(owd273))


# """ next take the Window3/Window1""" 
# aa1 = numpy.mean(owd273)/numpy.mean(owd271)
# aa2 = numpy.mean(owd273)/numpy.min(owd271)
# aa3 = numpy.mean(owd273)/numpy.max(owd271)

# aa4 = numpy.min(owd273)/numpy.mean(owd271)
# aa5 = numpy.min(owd273)/numpy.min(owd271)
# aa6 = numpy.min(owd273)/numpy.max(owd271)

# aa7 = numpy.max(owd273)/numpy.mean(owd271)
# aa8 = numpy.max(owd273)/numpy.min(owd271)
# aa9 = numpy.max(owd273)/numpy.max(owd271)

# """next take the Window3/Window2"""
# aa10 = numpy.mean(owd273)/numpy.mean(owd272)
# aa11 = numpy.mean(owd273)/numpy.min(owd272)
# aa12 = numpy.mean(owd273)/numpy.max(owd272)

# aa13 = numpy.min(owd273)/numpy.mean(owd272)
# aa14 = numpy.min(owd273)/numpy.min(owd272)
# aa15 = numpy.min(owd273)/numpy.max(owd272)

# aa16 = numpy.max(owd273)/numpy.mean(owd272)
# aa17 = numpy.max(owd273)/numpy.min(owd272)
# aa18 = numpy.max(owd273)/numpy.max(owd272)

# """ min/max window 3"""
# aa19 = numpy.min(owd273)/numpy.max(owd273)

# """standard dev values"""
# aa20 = numpy.std(owd273)/numpy.std(owd271)
# aa21 = numpy.std(owd273)/numpy.std(owd272)
# aa22 = numpy.std(owd271)/numpy.std(owd272)

# """next window1 / window2"""
# aa23 = numpy.mean(owd271)/numpy.mean(owd272)
# aa24 = numpy.mean(owd271)/numpy.min(owd272)
# aa25 = numpy.mean(owd271)/numpy.max(owd272)

# aa26 = numpy.min(owd271)/numpy.mean(owd272)
# aa27 = numpy.min(owd271)/numpy.min(owd272)
# aa28 = numpy.min(owd271)/numpy.max(owd272)

# aa29 = numpy.max(owd271)/numpy.mean(owd272)
# aa30 = numpy.max(owd271)/numpy.min(owd272)
# aa31 = numpy.max(owd271)/numpy.max(owd272)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(aa1)+"\n"
# print "avg-win3 / min-win1 = "+ str(aa2)+"\n"
# print "avg-win3 / max-win1 = "+ str(aa3)+"\n"

# print "min-win3 / avg-win1 = "+ str(aa4)+"\n"
# print "min-win3 / min-win1 = "+ str(aa5)+"\n"
# print "min-win3 / max-win1 = "+ str(aa6)+"\n"

# print "max-win3 / avg-win1 = "+ str(aa7)+"\n"
# print "max-win3 / min-win1 = "+ str(aa8)+"\n"
# print "max-win3 / max-win1 = "+ str(aa9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(aa10)+"\n"
# print "avg-win3 / min-win2 = "+ str(aa11)+"\n"
# print "avg-win3 / max-win2 = "+ str(aa12)+"\n"

# print "min-win3 / avg-win2 = "+ str(aa13)+"\n"
# print "min-win3 / min-win2 = "+ str(aa14)+"\n"
# print "min-win3 / max-win2 = "+ str(aa15)+"\n"

# print "max-win3 / avg-win2 = "+ str(aa16)+"\n"
# print "max-win3 / min-win2 = "+ str(aa17)+"\n"
# print "max-win3 / max-win2 = "+ str(aa18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(aa19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(aa20)+"\n"
# print "std-win3 / std-win2 = "+ str(aa21)+"\n"
# print "std-win1 / std-win2 = "+ str(aa22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(aa23)+"\n"
# print "avg-win1 / min-win2 = "+ str(aa24)+"\n"
# print "avg-win1 / max-win2 = "+ str(aa25)+"\n"

# print "min-win1 / avg-win2 = "+ str(aa26)+"\n"
# print "min-win1 / min-win2 = "+ str(aa27)+"\n"
# print "min-win1 / max-win2 = "+ str(aa28)+"\n"

# print "max-win1 / avg-win2 = "+ str(aa29)+"\n"
# print "max-win1 / min-win2 = "+ str(aa30)+"\n"
# print "max-win1 / max-win2 = "+ str(aa31)+"\n"

# print "#################################################"


# """LOSS # 28"""
# print "Loss # 28"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind281=win281-300
# ind282=win281-150
# ind283=win281

# print "\n index number for loss 28", ind281, ind282, ind283

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd281=[]
# owd282=[]
# owd283=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>=ind281 and nn<ind282:
# 		owd281.append(iat[nn])
# 	elif nn>=ind282 and nn<ind283:
# 		owd282.append(iat[nn])
# 	elif nn>=ind283 and nn<ind283+150:
# 		owd283.append(iat[nn])
# 		# print tt[nn], iat[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd281"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd281))
# """ owd281 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd281))
# """owd281 min"""
# print 'min11 = {}'.format(min(owd281))
# """owd281 max"""
# print 'max11 = {}'.format(max(owd281))
# """ owd281 std"""
# print 'std11 = {}'.format(numpy.std(owd281))

# """for owd282"""
# print "number of packets included = {}".format(len(owd282))
# print 'mean12 = {}'.format(numpy.mean(owd282))
# print 'min12 = {}'.format(min(owd282))
# print 'max12 = {}'.format(max(owd282))
# print 'std12 = {}'.format(numpy.std(owd282))

# """ for owd283"""
# print "number of packets included = {}".format(len(owd283))
# print 'mean13 = {}'.format(numpy.mean(owd283))
# print 'min13 = {}'.format(min(owd283))
# print 'max13 = {}'.format(max(owd283))
# print 'std13 = {}'.format(numpy.std(owd283))


# """ next take the Window3/Window1""" 
# ab1 = numpy.mean(owd283)/numpy.mean(owd281)
# ab2 = numpy.mean(owd283)/numpy.min(owd281)
# ab3 = numpy.mean(owd283)/numpy.max(owd281)

# ab4 = numpy.min(owd283)/numpy.mean(owd281)
# ab5 = numpy.min(owd283)/numpy.min(owd281)
# ab6 = numpy.min(owd283)/numpy.max(owd281)

# ab7 = numpy.max(owd283)/numpy.mean(owd281)
# ab8 = numpy.max(owd283)/numpy.min(owd281)
# ab9 = numpy.max(owd283)/numpy.max(owd281)

# """next take the Window3/Window2"""
# ab10 = numpy.mean(owd283)/numpy.mean(owd282)
# ab11 = numpy.mean(owd283)/numpy.min(owd282)
# ab12 = numpy.mean(owd283)/numpy.max(owd282)

# ab13 = numpy.min(owd283)/numpy.mean(owd282)
# ab14 = numpy.min(owd283)/numpy.min(owd282)
# ab15 = numpy.min(owd283)/numpy.max(owd282)

# ab16 = numpy.max(owd283)/numpy.mean(owd282)
# ab17 = numpy.max(owd283)/numpy.min(owd282)
# ab18 = numpy.max(owd283)/numpy.max(owd282)

# """ min/max window 3"""
# ab19 = numpy.min(owd283)/numpy.max(owd283)

# """standard dev values"""
# ab20 = numpy.std(owd283)/numpy.std(owd281)
# ab21 = numpy.std(owd283)/numpy.std(owd282)
# ab22 = numpy.std(owd281)/numpy.std(owd282)

# """next window1 / window2"""
# ab23 = numpy.mean(owd281)/numpy.mean(owd282)
# ab24 = numpy.mean(owd281)/numpy.min(owd282)
# ab25 = numpy.mean(owd281)/numpy.max(owd282)

# ab26 = numpy.min(owd281)/numpy.mean(owd282)
# ab27 = numpy.min(owd281)/numpy.min(owd282)
# ab28 = numpy.min(owd281)/numpy.max(owd282)

# ab29 = numpy.max(owd281)/numpy.mean(owd282)
# ab30 = numpy.max(owd281)/numpy.min(owd282)
# ab31 = numpy.max(owd281)/numpy.max(owd282)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ab1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ab2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ab3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ab4)+"\n"
# print "min-win3 / min-win1 = "+ str(ab5)+"\n"
# print "min-win3 / max-win1 = "+ str(ab6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ab7)+"\n"
# print "max-win3 / min-win1 = "+ str(ab8)+"\n"
# print "max-win3 / max-win1 = "+ str(ab9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ab10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ab11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ab12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ab13)+"\n"
# print "min-win3 / min-win2 = "+ str(ab14)+"\n"
# print "min-win3 / max-win2 = "+ str(ab15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ab16)+"\n"
# print "max-win3 / min-win2 = "+ str(ab17)+"\n"
# print "max-win3 / max-win2 = "+ str(ab18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ab19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ab20)+"\n"
# print "std-win3 / std-win2 = "+ str(ab21)+"\n"
# print "std-win1 / std-win2 = "+ str(ab22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ab23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ab24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ab25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ab26)+"\n"
# print "min-win1 / min-win2 = "+ str(ab27)+"\n"
# print "min-win1 / max-win2 = "+ str(ab28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ab29)+"\n"
# print "max-win1 / min-win2 = "+ str(ab30)+"\n"
# print "max-win1 / max-win2 = "+ str(ab31)+"\n"

# print "#################################################"




# ########################################

# """LOSS # 29"""
# print "Loss # 29"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind291=win_index[28]-300
# ind292=win_index[28]-150
# ind293=win_index[28]

# print "\n index number for loss 29", ind291, ind292, ind293

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd291=[]
# owd292=[]
# owd293=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind291 and nn<=ind292:
# 		owd291.append(iat[nn])
# 	elif nn>ind292 and nn<=ind293:
# 		owd292.append(iat[nn])
# 	elif nn>ind293 and nn<=ind293+150:
# 		owd293.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd291"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd291))
# """ owd291 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd291))
# """owd291 min"""
# print 'min11 = {}'.format(min(owd291))
# """owd291 max"""
# print 'max11 = {}'.format(max(owd291))
# """ owd291 std"""
# print 'std11 = {}'.format(numpy.std(owd291))

# """for owd292"""
# print "number of packets included = {}".format(len(owd292))
# print 'mean12 = {}'.format(numpy.mean(owd292))
# print 'min12 = {}'.format(min(owd292))
# print 'max12 = {}'.format(max(owd292))
# print 'std12 = {}'.format(numpy.std(owd292))

# """ for owd293"""
# print "number of packets included = {}".format(len(owd293))
# print 'mean13 = {}'.format(numpy.mean(owd293))
# print 'min13 = {}'.format(min(owd293))
# print 'max13 = {}'.format(max(owd293))
# print 'std13 = {}'.format(numpy.std(owd293))


# """ next take the Window3/Window1""" 
# ac1 = numpy.mean(owd293)/numpy.mean(owd291)
# ac2 = numpy.mean(owd293)/numpy.min(owd291)
# ac3 = numpy.mean(owd293)/numpy.max(owd291)

# ac4 = numpy.min(owd293)/numpy.mean(owd291)
# ac5 = numpy.min(owd293)/numpy.min(owd291)
# ac6 = numpy.min(owd293)/numpy.max(owd291)

# ac7 = numpy.max(owd293)/numpy.mean(owd291)
# ac8 = numpy.max(owd293)/numpy.min(owd291)
# ac9 = numpy.max(owd293)/numpy.max(owd291)

# """next take the Window3/Window2"""
# ac10 = numpy.mean(owd293)/numpy.mean(owd292)
# ac11 = numpy.mean(owd293)/numpy.min(owd292)
# ac12 = numpy.mean(owd293)/numpy.max(owd292)

# ac13 = numpy.min(owd293)/numpy.mean(owd292)
# ac14 = numpy.min(owd293)/numpy.min(owd292)
# ac15 = numpy.min(owd293)/numpy.max(owd292)

# ac16 = numpy.max(owd293)/numpy.mean(owd292)
# ac17 = numpy.max(owd293)/numpy.min(owd292)
# ac18 = numpy.max(owd293)/numpy.max(owd292)

# """ min/max window 3"""
# ac19 = numpy.min(owd293)/numpy.max(owd293)

# """standard dev values"""
# ac20 = numpy.std(owd293)/numpy.std(owd291)
# ac21 = numpy.std(owd293)/numpy.std(owd292)
# ac22 = numpy.std(owd291)/numpy.std(owd292)

# """next window1 / window2"""
# ac23 = numpy.mean(owd291)/numpy.mean(owd292)
# ac24 = numpy.mean(owd291)/numpy.min(owd292)
# ac25 = numpy.mean(owd291)/numpy.max(owd292)

# ac26 = numpy.min(owd291)/numpy.mean(owd292)
# ac27 = numpy.min(owd291)/numpy.min(owd292)
# ac28 = numpy.min(owd291)/numpy.max(owd292)

# ac29 = numpy.max(owd291)/numpy.mean(owd292)
# ac30 = numpy.max(owd291)/numpy.min(owd292)
# ac31 = numpy.max(owd291)/numpy.max(owd292)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ac1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ac2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ac3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ac4)+"\n"
# print "min-win3 / min-win1 = "+ str(ac5)+"\n"
# print "min-win3 / max-win1 = "+ str(ac6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ac7)+"\n"
# print "max-win3 / min-win1 = "+ str(ac8)+"\n"
# print "max-win3 / max-win1 = "+ str(ac9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ac10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ac11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ac12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ac13)+"\n"
# print "min-win3 / min-win2 = "+ str(ac14)+"\n"
# print "min-win3 / max-win2 = "+ str(ac15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ac16)+"\n"
# print "max-win3 / min-win2 = "+ str(ac17)+"\n"
# print "max-win3 / max-win2 = "+ str(ac18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ac19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ac20)+"\n"
# print "std-win3 / std-win2 = "+ str(ac21)+"\n"
# print "std-win1 / std-win2 = "+ str(ac22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ac23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ac24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ac25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ac26)+"\n"
# print "min-win1 / min-win2 = "+ str(ac27)+"\n"
# print "min-win1 / max-win2 = "+ str(ac28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ac29)+"\n"
# print "max-win1 / min-win2 = "+ str(ac30)+"\n"
# print "max-win1 / max-win2 = "+ str(ac31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 30"""
# print "Loss # 30"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind301=win_index[29]-300
# ind302=win_index[29]-150
# ind303=win_index[29]

# print "\n index number for loss 30", ind301, ind302, ind303

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd301=[]
# owd302=[]
# owd303=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind301 and nn<=ind302:
# 		owd301.append(iat[nn])
# 	elif nn>ind302 and nn<=ind303:
# 		owd302.append(iat[nn])
# 	elif nn>ind303 and nn<=ind303+150:
# 		owd303.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd301"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd301))
# """ owd301 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd301))
# """owd301 min"""
# print 'min11 = {}'.format(min(owd301))
# """owd301 max"""
# print 'max11 = {}'.format(max(owd301))
# """ owd301 std"""
# print 'std11 = {}'.format(numpy.std(owd301))

# """for owd302"""
# print "number of packets included = {}".format(len(owd302))
# print 'mean12 = {}'.format(numpy.mean(owd302))
# print 'min12 = {}'.format(min(owd302))
# print 'max12 = {}'.format(max(owd302))
# print 'std12 = {}'.format(numpy.std(owd302))

# """ for owd303"""
# print "number of packets included = {}".format(len(owd303))
# print 'mean13 = {}'.format(numpy.mean(owd303))
# print 'min13 = {}'.format(min(owd303))
# print 'max13 = {}'.format(max(owd303))
# print 'std13 = {}'.format(numpy.std(owd303))


# """ next take the Window3/Window1""" 
# ad1 = numpy.mean(owd303)/numpy.mean(owd301)
# ad2 = numpy.mean(owd303)/numpy.min(owd301)
# ad3 = numpy.mean(owd303)/numpy.max(owd301)

# ad4 = numpy.min(owd303)/numpy.mean(owd301)
# ad5 = numpy.min(owd303)/numpy.min(owd301)
# ad6 = numpy.min(owd303)/numpy.max(owd301)

# ad7 = numpy.max(owd303)/numpy.mean(owd301)
# ad8 = numpy.max(owd303)/numpy.min(owd301)
# ad9 = numpy.max(owd303)/numpy.max(owd301)

# """next take the Window3/Window2"""
# ad10 = numpy.mean(owd303)/numpy.mean(owd302)
# ad11 = numpy.mean(owd303)/numpy.min(owd302)
# ad12 = numpy.mean(owd303)/numpy.max(owd302)

# ad13 = numpy.min(owd303)/numpy.mean(owd302)
# ad14 = numpy.min(owd303)/numpy.min(owd302)
# ad15 = numpy.min(owd303)/numpy.max(owd302)

# ad16 = numpy.max(owd303)/numpy.mean(owd302)
# ad17 = numpy.max(owd303)/numpy.min(owd302)
# ad18 = numpy.max(owd303)/numpy.max(owd302)

# """ min/max window 3"""
# ad19 = numpy.min(owd303)/numpy.max(owd303)

# """standard dev values"""
# ad20 = numpy.std(owd303)/numpy.std(owd301)
# ad21 = numpy.std(owd303)/numpy.std(owd302)
# ad22 = numpy.std(owd301)/numpy.std(owd302)

# """next window1 / window2"""
# ad23 = numpy.mean(owd301)/numpy.mean(owd302)
# ad24 = numpy.mean(owd301)/numpy.min(owd302)
# ad25 = numpy.mean(owd301)/numpy.max(owd302)

# ad26 = numpy.min(owd301)/numpy.mean(owd302)
# ad27 = numpy.min(owd301)/numpy.min(owd302)
# ad28 = numpy.min(owd301)/numpy.max(owd302)

# ad29 = numpy.max(owd301)/numpy.mean(owd302)
# ad30 = numpy.max(owd301)/numpy.min(owd302)
# ad31 = numpy.max(owd301)/numpy.max(owd302)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ad1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ad2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ad3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ad4)+"\n"
# print "min-win3 / min-win1 = "+ str(ad5)+"\n"
# print "min-win3 / max-win1 = "+ str(ad6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ad7)+"\n"
# print "max-win3 / min-win1 = "+ str(ad8)+"\n"
# print "max-win3 / max-win1 = "+ str(ad9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ad10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ad11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ad12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ad13)+"\n"
# print "min-win3 / min-win2 = "+ str(ad14)+"\n"
# print "min-win3 / max-win2 = "+ str(ad15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ad16)+"\n"
# print "max-win3 / min-win2 = "+ str(ad17)+"\n"
# print "max-win3 / max-win2 = "+ str(ad18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ad19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ad20)+"\n"
# print "std-win3 / std-win2 = "+ str(ad21)+"\n"
# print "std-win1 / std-win2 = "+ str(ad22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ad23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ad24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ad25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ad26)+"\n"
# print "min-win1 / min-win2 = "+ str(ad27)+"\n"
# print "min-win1 / max-win2 = "+ str(ad28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ad29)+"\n"
# print "max-win1 / min-win2 = "+ str(ad30)+"\n"
# print "max-win1 / max-win2 = "+ str(ad31)+"\n"

# print "#################################################"


# ########################################

# """LOSS # 31"""
# print "Loss # 31"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind311=win_index[30]-300
# ind312=win_index[30]-150
# ind313=win_index[30]

# print "\n index number for loss 31", ind311, ind312, ind313

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd311=[]
# owd312=[]
# owd313=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind311 and nn<=ind312:
# 		owd311.append(iat[nn])
# 	elif nn>ind312 and nn<=ind313:
# 		owd312.append(iat[nn])
# 	elif nn>ind313 and nn<=ind313+150:
# 		owd313.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd311"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd311))
# """ owd311 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd311))
# """owd311 min"""
# print 'min11 = {}'.format(min(owd311))
# """owd311 max"""
# print 'max11 = {}'.format(max(owd311))
# """ owd311 std"""
# print 'std11 = {}'.format(numpy.std(owd311))

# """for owd312"""
# print "number of packets included = {}".format(len(owd312))
# print 'mean12 = {}'.format(numpy.mean(owd312))
# print 'min12 = {}'.format(min(owd312))
# print 'max12 = {}'.format(max(owd312))
# print 'std12 = {}'.format(numpy.std(owd312))

# """ for owd313"""
# print "number of packets included = {}".format(len(owd313))
# print 'mean13 = {}'.format(numpy.mean(owd313))
# print 'min13 = {}'.format(min(owd313))
# print 'max13 = {}'.format(max(owd313))
# print 'std13 = {}'.format(numpy.std(owd313))


# """ next take the Window3/Window1""" 
# ae1 = numpy.mean(owd313)/numpy.mean(owd311)
# ae2 = numpy.mean(owd313)/numpy.min(owd311)
# ae3 = numpy.mean(owd313)/numpy.max(owd311)

# ae4 = numpy.min(owd313)/numpy.mean(owd311)
# ae5 = numpy.min(owd313)/numpy.min(owd311)
# ae6 = numpy.min(owd313)/numpy.max(owd311)

# ae7 = numpy.max(owd313)/numpy.mean(owd311)
# ae8 = numpy.max(owd313)/numpy.min(owd311)
# ae9 = numpy.max(owd313)/numpy.max(owd311)

# """next take the Window3/Window2"""
# ae10 = numpy.mean(owd313)/numpy.mean(owd312)
# ae11 = numpy.mean(owd313)/numpy.min(owd312)
# ae12 = numpy.mean(owd313)/numpy.max(owd312)

# ae13 = numpy.min(owd313)/numpy.mean(owd312)
# ae14 = numpy.min(owd313)/numpy.min(owd312)
# ae15 = numpy.min(owd313)/numpy.max(owd312)

# ae16 = numpy.max(owd313)/numpy.mean(owd312)
# ae17 = numpy.max(owd313)/numpy.min(owd312)
# ae18 = numpy.max(owd313)/numpy.max(owd312)

# """ min/max window 3"""
# ae19 = numpy.min(owd313)/numpy.max(owd313)

# """standard dev values"""
# ae20 = numpy.std(owd313)/numpy.std(owd311)
# ae21 = numpy.std(owd313)/numpy.std(owd312)
# ae22 = numpy.std(owd311)/numpy.std(owd312)

# """next window1 / window2"""
# ae23 = numpy.mean(owd311)/numpy.mean(owd312)
# ae24 = numpy.mean(owd311)/numpy.min(owd312)
# ae25 = numpy.mean(owd311)/numpy.max(owd312)

# ae26 = numpy.min(owd311)/numpy.mean(owd312)
# ae27 = numpy.min(owd311)/numpy.min(owd312)
# ae28 = numpy.min(owd311)/numpy.max(owd312)

# ae29 = numpy.max(owd311)/numpy.mean(owd312)
# ae30 = numpy.max(owd311)/numpy.min(owd312)
# ae31 = numpy.max(owd311)/numpy.max(owd312)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ae1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ae2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ae3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ae4)+"\n"
# print "min-win3 / min-win1 = "+ str(ae5)+"\n"
# print "min-win3 / max-win1 = "+ str(ae6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ae7)+"\n"
# print "max-win3 / min-win1 = "+ str(ae8)+"\n"
# print "max-win3 / max-win1 = "+ str(ae9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ae10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ae11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ae12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ae13)+"\n"
# print "min-win3 / min-win2 = "+ str(ae14)+"\n"
# print "min-win3 / max-win2 = "+ str(ae15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ae16)+"\n"
# print "max-win3 / min-win2 = "+ str(ae17)+"\n"
# print "max-win3 / max-win2 = "+ str(ae18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ae19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ae20)+"\n"
# print "std-win3 / std-win2 = "+ str(ae21)+"\n"
# print "std-win1 / std-win2 = "+ str(ae22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ae23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ae24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ae25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ae26)+"\n"
# print "min-win1 / min-win2 = "+ str(ae27)+"\n"
# print "min-win1 / max-win2 = "+ str(ae28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ae29)+"\n"
# print "max-win1 / min-win2 = "+ str(ae30)+"\n"
# print "max-win1 / max-win2 = "+ str(ae31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 32"""
# print "Loss # 32"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind321=win_index[31]-300
# ind322=win_index[31]-150
# ind323=win_index[31]

# print "\n index number for loss 32", ind321, ind322, ind323

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd321=[]
# owd322=[]
# owd323=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind321 and nn<=ind322:
# 		owd321.append(iat[nn])
# 	elif nn>ind322 and nn<=ind323:
# 		owd322.append(iat[nn])
# 	elif nn>ind323 and nn<=ind323+150:
# 		owd323.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd321"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd321))
# """ owd321 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd321))
# """owd321 min"""
# print 'min11 = {}'.format(min(owd321))
# """owd321 max"""
# print 'max11 = {}'.format(max(owd321))
# """ owd321 std"""
# print 'std11 = {}'.format(numpy.std(owd321))

# """for owd322"""
# print "number of packets included = {}".format(len(owd322))
# print 'mean12 = {}'.format(numpy.mean(owd322))
# print 'min12 = {}'.format(min(owd322))
# print 'max12 = {}'.format(max(owd322))
# print 'std12 = {}'.format(numpy.std(owd322))

# """ for owd323"""
# print "number of packets included = {}".format(len(owd323))
# print 'mean13 = {}'.format(numpy.mean(owd323))
# print 'min13 = {}'.format(min(owd323))
# print 'max13 = {}'.format(max(owd323))
# print 'std13 = {}'.format(numpy.std(owd323))


# """ next take the Window3/Window1""" 
# af1 = numpy.mean(owd323)/numpy.mean(owd321)
# af2 = numpy.mean(owd323)/numpy.min(owd321)
# af3 = numpy.mean(owd323)/numpy.max(owd321)

# af4 = numpy.min(owd323)/numpy.mean(owd321)
# af5 = numpy.min(owd323)/numpy.min(owd321)
# af6 = numpy.min(owd323)/numpy.max(owd321)

# af7 = numpy.max(owd323)/numpy.mean(owd321)
# af8 = numpy.max(owd323)/numpy.min(owd321)
# af9 = numpy.max(owd323)/numpy.max(owd321)

# """next take the Window3/Window2"""
# af10 = numpy.mean(owd323)/numpy.mean(owd322)
# af11 = numpy.mean(owd323)/numpy.min(owd322)
# af12 = numpy.mean(owd323)/numpy.max(owd322)

# af13 = numpy.min(owd323)/numpy.mean(owd322)
# af14 = numpy.min(owd323)/numpy.min(owd322)
# af15 = numpy.min(owd323)/numpy.max(owd322)

# af16 = numpy.max(owd323)/numpy.mean(owd322)
# af17 = numpy.max(owd323)/numpy.min(owd322)
# af18 = numpy.max(owd323)/numpy.max(owd322)

# """ min/max window 3"""
# af19 = numpy.min(owd323)/numpy.max(owd323)

# """standard dev values"""
# af20 = numpy.std(owd323)/numpy.std(owd321)
# af21 = numpy.std(owd323)/numpy.std(owd322)
# af22 = numpy.std(owd321)/numpy.std(owd322)

# """next window1 / window2"""
# af23 = numpy.mean(owd321)/numpy.mean(owd322)
# af24 = numpy.mean(owd321)/numpy.min(owd322)
# af25 = numpy.mean(owd321)/numpy.max(owd322)

# af26 = numpy.min(owd321)/numpy.mean(owd322)
# af27 = numpy.min(owd321)/numpy.min(owd322)
# af28 = numpy.min(owd321)/numpy.max(owd322)

# af29 = numpy.max(owd321)/numpy.mean(owd322)
# af30 = numpy.max(owd321)/numpy.min(owd322)
# af31 = numpy.max(owd321)/numpy.max(owd322)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(af1)+"\n"
# print "avg-win3 / min-win1 = "+ str(af2)+"\n"
# print "avg-win3 / max-win1 = "+ str(af3)+"\n"

# print "min-win3 / avg-win1 = "+ str(af4)+"\n"
# print "min-win3 / min-win1 = "+ str(af5)+"\n"
# print "min-win3 / max-win1 = "+ str(af6)+"\n"

# print "max-win3 / avg-win1 = "+ str(af7)+"\n"
# print "max-win3 / min-win1 = "+ str(af8)+"\n"
# print "max-win3 / max-win1 = "+ str(af9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(af10)+"\n"
# print "avg-win3 / min-win2 = "+ str(af11)+"\n"
# print "avg-win3 / max-win2 = "+ str(af12)+"\n"

# print "min-win3 / avg-win2 = "+ str(af13)+"\n"
# print "min-win3 / min-win2 = "+ str(af14)+"\n"
# print "min-win3 / max-win2 = "+ str(af15)+"\n"

# print "max-win3 / avg-win2 = "+ str(af16)+"\n"
# print "max-win3 / min-win2 = "+ str(af17)+"\n"
# print "max-win3 / max-win2 = "+ str(af18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(af19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(af20)+"\n"
# print "std-win3 / std-win2 = "+ str(af21)+"\n"
# print "std-win1 / std-win2 = "+ str(af22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(af23)+"\n"
# print "avg-win1 / min-win2 = "+ str(af24)+"\n"
# print "avg-win1 / max-win2 = "+ str(af25)+"\n"

# print "min-win1 / avg-win2 = "+ str(af26)+"\n"
# print "min-win1 / min-win2 = "+ str(af27)+"\n"
# print "min-win1 / max-win2 = "+ str(af28)+"\n"

# print "max-win1 / avg-win2 = "+ str(af29)+"\n"
# print "max-win1 / min-win2 = "+ str(af30)+"\n"
# print "max-win1 / max-win2 = "+ str(af31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 33"""
# print "Loss # 33"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind331=win_index[32]-300
# ind332=win_index[32]-150
# ind333=win_index[32]

# print "\n index number for loss 33", ind331, ind332, ind333

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd331=[]
# owd332=[]
# owd333=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind331 and nn<=ind332:
# 		owd331.append(iat[nn])
# 	elif nn>ind332 and nn<=ind333:
# 		owd332.append(iat[nn])
# 	elif nn>ind333 and nn<=ind333+150:
# 		owd333.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd331"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd331))
# """ owd331 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd331))
# """owd331 min"""
# print 'min11 = {}'.format(min(owd331))
# """owd331 max"""
# print 'max11 = {}'.format(max(owd331))
# """ owd331 std"""
# print 'std11 = {}'.format(numpy.std(owd331))

# """for owd332"""
# print "number of packets included = {}".format(len(owd332))
# print 'mean12 = {}'.format(numpy.mean(owd332))
# print 'min12 = {}'.format(min(owd332))
# print 'max12 = {}'.format(max(owd332))
# print 'std12 = {}'.format(numpy.std(owd332))

# """ for owd333"""
# print "number of packets included = {}".format(len(owd333))
# print 'mean13 = {}'.format(numpy.mean(owd333))
# print 'min13 = {}'.format(min(owd333))
# print 'max13 = {}'.format(max(owd333))
# print 'std13 = {}'.format(numpy.std(owd333))


# """ next take the Window3/Window1""" 
# ag1 = numpy.mean(owd333)/numpy.mean(owd331)
# ag2 = numpy.mean(owd333)/numpy.min(owd331)
# ag3 = numpy.mean(owd333)/numpy.max(owd331)

# ag4 = numpy.min(owd333)/numpy.mean(owd331)
# ag5 = numpy.min(owd333)/numpy.min(owd331)
# ag6 = numpy.min(owd333)/numpy.max(owd331)

# ag7 = numpy.max(owd333)/numpy.mean(owd331)
# ag8 = numpy.max(owd333)/numpy.min(owd331)
# ag9 = numpy.max(owd333)/numpy.max(owd331)

# """next take the Window3/Window2"""
# ag10 = numpy.mean(owd333)/numpy.mean(owd332)
# ag11 = numpy.mean(owd333)/numpy.min(owd332)
# ag12 = numpy.mean(owd333)/numpy.max(owd332)

# ag13 = numpy.min(owd333)/numpy.mean(owd332)
# ag14 = numpy.min(owd333)/numpy.min(owd332)
# ag15 = numpy.min(owd333)/numpy.max(owd332)

# ag16 = numpy.max(owd333)/numpy.mean(owd332)
# ag17 = numpy.max(owd333)/numpy.min(owd332)
# ag18 = numpy.max(owd333)/numpy.max(owd332)

# """ min/max window 3"""
# ag19 = numpy.min(owd333)/numpy.max(owd333)

# """standard dev values"""
# ag20 = numpy.std(owd333)/numpy.std(owd331)
# ag21 = numpy.std(owd333)/numpy.std(owd332)
# ag22 = numpy.std(owd331)/numpy.std(owd332)

# """next window1 / window2"""
# ag23 = numpy.mean(owd331)/numpy.mean(owd332)
# ag24 = numpy.mean(owd331)/numpy.min(owd332)
# ag25 = numpy.mean(owd331)/numpy.max(owd332)

# ag26 = numpy.min(owd331)/numpy.mean(owd332)
# ag27 = numpy.min(owd331)/numpy.min(owd332)
# ag28 = numpy.min(owd331)/numpy.max(owd332)

# ag29 = numpy.max(owd331)/numpy.mean(owd332)
# ag30 = numpy.max(owd331)/numpy.min(owd332)
# ag31 = numpy.max(owd331)/numpy.max(owd332)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ag1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ag2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ag3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ag4)+"\n"
# print "min-win3 / min-win1 = "+ str(ag5)+"\n"
# print "min-win3 / max-win1 = "+ str(ag6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ag7)+"\n"
# print "max-win3 / min-win1 = "+ str(ag8)+"\n"
# print "max-win3 / max-win1 = "+ str(ag9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ag10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ag11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ag12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ag13)+"\n"
# print "min-win3 / min-win2 = "+ str(ag14)+"\n"
# print "min-win3 / max-win2 = "+ str(ag15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ag16)+"\n"
# print "max-win3 / min-win2 = "+ str(ag17)+"\n"
# print "max-win3 / max-win2 = "+ str(ag18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ag19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ag20)+"\n"
# print "std-win3 / std-win2 = "+ str(ag21)+"\n"
# print "std-win1 / std-win2 = "+ str(ag22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ag23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ag24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ag25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ag26)+"\n"
# print "min-win1 / min-win2 = "+ str(ag27)+"\n"
# print "min-win1 / max-win2 = "+ str(ag28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ag29)+"\n"
# print "max-win1 / min-win2 = "+ str(ag30)+"\n"
# print "max-win1 / max-win2 = "+ str(ag31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 34"""
# print "Loss # 34"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind341=win_index[33]-300
# ind342=win_index[33]-150
# ind343=win_index[33]

# print "\n index number for loss 34", ind341, ind342, ind343

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd341=[]
# owd342=[]
# owd343=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind341 and nn<=ind342:
# 		owd341.append(iat[nn])
# 	elif nn>ind342 and nn<=ind343:
# 		owd342.append(iat[nn])
# 	elif nn>ind343 and nn<=ind343+150:
# 		owd343.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd341"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd341))
# """ owd341 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd341))
# """owd341 min"""
# print 'min11 = {}'.format(min(owd341))
# """owd341 max"""
# print 'max11 = {}'.format(max(owd341))
# """ owd341 std"""
# print 'std11 = {}'.format(numpy.std(owd341))

# """for owd342"""
# print "number of packets included = {}".format(len(owd342))
# print 'mean12 = {}'.format(numpy.mean(owd342))
# print 'min12 = {}'.format(min(owd342))
# print 'max12 = {}'.format(max(owd342))
# print 'std12 = {}'.format(numpy.std(owd342))

# """ for owd343"""
# print "number of packets included = {}".format(len(owd343))
# print 'mean13 = {}'.format(numpy.mean(owd343))
# print 'min13 = {}'.format(min(owd343))
# print 'max13 = {}'.format(max(owd343))
# print 'std13 = {}'.format(numpy.std(owd343))


# """ next take the Window3/Window1""" 
# ah1 = numpy.mean(owd343)/numpy.mean(owd341)
# ah2 = numpy.mean(owd343)/numpy.min(owd341)
# ah3 = numpy.mean(owd343)/numpy.max(owd341)

# ah4 = numpy.min(owd343)/numpy.mean(owd341)
# ah5 = numpy.min(owd343)/numpy.min(owd341)
# ah6 = numpy.min(owd343)/numpy.max(owd341)

# ah7 = numpy.max(owd343)/numpy.mean(owd341)
# ah8 = numpy.max(owd343)/numpy.min(owd341)
# ah9 = numpy.max(owd343)/numpy.max(owd341)

# """next take the Window3/Window2"""
# ah10 = numpy.mean(owd343)/numpy.mean(owd342)
# ah11 = numpy.mean(owd343)/numpy.min(owd342)
# ah12 = numpy.mean(owd343)/numpy.max(owd342)

# ah13 = numpy.min(owd343)/numpy.mean(owd342)
# ah14 = numpy.min(owd343)/numpy.min(owd342)
# ah15 = numpy.min(owd343)/numpy.max(owd342)

# ah16 = numpy.max(owd343)/numpy.mean(owd342)
# ah17 = numpy.max(owd343)/numpy.min(owd342)
# ah18 = numpy.max(owd343)/numpy.max(owd342)

# """ min/max window 3"""
# ah19 = numpy.min(owd343)/numpy.max(owd343)

# """standard dev values"""
# ah20 = numpy.std(owd343)/numpy.std(owd341)
# ah21 = numpy.std(owd343)/numpy.std(owd342)
# ah22 = numpy.std(owd341)/numpy.std(owd342)

# """next window1 / window2"""
# ah23 = numpy.mean(owd341)/numpy.mean(owd342)
# ah24 = numpy.mean(owd341)/numpy.min(owd342)
# ah25 = numpy.mean(owd341)/numpy.max(owd342)

# ah26 = numpy.min(owd341)/numpy.mean(owd342)
# ah27 = numpy.min(owd341)/numpy.min(owd342)
# ah28 = numpy.min(owd341)/numpy.max(owd342)

# ah29 = numpy.max(owd341)/numpy.mean(owd342)
# ah30 = numpy.max(owd341)/numpy.min(owd342)
# ah31 = numpy.max(owd341)/numpy.max(owd342)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ah1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ah2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ah3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ah4)+"\n"
# print "min-win3 / min-win1 = "+ str(ah5)+"\n"
# print "min-win3 / max-win1 = "+ str(ah6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ah7)+"\n"
# print "max-win3 / min-win1 = "+ str(ah8)+"\n"
# print "max-win3 / max-win1 = "+ str(ah9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ah10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ah11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ah12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ah13)+"\n"
# print "min-win3 / min-win2 = "+ str(ah14)+"\n"
# print "min-win3 / max-win2 = "+ str(ah15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ah16)+"\n"
# print "max-win3 / min-win2 = "+ str(ah17)+"\n"
# print "max-win3 / max-win2 = "+ str(ah18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ah19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ah20)+"\n"
# print "std-win3 / std-win2 = "+ str(ah21)+"\n"
# print "std-win1 / std-win2 = "+ str(ah22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ah23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ah24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ah25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ah26)+"\n"
# print "min-win1 / min-win2 = "+ str(ah27)+"\n"
# print "min-win1 / max-win2 = "+ str(ah28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ah29)+"\n"
# print "max-win1 / min-win2 = "+ str(ah30)+"\n"
# print "max-win1 / max-win2 = "+ str(ah31)+"\n"

# print "#################################################"



# ########################################

# """LOSS # 35"""
# print "Loss # 35"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind351=win_index[34]-300
# ind352=win_index[34]-150
# ind353=win_index[34]

# print "\n index number for loss 35", ind351, ind352, ind353

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd351=[]
# owd352=[]
# owd353=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind351 and nn<=ind352:
# 		owd351.append(iat[nn])
# 	elif nn>ind352 and nn<=ind353:
# 		owd352.append(iat[nn])
# 	elif nn>ind353 and nn<=ind353+150:
# 		owd353.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd351"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd351))
# """ owd351 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd351))
# """owd351 min"""
# print 'min11 = {}'.format(min(owd351))
# """owd351 max"""
# print 'max11 = {}'.format(max(owd351))
# """ owd351 std"""
# print 'std11 = {}'.format(numpy.std(owd351))

# """for owd352"""
# print "number of packets included = {}".format(len(owd352))
# print 'mean12 = {}'.format(numpy.mean(owd352))
# print 'min12 = {}'.format(min(owd352))
# print 'max12 = {}'.format(max(owd352))
# print 'std12 = {}'.format(numpy.std(owd352))

# """ for owd353"""
# print "number of packets included = {}".format(len(owd353))
# print 'mean13 = {}'.format(numpy.mean(owd353))
# print 'min13 = {}'.format(min(owd353))
# print 'max13 = {}'.format(max(owd353))
# print 'std13 = {}'.format(numpy.std(owd353))


# """ next take the Window3/Window1""" 
# ai1 = numpy.mean(owd353)/numpy.mean(owd351)
# ai2 = numpy.mean(owd353)/numpy.min(owd351)
# ai3 = numpy.mean(owd353)/numpy.max(owd351)

# ai4 = numpy.min(owd353)/numpy.mean(owd351)
# ai5 = numpy.min(owd353)/numpy.min(owd351)
# ai6 = numpy.min(owd353)/numpy.max(owd351)

# ai7 = numpy.max(owd353)/numpy.mean(owd351)
# ai8 = numpy.max(owd353)/numpy.min(owd351)
# ai9 = numpy.max(owd353)/numpy.max(owd351)

# """next take the Window3/Window2"""
# ai10 = numpy.mean(owd353)/numpy.mean(owd352)
# ai11 = numpy.mean(owd353)/numpy.min(owd352)
# ai12 = numpy.mean(owd353)/numpy.max(owd352)

# ai13 = numpy.min(owd353)/numpy.mean(owd352)
# ai14 = numpy.min(owd353)/numpy.min(owd352)
# ai15 = numpy.min(owd353)/numpy.max(owd352)

# ai16 = numpy.max(owd353)/numpy.mean(owd352)
# ai17 = numpy.max(owd353)/numpy.min(owd352)
# ai18 = numpy.max(owd353)/numpy.max(owd352)

# """ min/max window 3"""
# ai19 = numpy.min(owd353)/numpy.max(owd353)

# """standard dev values"""
# ai20 = numpy.std(owd353)/numpy.std(owd351)
# ai21 = numpy.std(owd353)/numpy.std(owd352)
# ai22 = numpy.std(owd351)/numpy.std(owd352)

# """next window1 / window2"""
# ai23 = numpy.mean(owd351)/numpy.mean(owd352)
# ai24 = numpy.mean(owd351)/numpy.min(owd352)
# ai25 = numpy.mean(owd351)/numpy.max(owd352)

# ai26 = numpy.min(owd351)/numpy.mean(owd352)
# ai27 = numpy.min(owd351)/numpy.min(owd352)
# ai28 = numpy.min(owd351)/numpy.max(owd352)

# ai29 = numpy.max(owd351)/numpy.mean(owd352)
# ai30 = numpy.max(owd351)/numpy.min(owd352)
# ai31 = numpy.max(owd351)/numpy.max(owd352)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ai1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ai2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ai3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ai4)+"\n"
# print "min-win3 / min-win1 = "+ str(ai5)+"\n"
# print "min-win3 / max-win1 = "+ str(ai6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ai7)+"\n"
# print "max-win3 / min-win1 = "+ str(ai8)+"\n"
# print "max-win3 / max-win1 = "+ str(ai9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ai10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ai11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ai12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ai13)+"\n"
# print "min-win3 / min-win2 = "+ str(ai14)+"\n"
# print "min-win3 / max-win2 = "+ str(ai15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ai16)+"\n"
# print "max-win3 / min-win2 = "+ str(ai17)+"\n"
# print "max-win3 / max-win2 = "+ str(ai18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ai19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ai20)+"\n"
# print "std-win3 / std-win2 = "+ str(ai21)+"\n"
# print "std-win1 / std-win2 = "+ str(ai22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ai23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ai24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ai25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ai26)+"\n"
# print "min-win1 / min-win2 = "+ str(ai27)+"\n"
# print "min-win1 / max-win2 = "+ str(ai28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ai29)+"\n"
# print "max-win1 / min-win2 = "+ str(ai30)+"\n"
# print "max-win1 / max-win2 = "+ str(ai31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 36"""
# print "Loss # 36"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind361=win_index[35]-300
# ind362=win_index[35]-150
# ind363=win_index[35]

# print "\n index number for loss 36", ind361, ind362, ind363

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd361=[]
# owd362=[]
# owd363=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind361 and nn<=ind362:
# 		owd361.append(iat[nn])
# 	elif nn>ind362 and nn<=ind363:
# 		owd362.append(iat[nn])
# 	elif nn>ind363 and nn<=ind363+150:
# 		owd363.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd361"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd361))
# """ owd361 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd361))
# """owd361 min"""
# print 'min11 = {}'.format(min(owd361))
# """owd361 max"""
# print 'max11 = {}'.format(max(owd361))
# """ owd361 std"""
# print 'std11 = {}'.format(numpy.std(owd361))

# """for owd362"""
# print "number of packets included = {}".format(len(owd362))
# print 'mean12 = {}'.format(numpy.mean(owd362))
# print 'min12 = {}'.format(min(owd362))
# print 'max12 = {}'.format(max(owd362))
# print 'std12 = {}'.format(numpy.std(owd362))

# """ for owd363"""
# print "number of packets included = {}".format(len(owd363))
# print 'mean13 = {}'.format(numpy.mean(owd363))
# print 'min13 = {}'.format(min(owd363))
# print 'max13 = {}'.format(max(owd363))
# print 'std13 = {}'.format(numpy.std(owd363))


# """ next take the Window3/Window1""" 
# aj1 = numpy.mean(owd363)/numpy.mean(owd361)
# aj2 = numpy.mean(owd363)/numpy.min(owd361)
# aj3 = numpy.mean(owd363)/numpy.max(owd361)

# aj4 = numpy.min(owd363)/numpy.mean(owd361)
# aj5 = numpy.min(owd363)/numpy.min(owd361)
# aj6 = numpy.min(owd363)/numpy.max(owd361)

# aj7 = numpy.max(owd363)/numpy.mean(owd361)
# aj8 = numpy.max(owd363)/numpy.min(owd361)
# aj9 = numpy.max(owd363)/numpy.max(owd361)

# """next take the Window3/Window2"""
# aj10 = numpy.mean(owd363)/numpy.mean(owd362)
# aj11 = numpy.mean(owd363)/numpy.min(owd362)
# aj12 = numpy.mean(owd363)/numpy.max(owd362)

# aj13 = numpy.min(owd363)/numpy.mean(owd362)
# aj14 = numpy.min(owd363)/numpy.min(owd362)
# aj15 = numpy.min(owd363)/numpy.max(owd362)

# aj16 = numpy.max(owd363)/numpy.mean(owd362)
# aj17 = numpy.max(owd363)/numpy.min(owd362)
# aj18 = numpy.max(owd363)/numpy.max(owd362)

# """ min/max window 3"""
# aj19 = numpy.min(owd363)/numpy.max(owd363)

# """standard dev values"""
# aj20 = numpy.std(owd363)/numpy.std(owd361)
# aj21 = numpy.std(owd363)/numpy.std(owd362)
# aj22 = numpy.std(owd361)/numpy.std(owd362)

# """next window1 / window2"""
# aj23 = numpy.mean(owd361)/numpy.mean(owd362)
# aj24 = numpy.mean(owd361)/numpy.min(owd362)
# aj25 = numpy.mean(owd361)/numpy.max(owd362)

# aj26 = numpy.min(owd361)/numpy.mean(owd362)
# aj27 = numpy.min(owd361)/numpy.min(owd362)
# aj28 = numpy.min(owd361)/numpy.max(owd362)

# aj29 = numpy.max(owd361)/numpy.mean(owd362)
# aj30 = numpy.max(owd361)/numpy.min(owd362)
# aj31 = numpy.max(owd361)/numpy.max(owd362)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(aj1)+"\n"
# print "avg-win3 / min-win1 = "+ str(aj2)+"\n"
# print "avg-win3 / max-win1 = "+ str(aj3)+"\n"

# print "min-win3 / avg-win1 = "+ str(aj4)+"\n"
# print "min-win3 / min-win1 = "+ str(aj5)+"\n"
# print "min-win3 / max-win1 = "+ str(aj6)+"\n"

# print "max-win3 / avg-win1 = "+ str(aj7)+"\n"
# print "max-win3 / min-win1 = "+ str(aj8)+"\n"
# print "max-win3 / max-win1 = "+ str(aj9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(aj10)+"\n"
# print "avg-win3 / min-win2 = "+ str(aj11)+"\n"
# print "avg-win3 / max-win2 = "+ str(aj12)+"\n"

# print "min-win3 / avg-win2 = "+ str(aj13)+"\n"
# print "min-win3 / min-win2 = "+ str(aj14)+"\n"
# print "min-win3 / max-win2 = "+ str(aj15)+"\n"

# print "max-win3 / avg-win2 = "+ str(aj16)+"\n"
# print "max-win3 / min-win2 = "+ str(aj17)+"\n"
# print "max-win3 / max-win2 = "+ str(aj18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(aj19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(aj20)+"\n"
# print "std-win3 / std-win2 = "+ str(aj21)+"\n"
# print "std-win1 / std-win2 = "+ str(aj22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(aj23)+"\n"
# print "avg-win1 / min-win2 = "+ str(aj24)+"\n"
# print "avg-win1 / max-win2 = "+ str(aj25)+"\n"

# print "min-win1 / avg-win2 = "+ str(aj26)+"\n"
# print "min-win1 / min-win2 = "+ str(aj27)+"\n"
# print "min-win1 / max-win2 = "+ str(aj28)+"\n"

# print "max-win1 / avg-win2 = "+ str(aj29)+"\n"
# print "max-win1 / min-win2 = "+ str(aj30)+"\n"
# print "max-win1 / max-win2 = "+ str(aj31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 37"""
# print "Loss # 37"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind371=win_index[36]-300
# ind372=win_index[36]-150
# ind373=win_index[36]

# print "\n index number for loss 37", ind371, ind372, ind373

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd371=[]
# owd372=[]
# owd373=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind371 and nn<=ind372:
# 		owd371.append(iat[nn])
# 	elif nn>ind372 and nn<=ind373:
# 		owd372.append(iat[nn])
# 	elif nn>ind373 and nn<=ind373+150:
# 		owd373.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd371"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd371))
# """ owd371 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd371))
# """owd371 min"""
# print 'min11 = {}'.format(min(owd371))
# """owd371 max"""
# print 'max11 = {}'.format(max(owd371))
# """ owd371 std"""
# print 'std11 = {}'.format(numpy.std(owd371))

# """for owd372"""
# print "number of packets included = {}".format(len(owd372))
# print 'mean12 = {}'.format(numpy.mean(owd372))
# print 'min12 = {}'.format(min(owd372))
# print 'max12 = {}'.format(max(owd372))
# print 'std12 = {}'.format(numpy.std(owd372))

# """ for owd373"""
# print "number of packets included = {}".format(len(owd373))
# print 'mean13 = {}'.format(numpy.mean(owd373))
# print 'min13 = {}'.format(min(owd373))
# print 'max13 = {}'.format(max(owd373))
# print 'std13 = {}'.format(numpy.std(owd373))


# """ next take the Window3/Window1""" 
# ak1 = numpy.mean(owd373)/numpy.mean(owd371)
# ak2 = numpy.mean(owd373)/numpy.min(owd371)
# ak3 = numpy.mean(owd373)/numpy.max(owd371)

# ak4 = numpy.min(owd373)/numpy.mean(owd371)
# ak5 = numpy.min(owd373)/numpy.min(owd371)
# ak6 = numpy.min(owd373)/numpy.max(owd371)

# ak7 = numpy.max(owd373)/numpy.mean(owd371)
# ak8 = numpy.max(owd373)/numpy.min(owd371)
# ak9 = numpy.max(owd373)/numpy.max(owd371)

# """next take the Window3/Window2"""
# ak10 = numpy.mean(owd373)/numpy.mean(owd372)
# ak11 = numpy.mean(owd373)/numpy.min(owd372)
# ak12 = numpy.mean(owd373)/numpy.max(owd372)

# ak13 = numpy.min(owd373)/numpy.mean(owd372)
# ak14 = numpy.min(owd373)/numpy.min(owd372)
# ak15 = numpy.min(owd373)/numpy.max(owd372)

# ak16 = numpy.max(owd373)/numpy.mean(owd372)
# ak17 = numpy.max(owd373)/numpy.min(owd372)
# ak18 = numpy.max(owd373)/numpy.max(owd372)

# """ min/max window 3"""
# ak19 = numpy.min(owd373)/numpy.max(owd373)

# """standard dev values"""
# ak20 = numpy.std(owd373)/numpy.std(owd371)
# ak21 = numpy.std(owd373)/numpy.std(owd372)
# ak22 = numpy.std(owd371)/numpy.std(owd372)

# """next window1 / window2"""
# ak23 = numpy.mean(owd371)/numpy.mean(owd372)
# ak24 = numpy.mean(owd371)/numpy.min(owd372)
# ak25 = numpy.mean(owd371)/numpy.max(owd372)

# ak26 = numpy.min(owd371)/numpy.mean(owd372)
# ak27 = numpy.min(owd371)/numpy.min(owd372)
# ak28 = numpy.min(owd371)/numpy.max(owd372)

# ak29 = numpy.max(owd371)/numpy.mean(owd372)
# ak30 = numpy.max(owd371)/numpy.min(owd372)
# ak31 = numpy.max(owd371)/numpy.max(owd372)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ak1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ak2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ak3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ak4)+"\n"
# print "min-win3 / min-win1 = "+ str(ak5)+"\n"
# print "min-win3 / max-win1 = "+ str(ak6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ak7)+"\n"
# print "max-win3 / min-win1 = "+ str(ak8)+"\n"
# print "max-win3 / max-win1 = "+ str(ak9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ak10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ak11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ak12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ak13)+"\n"
# print "min-win3 / min-win2 = "+ str(ak14)+"\n"
# print "min-win3 / max-win2 = "+ str(ak15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ak16)+"\n"
# print "max-win3 / min-win2 = "+ str(ak17)+"\n"
# print "max-win3 / max-win2 = "+ str(ak18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ak19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ak20)+"\n"
# print "std-win3 / std-win2 = "+ str(ak21)+"\n"
# print "std-win1 / std-win2 = "+ str(ak22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ak23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ak24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ak25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ak26)+"\n"
# print "min-win1 / min-win2 = "+ str(ak27)+"\n"
# print "min-win1 / max-win2 = "+ str(ak28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ak29)+"\n"
# print "max-win1 / min-win2 = "+ str(ak30)+"\n"
# print "max-win1 / max-win2 = "+ str(ak31)+"\n"

# print "#################################################"


# ########################################

# """LOSS # 38"""
# print "Loss # 38"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind381=win_index[37]-300
# ind382=win_index[37]-150
# ind383=win_index[37]

# print "\n index number for loss 38", ind381, ind382, ind383

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd381=[]
# owd382=[]
# owd383=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind381 and nn<=ind382:
# 		owd381.append(iat[nn])
# 	elif nn>ind382 and nn<=ind383:
# 		owd382.append(iat[nn])
# 	elif nn>ind383 and nn<=ind383+150:
# 		owd383.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd381"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd381))
# """ owd381 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd381))
# """owd381 min"""
# print 'min11 = {}'.format(min(owd381))
# """owd381 max"""
# print 'max11 = {}'.format(max(owd381))
# """ owd381 std"""
# print 'std11 = {}'.format(numpy.std(owd381))

# """for owd382"""
# print "number of packets included = {}".format(len(owd382))
# print 'mean12 = {}'.format(numpy.mean(owd382))
# print 'min12 = {}'.format(min(owd382))
# print 'max12 = {}'.format(max(owd382))
# print 'std12 = {}'.format(numpy.std(owd382))

# """ for owd383"""
# print "number of packets included = {}".format(len(owd383))
# print 'mean13 = {}'.format(numpy.mean(owd383))
# print 'min13 = {}'.format(min(owd383))
# print 'max13 = {}'.format(max(owd383))
# print 'std13 = {}'.format(numpy.std(owd383))


# """ next take the Window3/Window1""" 
# al1 = numpy.mean(owd383)/numpy.mean(owd381)
# al2 = numpy.mean(owd383)/numpy.min(owd381)
# al3 = numpy.mean(owd383)/numpy.max(owd381)

# al4 = numpy.min(owd383)/numpy.mean(owd381)
# al5 = numpy.min(owd383)/numpy.min(owd381)
# al6 = numpy.min(owd383)/numpy.max(owd381)

# al7 = numpy.max(owd383)/numpy.mean(owd381)
# al8 = numpy.max(owd383)/numpy.min(owd381)
# al9 = numpy.max(owd383)/numpy.max(owd381)

# """next take the Window3/Window2"""
# al10 = numpy.mean(owd383)/numpy.mean(owd382)
# al11 = numpy.mean(owd383)/numpy.min(owd382)
# al12 = numpy.mean(owd383)/numpy.max(owd382)

# al13 = numpy.min(owd383)/numpy.mean(owd382)
# al14 = numpy.min(owd383)/numpy.min(owd382)
# al15 = numpy.min(owd383)/numpy.max(owd382)

# al16 = numpy.max(owd383)/numpy.mean(owd382)
# al17 = numpy.max(owd383)/numpy.min(owd382)
# al18 = numpy.max(owd383)/numpy.max(owd382)

# """ min/max window 3"""
# al19 = numpy.min(owd383)/numpy.max(owd383)

# """standard dev values"""
# al20 = numpy.std(owd383)/numpy.std(owd381)
# al21 = numpy.std(owd383)/numpy.std(owd382)
# al22 = numpy.std(owd381)/numpy.std(owd382)

# """next window1 / window2"""
# al23 = numpy.mean(owd381)/numpy.mean(owd382)
# al24 = numpy.mean(owd381)/numpy.min(owd382)
# al25 = numpy.mean(owd381)/numpy.max(owd382)

# al26 = numpy.min(owd381)/numpy.mean(owd382)
# al27 = numpy.min(owd381)/numpy.min(owd382)
# al28 = numpy.min(owd381)/numpy.max(owd382)

# al29 = numpy.max(owd381)/numpy.mean(owd382)
# al30 = numpy.max(owd381)/numpy.min(owd382)
# al31 = numpy.max(owd381)/numpy.max(owd382)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(al1)+"\n"
# print "avg-win3 / min-win1 = "+ str(al2)+"\n"
# print "avg-win3 / max-win1 = "+ str(al3)+"\n"

# print "min-win3 / avg-win1 = "+ str(al4)+"\n"
# print "min-win3 / min-win1 = "+ str(al5)+"\n"
# print "min-win3 / max-win1 = "+ str(al6)+"\n"

# print "max-win3 / avg-win1 = "+ str(al7)+"\n"
# print "max-win3 / min-win1 = "+ str(al8)+"\n"
# print "max-win3 / max-win1 = "+ str(al9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(al10)+"\n"
# print "avg-win3 / min-win2 = "+ str(al11)+"\n"
# print "avg-win3 / max-win2 = "+ str(al12)+"\n"

# print "min-win3 / avg-win2 = "+ str(al13)+"\n"
# print "min-win3 / min-win2 = "+ str(al14)+"\n"
# print "min-win3 / max-win2 = "+ str(al15)+"\n"

# print "max-win3 / avg-win2 = "+ str(al16)+"\n"
# print "max-win3 / min-win2 = "+ str(al17)+"\n"
# print "max-win3 / max-win2 = "+ str(al18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(al19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(al20)+"\n"
# print "std-win3 / std-win2 = "+ str(al21)+"\n"
# print "std-win1 / std-win2 = "+ str(al22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(al23)+"\n"
# print "avg-win1 / min-win2 = "+ str(al24)+"\n"
# print "avg-win1 / max-win2 = "+ str(al25)+"\n"

# print "min-win1 / avg-win2 = "+ str(al26)+"\n"
# print "min-win1 / min-win2 = "+ str(al27)+"\n"
# print "min-win1 / max-win2 = "+ str(al28)+"\n"

# print "max-win1 / avg-win2 = "+ str(al29)+"\n"
# print "max-win1 / min-win2 = "+ str(al30)+"\n"
# print "max-win1 / max-win2 = "+ str(al31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 39"""
# print "Loss # 39"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind391=win_index[38]-300
# ind392=win_index[38]-150
# ind393=win_index[38]

# print "\n index number for loss 39", ind391, ind392, ind393

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd391=[]
# owd392=[]
# owd393=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind391 and nn<=ind392:
# 		owd391.append(iat[nn])
# 	elif nn>ind392 and nn<=ind393:
# 		owd392.append(iat[nn])
# 	elif nn>ind393 and nn<=ind393+150:
# 		owd393.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd391"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd391))
# """ owd391 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd391))
# """owd391 min"""
# print 'min11 = {}'.format(min(owd391))
# """owd391 max"""
# print 'max11 = {}'.format(max(owd391))
# """ owd391 std"""
# print 'std11 = {}'.format(numpy.std(owd391))

# """for owd392"""
# print "number of packets included = {}".format(len(owd392))
# print 'mean12 = {}'.format(numpy.mean(owd392))
# print 'min12 = {}'.format(min(owd392))
# print 'max12 = {}'.format(max(owd392))
# print 'std12 = {}'.format(numpy.std(owd392))

# """ for owd393"""
# print "number of packets included = {}".format(len(owd393))
# print 'mean13 = {}'.format(numpy.mean(owd393))
# print 'min13 = {}'.format(min(owd393))
# print 'max13 = {}'.format(max(owd393))
# print 'std13 = {}'.format(numpy.std(owd393))


# """ next take the Window3/Window1""" 
# am1 = numpy.mean(owd393)/numpy.mean(owd391)
# am2 = numpy.mean(owd393)/numpy.min(owd391)
# am3 = numpy.mean(owd393)/numpy.max(owd391)

# am4 = numpy.min(owd393)/numpy.mean(owd391)
# am5 = numpy.min(owd393)/numpy.min(owd391)
# am6 = numpy.min(owd393)/numpy.max(owd391)

# am7 = numpy.max(owd393)/numpy.mean(owd391)
# am8 = numpy.max(owd393)/numpy.min(owd391)
# am9 = numpy.max(owd393)/numpy.max(owd391)

# """next take the Window3/Window2"""
# am10 = numpy.mean(owd393)/numpy.mean(owd392)
# am11 = numpy.mean(owd393)/numpy.min(owd392)
# am12 = numpy.mean(owd393)/numpy.max(owd392)

# am13 = numpy.min(owd393)/numpy.mean(owd392)
# am14 = numpy.min(owd393)/numpy.min(owd392)
# am15 = numpy.min(owd393)/numpy.max(owd392)

# am16 = numpy.max(owd393)/numpy.mean(owd392)
# am17 = numpy.max(owd393)/numpy.min(owd392)
# am18 = numpy.max(owd393)/numpy.max(owd392)

# """ min/max window 3"""
# am19 = numpy.min(owd393)/numpy.max(owd393)

# """standard dev values"""
# am20 = numpy.std(owd393)/numpy.std(owd391)
# am21 = numpy.std(owd393)/numpy.std(owd392)
# am22 = numpy.std(owd391)/numpy.std(owd392)

# """next window1 / window2"""
# am23 = numpy.mean(owd391)/numpy.mean(owd392)
# am24 = numpy.mean(owd391)/numpy.min(owd392)
# am25 = numpy.mean(owd391)/numpy.max(owd392)

# am26 = numpy.min(owd391)/numpy.mean(owd392)
# am27 = numpy.min(owd391)/numpy.min(owd392)
# am28 = numpy.min(owd391)/numpy.max(owd392)

# am29 = numpy.max(owd391)/numpy.mean(owd392)
# am30 = numpy.max(owd391)/numpy.min(owd392)
# am31 = numpy.max(owd391)/numpy.max(owd392)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(am1)+"\n"
# print "avg-win3 / min-win1 = "+ str(am2)+"\n"
# print "avg-win3 / max-win1 = "+ str(am3)+"\n"

# print "min-win3 / avg-win1 = "+ str(am4)+"\n"
# print "min-win3 / min-win1 = "+ str(am5)+"\n"
# print "min-win3 / max-win1 = "+ str(am6)+"\n"

# print "max-win3 / avg-win1 = "+ str(am7)+"\n"
# print "max-win3 / min-win1 = "+ str(am8)+"\n"
# print "max-win3 / max-win1 = "+ str(am9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(am10)+"\n"
# print "avg-win3 / min-win2 = "+ str(am11)+"\n"
# print "avg-win3 / max-win2 = "+ str(am12)+"\n"

# print "min-win3 / avg-win2 = "+ str(am13)+"\n"
# print "min-win3 / min-win2 = "+ str(am14)+"\n"
# print "min-win3 / max-win2 = "+ str(am15)+"\n"

# print "max-win3 / avg-win2 = "+ str(am16)+"\n"
# print "max-win3 / min-win2 = "+ str(am17)+"\n"
# print "max-win3 / max-win2 = "+ str(am18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(am19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(am20)+"\n"
# print "std-win3 / std-win2 = "+ str(am21)+"\n"
# print "std-win1 / std-win2 = "+ str(am22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(am23)+"\n"
# print "avg-win1 / min-win2 = "+ str(am24)+"\n"
# print "avg-win1 / max-win2 = "+ str(am25)+"\n"

# print "min-win1 / avg-win2 = "+ str(am26)+"\n"
# print "min-win1 / min-win2 = "+ str(am27)+"\n"
# print "min-win1 / max-win2 = "+ str(am28)+"\n"

# print "max-win1 / avg-win2 = "+ str(am29)+"\n"
# print "max-win1 / min-win2 = "+ str(am30)+"\n"
# print "max-win1 / max-win2 = "+ str(am31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 40"""
# print "Loss # 40"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind401=win_index[39]-300
# ind402=win_index[39]-150
# ind403=win_index[39]

# print "\n index number for loss 40", ind401, ind402, ind403

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd401=[]
# owd402=[]
# owd403=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind401 and nn<=ind402:
# 		owd401.append(iat[nn])
# 	elif nn>ind402 and nn<=ind403:
# 		owd402.append(iat[nn])
# 	elif nn>ind403 and nn<=ind403+150:
# 		owd403.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd401"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd401))
# """ owd401 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd401))
# """owd401 min"""
# print 'min11 = {}'.format(min(owd401))
# """owd401 max"""
# print 'max11 = {}'.format(max(owd401))
# """ owd401 std"""
# print 'std11 = {}'.format(numpy.std(owd401))

# """for owd402"""
# print "number of packets included = {}".format(len(owd402))
# print 'mean12 = {}'.format(numpy.mean(owd402))
# print 'min12 = {}'.format(min(owd402))
# print 'max12 = {}'.format(max(owd402))
# print 'std12 = {}'.format(numpy.std(owd402))

# """ for owd403"""
# print "number of packets included = {}".format(len(owd403))
# print 'mean13 = {}'.format(numpy.mean(owd403))
# print 'min13 = {}'.format(min(owd403))
# print 'max13 = {}'.format(max(owd403))
# print 'std13 = {}'.format(numpy.std(owd403))


# """ next take the Window3/Window1""" 
# an1 = numpy.mean(owd403)/numpy.mean(owd401)
# an2 = numpy.mean(owd403)/numpy.min(owd401)
# an3 = numpy.mean(owd403)/numpy.max(owd401)

# an4 = numpy.min(owd403)/numpy.mean(owd401)
# an5 = numpy.min(owd403)/numpy.min(owd401)
# an6 = numpy.min(owd403)/numpy.max(owd401)

# an7 = numpy.max(owd403)/numpy.mean(owd401)
# an8 = numpy.max(owd403)/numpy.min(owd401)
# an9 = numpy.max(owd403)/numpy.max(owd401)

# """next take the Window3/Window2"""
# an10 = numpy.mean(owd403)/numpy.mean(owd402)
# an11 = numpy.mean(owd403)/numpy.min(owd402)
# an12 = numpy.mean(owd403)/numpy.max(owd402)

# an13 = numpy.min(owd403)/numpy.mean(owd402)
# an14 = numpy.min(owd403)/numpy.min(owd402)
# an15 = numpy.min(owd403)/numpy.max(owd402)

# an16 = numpy.max(owd403)/numpy.mean(owd402)
# an17 = numpy.max(owd403)/numpy.min(owd402)
# an18 = numpy.max(owd403)/numpy.max(owd402)

# """ min/max window 3"""
# an19 = numpy.min(owd403)/numpy.max(owd403)

# """standard dev values"""
# an20 = numpy.std(owd403)/numpy.std(owd401)
# an21 = numpy.std(owd403)/numpy.std(owd402)
# an22 = numpy.std(owd401)/numpy.std(owd402)

# """next window1 / window2"""
# an23 = numpy.mean(owd401)/numpy.mean(owd402)
# an24 = numpy.mean(owd401)/numpy.min(owd402)
# an25 = numpy.mean(owd401)/numpy.max(owd402)

# an26 = numpy.min(owd401)/numpy.mean(owd402)
# an27 = numpy.min(owd401)/numpy.min(owd402)
# an28 = numpy.min(owd401)/numpy.max(owd402)

# an29 = numpy.max(owd401)/numpy.mean(owd402)
# an30 = numpy.max(owd401)/numpy.min(owd402)
# an31 = numpy.max(owd401)/numpy.max(owd402)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(an1)+"\n"
# print "avg-win3 / min-win1 = "+ str(an2)+"\n"
# print "avg-win3 / max-win1 = "+ str(an3)+"\n"

# print "min-win3 / avg-win1 = "+ str(an4)+"\n"
# print "min-win3 / min-win1 = "+ str(an5)+"\n"
# print "min-win3 / max-win1 = "+ str(an6)+"\n"

# print "max-win3 / avg-win1 = "+ str(an7)+"\n"
# print "max-win3 / min-win1 = "+ str(an8)+"\n"
# print "max-win3 / max-win1 = "+ str(an9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(an10)+"\n"
# print "avg-win3 / min-win2 = "+ str(an11)+"\n"
# print "avg-win3 / max-win2 = "+ str(an12)+"\n"

# print "min-win3 / avg-win2 = "+ str(an13)+"\n"
# print "min-win3 / min-win2 = "+ str(an14)+"\n"
# print "min-win3 / max-win2 = "+ str(an15)+"\n"

# print "max-win3 / avg-win2 = "+ str(an16)+"\n"
# print "max-win3 / min-win2 = "+ str(an17)+"\n"
# print "max-win3 / max-win2 = "+ str(an18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(an19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(an20)+"\n"
# print "std-win3 / std-win2 = "+ str(an21)+"\n"
# print "std-win1 / std-win2 = "+ str(an22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(an23)+"\n"
# print "avg-win1 / min-win2 = "+ str(an24)+"\n"
# print "avg-win1 / max-win2 = "+ str(an25)+"\n"

# print "min-win1 / avg-win2 = "+ str(an26)+"\n"
# print "min-win1 / min-win2 = "+ str(an27)+"\n"
# print "min-win1 / max-win2 = "+ str(an28)+"\n"

# print "max-win1 / avg-win2 = "+ str(an29)+"\n"
# print "max-win1 / min-win2 = "+ str(an30)+"\n"
# print "max-win1 / max-win2 = "+ str(an31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 41"""
# print "Loss # 41"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind411=win_index[40]-300
# ind412=win_index[40]-150
# ind413=win_index[40]

# print "\n index number for loss 41", ind411, ind412, ind413

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd411=[]
# owd412=[]
# owd413=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind411 and nn<=ind412:
# 		owd411.append(iat[nn])
# 	elif nn>ind412 and nn<=ind413:
# 		owd412.append(iat[nn])
# 	elif nn>ind413 and nn<=ind413+150:
# 		owd413.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd411"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd411))
# """ owd411 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd411))
# """owd411 min"""
# print 'min11 = {}'.format(min(owd411))
# """owd411 max"""
# print 'max11 = {}'.format(max(owd411))
# """ owd411 std"""
# print 'std11 = {}'.format(numpy.std(owd411))

# """for owd412"""
# print "number of packets included = {}".format(len(owd412))
# print 'mean12 = {}'.format(numpy.mean(owd412))
# print 'min12 = {}'.format(min(owd412))
# print 'max12 = {}'.format(max(owd412))
# print 'std12 = {}'.format(numpy.std(owd412))

# """ for owd413"""
# print "number of packets included = {}".format(len(owd413))
# print 'mean13 = {}'.format(numpy.mean(owd413))
# print 'min13 = {}'.format(min(owd413))
# print 'max13 = {}'.format(max(owd413))
# print 'std13 = {}'.format(numpy.std(owd413))


# """ next take the Window3/Window1""" 
# ao1 = numpy.mean(owd413)/numpy.mean(owd411)
# ao2 = numpy.mean(owd413)/numpy.min(owd411)
# ao3 = numpy.mean(owd413)/numpy.max(owd411)

# ao4 = numpy.min(owd413)/numpy.mean(owd411)
# ao5 = numpy.min(owd413)/numpy.min(owd411)
# ao6 = numpy.min(owd413)/numpy.max(owd411)

# ao7 = numpy.max(owd413)/numpy.mean(owd411)
# ao8 = numpy.max(owd413)/numpy.min(owd411)
# ao9 = numpy.max(owd413)/numpy.max(owd411)

# """next take the Window3/Window2"""
# ao10 = numpy.mean(owd413)/numpy.mean(owd412)
# ao11 = numpy.mean(owd413)/numpy.min(owd412)
# ao12 = numpy.mean(owd413)/numpy.max(owd412)

# ao13 = numpy.min(owd413)/numpy.mean(owd412)
# ao14 = numpy.min(owd413)/numpy.min(owd412)
# ao15 = numpy.min(owd413)/numpy.max(owd412)

# ao16 = numpy.max(owd413)/numpy.mean(owd412)
# ao17 = numpy.max(owd413)/numpy.min(owd412)
# ao18 = numpy.max(owd413)/numpy.max(owd412)

# """ min/max window 3"""
# ao19 = numpy.min(owd413)/numpy.max(owd413)

# """standard dev values"""
# ao20 = numpy.std(owd413)/numpy.std(owd411)
# ao21 = numpy.std(owd413)/numpy.std(owd412)
# ao22 = numpy.std(owd411)/numpy.std(owd412)

# """next window1 / window2"""
# ao23 = numpy.mean(owd411)/numpy.mean(owd412)
# ao24 = numpy.mean(owd411)/numpy.min(owd412)
# ao25 = numpy.mean(owd411)/numpy.max(owd412)

# ao26 = numpy.min(owd411)/numpy.mean(owd412)
# ao27 = numpy.min(owd411)/numpy.min(owd412)
# ao28 = numpy.min(owd411)/numpy.max(owd412)

# ao29 = numpy.max(owd411)/numpy.mean(owd412)
# ao30 = numpy.max(owd411)/numpy.min(owd412)
# ao31 = numpy.max(owd411)/numpy.max(owd412)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ao1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ao2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ao3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ao4)+"\n"
# print "min-win3 / min-win1 = "+ str(ao5)+"\n"
# print "min-win3 / max-win1 = "+ str(ao6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ao7)+"\n"
# print "max-win3 / min-win1 = "+ str(ao8)+"\n"
# print "max-win3 / max-win1 = "+ str(ao9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ao10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ao11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ao12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ao13)+"\n"
# print "min-win3 / min-win2 = "+ str(ao14)+"\n"
# print "min-win3 / max-win2 = "+ str(ao15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ao16)+"\n"
# print "max-win3 / min-win2 = "+ str(ao17)+"\n"
# print "max-win3 / max-win2 = "+ str(ao18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ao19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ao20)+"\n"
# print "std-win3 / std-win2 = "+ str(ao21)+"\n"
# print "std-win1 / std-win2 = "+ str(ao22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ao23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ao24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ao25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ao26)+"\n"
# print "min-win1 / min-win2 = "+ str(ao27)+"\n"
# print "min-win1 / max-win2 = "+ str(ao28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ao29)+"\n"
# print "max-win1 / min-win2 = "+ str(ao30)+"\n"
# print "max-win1 / max-win2 = "+ str(ao31)+"\n"

# print "#################################################"


# ########################################

# """LOSS # 42"""
# print "Loss # 42"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind421=win_index[41]-300
# ind422=win_index[41]-150
# ind423=win_index[41]

# print "\n index number for loss 42", ind421, ind422, ind423

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd421=[]
# owd422=[]
# owd423=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind421 and nn<=ind422:
# 		owd421.append(iat[nn])
# 	elif nn>ind422 and nn<=ind423:
# 		owd422.append(iat[nn])
# 	elif nn>ind423 and nn<=ind423+150:
# 		owd423.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd421"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd421))
# """ owd421 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd421))
# """owd421 min"""
# print 'min11 = {}'.format(min(owd421))
# """owd421 max"""
# print 'max11 = {}'.format(max(owd421))
# """ owd421 std"""
# print 'std11 = {}'.format(numpy.std(owd421))

# """for owd422"""
# print "number of packets included = {}".format(len(owd422))
# print 'mean12 = {}'.format(numpy.mean(owd422))
# print 'min12 = {}'.format(min(owd422))
# print 'max12 = {}'.format(max(owd422))
# print 'std12 = {}'.format(numpy.std(owd422))

# """ for owd423"""
# print "number of packets included = {}".format(len(owd423))
# print 'mean13 = {}'.format(numpy.mean(owd423))
# print 'min13 = {}'.format(min(owd423))
# print 'max13 = {}'.format(max(owd423))
# print 'std13 = {}'.format(numpy.std(owd423))


# """ next take the Window3/Window1""" 
# ap1 = numpy.mean(owd423)/numpy.mean(owd421)
# ap2 = numpy.mean(owd423)/numpy.min(owd421)
# ap3 = numpy.mean(owd423)/numpy.max(owd421)

# ap4 = numpy.min(owd423)/numpy.mean(owd421)
# ap5 = numpy.min(owd423)/numpy.min(owd421)
# ap6 = numpy.min(owd423)/numpy.max(owd421)

# ap7 = numpy.max(owd423)/numpy.mean(owd421)
# ap8 = numpy.max(owd423)/numpy.min(owd421)
# ap9 = numpy.max(owd423)/numpy.max(owd421)

# """next take the Window3/Window2"""
# ap10 = numpy.mean(owd423)/numpy.mean(owd422)
# ap11 = numpy.mean(owd423)/numpy.min(owd422)
# ap12 = numpy.mean(owd423)/numpy.max(owd422)

# ap13 = numpy.min(owd423)/numpy.mean(owd422)
# ap14 = numpy.min(owd423)/numpy.min(owd422)
# ap15 = numpy.min(owd423)/numpy.max(owd422)

# ap16 = numpy.max(owd423)/numpy.mean(owd422)
# ap17 = numpy.max(owd423)/numpy.min(owd422)
# ap18 = numpy.max(owd423)/numpy.max(owd422)

# """ min/max window 3"""
# ap19 = numpy.min(owd423)/numpy.max(owd423)

# """standard dev values"""
# ap20 = numpy.std(owd423)/numpy.std(owd421)
# ap21 = numpy.std(owd423)/numpy.std(owd422)
# ap22 = numpy.std(owd421)/numpy.std(owd422)

# """next window1 / window2"""
# ap23 = numpy.mean(owd421)/numpy.mean(owd422)
# ap24 = numpy.mean(owd421)/numpy.min(owd422)
# ap25 = numpy.mean(owd421)/numpy.max(owd422)

# ap26 = numpy.min(owd421)/numpy.mean(owd422)
# ap27 = numpy.min(owd421)/numpy.min(owd422)
# ap28 = numpy.min(owd421)/numpy.max(owd422)

# ap29 = numpy.max(owd421)/numpy.mean(owd422)
# ap30 = numpy.max(owd421)/numpy.min(owd422)
# ap31 = numpy.max(owd421)/numpy.max(owd422)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ap1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ap2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ap3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ap4)+"\n"
# print "min-win3 / min-win1 = "+ str(ap5)+"\n"
# print "min-win3 / max-win1 = "+ str(ap6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ap7)+"\n"
# print "max-win3 / min-win1 = "+ str(ap8)+"\n"
# print "max-win3 / max-win1 = "+ str(ap9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ap10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ap11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ap12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ap13)+"\n"
# print "min-win3 / min-win2 = "+ str(ap14)+"\n"
# print "min-win3 / max-win2 = "+ str(ap15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ap16)+"\n"
# print "max-win3 / min-win2 = "+ str(ap17)+"\n"
# print "max-win3 / max-win2 = "+ str(ap18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ap19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ap20)+"\n"
# print "std-win3 / std-win2 = "+ str(ap21)+"\n"
# print "std-win1 / std-win2 = "+ str(ap22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ap23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ap24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ap25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ap26)+"\n"
# print "min-win1 / min-win2 = "+ str(ap27)+"\n"
# print "min-win1 / max-win2 = "+ str(ap28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ap29)+"\n"
# print "max-win1 / min-win2 = "+ str(ap30)+"\n"
# print "max-win1 / max-win2 = "+ str(ap31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 43"""
# print "Loss # 43"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind431=win_index[42]-300
# ind432=win_index[42]-150
# ind433=win_index[42]

# print "\n index number for loss 43", ind431, ind432, ind433

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd431=[]
# owd432=[]
# owd433=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind431 and nn<=ind432:
# 		owd431.append(iat[nn])
# 	elif nn>ind432 and nn<=ind433:
# 		owd432.append(iat[nn])
# 	elif nn>ind433 and nn<=ind433+150:
# 		owd433.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd431"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd431))
# """ owd431 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd431))
# """owd431 min"""
# print 'min11 = {}'.format(min(owd431))
# """owd431 max"""
# print 'max11 = {}'.format(max(owd431))
# """ owd431 std"""
# print 'std11 = {}'.format(numpy.std(owd431))

# """for owd432"""
# print "number of packets included = {}".format(len(owd432))
# print 'mean12 = {}'.format(numpy.mean(owd432))
# print 'min12 = {}'.format(min(owd432))
# print 'max12 = {}'.format(max(owd432))
# print 'std12 = {}'.format(numpy.std(owd432))

# """ for owd433"""
# print "number of packets included = {}".format(len(owd433))
# print 'mean13 = {}'.format(numpy.mean(owd433))
# print 'min13 = {}'.format(min(owd433))
# print 'max13 = {}'.format(max(owd433))
# print 'std13 = {}'.format(numpy.std(owd433))


# """ next take the Window3/Window1""" 
# aq1 = numpy.mean(owd433)/numpy.mean(owd431)
# aq2 = numpy.mean(owd433)/numpy.min(owd431)
# aq3 = numpy.mean(owd433)/numpy.max(owd431)

# aq4 = numpy.min(owd433)/numpy.mean(owd431)
# aq5 = numpy.min(owd433)/numpy.min(owd431)
# aq6 = numpy.min(owd433)/numpy.max(owd431)

# aq7 = numpy.max(owd433)/numpy.mean(owd431)
# aq8 = numpy.max(owd433)/numpy.min(owd431)
# aq9 = numpy.max(owd433)/numpy.max(owd431)

# """next take the Window3/Window2"""
# aq10 = numpy.mean(owd433)/numpy.mean(owd432)
# aq11 = numpy.mean(owd433)/numpy.min(owd432)
# aq12 = numpy.mean(owd433)/numpy.max(owd432)

# aq13 = numpy.min(owd433)/numpy.mean(owd432)
# aq14 = numpy.min(owd433)/numpy.min(owd432)
# aq15 = numpy.min(owd433)/numpy.max(owd432)

# aq16 = numpy.max(owd433)/numpy.mean(owd432)
# aq17 = numpy.max(owd433)/numpy.min(owd432)
# aq18 = numpy.max(owd433)/numpy.max(owd432)

# """ min/max window 3"""
# aq19 = numpy.min(owd433)/numpy.max(owd433)

# """standard dev values"""
# aq20 = numpy.std(owd433)/numpy.std(owd431)
# aq21 = numpy.std(owd433)/numpy.std(owd432)
# aq22 = numpy.std(owd431)/numpy.std(owd432)

# """next window1 / window2"""
# aq23 = numpy.mean(owd431)/numpy.mean(owd432)
# aq24 = numpy.mean(owd431)/numpy.min(owd432)
# aq25 = numpy.mean(owd431)/numpy.max(owd432)

# aq26 = numpy.min(owd431)/numpy.mean(owd432)
# aq27 = numpy.min(owd431)/numpy.min(owd432)
# aq28 = numpy.min(owd431)/numpy.max(owd432)

# aq29 = numpy.max(owd431)/numpy.mean(owd432)
# aq30 = numpy.max(owd431)/numpy.min(owd432)
# aq31 = numpy.max(owd431)/numpy.max(owd432)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(aq1)+"\n"
# print "avg-win3 / min-win1 = "+ str(aq2)+"\n"
# print "avg-win3 / max-win1 = "+ str(aq3)+"\n"

# print "min-win3 / avg-win1 = "+ str(aq4)+"\n"
# print "min-win3 / min-win1 = "+ str(aq5)+"\n"
# print "min-win3 / max-win1 = "+ str(aq6)+"\n"

# print "max-win3 / avg-win1 = "+ str(aq7)+"\n"
# print "max-win3 / min-win1 = "+ str(aq8)+"\n"
# print "max-win3 / max-win1 = "+ str(aq9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(aq10)+"\n"
# print "avg-win3 / min-win2 = "+ str(aq11)+"\n"
# print "avg-win3 / max-win2 = "+ str(aq12)+"\n"

# print "min-win3 / avg-win2 = "+ str(aq13)+"\n"
# print "min-win3 / min-win2 = "+ str(aq14)+"\n"
# print "min-win3 / max-win2 = "+ str(aq15)+"\n"

# print "max-win3 / avg-win2 = "+ str(aq16)+"\n"
# print "max-win3 / min-win2 = "+ str(aq17)+"\n"
# print "max-win3 / max-win2 = "+ str(aq18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(aq19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(aq20)+"\n"
# print "std-win3 / std-win2 = "+ str(aq21)+"\n"
# print "std-win1 / std-win2 = "+ str(aq22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(aq23)+"\n"
# print "avg-win1 / min-win2 = "+ str(aq24)+"\n"
# print "avg-win1 / max-win2 = "+ str(aq25)+"\n"

# print "min-win1 / avg-win2 = "+ str(aq26)+"\n"
# print "min-win1 / min-win2 = "+ str(aq27)+"\n"
# print "min-win1 / max-win2 = "+ str(aq28)+"\n"

# print "max-win1 / avg-win2 = "+ str(aq29)+"\n"
# print "max-win1 / min-win2 = "+ str(aq30)+"\n"
# print "max-win1 / max-win2 = "+ str(aq31)+"\n"

# print "#################################################"


# ########################################

# """LOSS # 44"""
# print "Loss # 44"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind441=win_index[43]-300
# ind442=win_index[43]-150
# ind443=win_index[43]

# print "\n index number for loss 44", ind441, ind442, ind443

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd441=[]
# owd442=[]
# owd443=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind441 and nn<=ind442:
# 		owd441.append(iat[nn])
# 	elif nn>ind442 and nn<=ind443:
# 		owd442.append(iat[nn])
# 	elif nn>ind443 and nn<=ind443+150:
# 		owd443.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd441"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd441))
# """ owd441 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd441))
# """owd441 min"""
# print 'min11 = {}'.format(min(owd441))
# """owd441 max"""
# print 'max11 = {}'.format(max(owd441))
# """ owd441 std"""
# print 'std11 = {}'.format(numpy.std(owd441))

# """for owd442"""
# print "number of packets included = {}".format(len(owd442))
# print 'mean12 = {}'.format(numpy.mean(owd442))
# print 'min12 = {}'.format(min(owd442))
# print 'max12 = {}'.format(max(owd442))
# print 'std12 = {}'.format(numpy.std(owd442))

# """ for owd443"""
# print "number of packets included = {}".format(len(owd443))
# print 'mean13 = {}'.format(numpy.mean(owd443))
# print 'min13 = {}'.format(min(owd443))
# print 'max13 = {}'.format(max(owd443))
# print 'std13 = {}'.format(numpy.std(owd443))


# """ next take the Window3/Window1""" 
# ar1 = numpy.mean(owd443)/numpy.mean(owd441)
# ar2 = numpy.mean(owd443)/numpy.min(owd441)
# ar3 = numpy.mean(owd443)/numpy.max(owd441)

# ar4 = numpy.min(owd443)/numpy.mean(owd441)
# ar5 = numpy.min(owd443)/numpy.min(owd441)
# ar6 = numpy.min(owd443)/numpy.max(owd441)

# ar7 = numpy.max(owd443)/numpy.mean(owd441)
# ar8 = numpy.max(owd443)/numpy.min(owd441)
# ar9 = numpy.max(owd443)/numpy.max(owd441)

# """next take the Window3/Window2"""
# ar10 = numpy.mean(owd443)/numpy.mean(owd442)
# ar11 = numpy.mean(owd443)/numpy.min(owd442)
# ar12 = numpy.mean(owd443)/numpy.max(owd442)

# ar13 = numpy.min(owd443)/numpy.mean(owd442)
# ar14 = numpy.min(owd443)/numpy.min(owd442)
# ar15 = numpy.min(owd443)/numpy.max(owd442)

# ar16 = numpy.max(owd443)/numpy.mean(owd442)
# ar17 = numpy.max(owd443)/numpy.min(owd442)
# ar18 = numpy.max(owd443)/numpy.max(owd442)

# """ min/max window 3"""
# ar19 = numpy.min(owd443)/numpy.max(owd443)

# """standard dev values"""
# ar20 = numpy.std(owd443)/numpy.std(owd441)
# ar21 = numpy.std(owd443)/numpy.std(owd442)
# ar22 = numpy.std(owd441)/numpy.std(owd442)

# """next window1 / window2"""
# ar23 = numpy.mean(owd441)/numpy.mean(owd442)
# ar24 = numpy.mean(owd441)/numpy.min(owd442)
# ar25 = numpy.mean(owd441)/numpy.max(owd442)

# ar26 = numpy.min(owd441)/numpy.mean(owd442)
# ar27 = numpy.min(owd441)/numpy.min(owd442)
# ar28 = numpy.min(owd441)/numpy.max(owd442)

# ar29 = numpy.max(owd441)/numpy.mean(owd442)
# ar30 = numpy.max(owd441)/numpy.min(owd442)
# ar31 = numpy.max(owd441)/numpy.max(owd442)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ar1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ar2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ar3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ar4)+"\n"
# print "min-win3 / min-win1 = "+ str(ar5)+"\n"
# print "min-win3 / max-win1 = "+ str(ar6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ar7)+"\n"
# print "max-win3 / min-win1 = "+ str(ar8)+"\n"
# print "max-win3 / max-win1 = "+ str(ar9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ar10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ar11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ar12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ar13)+"\n"
# print "min-win3 / min-win2 = "+ str(ar14)+"\n"
# print "min-win3 / max-win2 = "+ str(ar15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ar16)+"\n"
# print "max-win3 / min-win2 = "+ str(ar17)+"\n"
# print "max-win3 / max-win2 = "+ str(ar18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ar19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ar20)+"\n"
# print "std-win3 / std-win2 = "+ str(ar21)+"\n"
# print "std-win1 / std-win2 = "+ str(ar22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ar23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ar24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ar25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ar26)+"\n"
# print "min-win1 / min-win2 = "+ str(ar27)+"\n"
# print "min-win1 / max-win2 = "+ str(ar28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ar29)+"\n"
# print "max-win1 / min-win2 = "+ str(ar30)+"\n"
# print "max-win1 / max-win2 = "+ str(ar31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 45"""
# print "Loss # 45"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind451=win_index[44]-300
# ind452=win_index[44]-150
# ind453=win_index[44]

# print "\n index number for loss 45", ind451, ind452, ind453

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd451=[]
# owd452=[]
# owd453=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind451 and nn<=ind452:
# 		owd451.append(iat[nn])
# 	elif nn>ind452 and nn<=ind453:
# 		owd452.append(iat[nn])
# 	elif nn>ind453 and nn<=ind453+150:
# 		owd453.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd451"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd451))
# """ owd451 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd451))
# """owd451 min"""
# print 'min11 = {}'.format(min(owd451))
# """owd451 max"""
# print 'max11 = {}'.format(max(owd451))
# """ owd451 std"""
# print 'std11 = {}'.format(numpy.std(owd451))

# """for owd452"""
# print "number of packets included = {}".format(len(owd452))
# print 'mean12 = {}'.format(numpy.mean(owd452))
# print 'min12 = {}'.format(min(owd452))
# print 'max12 = {}'.format(max(owd452))
# print 'std12 = {}'.format(numpy.std(owd452))

# """ for owd453"""
# print "number of packets included = {}".format(len(owd453))
# print 'mean13 = {}'.format(numpy.mean(owd453))
# print 'min13 = {}'.format(min(owd453))
# print 'max13 = {}'.format(max(owd453))
# print 'std13 = {}'.format(numpy.std(owd453))


# """ next take the Window3/Window1""" 
# as1 = numpy.mean(owd453)/numpy.mean(owd451)
# as2 = numpy.mean(owd453)/numpy.min(owd451)
# as3 = numpy.mean(owd453)/numpy.max(owd451)

# as4 = numpy.min(owd453)/numpy.mean(owd451)
# as5 = numpy.min(owd453)/numpy.min(owd451)
# as6 = numpy.min(owd453)/numpy.max(owd451)

# as7 = numpy.max(owd453)/numpy.mean(owd451)
# as8 = numpy.max(owd453)/numpy.min(owd451)
# as9 = numpy.max(owd453)/numpy.max(owd451)

# """next take the Window3/Window2"""
# as10 = numpy.mean(owd453)/numpy.mean(owd452)
# as11 = numpy.mean(owd453)/numpy.min(owd452)
# as12 = numpy.mean(owd453)/numpy.max(owd452)

# as13 = numpy.min(owd453)/numpy.mean(owd452)
# as14 = numpy.min(owd453)/numpy.min(owd452)
# as15 = numpy.min(owd453)/numpy.max(owd452)

# as16 = numpy.max(owd453)/numpy.mean(owd452)
# as17 = numpy.max(owd453)/numpy.min(owd452)
# as18 = numpy.max(owd453)/numpy.max(owd452)

# """ min/max window 3"""
# as19 = numpy.min(owd453)/numpy.max(owd453)

# """standard dev values"""
# as20 = numpy.std(owd453)/numpy.std(owd451)
# as21 = numpy.std(owd453)/numpy.std(owd452)
# as22 = numpy.std(owd451)/numpy.std(owd452)

# """next window1 / window2"""
# as23 = numpy.mean(owd451)/numpy.mean(owd452)
# as24 = numpy.mean(owd451)/numpy.min(owd452)
# as25 = numpy.mean(owd451)/numpy.max(owd452)

# as26 = numpy.min(owd451)/numpy.mean(owd452)
# as27 = numpy.min(owd451)/numpy.min(owd452)
# as28 = numpy.min(owd451)/numpy.max(owd452)

# as29 = numpy.max(owd451)/numpy.mean(owd452)
# as30 = numpy.max(owd451)/numpy.min(owd452)
# as31 = numpy.max(owd451)/numpy.max(owd452)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(as1)+"\n"
# print "avg-win3 / min-win1 = "+ str(as2)+"\n"
# print "avg-win3 / max-win1 = "+ str(as3)+"\n"

# print "min-win3 / avg-win1 = "+ str(as4)+"\n"
# print "min-win3 / min-win1 = "+ str(as5)+"\n"
# print "min-win3 / max-win1 = "+ str(as6)+"\n"

# print "max-win3 / avg-win1 = "+ str(as7)+"\n"
# print "max-win3 / min-win1 = "+ str(as8)+"\n"
# print "max-win3 / max-win1 = "+ str(as9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(as10)+"\n"
# print "avg-win3 / min-win2 = "+ str(as11)+"\n"
# print "avg-win3 / max-win2 = "+ str(as12)+"\n"

# print "min-win3 / avg-win2 = "+ str(as13)+"\n"
# print "min-win3 / min-win2 = "+ str(as14)+"\n"
# print "min-win3 / max-win2 = "+ str(as15)+"\n"

# print "max-win3 / avg-win2 = "+ str(as16)+"\n"
# print "max-win3 / min-win2 = "+ str(as17)+"\n"
# print "max-win3 / max-win2 = "+ str(as18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(as19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(as20)+"\n"
# print "std-win3 / std-win2 = "+ str(as21)+"\n"
# print "std-win1 / std-win2 = "+ str(as22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(as23)+"\n"
# print "avg-win1 / min-win2 = "+ str(as24)+"\n"
# print "avg-win1 / max-win2 = "+ str(as25)+"\n"

# print "min-win1 / avg-win2 = "+ str(as26)+"\n"
# print "min-win1 / min-win2 = "+ str(as27)+"\n"
# print "min-win1 / max-win2 = "+ str(as28)+"\n"

# print "max-win1 / avg-win2 = "+ str(as29)+"\n"
# print "max-win1 / min-win2 = "+ str(as30)+"\n"
# print "max-win1 / max-win2 = "+ str(as31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 46"""
# print "Loss # 46"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind461=win_index[45]-300
# ind462=win_index[45]-150
# ind463=win_index[45]

# print "\n index number for loss 46", ind461, ind462, ind463

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd461=[]
# owd462=[]
# owd463=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind461 and nn<=ind462:
# 		owd461.append(iat[nn])
# 	elif nn>ind462 and nn<=ind463:
# 		owd462.append(iat[nn])
# 	elif nn>ind463 and nn<=ind463+150:
# 		owd463.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd461"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd461))
# """ owd461 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd461))
# """owd461 min"""
# print 'min11 = {}'.format(min(owd461))
# """owd461 max"""
# print 'max11 = {}'.format(max(owd461))
# """ owd461 std"""
# print 'std11 = {}'.format(numpy.std(owd461))

# """for owd462"""
# print "number of packets included = {}".format(len(owd462))
# print 'mean12 = {}'.format(numpy.mean(owd462))
# print 'min12 = {}'.format(min(owd462))
# print 'max12 = {}'.format(max(owd462))
# print 'std12 = {}'.format(numpy.std(owd462))

# """ for owd463"""
# print "number of packets included = {}".format(len(owd463))
# print 'mean13 = {}'.format(numpy.mean(owd463))
# print 'min13 = {}'.format(min(owd463))
# print 'max13 = {}'.format(max(owd463))
# print 'std13 = {}'.format(numpy.std(owd463))


# """ next take the Window3/Window1""" 
# at1 = numpy.mean(owd463)/numpy.mean(owd461)
# at2 = numpy.mean(owd463)/numpy.min(owd461)
# at3 = numpy.mean(owd463)/numpy.max(owd461)

# at4 = numpy.min(owd463)/numpy.mean(owd461)
# at5 = numpy.min(owd463)/numpy.min(owd461)
# at6 = numpy.min(owd463)/numpy.max(owd461)

# at7 = numpy.max(owd463)/numpy.mean(owd461)
# at8 = numpy.max(owd463)/numpy.min(owd461)
# at9 = numpy.max(owd463)/numpy.max(owd461)

# """next take the Window3/Window2"""
# at10 = numpy.mean(owd463)/numpy.mean(owd462)
# at11 = numpy.mean(owd463)/numpy.min(owd462)
# at12 = numpy.mean(owd463)/numpy.max(owd462)

# at13 = numpy.min(owd463)/numpy.mean(owd462)
# at14 = numpy.min(owd463)/numpy.min(owd462)
# at15 = numpy.min(owd463)/numpy.max(owd462)

# at16 = numpy.max(owd463)/numpy.mean(owd462)
# at17 = numpy.max(owd463)/numpy.min(owd462)
# at18 = numpy.max(owd463)/numpy.max(owd462)

# """ min/max window 3"""
# at19 = numpy.min(owd463)/numpy.max(owd463)

# """standard dev values"""
# at20 = numpy.std(owd463)/numpy.std(owd461)
# at21 = numpy.std(owd463)/numpy.std(owd462)
# at22 = numpy.std(owd461)/numpy.std(owd462)

# """next window1 / window2"""
# at23 = numpy.mean(owd461)/numpy.mean(owd462)
# at24 = numpy.mean(owd461)/numpy.min(owd462)
# at25 = numpy.mean(owd461)/numpy.max(owd462)

# at26 = numpy.min(owd461)/numpy.mean(owd462)
# at27 = numpy.min(owd461)/numpy.min(owd462)
# at28 = numpy.min(owd461)/numpy.max(owd462)

# at29 = numpy.max(owd461)/numpy.mean(owd462)
# at30 = numpy.max(owd461)/numpy.min(owd462)
# at31 = numpy.max(owd461)/numpy.max(owd462)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(at1)+"\n"
# print "avg-win3 / min-win1 = "+ str(at2)+"\n"
# print "avg-win3 / max-win1 = "+ str(at3)+"\n"

# print "min-win3 / avg-win1 = "+ str(at4)+"\n"
# print "min-win3 / min-win1 = "+ str(at5)+"\n"
# print "min-win3 / max-win1 = "+ str(at6)+"\n"

# print "max-win3 / avg-win1 = "+ str(at7)+"\n"
# print "max-win3 / min-win1 = "+ str(at8)+"\n"
# print "max-win3 / max-win1 = "+ str(at9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(at10)+"\n"
# print "avg-win3 / min-win2 = "+ str(at11)+"\n"
# print "avg-win3 / max-win2 = "+ str(at12)+"\n"

# print "min-win3 / avg-win2 = "+ str(at13)+"\n"
# print "min-win3 / min-win2 = "+ str(at14)+"\n"
# print "min-win3 / max-win2 = "+ str(at15)+"\n"

# print "max-win3 / avg-win2 = "+ str(at16)+"\n"
# print "max-win3 / min-win2 = "+ str(at17)+"\n"
# print "max-win3 / max-win2 = "+ str(at18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(at19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(at20)+"\n"
# print "std-win3 / std-win2 = "+ str(at21)+"\n"
# print "std-win1 / std-win2 = "+ str(at22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(at23)+"\n"
# print "avg-win1 / min-win2 = "+ str(at24)+"\n"
# print "avg-win1 / max-win2 = "+ str(at25)+"\n"

# print "min-win1 / avg-win2 = "+ str(at26)+"\n"
# print "min-win1 / min-win2 = "+ str(at27)+"\n"
# print "min-win1 / max-win2 = "+ str(at28)+"\n"

# print "max-win1 / avg-win2 = "+ str(at29)+"\n"
# print "max-win1 / min-win2 = "+ str(at30)+"\n"
# print "max-win1 / max-win2 = "+ str(at31)+"\n"

# print "#################################################"


# ########################################

# """LOSS # 47"""
# print "Loss # 47"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind471=win_index[46]-300
# ind472=win_index[46]-150
# ind473=win_index[46]

# print "\n index number for loss 47", ind471, ind472, ind473

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd471=[]
# owd472=[]
# owd473=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind471 and nn<=ind472:
# 		owd471.append(iat[nn])
# 	elif nn>ind472 and nn<=ind473:
# 		owd472.append(iat[nn])
# 	elif nn>ind473 and nn<=ind473+150:
# 		owd473.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd471"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd471))
# """ owd471 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd471))
# """owd471 min"""
# print 'min11 = {}'.format(min(owd471))
# """owd471 max"""
# print 'max11 = {}'.format(max(owd471))
# """ owd471 std"""
# print 'std11 = {}'.format(numpy.std(owd471))

# """for owd472"""
# print "number of packets included = {}".format(len(owd472))
# print 'mean12 = {}'.format(numpy.mean(owd472))
# print 'min12 = {}'.format(min(owd472))
# print 'max12 = {}'.format(max(owd472))
# print 'std12 = {}'.format(numpy.std(owd472))

# """ for owd473"""
# print "number of packets included = {}".format(len(owd473))
# print 'mean13 = {}'.format(numpy.mean(owd473))
# print 'min13 = {}'.format(min(owd473))
# print 'max13 = {}'.format(max(owd473))
# print 'std13 = {}'.format(numpy.std(owd473))


# """ next take the Window3/Window1""" 
# au1 = numpy.mean(owd473)/numpy.mean(owd471)
# au2 = numpy.mean(owd473)/numpy.min(owd471)
# au3 = numpy.mean(owd473)/numpy.max(owd471)

# au4 = numpy.min(owd473)/numpy.mean(owd471)
# au5 = numpy.min(owd473)/numpy.min(owd471)
# au6 = numpy.min(owd473)/numpy.max(owd471)

# au7 = numpy.max(owd473)/numpy.mean(owd471)
# au8 = numpy.max(owd473)/numpy.min(owd471)
# au9 = numpy.max(owd473)/numpy.max(owd471)

# """next take the Window3/Window2"""
# au10 = numpy.mean(owd473)/numpy.mean(owd472)
# au11 = numpy.mean(owd473)/numpy.min(owd472)
# au12 = numpy.mean(owd473)/numpy.max(owd472)

# au13 = numpy.min(owd473)/numpy.mean(owd472)
# au14 = numpy.min(owd473)/numpy.min(owd472)
# au15 = numpy.min(owd473)/numpy.max(owd472)

# au16 = numpy.max(owd473)/numpy.mean(owd472)
# au17 = numpy.max(owd473)/numpy.min(owd472)
# au18 = numpy.max(owd473)/numpy.max(owd472)

# """ min/max window 3"""
# au19 = numpy.min(owd473)/numpy.max(owd473)

# """standard dev values"""
# au20 = numpy.std(owd473)/numpy.std(owd471)
# au21 = numpy.std(owd473)/numpy.std(owd472)
# au22 = numpy.std(owd471)/numpy.std(owd472)

# """next window1 / window2"""
# au23 = numpy.mean(owd471)/numpy.mean(owd472)
# au24 = numpy.mean(owd471)/numpy.min(owd472)
# au25 = numpy.mean(owd471)/numpy.max(owd472)

# au26 = numpy.min(owd471)/numpy.mean(owd472)
# au27 = numpy.min(owd471)/numpy.min(owd472)
# au28 = numpy.min(owd471)/numpy.max(owd472)

# au29 = numpy.max(owd471)/numpy.mean(owd472)
# au30 = numpy.max(owd471)/numpy.min(owd472)
# au31 = numpy.max(owd471)/numpy.max(owd472)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(au1)+"\n"
# print "avg-win3 / min-win1 = "+ str(au2)+"\n"
# print "avg-win3 / max-win1 = "+ str(au3)+"\n"

# print "min-win3 / avg-win1 = "+ str(au4)+"\n"
# print "min-win3 / min-win1 = "+ str(au5)+"\n"
# print "min-win3 / max-win1 = "+ str(au6)+"\n"

# print "max-win3 / avg-win1 = "+ str(au7)+"\n"
# print "max-win3 / min-win1 = "+ str(au8)+"\n"
# print "max-win3 / max-win1 = "+ str(au9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(au10)+"\n"
# print "avg-win3 / min-win2 = "+ str(au11)+"\n"
# print "avg-win3 / max-win2 = "+ str(au12)+"\n"

# print "min-win3 / avg-win2 = "+ str(au13)+"\n"
# print "min-win3 / min-win2 = "+ str(au14)+"\n"
# print "min-win3 / max-win2 = "+ str(au15)+"\n"

# print "max-win3 / avg-win2 = "+ str(au16)+"\n"
# print "max-win3 / min-win2 = "+ str(au17)+"\n"
# print "max-win3 / max-win2 = "+ str(au18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(au19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(au20)+"\n"
# print "std-win3 / std-win2 = "+ str(au21)+"\n"
# print "std-win1 / std-win2 = "+ str(au22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(au23)+"\n"
# print "avg-win1 / min-win2 = "+ str(au24)+"\n"
# print "avg-win1 / max-win2 = "+ str(au25)+"\n"

# print "min-win1 / avg-win2 = "+ str(au26)+"\n"
# print "min-win1 / min-win2 = "+ str(au27)+"\n"
# print "min-win1 / max-win2 = "+ str(au28)+"\n"

# print "max-win1 / avg-win2 = "+ str(au29)+"\n"
# print "max-win1 / min-win2 = "+ str(au30)+"\n"
# print "max-win1 / max-win2 = "+ str(au31)+"\n"

# print "#################################################"

# ########################################

# """LOSS # 48"""
# print "Loss # 48"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind481=win_index[47]-300
# ind482=win_index[47]-150
# ind483=win_index[47]

# print "\n index number for loss 48", ind481, ind482, ind483

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd481=[]
# owd482=[]
# owd483=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind481 and nn<=ind482:
# 		owd481.append(iat[nn])
# 	elif nn>ind482 and nn<=ind483:
# 		owd482.append(iat[nn])
# 	elif nn>ind483 and nn<=ind483+150:
# 		owd483.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd481"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd481))
# """ owd481 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd481))
# """owd481 min"""
# print 'min11 = {}'.format(min(owd481))
# """owd481 max"""
# print 'max11 = {}'.format(max(owd481))
# """ owd481 std"""
# print 'std11 = {}'.format(numpy.std(owd481))

# """for owd482"""
# print "number of packets included = {}".format(len(owd482))
# print 'mean12 = {}'.format(numpy.mean(owd482))
# print 'min12 = {}'.format(min(owd482))
# print 'max12 = {}'.format(max(owd482))
# print 'std12 = {}'.format(numpy.std(owd482))

# """ for owd483"""
# print "number of packets included = {}".format(len(owd483))
# print 'mean13 = {}'.format(numpy.mean(owd483))
# print 'min13 = {}'.format(min(owd483))
# print 'max13 = {}'.format(max(owd483))
# print 'std13 = {}'.format(numpy.std(owd483))


# """ next take the Window3/Window1""" 
# av1 = numpy.mean(owd483)/numpy.mean(owd481)
# av2 = numpy.mean(owd483)/numpy.min(owd481)
# av3 = numpy.mean(owd483)/numpy.max(owd481)

# av4 = numpy.min(owd483)/numpy.mean(owd481)
# av5 = numpy.min(owd483)/numpy.min(owd481)
# av6 = numpy.min(owd483)/numpy.max(owd481)

# av7 = numpy.max(owd483)/numpy.mean(owd481)
# av8 = numpy.max(owd483)/numpy.min(owd481)
# av9 = numpy.max(owd483)/numpy.max(owd481)

# """next take the Window3/Window2"""
# av10 = numpy.mean(owd483)/numpy.mean(owd482)
# av11 = numpy.mean(owd483)/numpy.min(owd482)
# av12 = numpy.mean(owd483)/numpy.max(owd482)

# av13 = numpy.min(owd483)/numpy.mean(owd482)
# av14 = numpy.min(owd483)/numpy.min(owd482)
# av15 = numpy.min(owd483)/numpy.max(owd482)

# av16 = numpy.max(owd483)/numpy.mean(owd482)
# av17 = numpy.max(owd483)/numpy.min(owd482)
# av18 = numpy.max(owd483)/numpy.max(owd482)

# """ min/max window 3"""
# av19 = numpy.min(owd483)/numpy.max(owd483)

# """standard dev values"""
# av20 = numpy.std(owd483)/numpy.std(owd481)
# av21 = numpy.std(owd483)/numpy.std(owd482)
# av22 = numpy.std(owd481)/numpy.std(owd482)

# """next window1 / window2"""
# av23 = numpy.mean(owd481)/numpy.mean(owd482)
# av24 = numpy.mean(owd481)/numpy.min(owd482)
# av25 = numpy.mean(owd481)/numpy.max(owd482)

# av26 = numpy.min(owd481)/numpy.mean(owd482)
# av27 = numpy.min(owd481)/numpy.min(owd482)
# av28 = numpy.min(owd481)/numpy.max(owd482)

# av29 = numpy.max(owd481)/numpy.mean(owd482)
# av30 = numpy.max(owd481)/numpy.min(owd482)
# av31 = numpy.max(owd481)/numpy.max(owd482)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(av1)+"\n"
# print "avg-win3 / min-win1 = "+ str(av2)+"\n"
# print "avg-win3 / max-win1 = "+ str(av3)+"\n"

# print "min-win3 / avg-win1 = "+ str(av4)+"\n"
# print "min-win3 / min-win1 = "+ str(av5)+"\n"
# print "min-win3 / max-win1 = "+ str(av6)+"\n"

# print "max-win3 / avg-win1 = "+ str(av7)+"\n"
# print "max-win3 / min-win1 = "+ str(av8)+"\n"
# print "max-win3 / max-win1 = "+ str(av9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(av10)+"\n"
# print "avg-win3 / min-win2 = "+ str(av11)+"\n"
# print "avg-win3 / max-win2 = "+ str(av12)+"\n"

# print "min-win3 / avg-win2 = "+ str(av13)+"\n"
# print "min-win3 / min-win2 = "+ str(av14)+"\n"
# print "min-win3 / max-win2 = "+ str(av15)+"\n"

# print "max-win3 / avg-win2 = "+ str(av16)+"\n"
# print "max-win3 / min-win2 = "+ str(av17)+"\n"
# print "max-win3 / max-win2 = "+ str(av18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(av19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(av20)+"\n"
# print "std-win3 / std-win2 = "+ str(av21)+"\n"
# print "std-win1 / std-win2 = "+ str(av22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(av23)+"\n"
# print "avg-win1 / min-win2 = "+ str(av24)+"\n"
# print "avg-win1 / max-win2 = "+ str(av25)+"\n"

# print "min-win1 / avg-win2 = "+ str(av26)+"\n"
# print "min-win1 / min-win2 = "+ str(av27)+"\n"
# print "min-win1 / max-win2 = "+ str(av28)+"\n"

# print "max-win1 / avg-win2 = "+ str(av29)+"\n"
# print "max-win1 / min-win2 = "+ str(av30)+"\n"
# print "max-win1 / max-win2 = "+ str(av31)+"\n"

# print "#################################################"
# ########################################

# """LOSS # 49"""
# print "Loss # 49"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind491=win_index[48]-300
# ind492=win_index[48]-150
# ind493=win_index[48]

# print "\n index number for loss 49", ind491, ind492, ind493

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd491=[]
# owd492=[]
# owd493=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind491 and nn<=ind492:
# 		owd491.append(iat[nn])
# 	elif nn>ind492 and nn<=ind493:
# 		owd492.append(iat[nn])
# 	elif nn>ind493 and nn<=ind493+150:
# 		owd493.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd491"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd491))
# """ owd491 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd491))
# """owd491 min"""
# print 'min11 = {}'.format(min(owd491))
# """owd491 max"""
# print 'max11 = {}'.format(max(owd491))
# """ owd491 std"""
# print 'std11 = {}'.format(numpy.std(owd491))

# """for owd492"""
# print "number of packets included = {}".format(len(owd492))
# print 'mean12 = {}'.format(numpy.mean(owd492))
# print 'min12 = {}'.format(min(owd492))
# print 'max12 = {}'.format(max(owd492))
# print 'std12 = {}'.format(numpy.std(owd492))

# """ for owd493"""
# print "number of packets included = {}".format(len(owd493))
# print 'mean13 = {}'.format(numpy.mean(owd493))
# print 'min13 = {}'.format(min(owd493))
# print 'max13 = {}'.format(max(owd493))
# print 'std13 = {}'.format(numpy.std(owd493))


# """ next take the Window3/Window1""" 
# aw1 = numpy.mean(owd493)/numpy.mean(owd491)
# aw2 = numpy.mean(owd493)/numpy.min(owd491)
# aw3 = numpy.mean(owd493)/numpy.max(owd491)

# aw4 = numpy.min(owd493)/numpy.mean(owd491)
# aw5 = numpy.min(owd493)/numpy.min(owd491)
# aw6 = numpy.min(owd493)/numpy.max(owd491)

# aw7 = numpy.max(owd493)/numpy.mean(owd491)
# aw8 = numpy.max(owd493)/numpy.min(owd491)
# aw9 = numpy.max(owd493)/numpy.max(owd491)

# """next take the Window3/Window2"""
# aw10 = numpy.mean(owd493)/numpy.mean(owd492)
# aw11 = numpy.mean(owd493)/numpy.min(owd492)
# aw12 = numpy.mean(owd493)/numpy.max(owd492)

# aw13 = numpy.min(owd493)/numpy.mean(owd492)
# aw14 = numpy.min(owd493)/numpy.min(owd492)
# aw15 = numpy.min(owd493)/numpy.max(owd492)

# aw16 = numpy.max(owd493)/numpy.mean(owd492)
# aw17 = numpy.max(owd493)/numpy.min(owd492)
# aw18 = numpy.max(owd493)/numpy.max(owd492)

# """ min/max window 3"""
# aw19 = numpy.min(owd493)/numpy.max(owd493)

# """standard dev values"""
# aw20 = numpy.std(owd493)/numpy.std(owd491)
# aw21 = numpy.std(owd493)/numpy.std(owd492)
# aw22 = numpy.std(owd491)/numpy.std(owd492)

# """next window1 / window2"""
# aw23 = numpy.mean(owd491)/numpy.mean(owd492)
# aw24 = numpy.mean(owd491)/numpy.min(owd492)
# aw25 = numpy.mean(owd491)/numpy.max(owd492)

# aw26 = numpy.min(owd491)/numpy.mean(owd492)
# aw27 = numpy.min(owd491)/numpy.min(owd492)
# aw28 = numpy.min(owd491)/numpy.max(owd492)

# aw29 = numpy.max(owd491)/numpy.mean(owd492)
# aw30 = numpy.max(owd491)/numpy.min(owd492)
# aw31 = numpy.max(owd491)/numpy.max(owd492)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(aw1)+"\n"
# print "avg-win3 / min-win1 = "+ str(aw2)+"\n"
# print "avg-win3 / max-win1 = "+ str(aw3)+"\n"

# print "min-win3 / avg-win1 = "+ str(aw4)+"\n"
# print "min-win3 / min-win1 = "+ str(aw5)+"\n"
# print "min-win3 / max-win1 = "+ str(aw6)+"\n"

# print "max-win3 / avg-win1 = "+ str(aw7)+"\n"
# print "max-win3 / min-win1 = "+ str(aw8)+"\n"
# print "max-win3 / max-win1 = "+ str(aw9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(aw10)+"\n"
# print "avg-win3 / min-win2 = "+ str(aw11)+"\n"
# print "avg-win3 / max-win2 = "+ str(aw12)+"\n"

# print "min-win3 / avg-win2 = "+ str(aw13)+"\n"
# print "min-win3 / min-win2 = "+ str(aw14)+"\n"
# print "min-win3 / max-win2 = "+ str(aw15)+"\n"

# print "max-win3 / avg-win2 = "+ str(aw16)+"\n"
# print "max-win3 / min-win2 = "+ str(aw17)+"\n"
# print "max-win3 / max-win2 = "+ str(aw18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(aw19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(aw20)+"\n"
# print "std-win3 / std-win2 = "+ str(aw21)+"\n"
# print "std-win1 / std-win2 = "+ str(aw22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(aw23)+"\n"
# print "avg-win1 / min-win2 = "+ str(aw24)+"\n"
# print "avg-win1 / max-win2 = "+ str(aw25)+"\n"

# print "min-win1 / avg-win2 = "+ str(aw26)+"\n"
# print "min-win1 / min-win2 = "+ str(aw27)+"\n"
# print "min-win1 / max-win2 = "+ str(aw28)+"\n"

# print "max-win1 / avg-win2 = "+ str(aw29)+"\n"
# print "max-win1 / min-win2 = "+ str(aw30)+"\n"
# print "max-win1 / max-win2 = "+ str(aw31)+"\n"

# print "#################################################"

# ########################################
# ########################################

# """LOSS # 50"""
# print "Loss # 50"

# """SECOND VALUE OF WIN INDEX, AND TAKE ONLY 150 IN EACH WINDOW 1,2,3"""
# ind501=win_index[49]-300
# ind502=win_index[49]-150
# ind503=win_index[49]

# print "\n index number for loss 50", ind501, ind502, ind503

# """ CALCULATION FOR SECOND PEAK PARAMETERS (WIN 1,2,3)"""
# owd501=[]
# owd502=[]
# owd503=[]

# """APPENDING THE DELAYS INTO OWD VARIABLES"""
# for nn in range(len(iat)):
# 	if nn>ind501 and nn<=ind502:
# 		owd501.append(iat[nn])
# 	elif nn>ind502 and nn<=ind503:
# 		owd502.append(iat[nn])
# 	elif nn>ind503 and nn<=ind503+150:
# 		owd503.append(iat[nn])
# 		# print x[nn], d[nn]
		

# """ TAKE THE AVG, MAX MIN OF EACH WINDOW"""

# """ for owd501"""

# """ Number of packet in a window"""
# print "number of packets included = {}".format(len(owd501))
# """ owd501 avg"""
# print 'mean11 = {}'.format(numpy.mean(owd501))
# """owd501 min"""
# print 'min11 = {}'.format(min(owd501))
# """owd501 max"""
# print 'max11 = {}'.format(max(owd501))
# """ owd501 std"""
# print 'std11 = {}'.format(numpy.std(owd501))

# """for owd502"""
# print "number of packets included = {}".format(len(owd502))
# print 'mean12 = {}'.format(numpy.mean(owd502))
# print 'min12 = {}'.format(min(owd502))
# print 'max12 = {}'.format(max(owd502))
# print 'std12 = {}'.format(numpy.std(owd502))

# """ for owd503"""
# print "number of packets included = {}".format(len(owd503))
# print 'mean13 = {}'.format(numpy.mean(owd503))
# print 'min13 = {}'.format(min(owd503))
# print 'max13 = {}'.format(max(owd503))
# print 'std13 = {}'.format(numpy.std(owd503))


# """ next take the Window3/Window1""" 
# ax1 = numpy.mean(owd503)/numpy.mean(owd501)
# ax2 = numpy.mean(owd503)/numpy.min(owd501)
# ax3 = numpy.mean(owd503)/numpy.max(owd501)

# ax4 = numpy.min(owd503)/numpy.mean(owd501)
# ax5 = numpy.min(owd503)/numpy.min(owd501)
# ax6 = numpy.min(owd503)/numpy.max(owd501)

# ax7 = numpy.max(owd503)/numpy.mean(owd501)
# ax8 = numpy.max(owd503)/numpy.min(owd501)
# ax9 = numpy.max(owd503)/numpy.max(owd501)

# """next take the Window3/Window2"""
# ax10 = numpy.mean(owd503)/numpy.mean(owd502)
# ax11 = numpy.mean(owd503)/numpy.min(owd502)
# ax12 = numpy.mean(owd503)/numpy.max(owd502)

# ax13 = numpy.min(owd503)/numpy.mean(owd502)
# ax14 = numpy.min(owd503)/numpy.min(owd502)
# ax15 = numpy.min(owd503)/numpy.max(owd502)

# ax16 = numpy.max(owd503)/numpy.mean(owd502)
# ax17 = numpy.max(owd503)/numpy.min(owd502)
# ax18 = numpy.max(owd503)/numpy.max(owd502)

# """ min/max window 3"""
# ax19 = numpy.min(owd503)/numpy.max(owd503)

# """standard dev values"""
# ax20 = numpy.std(owd503)/numpy.std(owd501)
# ax21 = numpy.std(owd503)/numpy.std(owd502)
# ax22 = numpy.std(owd501)/numpy.std(owd502)

# """next window1 / window2"""
# ax23 = numpy.mean(owd501)/numpy.mean(owd502)
# ax24 = numpy.mean(owd501)/numpy.min(owd502)
# ax25 = numpy.mean(owd501)/numpy.max(owd502)

# ax26 = numpy.min(owd501)/numpy.mean(owd502)
# ax27 = numpy.min(owd501)/numpy.min(owd502)
# ax28 = numpy.min(owd501)/numpy.max(owd502)

# ax29 = numpy.max(owd501)/numpy.mean(owd502)
# ax30 = numpy.max(owd501)/numpy.min(owd502)
# ax31 = numpy.max(owd501)/numpy.max(owd502)

# """PRINTING THE VALUES Window3/Window1"""
# """Win3 / Win 1"""
# print "avg-win3 / avg-win1 = "+ str(ax1)+"\n"
# print "avg-win3 / min-win1 = "+ str(ax2)+"\n"
# print "avg-win3 / max-win1 = "+ str(ax3)+"\n"

# print "min-win3 / avg-win1 = "+ str(ax4)+"\n"
# print "min-win3 / min-win1 = "+ str(ax5)+"\n"
# print "min-win3 / max-win1 = "+ str(ax6)+"\n"

# print "max-win3 / avg-win1 = "+ str(ax7)+"\n"
# print "max-win3 / min-win1 = "+ str(ax8)+"\n"
# print "max-win3 / max-win1 = "+ str(ax9)+"\n"


# """Window3/Window2"""
# print "avg-win3 / avg-win2 = "+ str(ax10)+"\n"
# print "avg-win3 / min-win2 = "+ str(ax11)+"\n"
# print "avg-win3 / max-win2 = "+ str(ax12)+"\n"

# print "min-win3 / avg-win2 = "+ str(ax13)+"\n"
# print "min-win3 / min-win2 = "+ str(ax14)+"\n"
# print "min-win3 / max-win2 = "+ str(ax15)+"\n"

# print "max-win3 / avg-win2 = "+ str(ax16)+"\n"
# print "max-win3 / min-win2 = "+ str(ax17)+"\n"
# print "max-win3 / max-win2 = "+ str(ax18)+"\n"

# """ min/max of window3"""
# print "min-win3 / max-win3 = "+ str(ax19)+"\n"

# """ Standar dev values"""
# print "std-win3 / std-win1 = "+ str(ax20)+"\n"
# print "std-win3 / std-win2 = "+ str(ax21)+"\n"
# print "std-win1 / std-win2 = "+ str(ax22)+"\n"

# """ window1 / window2"""
# print "avg-win1 / avg-win2 = "+ str(ax23)+"\n"
# print "avg-win1 / min-win2 = "+ str(ax24)+"\n"
# print "avg-win1 / max-win2 = "+ str(ax25)+"\n"

# print "min-win1 / avg-win2 = "+ str(ax26)+"\n"
# print "min-win1 / min-win2 = "+ str(ax27)+"\n"
# print "min-win1 / max-win2 = "+ str(ax28)+"\n"

# print "max-win1 / avg-win2 = "+ str(ax29)+"\n"
# print "max-win1 / min-win2 = "+ str(ax30)+"\n"
# print "max-win1 / max-win2 = "+ str(ax31)+"\n"

# print "#################################################"



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
		str(l25)+","+str(l26)+","+str(l27)+","+str(l28)+","+str(l29)+","+str(l30)+","+str(l31)+","+"n""\n")
		# +str(m1)+","+str(m2)+","+str(m3)+","+str(m4)+","+str(m5)+","+str(m6)+","+str(m7)+","+str(m8)+","+
		# str(m9)+","+str(m10)+","+str(m11)+","+str(m12)+","+str(m13)+","+str(m14)+","+str(m15)+","+str(m16)+","+
		# str(m17)+","+str(m18)+","+str(m19)+","+str(m20)+","+str(m21)+","+str(m22)+","+str(m23)+","+str(m24)+","+
		# str(m25)+","+str(m26)+","+str(m27)+","+str(m28)+","+str(m29)+","+str(m30)+","+str(m31)+","+"n""\n"
		# +str(n1)+","+str(n2)+","+str(n3)+","+str(n4)+","+str(n5)+","+str(n6)+","+str(n7)+","+str(n8)+","+
		# str(n9)+","+str(n10)+","+str(n11)+","+str(n12)+","+str(n13)+","+str(n14)+","+str(n15)+","+str(n16)+","+
		# str(n17)+","+str(n18)+","+str(n19)+","+str(n20)+","+str(n21)+","+str(n22)+","+str(n23)+","+str(n24)+","+
		# str(n25)+","+str(n26)+","+str(n27)+","+str(n28)+","+str(n29)+","+str(n30)+","+str(n31)+","+"n""\n"
		# +str(o1)+","+str(o2)+","+str(o3)+","+str(o4)+","+str(o5)+","+str(o6)+","+str(o7)+","+str(o8)+","+
		# str(o9)+","+str(o10)+","+str(o11)+","+str(o12)+","+str(o13)+","+str(o14)+","+str(o15)+","+str(o16)+","+
		# str(o17)+","+str(o18)+","+str(o19)+","+str(o20)+","+str(o21)+","+str(o22)+","+str(o23)+","+str(o24)+","+
		# str(o25)+","+str(o26)+","+str(o27)+","+str(o28)+","+str(o29)+","+str(o30)+","+str(o31)+","+"n""\n"
		# +str(p1)+","+str(p2)+","+str(p3)+","+str(p4)+","+str(p5)+","+str(p6)+","+str(p7)+","+str(p8)+","+
		# str(p9)+","+str(p10)+","+str(p11)+","+str(p12)+","+str(p13)+","+str(p14)+","+str(p15)+","+str(p16)+","+
		# str(p17)+","+str(p18)+","+str(p19)+","+str(p20)+","+str(p21)+","+str(p22)+","+str(p23)+","+str(p24)+","+
		# str(p25)+","+str(p26)+","+str(p27)+","+str(p28)+","+str(p29)+","+str(p30)+","+str(p31)+","+"n""\n"
		# +str(q1)+","+str(q2)+","+str(q3)+","+str(q4)+","+str(q5)+","+str(q6)+","+str(q7)+","+str(q8)+","+
		# str(q9)+","+str(q10)+","+str(q11)+","+str(q12)+","+str(q13)+","+str(q14)+","+str(q15)+","+str(q16)+","+
		# str(q17)+","+str(q18)+","+str(q19)+","+str(q20)+","+str(q21)+","+str(q22)+","+str(q23)+","+str(q24)+","+
		# str(q25)+","+str(q26)+","+str(q27)+","+str(q28)+","+str(q29)+","+str(q30)+","+str(q31)+","+"n""\n"
		# +str(r1)+","+str(r2)+","+str(r3)+","+str(r4)+","+str(r5)+","+str(r6)+","+str(r7)+","+str(r8)+","+
		# str(r9)+","+str(r10)+","+str(r11)+","+str(r12)+","+str(r13)+","+str(r14)+","+str(r15)+","+str(r16)+","+
		# str(r17)+","+str(r18)+","+str(r19)+","+str(r20)+","+str(r21)+","+str(r22)+","+str(r23)+","+str(r24)+","+
		# str(r25)+","+str(r26)+","+str(r27)+","+str(r28)+","+str(r29)+","+str(r30)+","+str(r31)+","+"n""\n"
		# +str(s1)+","+str(s2)+","+str(s3)+","+str(s4)+","+str(s5)+","+str(s6)+","+str(s7)+","+str(s8)+","+
		# str(s9)+","+str(s10)+","+str(s11)+","+str(s12)+","+str(s13)+","+str(s14)+","+str(s15)+","+str(s16)+","+
		# str(s17)+","+str(s18)+","+str(s19)+","+str(s20)+","+str(s21)+","+str(s22)+","+str(s23)+","+str(s24)+","+
		# str(s25)+","+str(s26)+","+str(s27)+","+str(s28)+","+str(s29)+","+str(s30)+","+str(s31)+","+"n""\n"
		# +str(t1)+","+str(t2)+","+str(t3)+","+str(t4)+","+str(t5)+","+str(t6)+","+str(t7)+","+str(t8)+","+
		# str(t9)+","+str(t10)+","+str(t11)+","+str(t12)+","+str(t13)+","+str(t14)+","+str(t15)+","+str(t16)+","+
		# str(t17)+","+str(t18)+","+str(t19)+","+str(t20)+","+str(t21)+","+str(t22)+","+str(t23)+","+str(t24)+","+
		# str(t25)+","+str(t26)+","+str(t27)+","+str(t28)+","+str(t29)+","+str(t30)+","+str(t31)+","+"n""\n"
		# +str(u1)+","+str(u2)+","+str(u3)+","+str(u4)+","+str(u5)+","+str(u6)+","+str(u7)+","+str(u8)+","+
		# str(u9)+","+str(u10)+","+str(u11)+","+str(u12)+","+str(u13)+","+str(u14)+","+str(u15)+","+str(u16)+","+
		# str(u17)+","+str(u18)+","+str(u19)+","+str(u20)+","+str(u21)+","+str(u22)+","+str(u23)+","+str(u24)+","+
		# str(u25)+","+str(u26)+","+str(u27)+","+str(u28)+","+str(u29)+","+str(u30)+","+str(u31)+","+"n""\n"
		# +str(v1)+","+str(v2)+","+str(v3)+","+str(v4)+","+str(v5)+","+str(v6)+","+str(v7)+","+str(v8)+","+
		# str(v9)+","+str(v10)+","+str(v11)+","+str(v12)+","+str(v13)+","+str(v14)+","+str(v15)+","+str(v16)+","+
		# str(v17)+","+str(v18)+","+str(v19)+","+str(v20)+","+str(v21)+","+str(v22)+","+str(v23)+","+str(v24)+","+
		# str(v25)+","+str(v26)+","+str(v27)+","+str(v28)+","+str(v29)+","+str(v30)+","+str(v31)+","+"n""\n"
		# +str(w1)+","+str(w2)+","+str(w3)+","+str(w4)+","+str(w5)+","+str(w6)+","+str(w7)+","+str(w8)+","+
		# str(w9)+","+str(w10)+","+str(w11)+","+str(w12)+","+str(w13)+","+str(w14)+","+str(w15)+","+str(w16)+","+
		# str(w17)+","+str(w18)+","+str(w19)+","+str(w20)+","+str(w21)+","+str(w22)+","+str(w23)+","+str(w24)+","+
		# str(w25)+","+str(w26)+","+str(w27)+","+str(w28)+","+str(w29)+","+str(w30)+","+str(w31)+","+"n""\n"
		# +str(x1)+","+str(x2)+","+str(x3)+","+str(x4)+","+str(x5)+","+str(x6)+","+str(x7)+","+str(x8)+","+
		# str(x9)+","+str(x10)+","+str(x11)+","+str(x12)+","+str(x13)+","+str(x14)+","+str(x15)+","+str(x16)+","+
		# str(x17)+","+str(x18)+","+str(x19)+","+str(x20)+","+str(x21)+","+str(x22)+","+str(x23)+","+str(x24)+","+
		# str(x25)+","+str(x26)+","+str(x27)+","+str(x28)+","+str(x29)+","+str(x30)+","+str(x31)+","+"n""\n"
		# +str(y1)+","+str(y2)+","+str(y3)+","+str(y4)+","+str(y5)+","+str(y6)+","+str(y7)+","+str(y8)+","+
		# str(y9)+","+str(y10)+","+str(y11)+","+str(y12)+","+str(y13)+","+str(y14)+","+str(y15)+","+str(y16)+","+
		# str(y17)+","+str(y18)+","+str(y19)+","+str(y20)+","+str(y21)+","+str(y22)+","+str(y23)+","+str(y24)+","+
		# str(y25)+","+str(y26)+","+str(y27)+","+str(y28)+","+str(y29)+","+str(y30)+","+str(y31)+","+"n""\n"
		# +str(z1)+","+str(z2)+","+str(z3)+","+str(z4)+","+str(z5)+","+str(z6)+","+str(z7)+","+str(z8)+","+
		# str(z9)+","+str(z10)+","+str(z11)+","+str(z12)+","+str(z13)+","+str(z14)+","+str(z15)+","+str(z16)+","+
		# str(z17)+","+str(z18)+","+str(z19)+","+str(z20)+","+str(z21)+","+str(z22)+","+str(z23)+","+str(z24)+","+
		# str(z25)+","+str(z26)+","+str(z27)+","+str(z28)+","+str(z29)+","+str(z30)+","+str(z31)+","+"n""\n"
		# +str(aa1)+","+str(aa2)+","+str(aa3)+","+str(aa4)+","+str(aa5)+","+str(aa6)+","+str(aa7)+","+str(aa8)+","+
		# str(aa9)+","+str(aa10)+","+str(aa11)+","+str(aa12)+","+str(aa13)+","+str(aa14)+","+str(aa15)+","+str(aa16)+","+
		# str(aa17)+","+str(aa18)+","+str(aa19)+","+str(aa20)+","+str(aa21)+","+str(aa22)+","+str(aa23)+","+str(aa24)+","+
		# str(aa25)+","+str(aa26)+","+str(aa27)+","+str(aa28)+","+str(aa29)+","+str(aa30)+","+str(aa31)+","+"n""\n"
		# +str(ab1)+","+str(ab2)+","+str(ab3)+","+str(ab4)+","+str(ab5)+","+str(ab6)+","+str(ab7)+","+str(ab8)+","+
		# str(ab9)+","+str(ab10)+","+str(ab11)+","+str(ab12)+","+str(ab13)+","+str(ab14)+","+str(ab15)+","+str(ab16)+","+
		# str(ab17)+","+str(ab18)+","+str(ab19)+","+str(ab20)+","+str(ab21)+","+str(ab22)+","+str(ab23)+","+str(ab24)+","+
		# str(ab25)+","+str(ab26)+","+str(ab27)+","+str(ab28)+","+str(ab29)+","+str(ab30)+","+str(ab31)+","+"n""\n"
		# +str(ac1)+","+str(ac2)+","+str(ac3)+","+str(ac4)+","+str(ac5)+","+str(ac6)+","+str(ac7)+","+str(ac8)+","+
		# str(ac9)+","+str(ac10)+","+str(ac11)+","+str(ac12)+","+str(ac13)+","+str(ac14)+","+str(ac15)+","+str(ac16)+","+
		# str(ac17)+","+str(ac18)+","+str(ac19)+","+str(ac20)+","+str(ac21)+","+str(ac22)+","+str(ac23)+","+str(ac24)+","+
		# str(ac25)+","+str(ac26)+","+str(ac27)+","+str(ac28)+","+str(ac29)+","+str(ac30)+","+str(ac31)+","+"n""\n"
		# +str(ad1)+","+str(ad2)+","+str(ad3)+","+str(ad4)+","+str(ad5)+","+str(ad6)+","+str(ad7)+","+str(ad8)+","+
		# str(ad9)+","+str(ad10)+","+str(ad11)+","+str(ad12)+","+str(ad13)+","+str(ad14)+","+str(ad15)+","+str(ad16)+","+
		# str(ad17)+","+str(ad18)+","+str(ad19)+","+str(ad20)+","+str(ad21)+","+str(ad22)+","+str(ad23)+","+str(ad24)+","+
		# str(ad25)+","+str(ad26)+","+str(ad27)+","+str(ad28)+","+str(ad29)+","+str(ad30)+","+str(ad31)+","+"n""\n"
		# +str(ae1)+","+str(ae2)+","+str(ae3)+","+str(ae4)+","+str(ae5)+","+str(ae6)+","+str(ae7)+","+str(ae8)+","+
		# str(ae9)+","+str(ae10)+","+str(ae11)+","+str(ae12)+","+str(ae13)+","+str(ae14)+","+str(ae15)+","+str(ae16)+","+
		# str(ae17)+","+str(ae18)+","+str(ae19)+","+str(ae20)+","+str(ae21)+","+str(ae22)+","+str(ae23)+","+str(ae24)+","+
		# str(ae25)+","+str(ae26)+","+str(ae27)+","+str(ae28)+","+str(ae29)+","+str(ae30)+","+str(ae31)+","+"n""\n"
		# +str(af1)+","+str(af2)+","+str(af3)+","+str(af4)+","+str(af5)+","+str(af6)+","+str(af7)+","+str(af8)+","+
		# str(af9)+","+str(af10)+","+str(af11)+","+str(af12)+","+str(af13)+","+str(af14)+","+str(af15)+","+str(af16)+","+
		# str(af17)+","+str(af18)+","+str(af19)+","+str(af20)+","+str(af21)+","+str(af22)+","+str(af23)+","+str(af24)+","+
		# str(af25)+","+str(af26)+","+str(af27)+","+str(af28)+","+str(af29)+","+str(af30)+","+str(af31)+","+"n""\n"
		# +str(ag1)+","+str(ag2)+","+str(ag3)+","+str(ag4)+","+str(ag5)+","+str(ag6)+","+str(ag7)+","+str(ag8)+","+
		# str(ag9)+","+str(ag10)+","+str(ag11)+","+str(ag12)+","+str(ag13)+","+str(ag14)+","+str(ag15)+","+str(ag16)+","+
		# str(ag17)+","+str(ag18)+","+str(ag19)+","+str(ag20)+","+str(ag21)+","+str(ag22)+","+str(ag23)+","+str(ag24)+","+
		# str(ag25)+","+str(ag26)+","+str(ag27)+","+str(ag28)+","+str(ag29)+","+str(ag30)+","+str(ag31)+","+"n""\n"
		# +str(ah1)+","+str(ah2)+","+str(ah3)+","+str(ah4)+","+str(ah5)+","+str(ah6)+","+str(ah7)+","+str(ah8)+","+
		# str(ah9)+","+str(ah10)+","+str(ah11)+","+str(ah12)+","+str(ah13)+","+str(ah14)+","+str(ah15)+","+str(ah16)+","+
		# str(ah17)+","+str(ah18)+","+str(ah19)+","+str(ah20)+","+str(ah21)+","+str(ah22)+","+str(ah23)+","+str(ah24)+","+
		# str(ah25)+","+str(ah26)+","+str(ah27)+","+str(ah28)+","+str(ah29)+","+str(ah30)+","+str(ah31)+","+"n""\n"
		# +str(ai1)+","+str(ai2)+","+str(ai3)+","+str(ai4)+","+str(ai5)+","+str(ai6)+","+str(ai7)+","+str(ai8)+","+
		# str(ai9)+","+str(ai10)+","+str(ai11)+","+str(ai12)+","+str(ai13)+","+str(ai14)+","+str(ai15)+","+str(ai16)+","+
		# str(ai17)+","+str(ai18)+","+str(ai19)+","+str(ai20)+","+str(ai21)+","+str(ai22)+","+str(ai23)+","+str(ai24)+","+
		# str(ai25)+","+str(ai26)+","+str(ai27)+","+str(ai28)+","+str(ai29)+","+str(ai30)+","+str(ai31)+","+"n""\n"
		# +str(aj1)+","+str(aj2)+","+str(aj3)+","+str(aj4)+","+str(aj5)+","+str(aj6)+","+str(aj7)+","+str(aj8)+","+
		# str(aj9)+","+str(aj10)+","+str(aj11)+","+str(aj12)+","+str(aj13)+","+str(aj14)+","+str(aj15)+","+str(aj16)+","+
		# str(aj17)+","+str(aj18)+","+str(aj19)+","+str(aj20)+","+str(aj21)+","+str(aj22)+","+str(aj23)+","+str(aj24)+","+
		# str(aj25)+","+str(aj26)+","+str(aj27)+","+str(aj28)+","+str(aj29)+","+str(aj30)+","+str(aj31)+","+"n""\n"
		# +str(ak1)+","+str(ak2)+","+str(ak3)+","+str(ak4)+","+str(ak5)+","+str(ak6)+","+str(ak7)+","+str(ak8)+","+
		# str(ak9)+","+str(ak10)+","+str(ak11)+","+str(ak12)+","+str(ak13)+","+str(ak14)+","+str(ak15)+","+str(ak16)+","+
		# str(ak17)+","+str(ak18)+","+str(ak19)+","+str(ak20)+","+str(ak21)+","+str(ak22)+","+str(ak23)+","+str(ak24)+","+
		# str(ak25)+","+str(ak26)+","+str(ak27)+","+str(ak28)+","+str(ak29)+","+str(ak30)+","+str(ak31)+","+"n""\n"
		# +str(al1)+","+str(al2)+","+str(al3)+","+str(al4)+","+str(al5)+","+str(al6)+","+str(al7)+","+str(al8)+","+
		# str(al9)+","+str(al10)+","+str(al11)+","+str(al12)+","+str(al13)+","+str(al14)+","+str(al15)+","+str(al16)+","+
		# str(al17)+","+str(al18)+","+str(al19)+","+str(al20)+","+str(al21)+","+str(al22)+","+str(al23)+","+str(al24)+","+
		# str(al25)+","+str(al26)+","+str(al27)+","+str(al28)+","+str(al29)+","+str(al30)+","+str(al31)+","+"n""\n"
		# +str(am1)+","+str(am2)+","+str(am3)+","+str(am4)+","+str(am5)+","+str(am6)+","+str(am7)+","+str(am8)+","+
		# str(am9)+","+str(am10)+","+str(am11)+","+str(am12)+","+str(am13)+","+str(am14)+","+str(am15)+","+str(am16)+","+
		# str(am17)+","+str(am18)+","+str(am19)+","+str(am20)+","+str(am21)+","+str(am22)+","+str(am23)+","+str(am24)+","+
		# str(am25)+","+str(am26)+","+str(am27)+","+str(am28)+","+str(am29)+","+str(am30)+","+str(am31)+","+"n""\n"
		# +str(an1)+","+str(an2)+","+str(an3)+","+str(an4)+","+str(an5)+","+str(an6)+","+str(an7)+","+str(an8)+","+
		# str(an9)+","+str(an10)+","+str(an11)+","+str(an12)+","+str(an13)+","+str(an14)+","+str(an15)+","+str(an16)+","+
		# str(an17)+","+str(an18)+","+str(an19)+","+str(an20)+","+str(an21)+","+str(an22)+","+str(an23)+","+str(an24)+","+
		# str(an25)+","+str(an26)+","+str(an27)+","+str(an28)+","+str(an29)+","+str(an30)+","+str(an31)+","+"n""\n"
		# +str(ao1)+","+str(ao2)+","+str(ao3)+","+str(ao4)+","+str(ao5)+","+str(ao6)+","+str(ao7)+","+str(ao8)+","+
		# str(ao9)+","+str(ao10)+","+str(ao11)+","+str(ao12)+","+str(ao13)+","+str(ao14)+","+str(ao15)+","+str(ao16)+","+
		# str(ao17)+","+str(ao18)+","+str(ao19)+","+str(ao20)+","+str(ao21)+","+str(ao22)+","+str(ao23)+","+str(ao24)+","+
		# str(ao25)+","+str(ao26)+","+str(ao27)+","+str(ao28)+","+str(ao29)+","+str(ao30)+","+str(ao31)+","+"n""\n"
		# +str(ap1)+","+str(ap2)+","+str(ap3)+","+str(ap4)+","+str(ap5)+","+str(ap6)+","+str(ap7)+","+str(ap8)+","+
		# str(ap9)+","+str(ap10)+","+str(ap11)+","+str(ap12)+","+str(ap13)+","+str(ap14)+","+str(ap15)+","+str(ap16)+","+
		# str(ap17)+","+str(ap18)+","+str(ap19)+","+str(ap20)+","+str(ap21)+","+str(ap22)+","+str(ap23)+","+str(ap24)+","+
		# str(ap25)+","+str(ap26)+","+str(ap27)+","+str(ap28)+","+str(ap29)+","+str(ap30)+","+str(ap31)+","+"n""\n"
		# +str(aq1)+","+str(aq2)+","+str(aq3)+","+str(aq4)+","+str(aq5)+","+str(aq6)+","+str(aq7)+","+str(aq8)+","+
		# str(aq9)+","+str(aq10)+","+str(aq11)+","+str(aq12)+","+str(aq13)+","+str(aq14)+","+str(aq15)+","+str(aq16)+","+
		# str(aq17)+","+str(aq18)+","+str(aq19)+","+str(aq20)+","+str(aq21)+","+str(aq22)+","+str(aq23)+","+str(aq24)+","+
		# str(aq25)+","+str(aq26)+","+str(aq27)+","+str(aq28)+","+str(aq29)+","+str(aq30)+","+str(aq31)+","+"n""\n"
		# +str(ar1)+","+str(ar2)+","+str(ar3)+","+str(ar4)+","+str(ar5)+","+str(ar6)+","+str(ar7)+","+str(ar8)+","+
		# str(ar9)+","+str(ar10)+","+str(ar11)+","+str(ar12)+","+str(ar13)+","+str(ar14)+","+str(ar15)+","+str(ar16)+","+
		# str(ar17)+","+str(ar18)+","+str(ar19)+","+str(ar20)+","+str(ar21)+","+str(ar22)+","+str(ar23)+","+str(ar24)+","+
		# str(ar25)+","+str(ar26)+","+str(ar27)+","+str(ar28)+","+str(ar29)+","+str(ar30)+","+str(ar31)+","+"n""\n"
		# +str(as1)+","+str(as2)+","+str(as3)+","+str(as4)+","+str(as5)+","+str(as6)+","+str(as7)+","+str(as8)+","+
		# str(as9)+","+str(as10)+","+str(as11)+","+str(as12)+","+str(as13)+","+str(as14)+","+str(as15)+","+str(as16)+","+
		# str(as17)+","+str(as18)+","+str(as19)+","+str(as20)+","+str(as21)+","+str(as22)+","+str(as23)+","+str(as24)+","+
		# str(as25)+","+str(as26)+","+str(as27)+","+str(as28)+","+str(as29)+","+str(as30)+","+str(as31)+","+"n""\n"
		# +str(at1)+","+str(at2)+","+str(at3)+","+str(at4)+","+str(at5)+","+str(at6)+","+str(at7)+","+str(at8)+","+
		# str(at9)+","+str(at10)+","+str(at11)+","+str(at12)+","+str(at13)+","+str(at14)+","+str(at15)+","+str(at16)+","+
		# str(at17)+","+str(at18)+","+str(at19)+","+str(at20)+","+str(at21)+","+str(at22)+","+str(at23)+","+str(at24)+","+
		# str(at25)+","+str(at26)+","+str(at27)+","+str(at28)+","+str(at29)+","+str(at30)+","+str(at31)+","+"n""\n"
		# +str(au1)+","+str(au2)+","+str(au3)+","+str(au4)+","+str(au5)+","+str(au6)+","+str(au7)+","+str(au8)+","+
		# str(au9)+","+str(au10)+","+str(au11)+","+str(au12)+","+str(au13)+","+str(au14)+","+str(au15)+","+str(au16)+","+
		# str(au17)+","+str(au18)+","+str(au19)+","+str(au20)+","+str(au21)+","+str(au22)+","+str(au23)+","+str(au24)+","+
		# str(au25)+","+str(au26)+","+str(au27)+","+str(au28)+","+str(au29)+","+str(au30)+","+str(au31)+","+"n""\n"
		# +str(av1)+","+str(av2)+","+str(av3)+","+str(av4)+","+str(av5)+","+str(av6)+","+str(av7)+","+str(av8)+","+
		# str(av9)+","+str(av10)+","+str(av11)+","+str(av12)+","+str(av13)+","+str(av14)+","+str(av15)+","+str(av16)+","+
		# str(av17)+","+str(av18)+","+str(av19)+","+str(av20)+","+str(av21)+","+str(av22)+","+str(av23)+","+str(av24)+","+
		# str(av25)+","+str(av26)+","+str(av27)+","+str(av28)+","+str(av29)+","+str(av30)+","+str(av31)+","+"n""\n"
		# +str(aw1)+","+str(aw2)+","+str(aw3)+","+str(aw4)+","+str(aw5)+","+str(aw6)+","+str(aw7)+","+str(aw8)+","+
		# str(aw9)+","+str(aw10)+","+str(aw11)+","+str(aw12)+","+str(aw13)+","+str(aw14)+","+str(aw15)+","+str(aw16)+","+
		# str(aw17)+","+str(aw18)+","+str(aw19)+","+str(aw20)+","+str(aw21)+","+str(aw22)+","+str(aw23)+","+str(aw24)+","+
		# str(aw25)+","+str(aw26)+","+str(aw27)+","+str(aw28)+","+str(aw29)+","+str(aw30)+","+str(aw31)+","+"n""\n"
		# +str(ax1)+","+str(ax2)+","+str(ax3)+","+str(ax4)+","+str(ax5)+","+str(ax6)+","+str(ax7)+","+str(ax8)+","+
		# str(ax9)+","+str(ax10)+","+str(ax11)+","+str(ax12)+","+str(ax13)+","+str(ax14)+","+str(ax15)+","+str(ax16)+","+
		# str(ax17)+","+str(ax18)+","+str(ax19)+","+str(ax20)+","+str(ax21)+","+str(ax22)+","+str(ax23)+","+str(ax24)+","+
		# str(ax25)+","+str(ax26)+","+str(ax27)+","+str(ax28)+","+str(ax29)+","+str(ax30)+","+str(ax31)+","+"n""\n")



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
