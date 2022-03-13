#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    line = re.sub(r'\^', 'ⁿ', line.rstrip())
    line = re.sub(r'\|', '\u030d', line.rstrip())
    line = re.sub(r'w', 'ṳ', line)
    line = re.sub(r'ẃ', 'ṳ́', line)
    line = re.sub(r'ẁ', 'ṳ̀', line)
    line = re.sub(r'w̄', 'ṳ̄', line)
    line = re.sub(r'w̃', 'ṳ̃', line)
    print(line)

