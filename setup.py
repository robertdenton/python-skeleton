try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project description',
    'author': 'Rob Denton',
    'url': 'https://github.com/robertdenton/python-skeleton/',
    'download_url': 'https://github.com/robertdenton/python-skeleton',
    'author_email': 'rob@robertrdenton.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['name'],
    'scripts': [],
    'name': 'Python project skeleton'
}

setup(**config)

