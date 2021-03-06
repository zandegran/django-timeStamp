
import os

from setuptools import setup

from timeStamps import get_version


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('timeStamps'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or '__pycache__' in dirname:
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[11:]  # Strip "timeStamps/" or "timeStamps\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='django-timeStamp',
      zip_safe=False,  # eggs are the devil.
      version=get_version().replace(' ', '-'),
      description='An extensible timeStamp application for Django',
      author='Ansel Zandegran',
      author_email='zandegran@gmail.com',
      url='https://github.com/zandegran/django-timeStamp',
      package_dir={'timeStamps': 'timeStamps'},
      packages=packages,
      package_data={'timeStamps': data_files},
      test_suite='timeStamps.runtests.run_tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.9',
          'Framework :: Django :: 1.10',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities'],
      )