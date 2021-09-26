# coding=utf-8
"""Install LabPtPtm1."""

from setuptools import setup, find_packages

setup(name='labptptm1',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'zarr==2.9.5',
        'fsspec',
        's3fs'
    ]
)
