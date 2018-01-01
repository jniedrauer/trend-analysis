trend-analysis
==============
A python app for analysing keyword trends from webpages

Dev Setup
---------
The bootstrap script will set up a virtualenv using virtualenvwrapper.
It will include environment variables for debugging. It is designed to work
with Linux or MacOS.

Use:

    ./bootstrap.sh::
    workon technical-analysis

Testing
-------
Tests should be run with tox. Install tox using your distro's package manager
or using pip. Run tests with:

    tox::

Debugging
---------
You can run the application in debug mode using the helper script:

    debug.sh::
