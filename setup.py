from setuptools import setup, find_packages

setup(
    name="w3droid",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=["numpy", "gym"],
    description="A community-led effort to developRTS AI for Warcraft III.",
)
