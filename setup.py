from setuptools import setup, find_packages

setup(
    name="sales_pipeline",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark==3.5.0",
        "pandas==2.0.0",
        "pyyaml==6.0.1",
        "requests==2.31.0",
        "python-dotenv==1.0.0",
    ]
)
