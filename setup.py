from setuptools import setup, find_packages

setup(
	name='Twitto',
	version='1.0',
	description='A simple tweeter clone with a mongoDB backend',
	author='Arie Bro',
	install_requires=["tornado", "mongoengine"]
)
