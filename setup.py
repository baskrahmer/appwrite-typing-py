from setuptools import setup, find_packages

setup(
    name='appwrite-typing',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    author='Bas Krahmer',
    description='Type hints for Appwrite Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    # Additional classifiers can be found at https://pypi.org/classifiers/
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
