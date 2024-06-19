### Minimal reproducer for issue https://github.com/pypa/setuptools/issues/4399

Confirmed in Python 3.10.12. Does not appear in Python 3.12

#### Steps to reproduce

* Clone repo
* cd into root of repo
* Create fresh virtualenv with python 3.10
* pip install setuptools==70.0.0
* pip install -e .
* run 'mypackage'

If you remove the `zope-interface` requirement in setup.py or even change it to `zope.interface` the bug goes away.