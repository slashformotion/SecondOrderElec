##
# This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.
#
# @authors: vincentchoqueuse, slashformotion
##
import matplotlib.pyplot as plt
import numpy as np


def plot_time(t, s, *args):
    """plot 's' function of 't'

    Args:
        t (array_like): time or variable x-axis
        s (array_like): y-axis variable
    """
    plt.plot(t, s)
    for arg in args:
        plt.plot(t, arg)
    plt.xlabel("time (s)")


def plot_bode(w, Tjw):
    """plot the frequency reponse

    Args:
        w (array_like): angular velocity (rad/s)
        Tjw (array_like): frequency response
    """
    plt.figure("mag")
    plt.loglog(w, np.abs(Tjw))
    plt.ylabel("Modulus")
    plt.xlabel("Angular Frequency (rad/s)")

    plt.figure("phase")
    plt.semilogx(w, np.angle(Tjw, deg=True))
    plt.ylabel("Argument")
    plt.xlabel("Angular Frequency (rad/s)")


def plot_pzmap(poles, zeros):
    """plot poles and zeros

    Args:
        poles (array_like: poles
        zeros (array_like): zeros
    """
    plt.plot(poles.real, poles.imag, "x", markersize=5)
    plt.plot(zeros.real, zeros.imag, "o", markersize=5)

    plt.axis("scaled")
    plt.grid()
    plt.xlabel("Real Part")
    plt.ylabel("Imag Part")
