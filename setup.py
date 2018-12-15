from setuptools import setup

setup(name='silverpm',
      version='1.0',
      description='Python interface to Gembird Silvershield SIS-PMS',
      author='Magnus Olsson',
      author_email='magnus@minimum.se',
      url='https://github.com/blastur/silverpm',
      scripts=['scripts/silverpm.py'],
      install_requires=['pyusb'],
     )