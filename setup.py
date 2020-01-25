from setuptools import setup

setup(name='acasearch',
      version='0.1',
      description='Search academia',
      url='https://github.com/AtomScott/scholar-api',
      author='Atom Scott',
      author_email='atom.james.scott@gmail.com',
      license='MIT',
      packages=['acasearch'],
      install_requires=[
        'arxiv',
        'colorlog'
      ],
      scripts=[
        'bin/acasearch',
      ],
      zip_safe=False)
