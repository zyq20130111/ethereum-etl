from setuptools import setup

version = '1.0.0'

setup(
    name='ethereum-etl',
    version=version,
    packages=['ethereumetl', 'ethereumetl.domain', 'ethereumetl.mappers', 'ethereumetl.service'],
    url='https://github.com/blockchain-etl/ethereum-etl',
    license='MIT',
    author='medvedev1088',
    author_email='evge.medvedev@gmail.com',
    description='ETL (extract, transform, and load) tools for Ethereum blockchain'
)
