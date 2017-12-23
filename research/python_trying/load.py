from distutils.core import setup, Extension

ext = Extension("hello", sources=["module.cpp"])

setup(name="YotamsPackage", version="1.0", description="This is an hello world package", ext_modules=[ext])

