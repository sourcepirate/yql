from setuptools import setup

def readme():
    return open("README.md", "r").read()

requirements = [
    'six',
    'requests',
    'urllib3'
]

setup(
    name = 'yql',
    packages = ['yql', 'yql.api'],
    version = '1.0.1',
    long_description= readme(),
    description = "python interface for yql",
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/yql.git',
    license="MIT",
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
    ],
    install_requires= requirements
)
