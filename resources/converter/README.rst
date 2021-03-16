XHTML2PDF
=========

.. image:: https://img.shields.io/pypi/v/xhtml2pdf?label=PyPI&logo=PyPI&logoColor=white&color=blue
    :target: https://pypi.python.org/pypi/xhtml2pdf
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/xhtml2pdf?label=Python&logo=Python&logoColor=white
    :target: https://www.python.org/downloads
    :alt: Python versions

.. image:: https://img.shields.io/travis/xhtml2pdf/xhtml2pdf/master.svg?label=Travis%20CI&logo=Travis&logoColor=white
    :target: https://travis-ci.org/xhtml2pdf/xhtml2pdf
    :alt: Travis CI

.. image:: https://img.shields.io/appveyor/build/LegoStormtroopr/xhtml2pdf?label=AppVeyor&logo=appveyor&logoColor=white
    :target: https://ci.appveyor.com/project/LegoStormtroopr/xhtml2pdf/branch/master
    :alt: AppVeyor

.. image:: https://img.shields.io/coveralls/github/xhtml2pdf/xhtml2pdf?label=Coveralls&logo=Coveralls&logoColor=white
    :target: https://coveralls.io/github/xhtml2pdf/xhtml2pdf
    :alt: Coveralls

.. image:: https://img.shields.io/readthedocs/xhtml2pdf?label=Read%20the%20Docs&logo=read%20the%20docs&logoColor=white
   :target: http://xhtml2pdf.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs

|

The current release of xhtml2pdf is **xhtml2pdf 0.2.5**. Release Notes can be found here: `Release Notes <https://xhtml2pdf.readthedocs.io/en/latest/release-notes.html>`__
As with all open-source software, its use in production depends on many factors, so be aware that you may find issues in some cases.

**Big thanks** to everyone who has worked on this project so far and to those who help maintain it.

About
=====

xhtml2pdf is a HTML to PDF converter using Python, the ReportLab Toolkit, html5lib and PyPDF2. It supports HTML5 and CSS 2.1 (and some of CSS 3). It is completely written in pure Python, so it is platform independent.

The main benefit of this tool is that a user with web skills like HTML and CSS is able to generate PDF templates very quickly without learning new technologies.


Documentation
==============

The documentation of xhtml2pdf is available at `Read the Docs <http://xhtml2pdf.readthedocs.io>`__.

And we could use your help improving it! A good place to start is ``doc/source/usage.rst``.


Installation
============

This is a typical Python library and can be installed using pip::

    pip install xhtml2pdf


Requirements
============

Python 2.7+. Only Python 3.4+ is tested and guaranteed to work.

All additional requirements are listed in the ``requirements.txt`` file and are installed automatically using the ``pip install xhtml2pdf`` method.


Alternatives
==============================

You can try `WeasyPrint <http://weasyprint.org>`__. The codebase is pretty, it has different features and it does a lot of what xhtml2pdf does.


Call for testing
================

This project is heavily dependent on getting its test coverage up! Furthermore, parts of the codebase could do well with cleanups and refactoring.

If you benefit from xhtml2pdf, perhaps look at the `test coverage <https://coveralls.io/github/xhtml2pdf/xhtml2pdf>`__ and identify parts that are yet untouched.


Development environment
=======================

#. If you don't have it, install ``pip``, the python package installer::

    sudo easy_install pip

   For more information about ``pip`` refer to http://www.pip-installer.org

#. We will recommend using ``virtualenv`` for development. It's great to have a separate environment for each project, keeping the dependencies for multiple projects separated::

    sudo pip install virtualenv

   For more information about ``virtualenv`` refer to http://www.virtualenv.org

#. Create a virtualenv for the project. This can be inside the project directory, but cannot be under version control::

    virtualenv --distribute xhtml2pdfenv --python=python2

#. Activate your virtualenv::

    source xhtml2pdfenv/bin/activate

   Later to deactivate it use::

    deactivate

#. The next step will be to install/upgrade dependencies from the ``requirements.txt`` file::

    pip install -r requirements.txt

#. Run tests to check your configuration::

    nosetests --with-coverage

   You should have a log with the following success status::

    Ran 36 tests in 0.322s

    OK


Python integration
==================

Some simple demos of how to integrate xhtml2pdf into a Python program may be found here: ``test/simple.py``


Running tests
=============

Two different test suites are available to assert that xhtml2pdf works reliably:

#. Unit tests. The unit testing framework is currently minimal, but is being
   improved on a regular basis (contributions welcome). They should run in the
   expected way for Python's unittest module, i.e.::

        nosetests --with-coverage (or your personal favorite)

#. Functional tests. Thanks to mawe42's super cool work, a full functional
   test suite is available at ``testrender/``.


Contact
=======

This project is community-led! Feel free to open up issues on GitHub about new ideas to improve xhtml2pdf.


History
=======

These are the major milestones and the maintainers of the project:

* 2000-2007, commercial project, spirito.de, written by Dirk Holtwich
* 2007-2010 Dirk Holtwich (project named "Pisa", project released as GPL)
* 2010-2012 Dirk Holtwick (project named "xhtml2pdf", changed license to Apache)
* 2012-2015 Chris Glass (@chrisglass)
* 2015-2016 Benjamin Bach (@benjaoming)
* 2016-2018 Sam Spencer (@LegoStormtroopr)
* 2018-Current Luis Zarate (@luisza) 

For more history, see the ``CHANGELOG.txt`` file.

License
=======

Copyright 2010 Dirk Holtwick, holtwick.it

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
