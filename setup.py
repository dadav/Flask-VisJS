import os
from setuptools import setup

with open("flask_visjs/_version.py", "r", encoding="utf-8") as fh:
    pkg_version = fh.read().split()[2].strip("'")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Flask-VisJS',
    version=pkg_version,
    url='https://github.com/dadav/Flask-VisJS',
    project_urls={
        'Bug Tracker': 'https://github.com/dadav/Flask-VisJS/issues',
    },
    author='dadav',
    author_email='dadav@protonmail.com',
    maintainer='dadav',
    maintainer_email='dadav@protonmail.com',
    license='BSD',
    license_file='LICENSE',
    description='A simple flask wrapper for the famous visjs library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='flask,visjs',
    platforms='any',
    packages=['flask_visjs'],
    package_data={"flask_visjs": ["static/*", "templates/*"]},
    python_requires=">=3.6",
    install_requires=[
        "Flask<3",
        "pyvis",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
