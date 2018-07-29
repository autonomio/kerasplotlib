#! /usr/bin/env python
#
import os
os.environ["MPLCONFIGDIR"] = "."

DESCRIPTION = "Kerasplotlib is a visualization library for Keras"
LONG_DESCRIPTION = """\
Kerasplotlib provides a useful interface for Keras users that meet
many common visualization needs related with training and evaluating
deep learning models.
"""

DISTNAME = 'kerasplotlib'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://mikkokotila.com'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/autonomio/kerasplotlib'
VERSION = '0.1.4'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():
    install_requires = []

    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')
    try:
        import keras
    except ImportError:
        install_requires.append('keras')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        include_package_data=True,
#        package_data={'kerasplotlib.extras': ['*']},
        install_requires=install_requires,
        packages=['kerasplotlib'],
        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Scientific/Engineering :: Visualization',
                     'Topic :: Multimedia :: Graphics',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )
