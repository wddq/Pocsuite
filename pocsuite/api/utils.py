#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2015 pocsuite developers (http://sebug.net)
See the file 'docs/COPYING' for copying permission
"""

from pocsuite.lib.core.data import logger
from pocsuite.lib.core.enums import CUSTOM_LOGGING

from pocsuite.lib.utils.password import getLargeWeakPassword
from pocsuite.lib.utils.password import getWeakPassword
from pocsuite.lib.utils.password import genPassword

from pocsuite.lib.utils.funs import url2ip
