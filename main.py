#!/usr/bin/env python
from pathlib import Path
import tika
from tika import parser

# configurable constants
DIRECTORY = './files'

# initialize tika service
tika.initVM()

# grab all the files within a directory
pathlist = Path(DIRECTORY).glob('**/*')

# loop thru all the files
for path in pathlist:
    print(path)
    parsed = parser.from_file(str(path))
    print('METADATA')
    print(parsed["metadata"])
    print('CONTENT')
    print(parsed["content"])
    print('---')