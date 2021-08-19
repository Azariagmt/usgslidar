from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='usgs-lidar',
  version='0.0.1',
  description='A basic package to fetch usgs agriculture data',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Azaria Gebremichael',
  author_email='azariagebremichael10@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='usgs', 
  packages=find_packages(),
  install_requires=[''] 
)