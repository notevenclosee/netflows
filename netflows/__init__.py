# -*- coding: utf-8 -*-
"""
netflows
========

netflows is a Python package for optimal traffic assignment / Wardrop Equilibrium on brain or transportation networks.

Source::

    https://github.com/yingqiuz/netflows
    
Simple example
---------------------
TBC

License
---------------------
TBC
"""

__all__ = [
    '__author__', '__description__', '__email__', '__license__',
    '__packagename__','__url__', '__version__',
    'Graph', 'WElinearsolve', 'SOlinearsolve', 'WEaffinesolve',
    'SOaffinesolve', 'WEbprsolve', 'SObprsolve'
]

from .info import (
    __version__,
    __author__,
    __description__,
    __email__,
    __license__,
    __packagename__,
    __url__
)

from .Graph import Graph
from .funcs import (
    WElinearsolve,
    SOlinearsolve,
    WEaffinesolve,
    SOaffinesolve,
    WEbprsolve,
    SObprsolve
)


