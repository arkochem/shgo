from setuptools import setup

setup(name='shgo',
      version='0.1.2',
      description='Simplicial homology global optimisation',
      url='https://github.com/stefan-endres/shgo',
      author='stefan-endres',
      author_email='stefan.c.endres@gmail.com',
      license='MIT',
      packages=['shgo'],
      install_requires=[
          'scipy',
          'numpy'
      ],
      test_suite='./shgo_tests.py',
      zip_safe=False)