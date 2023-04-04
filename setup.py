from setuptools import setup, find_packages

setup(
    entry_points={
        'console_scripts': [
            'get_html = get_html:main',
        ],
    },
    name='html_source_get',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    author='Steve Dondley',
    author_email='s@dondley.com',
    description='Fetches HTML from the Safari browser',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    #url='https://github.com/yourusername/my-library',
)
