from setuptools import setup, find_packages


setup(
    name="xpdconf",
    version='0.4.0',
    packages=find_packages(),
    description="data processing module",
    zip_safe=False,
    package_data={"xpdconf": ["examples/*"]},
    include_package_data=True,
    url="http:/github.com/xpdAcq/xpdConf",
)
