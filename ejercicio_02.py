import scipy
import numpy as np
import matplotlib.pyplot as pp

#2a)
x= np.array([7.5,4.48,8.60,7.73,5.28,4.25,6.99,6.31,9.15,5.06])
y= np.array([28.66,20.37,22.33,26.35,22.29,21.74,23.11,23.13,24.68,21.89])
#x= (7.5,4.48,8.60,7.73,5.28,4.25,6.99,6.31,9.15,5.06)
#y= (28.66,20.37,22.33,26.35,22.29,21.74,23.11,23.13,24.68,21.89)
print x
pp.scatter (x,y)
#pp.show ()
#pp.savefig ("fig_02a.png")

#2b)
z=np.polyfit(x,y,1)
p=np.poly1d(z)
xp=np.linspace(-1,15)
_=pp.plot(x, y, '.', xp, p(xp), '-')
pp.ylim(0, 40)
pp.xlabel ('x', fontsize = 16)
pp.ylabel ('y', fontsize = 16)
#pp.show ()
pp.savefig ("fig_02c.png")
