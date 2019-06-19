
from setuptools import setup
from setuptools import find_packages


version_py = "selfish/_version.py"
exec(open(version_py).read())

setup(
    name = "selfish_hic",
    version =__version__,
    description = 'Hi-C Differential Analysis software created and maintained by the Ay Lab',
    long_description = "SELFISH is a tool for finding differential chromatin interactions between two Hi-C contact maps. It uses self-similarity to model interactions in a robust way.",
    url = 'http://github.com/ay-lab/selfish/',
    entry_points = {
        "console_scripts": ['selfish = selfish.selfish:main']
        },
    python_requires = '~=3.6',
    author = 'Ferhat Ay',
    author_email = 'ferhatay@lji.org',
    license = 'MIT',
    packages = ['selfish_hic'],
    install_requires = [
        'numpy',
        'matplotlib',
        'scipy',
        'pandas',
        'seaborn',
        'statsmodels'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe = False,
  )