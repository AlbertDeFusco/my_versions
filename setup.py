from setuptools import setup

setup( name='my_versions',
        version='0.6',
        description='Show package versions',
        author='Albert DeFusco',
        license='MIT',
        packages=['my_versions'],

        entry_points = {
            'gui_scripts':'my_versions = my_versions.__main__:main'
            }

        )

