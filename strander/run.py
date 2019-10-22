#!/usr/bin/env python3.7

import argparse
import subprocess
import re
import sys
import textwrap

art = {"SF": """
5'--====1====>-----------------3'
3'-----------------------------5'""",
       "SR": """
5'-----------------------------3'
3'-----------------<====2====--5'""",
       "ISF": """
5'--====1====>-----------------3'
3'-----------------<====2====--5'""",
       "ISR": """
5'--====2====>-----------------3'
3'-----------------<====1====--5'""",
       "IU": """
5'--====1====>-----------------3'
3'-----------------<====2====--5'
                +
5'--====2====>-----------------3
3'-----------------<====1====--5"""}


def salmon(r1, r2=None):
    cmd = ['salmon', 'quant',
           '--libType', 'A',
           '-i', '/opt/strander/data/gencode_v32_overlap_transcripts_index',
           '-o', '/tmp/salmon_out']

    if r2 is None:
        cmd = cmd + ['-r', r1]

    else:
        cmd = cmd + ['-1', r1,
                     '-2', r2]

    regex = re.compile("Automatically detected most likely library type as (?P<libtype>\w+)")

    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    for stderr_line in iter(proc.stderr.readline, ""):
        m = regex.search(stderr_line)
        if m:
            libtype = m.groupdict()["libtype"]
            print("Library Type: %s" % libtype)
            if libtype in art:
                print(textwrap.dedent(art[libtype]))
            sys.exit()

def main():
    """
    Uses salmon to infer the library type.
    """
    parser = argparse.ArgumentParser(description=main.__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-1',
                        dest='r1',
                        help='Path to first fasta file.')

    parser.add_argument('-2',
                        dest='r2',
                        help='Path to paired fasta file.')

    args = parser.parse_args()
    salmon(args.r1, args.r2)


if __name__ == '__main__':
    main()
