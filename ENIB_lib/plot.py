import matplotlib.pyplot as plt
import numpy as np


def plot_time(t, s):
    plt.plot(t, s)
    plt.xlabel("time (s)")


def plot_bode(w, Tjw):
    plt.figure("mag")
    plt.loglog(w, np.abs(Tjw))
    plt.ylabel("Modulus")
    plt.xlabel("Angular Frequency (rad/s)")

    plt.figure("phase")
    plt.semilogx(w, 180 * np.angle(Tjw) / np.pi)
    plt.ylabel("Argument")
    plt.xlabel("Angular Frequency (rad/s)")


def plot_pzmap(poles, zeros):
    plt.plot(poles.real, poles.imag, "x", markersize=5)
    plt.plot(zeros.real, zeros.imag, "o", markersize=5)

    plt.axis("scaled")
    plt.grid()
    plt.xlabel("Real Part")
    plt.ylabel("Imag Part")
