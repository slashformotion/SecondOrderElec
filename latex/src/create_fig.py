import sys
sys.path.append("../../")

import numpy as np
from ENIB_lib import *

# LP
T_num = 2
w0 = 1000
m_list = [3,0.1]

filter_list = [LP, HP, BP, Notch]

for filter in filter_list:
    
    for index,m in enumerate(m_list):
        T = filter(T_num,m,w0)
        
        filename = "../csv/{}_{}".format(T.type,index)
        
        poles,zeros = T.pzmap(plot=False)
        export_csv([np.real(poles),np.imag(poles)],filename="{}_poles.csv".format(filename),header="re_p,im_p")
        export_csv([np.real(zeros),np.imag(zeros)],filename="{}_zeros.csv".format(filename),header="re_z,im_z")
    
        t,s = T.impulse(N = 200,plot=False)
        export_csv([t,s],filename="{}_impulse.csv".format(filename),header="t,s")
    
        t,s = T.step(N = 200,plot=False)
        export_csv([t,s],filename="{}_step.csv".format(filename),header="t,s")
    
        w,Tjw = T.freqresp(n=500,plot=False)
        mag = np.abs(Tjw)
        phase = np.angle(Tjw)*180/np.pi
        export_csv([w,mag,phase],filename="{}_freqresp.csv".format(filename),header="w,mag,phase")

