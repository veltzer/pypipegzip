#!/usr/bin/python3

import os
import subprocess
import sys
import common


# PIP="pip"
PIP="pip3"
module = os.path.basename(os.getcwd())
common.check_call_no_output([
    "sudo",
    "-H",
    "{PIP}".format(**vars()),
    "install",
    "--quiet",
    "--upgrade",
    "{module}".format(**vars()),
])
output = subprocess.check_output([
    "{PIP}".format(**vars()),
    "show",
    "{module}".format(**vars()),
])
#grep -e "^Version"
print(output)
