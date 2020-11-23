from setuptools import setup, find_namespace_packages

VERSION = {}

with open("src/mystream/__init__.py") as version:
    exec(version.read(), VERSION)

setup(
    name="mystream",
    author="Selin Gungor",
    author_email="selingungor01gmail.com",
    description="""This project gets data from Twitter filtered streaming api and sends the data to GCP Pub/Sub, DataFlow and writes the output to BigQuery.""",
    version=VERSION.get("__version__", None),
    package_dir={"": "src"},
    packages=find_namespace_packages(where="streaming-data"),
    include_package_data=True,
    entry_points={"console_scripts": ["mystream=mystream.stream_data:main"]}
)
