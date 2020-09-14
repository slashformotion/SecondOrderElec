Installation
============
The minimal working python version is 3.6.x

We recommend that you use an anaconda environment for better compatibilitty between scientifics modules.

.. code-block:: bash

    pip install -U SecondOrderElec

Manual installation
-------------------

You can install SecondOrderElec from this repository if you want the latest
but possibly non-compiling version::

    git clone https://github.com/slashformotion/SecondOrderElec.git
    cd SecondOrderElec
    python setup.py build
    
    python setup.py install --user

Run tests after install::

    python -m unittest discover tests -v