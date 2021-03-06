from setuptools import find_packages, setup

setup(
    name="macvendorupdate",
    version="0.2.7",
    description="Scripts to update the mac address brand list to a Python file or a MySQL DataBase",
    author="sWallyx",
    keywords=[
        "mac address",
        "wi-fi",
        "brands",
        "people",
        "oui",
        "devices",
        "python",
        "mysql",
        "download",
    ],
    classifiers=[],
    install_requires=["click", "mysql-connector-python", "progress", "requests"],
    setup_requires=[],
    tests_require=[],
    packages=find_packages(),
)
