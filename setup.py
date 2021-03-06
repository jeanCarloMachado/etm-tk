# from distutils.core import setup
from setuptools import setup, find_packages
from etmTk.v import version
import glob

import sys
if sys.version_info >= (3, 2):
    REQUIRES = ["python-dateutil>=1.5", "PyYaml>=3.10"]
else:
    REQUIRES = ["python>=2.7.6,<3.0", "python-dateutil>=1.5", "PyYaml>=3.10"]

APP = ['etm']

EXTRAS = {"icalendar": ["icalendar>=3.8.4"], "pytz": ["pytz>=2015.1"]},

OPTIONS = {'build': {'build_exe': 'releases/etmtk-{0}'.format(version)},
              'build_exe': {'icon': 'etmTk/etmlogo.gif', 'optimize': '2',
                            'compressed': 1},
              'build_mac': {'iconfile': 'etmTk/etmlogo.gif',
                            'bundle_name': 'etm'},
              'Executable': {'targetDir': 'releases/etmtk-{0}'.format(version)}
            }

setup(
    name='etmtk',
    version=version,
    include_package_data=True,
    zip_safe=False,
    url='http://people.duke.edu/~dgraham/etmtk',
    description='event and task manager',
    long_description='manage events and tasks using simple text files',
    platforms='Any',
    license='License :: OSI Approved :: GNU General Public License (GPL)',
    author='Daniel A Graham',
    author_email='daniel.graham@duke.edu',
    # options=OPTIONS,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business :: Scheduling'],
    packages=['etmTk'],
    scripts=['etm'],
    install_requires=REQUIRES,
    extras_require={"icalendar": ["icalendar>=3.8.4"]},
    package_data={
        'etmTk': ['icons/*', 'etm.desktop', 'etm.appdata.xml', 'CHANGES', 'etm.1', 'etm.xpm'],
        'etmTk/help' : ['help/UserManual.html'],
        'etmTk/icons': ['icons/*']},
    data_files=[
        ('share/man/man1', ['etmTk/etm.1']),
        ('share/doc/etm', ['etmTk/CHANGES']),
        ('share/pixmaps', ['etmTk/etm.xpm']),
        ('share/icons', glob.glob('etmTk/icons/*.gif')),
        ('share/applications', ['etmTk/etm.desktop']),
        ('share/appdata', ['etmTk/etm.appdata.xml']),
    ]
)
