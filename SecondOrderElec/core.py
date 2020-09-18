##
# This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.
#
# @authors: vincentchoqueuse, slashformotion
##
import numpy as np
from scipy.signal import lti
from .plot import plot_time, plot_bode, plot_pzmap


class Second_Order_LTI:

    """ General Class for Second order LTI systems"""

    @property
    def R(self):
        if self.m < 1:
            R = np.exp(2 * np.pi * self.m / np.sqrt(1 - self.m ** 2))
        else:
            R = 0
        return R

    @property
    def wp(self):
        if self.m < 1:
            wp = self.w0 * np.sqrt(1 - self.m ** 2)
        else:
            wp = None
        return wp

    @property
    def Tp(self):
        if self.wp:
            Fp = self.wp / (2 * np.pi)
            Tp = 1 / Fp
        else:
            Tp = None
        return Tp

    @property
    def Q(self):
        return 1 / (2 * self.m)

    def pzmap(self, plot=True):
        """return poles and zeros.


        Args:
            plot (bool, optional): plot poles and zeros. Defaults to True.

        Returns:
            tuple: (poles,zeros)
        """
        poles = self.lti.poles
        zeros = self.lti.zeros
        if plot == True:
            plot_pzmap(poles, zeros)
        return poles, zeros

    def impulse(self, X0=None, T=None, N=None, plot=True):
        """return impulse response from continuous-time system. (in this case, self)

        Args:
            X0 (array, optional): Initial state-vector. Defaults to None.
            T (array, optional): Time points. Computed if not given.. Defaults to None.
            N (int, optional): The number of time points to compute (if T is not given). Defaults to None.
            plot (bool, optional): plot the impulse response. Defaults to True.

        Returns:
            tuple: (array t: time (x-axis),
                    array s: impulse response (y-axis)
        """
        t, s = self.lti.impulse(X0=X0, T=T, N=N)
        if plot == True:
            plot_time(t, s)
        return t, s

    def step(self, X0=None, T=None, N=None, plot=True):
        """return step response

        Args:
            X0 (array_like, optional): Initial state-vector. Defaults to None.
            T (array_like, optional): Time points. Defaults to None.
            N (int, optional): Number of time points to compute if T is not given. Defaults to None.
            plot (bool, optional): plot the step reponse. Defaults to True.

        Returns:
            tuple(ndarray, ndarray): Time values for step response, step response
        """
        t, s = self.lti.step(X0=X0, T=T, N=N)
        t = np.hstack(([-0.001, -0.00001, 0], t))
        s = np.hstack(([0, 0, 0], s))
        step = t >= 0
        if plot == True:
            plot_time(t, s, step)

        return t, s

    def output(self, U, T, X0=None, plot=True):
        """return output of a continuous-time linear system.

        Args:
            U (array_like): An input array describing the input at each time T (interpolation is assumed between given times). If there are multiple inputs, then each column of the rank-2 array represents an input. If U = 0 or None, a zero input is used.
            T (array_like): The time steps at which the input is defined and at which the output is desired. Must be nonnegative, increasing, and equally spaced.
            X0 (array_like, optional): The initial conditions on the state vector (zero by default). Defaults to None.
            plot (bool, optional): plot output. Defaults to True.

        Returns:
            tuple(1D ndarray, 1D ndarray, ndarray): Time values for the output, system output, time evolution of the state vector
        """
        t, s, x = self.lti.output(U, T, X0=X0)
        if plot == True:
            plot_time(t, s)
        return t, s, x

    def freqresp(self, w=None, n=10000, plot=True):
        """return frequency response. (This method can plot it too)

        Args:
            w (array_like, optional): Array of frequencies (in rad/s). Magnitude and phase data is calculated for every value in this array. If not given, a reasonable set will be calculated.. Defaults to None.
            n (int, optional): Number of frequency points to compute if w is not given. The n frequencies are logarithmically spaced in an interval chosen to include the influence of the poles and zeros of the system.. Defaults to 10000.
            plot (bool, optional): plot the frequency response. Defaults to True.

        Returns:
            tuple(1D ndarray, 1D ndarray): (frequency array [rad/s], array of complex magnitude values)
        """
        w, Tjw = self.lti.freqresp(w=w, n=n)
        if plot == True:
            plot_bode(w, Tjw)
        return w, Tjw

    def discontinuities(self, var_input, var_diff_input):
        # TODO: understand wtf this is
        b2, b1, b0 = self.den
        a2, a1, a0 = self.den
        H = (1 / (a2 ** 2)) * np.array([[a2 * b2, 0], [a2 * b1 - a1 * b2, a2 * b2]])
        x = np.array([[var_input], [var_diff_input]])
        y = np.dot(H, x)
        return y


class General_Second_Order(Second_Order_LTI):

    """ Class for Second order LTI systems"""

    type = "second_order"

    def __init__(self, m, w0):
        """
        General Second Order filter instance constructor

        Args:
            m (float): damping coefficient
            w0 (float): caracteristic frequency
        """

        self.normalize()

    @property
    def lti(self):
        return lti(self.num, self.den)

    @property
    def w0(self):
        """Natural frequency

        Returns:
            float: natural frequency (commonly known as w0)
        """
        a_2_norm = self.den[0]  # a_2_norm = 1/(w0**2)
        w0 = 1 / np.sqrt(a_2_norm)
        return w0

    @property
    def m(self):
        """Damping factor

        Returns:
            float: damping factor, or damping coefficient
        """
        a_1_norm = self.den[1]  # a_1_norm = 2m/(w0) ->m = a_1_norm *w0/2
        w0 = self.w0
        m = a_1_norm * w0 / 2
        return m

    def normalize(self):
        """normalize the linear system"""
        self.num = self.num / self.den[-1]
        self.den = self.den / self.den[-1]


class LP(Second_Order_LTI):
    """
    Low Pass filter

    Args:
        Second_Order_LTI (class): General class for second order LTI

    """

    type = "LP"

    def __init__(self, T0, m, w0):
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
        """System numerator

        Returns:
            float: numerator (here T0)
        """
        return self.T0

    @property
    def den(self):
        """System denominator

        Returns:
            array_like: denominator
        """
        return np.array([1 / (self.w0 ** 2), 2 * self.m / self.w0, 1])

    @property
    def lti(self):
        return lti(self.num, self.den)

    @property
    def wr(self):
        return self.w0 * np.sqrt(1 - 2 * self.m ** 2)

    @property
    def MdB(self):
        return 1 / (2 * self.m * np.sqrt(1 * self.m ** 2))


class BP(Second_Order_LTI):
    """
    Band Pass filter class

    Args:
        Second_Order_LTI (class):  General class for second order LTI

    """

    type = "BP"

    def __init__(self, Tm, m, w0):
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
        """System Numerator

        Returns:
            array_like: system's numerator
        """
        return np.array([2 * self.m * self.Tm / (self.w0), 0])

    @property
    def den(self):
        """System Denominator

        Returns:
            array_like: system's denominator
        """
        return np.array([1 / (self.w0 ** 2), 2 * self.m / self.w0, 1])

    @property
    def lti(self):
        """Continuous-time linear time invariant system

        Returns:
            scipy.signal.lti: lti object
        """
        return lti(self.num, self.den)

    @property
    def wc(self):
        """Filter pass band

        Returns:
            list(float, float): start and stop frequencies of the pass band
        """
        wc1 = self.w0 * (-self.m + np.sqrt(1 + self.m ** 2))
        wc2 = self.w0 * (self.m + np.sqrt(1 + self.m ** 2))
        return [wc1, wc2]

    @property
    def delta_w(self):
        """Filter bandwidth

        Returns:
            float: bandwidth of the pass band
        """
        return 2 * self.m * self.w0


class HP(Second_Order_LTI):
    """
    High Pass filter class

    Args:
        Second_Order_LTI (class):  General class for second order LTI

    """

    type = "HP"

    def __init__(self, Too, m, w0):
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
        """System Numerator

        Returns:
            array_like: system's numerator
        """
        return np.array([self.Too / (self.w0 ** 2), 0, 0])

    @property
    def den(self):
        """System Denominator

        Returns:
            array_like: system's denominator
        """
        return np.array([1 / (self.w0 ** 2), 2 * self.m / self.w0, 1])

    @property
    def lti(self):
        """Continuous-time linear time invariant system

        Returns:
            scipy.signal.lti: lti object
        """
        return lti(self.num, self.den)

    @property
    def wr(self):
        return self.w0 / np.sqrt(1 - 2 * self.m ** 2)

    @property
    def MdB(self):
        return 1 / (2 * self.m * np.sqrt(1 * self.m ** 2))


class Notch(Second_Order_LTI):
    """
    Notch filter class

    Args:
        Second_Order_LTI (class):  General class for second order LTI

    """

    type = "Notch"

    def __init__(self, T0, m, w0):
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
        return np.array([self.T0 / (self.w0 ** 2), 0, self.T0])

    @property
    def den(self):
        return np.array([1 / (self.w0 ** 2), 2 * self.m / self.w0, 1])

    @property
    def lti(self):
        """Continuous-time linear time invariant system

        Returns:
            scipy.signal.lti: lti object
        """
        return lti(self.num, self.den)

    @property
    def wc(self):
        """Rejected band

        Returns:
            list(float, float): start and stop frequencies of the rejected band stop
        """
        wc1 = self.w0 * (-self.m + np.sqrt(1 + self.m ** 2))
        wc2 = self.w0 * (self.m + np.sqrt(1 + self.m ** 2))
        return [wc1, wc2]

    @property
    def delta_w(self):
        return 2 * self.m * self.w0
