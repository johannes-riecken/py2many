#!/bin/bash
set -xeu
perl -nE 'print "$. $_" if /def visit_nparray/ ... /^$/' pyjl/external/modules/numpy.py
