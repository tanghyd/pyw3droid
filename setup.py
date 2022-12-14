from setuptools import setup, find_packages

setup(
    name="pyw3droid",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=["numpy", "gym"],
    description="A community-led Python RL environment to develop a Warcraft III AI.",
)
