from setuptools import setup, find_packages
from sense import VERSION

setup(
    name="sense",
    version=VERSION,
    url="http://github.com/diegorubin/sense",
    author="Diego Rubin",
    author_email="rubin.diego@gmail.com",
    license="GPL2",
    scripts=['bin/sense', 'bin/think'],
    include_package_data=True,
    description="Sense Daemon",
    install_requires=[
        "pyro4",
        "tinydb",
        "GitPython"
    ],
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages()
)

