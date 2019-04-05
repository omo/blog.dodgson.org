#!/usr/bin/env python3

import glob

for f in glob.glob('**/*.html', recursive=True):
  content = open(f).read()
  content = content.replace('http://i.', '//i.')
  open(f, 'w').write(content)