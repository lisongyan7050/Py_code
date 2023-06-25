import os,zipfile
newzip=zipfile.ZipFile('new.zip','w')
newzip.write('one.py',compress_type=zipfile.ZIP_DEFLATED)
newzip.close()