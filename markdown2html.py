#!/usr/bin/python3
"""
markdown2html - converts a markdown file to HTML
"""

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(md_file):
        sys.stderr.write("Missing {}\n".format(md_file))
        sys.exit(1)

    sys.exit(0)

