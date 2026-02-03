# coding=utf-8
"""Install LabPtPtm1."""

from setuptools import setup, find_packages

setup(name='labptptm1',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'zarr>=3.0',
        'fsspec',
        's3fs',
        'rich'
    ]
)
