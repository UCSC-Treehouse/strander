#!/usr/bin/env python3.7

import argparse
import subprocess
import re
import sys


def salmon(r1, r2=None):
    cmd = ['salmon', 'quant',
           '-i', '/opt/strander/data/gencode_v32_overlap_transcripts_index',
           '--libType', 'A'
           '-o', '/tmp/salmon_out']

    if r2 is None:
        cmd = cmd + ['-r', r1]

    else:
        cmd = cmd + ['-1', r1,
                     '-2', r2]

    regex = re.compile("Automatically detected most likely library type as (?P<libtype>\w+)")

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    while True:
        output = proc.stdout.readline()
        m = regex.search(output)
        if m:
            print("Library Type: %s", m.groups("libtype"))
            sys.exit()

def main():
    """
    Uses salmon to infer the library type.
    """
    parser = argparse.ArgumentParser(description=main.__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-1',
                        help='Path to first fasta file.')

    parser.add_argument('-2',
                        help='Path to paired fasta file.')




if __name__ == '__main__':
    main()
