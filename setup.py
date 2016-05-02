"""


Python-Card-Me parses iCalendar and vCard files into Python data structures,
decoding the relevant encodings.
It can also serialize vobject data structures to iCalendar, vCard, or hCalendar unicode strings.

It is a substantially reworked version of Vobject, updated for python3, with other improvements.

Requirements
------------

Requires Python 2.7 or later, dateutil (http://labix.org/python-dateutil) 2.4 or later, and six.

For older changes, see
   - http://vobject.skyhouseconsulting.com/history.html or
   - http://websvn.osafoundation.org/listing.php?repname=vobject&path=/trunk/

"""

from setuptools import setup, find_packages

# Docstring may not be present in optimized Python run mode, so if the
# docstring is missing just use empty strings so install still works
doclines = (__doc__ or '').splitlines() or ['', '']

setup(name="python-card-me",
      version="0.9.3",
      author="Tim Baxter, Jeffrey Harris",
      author_email="mail.baxter@gmail.com",
      license="Apache",
      zip_safe=True,
      url="https://github.com/tBaxter/python-card-me",
      entry_points={
          'console_scripts': [
              'ics_diff = card_me.ics_diff:main',
              'change_tz = card_me.change_tz:main'
          ]
      },
      include_package_data=True,
      install_requires=['python-dateutil'],
      platforms=["any"],
      packages=find_packages(),
      description=doclines[0],
      long_description="\n".join(doclines[2:]),
      classifiers="""
          Development Status :: 5 - Production/Stable
          Environment :: Console
          License :: OSI Approved :: BSD License
          Intended Audience :: Developers
          Natural Language :: English
          Programming Language :: Python
          Operating System :: OS Independent
          Topic :: Text Processing""".strip().splitlines()
      )
