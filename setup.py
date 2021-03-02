from setuptools import setup, find_packages


setup(
    name="xpdconf",
    version='0.4.3',
    packages=find_packages(),
    description="data processing module",
    zip_safe=False,
    package_data={"xpdconf": ["examples/*"]},
    include_package_data=True,
    url="https://github.com/xpdAcq/xpdConf",
)
