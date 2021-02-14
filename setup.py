from setuptools import find_packages,setup
setup(
    name = 'gitacc',
    version = '0.2',
    packages = find_packages(),
    entry_points={
        'console_scripts':[
            'gitacc=gitacc:acc'
        ]
    },
)