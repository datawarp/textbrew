from setuptools import setup
import setuptools

setup(
    name='textbrew',
    packages=setuptools.find_packages(),
    version='0.1.0',
    description='Brew your raw text to a more structured and Machine Learning complaint format.',
    license='MIT',
    author='datawarp',
    author_email='rishy.s13@gmail.com',
    url='https://github.com/datawarp/textbrew',
    download_url='https://github.com/datawarp/textbrew.git',
    install_requires=[
        'numpy==1.12.0',
        'spacy==1.6.0'
    ],
    keywords=['textbrew'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Topic :: Text Cleaning',
                 'License :: MIT License',
                 'Programming Language :: Python :: 3.5',
                ],

)
