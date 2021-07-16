# python #
* to install portable python for windows 10 i did:
    * download python 3.9 embedded :
    https://www.python.org/ftp/python/3.9.0/python-3.9.0b1-embed-amd64.zip;
    * update python39._pth:
        * add "Lib/site-packages" on the top;
        * uncomment the lower line: import site;
    * set environment variables for python and python/scripts directory;
    * execute from the command line:
        * curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py;
        * python get-pip.py;
* to use local pip: python -m pip install THE_MODULE_NAME;