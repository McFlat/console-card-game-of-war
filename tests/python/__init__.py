import os
import sys

# add path to source
path = '%s/src/python' % os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if path not in sys.path:
    sys.path.insert(0, path)

# add path to tests
path = '%s/tests/python' % os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if path not in sys.path:
    sys.path.insert(0, path)

from wargame_tests import *
