from setuptools import setup


setup(
    name='zwoparse',
    version='1.0dev',
    py_modules=['zwoparse'],
    install_requires=[
        'Click',
    ],
    entry_points = {
        'console_scripts':['zwoparse=zwoparse:main'],
    } 
)
