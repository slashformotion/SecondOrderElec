.. SecondOrderElec documentation master file, created by
   sphinx-quickstart on Mon Sep 14 11:04:07 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SecondOrderElec's documentation!
===========================================



The SecondOrderElec module has been designed to allow quick developpement of second order filters.



About this Library
------------------

This library is only python written and use scipy, matplotlib and numpy.

Quickstart
----------

Create filters:

.. code-block:: python

   from SecondOrderElec import LP, HP, BP, Notch
   import numpy as np

   filter_instance_low_pass = LP(T0=1, m=1.1, w0=6000)
   filter_instance_high_pass = HP(Too=1, m=1.1, w0=6000)
   filter_instance_band_pass = BP(Tm=1, m=1.1, w0=6000)
   filter_instance_notch = Notch(T0=1, m=1.1, w0=6000)


General
-------
.. toctree::
   :maxdepth: 1

   installation
   modules




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
