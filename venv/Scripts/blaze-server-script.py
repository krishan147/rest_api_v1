#!C:\Users\Krishan\Google_Drive\Homework\py_scripts\r_restapi_test_v1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'blaze==0.10.1','console_scripts','blaze-server'
__requires__ = 'blaze==0.10.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('blaze==0.10.1', 'console_scripts', 'blaze-server')()
    )
