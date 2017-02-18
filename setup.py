from setuptools import setup
from setuptools import find_packages


setup(name='pylivecap',
      version='0.0.1',
      description='Grabbing livestream frame as image, including YouTube, Twitch...etc',
      author='Louie Lu',
      author_email='me@louie.lu',
      url='https://github.com/pynayzr/livestream-frame-capture',
      license='MIT',
      install_requires=['streamlink'],
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=find_packages())
