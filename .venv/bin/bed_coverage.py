#!/home/galaxy/galaxy/.venv/bin/python

"""
Print number of bases covered by all intervals in a bed file (bases covered by
more than one interval are counted only once). Multiple bed files can be 
provided on the command line or to stdin.

usage: %prog bed files ...
"""

import psyco_full
import sys
from bx.bitset import BinnedBitSet
from bx.bitset_builders import *
from itertools import *

bed_filenames = sys.argv[1:]
if bed_filenames:
    input = chain( * imap( open, bed_filenames ) )
else:
    input = sys.stdin

bitsets = binned_bitsets_from_file( input )

total = 0
for chrom in bitsets:
    total += bitsets[chrom].count_range( 0, bitsets[chrom].size )

print total    
