from setuptools import setup, find_packages
from pysense import VERSION

setup(
    name="pysense-daemon",
    version=VERSION,
    url="http://github.com/diegorubin/pysense",
    author="Diego Rubin",
    author_email="rubin.diego@gmail.com",
    license="GPL2",
    scripts=['bin/pysense', 'bin/think'],
    include_package_data=True,
    description="Organize your thoughts",
    install_requires=[
        "pyro4",
        "tinydb",
        "GitPython"
    ],
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages()
)

