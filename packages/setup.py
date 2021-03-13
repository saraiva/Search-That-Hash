# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='search-that-hash',
    version='0.2.2',
    description='Search hashes quickly before cracking them',
    python_requires='==3.*,>=3.7.0',
    author='brandon',
    author_email='brandon@skerritt.blog',
    maintainer='jayy',
    maintainer_email='jayy2004@gmx.co.uk',
    license='GPL-3.0-or-later',
    entry_points={
        "console_scripts": [
            "sth = search_that_hash.__main__:main",
            "search-that-hash = search_that_hash.__main__:main"
        ]
    },
    packages=[
        'Search_That_Hash', 'Search_That_Hash.cracker',
        'Search_That_Hash.cracker.fast_mode_mod',
        'Search_That_Hash.cracker.greppable_mode_mod',
        'Search_That_Hash.cracker.offline_mod',
        'Search_That_Hash.cracker.online_mod',
        'Search_That_Hash.cracker.sth_mod'
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'appdirs==1.*,>=1.4.4', 'click==7.*,>=7.1.2',
        'cloudscraper==1.*,>=1.2.56', 'coloredlogs==15.*,>=15.0.0',
        'loguru==0.*,>=0.5.3', 'name-that-hash==1.*,>=1.1.6',
        'requests==2.*,>=2.25.1', 'rich==9.*,>=9.12.2', 'toml==0.*,>=0.10.2'
    ],
    extras_require={
        "dev": [
            "codecov==2.*,>=2.1.11", "coverage[toml]==5.*,>=5.5.0",
            "pytest==6.*,>=6.2.2", "pytest-cov==2.*,>=2.11.1"
        ]
    },
)
