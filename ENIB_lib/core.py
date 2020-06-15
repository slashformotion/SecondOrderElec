import numpy as np
from scipy.signal import lti
from .plot import plot_time, plot_bode, plot_pzmap

class Second_Order_LTI():
    
    """ General Class for Second order LTI systems"""
    
    @property
    def R(self):
        if self.m < 1 :
            R = np.exp(2*np.pi*self.m/np.sqrt(1-self.m**2))
        else:
            R = 0
        return R
    
    @property
    def wp(self):
        if self.m < 1:
            wp = self.w0*np.sqrt(1-self.m**2)
        else:
            wp = None
        return wp
    
    @property
    def Tp(self):
        if self.wp :
            Fp = self.wp/(2*np.pi)
            Tp = 1/Fp
        else :
            Tp = None
        return Tp
    
    @property
    def Q(self):
        return 1/(2*self.m)
    
    def pzmap(self,plot=True):
        poles = self.lti.poles
        zeros = self.lti.zeros
        if plot == True :
            plot_pzmap(poles,zeros)
        return poles,zeros
    
    def impulse(self, X0=None, T=None, N=None,plot=True):
        t,s = self.lti.impulse(X0=X0, T=T, N=N)
        if plot == True :
            plot_time(t,s)
        return t,s
    
    def step(self,  X0=None, T=None, N=None,plot=True):
        t,s = self.lti.step(X0=X0, T=T, N=N)
        if plot == True :
            plot_time(t,s)
        return t,s
    
    def output(self, U, T, X0=None,plot=True):
        t,s = self.lti.output(U, T, X0=X0)
        if plot == True :
            plot_time(t,s)
        return self.lti.output(U, T, X0=X0)

    def freqresp(self, w=None, n=10000,plot=True):
        w, Tjw = self.lti.freqresp(w=w, n=n)
        if plot == True :
            plot_bode(w,Tjw)
        return w, Tjw

    def discontinuities(self,var_input,var_diff_input):
        b2,b1,b0 = self.den
        a2,a1,a0 = self.den
        H = (1/(a2**2))*np.array([[a2*b2,0],[a2*b1-a1*b2,a2*b2]])
        x = np.array([[var_input],[var_diff_input]])
        y = np.dot(H,x)
        return y


class General_Second_Order(Second_Order_LTI):

    """ Class for Second order LTI systems"""
    
    type = "second_order"

    def __init__(self,m,w0):
        """
        General Second Order filter instance constructor

        Args:
            m (float): damping coefficient
            w0 (float): caracteristic frequency
        """
        self.num = num
        self.den = den
        self.normalize()
    
    @property
    def lti(self):
        return lti(self.num,self.den)

    @property
    def w0(self):
        a_2_norm = self.den[0]  #a_2_norm = 1/(w0**2)
        w0 = 1/np.sqrt(a_2_norm)
        return w0

    @property
    def m(self):
        a_1_norm = self.den[1]  #a_1_norm = 2m/(w0) ->m = a_1_norm *w0/2
        w0 = self.w0
        m = a_1_norm*w0/2

    def normalize(self):
        self.num = self.num/self.den[-1]
        self.den = self.den/self.den[-1]


class LP(Second_Order_LTI):
    """
    Low Pass filter

    Args:
        Second_Order_LTI (class): General class for second order LTI
    
    """
    
    type = "LP"

    def __init__(self,T0,m,w0):
        """
        LP instance constructor

        Args:
            T0 (float): amplification
            m (float): damping coefficient
            w0 (float): cut-off frequency
        """
        self.T0 = T0
        self.m = m
        self.w0 = w0
    
    @property
    def num(self):
        return self.T0
    
    @property
    def den(self):
        return np.array([1/(self.w0**2),2*self.m/self.w0,1])

    @property
    def lti(self):
        return lti(self.num,self.den)

    @property
    def wr(self):
        return self.w0*np.sqrt(1-2*self.m**2)

    @property
    def MdB(self):
        return 1/(2*self.m*np.sqrt(1*self.m**2))



class BP(Second_Order_LTI):
    """
    Band Pass filter class

    Args:
        Second_Order_LTI (class):  General class for second order LTI
    
    """
    
    type = "BP"
    
    def __init__(self,Tm,m,w0):
        """
        Band Pass filter instance constructor

        Args:
            Tm (float): amplification
            m (float): damping coefficient
            w0 (float): center frequency
        """
        self.Tm = Tm
        self.m = m
        self.w0 = w0
    
    @property
    def num(self):
        return np.array([2*self.m*self.Tm/(self.w0),0])
    
    @property
    def den(self):
        return np.array([1/(self.w0**2),2*self.m/self.w0,1])
    
    @property
    def lti(self):
        return lti(self.num,self.den)
    
    @property
    def wc(self):
        wc1 = self.w0*(-self.m+np.sqrt(1+self.m**2))
        wc2 = self.w0*(self.m+np.sqrt(1+self.m**2))
        return [wc1,wc2]

    @property
    def delta_w(self):
        return 2*self.m*self.w0


class HP(Second_Order_LTI):
    """
    High Pass filter class

    Args:
        Second_Order_LTI (class):  General class for second order LTI
    
    """

    type = "HP"
    
    def __init__(self,Too,m,w0):
        """
        High Pass filter instance constructor

        Args:
            Too (float): amplification
            m (float): damping coefficient
            w0 (float): cut-off frequency
        """
        self.Too = Too
        self.m = m
        self.w0 = w0
    
    @property
    def num(self):
        return np.array([self.Too/(self.w0**2),0,0])
    
    @property
    def den(self):
        return np.array([1/(self.w0**2),2*self.m/self.w0,1])
    
    @property
    def lti(self):
        return lti(self.num,self.den)

    @property
    def wr(self):
        return self.w0/np.sqrt(1-2*self.m**2)

    @property
    def MdB(self):
        return 1/(2*self.m*np.sqrt(1*self.m**2))


class Notch(Second_Order_LTI):
    """
    Notch filter class

    Args:
        Second_Order_LTI (class):  General class for second order LTI
    
    """
    
    type = "Notch"
    
    def __init__(self,T0,m,w0):
        """
        Notch filter instance constructor

        Args:
            T0 (float): amplification
            m (float): damping coefficient
            w0 (float): center frequency
        """
        self.T0 = T0
        self.m = m
        self.w0 = w0
    
    @property
    def num(self):
        return np.array([self.T0/(self.w0**2),0,self.T0])
    
    @property
    def den(self):
        return np.array([1/(self.w0**2),2*self.m/self.w0,1])
    
    @property
    def lti(self):
        return lti(self.num,self.den)
    
    @property
    def wc(self):
        wc1 = self.w0*(-self.m+np.sqrt(1+self.m**2))
        wc2 = self.w0*(self.m+np.sqrt(1+self.m**2))
        return [wc1,wc2]

    @property
    def delta_w(self):
        return 2*self.m*self.w0

