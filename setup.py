from setuptools import setup, find_packages

setup(
    name='decisioncanvas',
    version='1.0.0',
    description='Easy decision boundary visualization for classifiers',
    author='Krunal Wankahde , Parimal Kalpande',
    author_email='krunal.wankahde1810@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'matplotlib',
    ],
    python_requires='>=3.7',
    url='https://github.com/yourusername/decisioncanvas',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
