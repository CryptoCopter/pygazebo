"""
Python bindings to the Gazebo multi-robot simulator
===================================================

This package provides a python API to interact with the Gazebo
multi-robot simulator, http://www.gazebosim.org.  Gazebo is a
multi-robot simulator for outdoor environments. Like Stage, it is
capable of simulating a population of robots, sensors and objects, but
does so in a three-dimensional world. It generates both realistic
sensor feedback and physically plausible interactions between objects
(it includes an accurate simulation of rigid-body physics).

pygazebo implements the Gazebo network publish-subscribe protocol, so
that python applications can seamlessly interact with Gazebo entities.

pygazebo is based on eventlet for asynchronous network operations.
"""

__all__ = ["pygazebo", "msg"]

__author__ = "Markus Sommer"
__email__ = "msommer@informatik.uni-marburg.de"
__version__ = "4.0.0"
