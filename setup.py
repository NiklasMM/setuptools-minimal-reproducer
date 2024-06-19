from setuptools import setup, find_packages

setup(
    name='MyPackageName',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    # 1) change this to 'zope.interface' and the bug will go away
    # 2) just require "twisted" (which in turn requires zope.interface) and it will appear again
    install_requires=["zope-interface"],
    entry_points={
        "console_scripts": [
            "mypackage=mypackage.foo:bar",
        ],
    },
)