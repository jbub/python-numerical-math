# -*- coding: utf-8 -*-

"""
numa

:copyright: (c) 2013 by Juraj Bubniak.
:license: BSD, see LICENSE for more details.

"""

__title__ = 'numa'
__author__ = 'Juraj Bubniak'
__license__ = 'BSD'
__copyright__ = 'Copyright 2013 Juraj Bubniak'


from .utils import int_input, float_input, expr_input, matrix_input, \
    eval_expr, list_input

import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))