"""Package info"""
# pylint: disable=invalid-name,redefined-builtin


modname = distname = 'trend_analysis'
numversion = [0, 0, 1]
numrelease = ['.dev', 1] # '.dev', 'a', 'b', 'rc' or empty for release
version = '.'.join([str(i) for i in numversion]) + ''.join(
    [str(i) for i in numrelease])

install_requires = []

license = 'MIT'
description = 'Analyse webpages for keywords'
url = 'https://github.com/jniedrauer/trend-analysis'
author = 'Josiah Niedrauer'
author_email = 'jniedrauer@gmail.com'

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities'
]


long_description = """"""

entry_points = {
    'console_scripts': [
        'trend-analysis=trend_analysis.main:main',
    ],
}
