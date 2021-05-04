from setuptools import setup, find_packages

setup(
      name='clean_folder',
      version='1.0.0',
      description='Remove files to folders',
      entry_points={
         'console_scripts': ['clean-folder=clean_folder.clean:main'],
      url='',
      author='Olga Fomenko',
      author_email='helga.fomenko@gmail.com',
      packages=find_packages()
    )
