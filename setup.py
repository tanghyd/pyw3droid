from setuptools import setup, find_packages

setup(
    name="w3droid",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A community-led effort to development RTS AI for Warcraft III.",
)