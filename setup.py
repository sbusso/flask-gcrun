"""
FlaskGCRun
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='flaskgcrun',
    version='1.11',
    url='https://github.com/sbusso/flask-gcrun',
    license='MIT',
    author='Stephane Busso',
    author_email='stephane.busso@gmail.com',
    description='Wrapper for Flask service on Google Cloud Run',
    long_description=__doc__,
    # py_modules=['flaskgcrun'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flaskgcrun'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'flask==2.3.2',
        'google-cloud-pubsub==1.7.0',
        'google-cloud-storage==1.3.0'
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
