#!/usr/bin/env python
from setuptools import setup

setup(
    name="jupyter_qtconsole_colorschemes",
    version="0.4.2-1",
    author="Joon Ro",
    author_email="joon.ro@outlook.com",
    url="https://bitbucket.org/joon/color-schemes-for-ipython-qt-console",
    download_url="https://bitbucket.org/joon/color-schemes-for-ipython-qt-console/get/v0.4.2-1.zip",
    description="Color Schemes for Jupyter Qt Console",
    packages=["jupyter_qtconsole_colorschemes"],
    package_data={"jupyter_qtconsole_colorschemes": ["*.css"]},
    entry_points={"pygments.styles": [
        "base16_ocean_dark = jupyter_qtconsole_colorschemes.base16_ocean_dark:Base16OceanDarkStyle",
        "solarizeddark = jupyter_qtconsole_colorschemes.solarizeddark:SolarizeddarkStyle",
        "solarizedlight = jupyter_qtconsole_colorschemes.solarizedlight:SolarizedlightStyle",
        "tomorrow = jupyter_qtconsole_colorschemes.tomorrow:TomorrowStyle",
        "zenburn = jupyter_qtconsole_colorschemes.zenburn:ZenburnStyle"]}
)

