#!/bin/bash
set -xeu
perl -nE 'print "$. $_" if /^FUNC_DISPATCH_TABLE/ ... /^\}/' pyjl/external/modules/numpy.py
