#!/usr/bin/env python3
# Some systems don't have `python3` in their PATH. This isn't supported by x.py directly;
# they should use `x` or `x.ps1` instead.

# This file is only a "symlink" to bootstrap.py, all logic should go there.

# Author: CODEWITHASAD
# website: codwithasad.org
# i just simply add comment for participation in hacktoberfest

import os
import sys

# If this is python2, check if python3 is available and re-execute with that
# interpreter. Only python3 allows downloading CI LLVM.
#
# This matters if someone's system `python` is python2.
if sys.version_info.major < 3:
    try:
        os.execvp("py", ["py", "-3"] + sys.argv)
    except OSError:
        try:
            os.execvp("python3", ["python3"] + sys.argv)
        except OSError:
            # Python 3 isn't available, fall back to python 2
            pass

rust_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(rust_dir, "src", "bootstrap"))

import bootstrap
bootstrap.main()
