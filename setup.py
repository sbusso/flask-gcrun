"""
Flask-Service
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-GCRun-Service',
    version='1.0',
    url='https://github.com/sbusso/flask_gcrun',
    license='MIT',
    author='Stephane Busso',
    author_email='stephane.busso@gmail.com',
    description='Wrapper for Flask service on Google Cloud Run',
    long_description=__doc__,
    py_modules=['flask_gcrun_service'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_gcrun_service'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
