.. My Project documentation master file, created by
   sphinx-quickstart on Mon Dec 14 23:07:31 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to My Project's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Definitions<definitions>

Introduction
============

This is the documentation for the sample project.

Installation
============

Nothing to do...

Getting started
===============

To use the package:

.. code-block:: python

    from my_project import math

    seq = [1,2,3]
    s = math.Sequence(seq)
    a_mean = s.arithmetic_mean()
    print(a_mean)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
