from setuptools import setup, find_namespace_packages
from setup_helper import find_all_resource_files

# -- Apps Definition -- #
namespace = 'tethysapp'
app_package = "geoglows_hydroviewer"
release_package = "tethysapp-" + app_package

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, namespace)


setup(
    name=release_package,
    version="1.9",
    description="GUI for the GEOGloWS ECMWF Streamflow model",
    long_description="GUI for the GEOGloWS ECMWF Streamflow model",
    keywords="replace_keywords",
    author="Riley Hales",
    author_email="Riley Hales_email",
    url="https://geoglows.ecmwf.int",
    license="BSD 3-Clause Clear",
    packages=find_namespace_packages(),
    package_data={"": resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
