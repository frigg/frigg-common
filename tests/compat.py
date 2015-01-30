# -*- coding: utf8 -*-
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    builtin_str = 'builtins'
else:
    builtin_str = '__builtin__'
