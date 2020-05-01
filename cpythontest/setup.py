#!/usr/bin/env python
from setuptools import setup
from Cython.Build import cythonize
from setuptools import setup, Extension
ext_modules = cythonize([
        Extension("ml.ml.hello", ["ml/ml/hello.py"]),
        Extension("ml.ml.hello1", ["ml/ml/hello1.py"])
        #Extension("ml/ml", ["ml/ml/cms_code_categorizer_python/algrxcc/categorizer.py"])
    ])
setup(
    ext_modules=ext_modules
)