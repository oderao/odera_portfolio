from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in odera/__init__.py
from odera import __version__ as version

setup(
	name="odera",
	version=version,
	description="Portfolio Template for Odera",
	author="Odera Inc",
	author_email="tripleo4u@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
