<p align="center">
    <img src="https://user-images.githubusercontent.com/56393921/130352761-91b39f46-5f1d-4131-a8c0-d118bf77c48f.png">
</p>
<p align="center">
  
[![PyPI version](https://badge.fury.io/py/usgslidar.svg)](https://badge.fury.io/py/usgslidar) 
![GitHub issues](https://img.shields.io/github/issues-raw/Azariagmt/AgriTech-USGS-LIDAR)
![GitHub](https://img.shields.io/github/license/Azariagmt/AgriTech-USGS-LIDAR)
[![Documentation Status](https://readthedocs.org/projects/usgslidar/badge/?version=latest)](https://usgslidar.readthedocs.io/en/latest/?badge=latest)
 </p>
 
<div>  
  The USGS recently released high resolution elevation data as a lidar point cloud called <a href="https://www.usgs.gov/core-science-systems/ngp/3dep">USGS 3DEP</a> in a <a href="https://registry.opendata.aws/usgs-lidar/">public dataset on Amazon</a>. This dataset is essential to build models of water flow and predict plant health and maize harvest. 
</div>

<br>
<div>
  The purpose of this package (<b><a href="https://pypi.org/project/usgslidar/">usgslidar</a></b>) is to produce an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data. In particular, it interfaces with USGS 3DEP and fetches data available in the s3 instance. 
</div>

<h2>Table of content</h2>

1. <a href="#setup">Setup</a>
2. <a href="#usage">Usage</a>
3. <a href="#starting">Getting started (tutorial)</a>
4. <a href="#example">Example notebook</a>

<h3 id="setup"> Setup </h3>
To build our pipeline we actually use <a href="https://pdal.io/tutorial/iowa-entwine.html">PDAL</a> under the hood. Since PDAL doesnt build properly with pip in the current version, you need to use conda to manage your dependencies. 
<br>

<p>

  * Install [Anaconda](https://www.anaconda.com/)
  * In a conda environment install PDAL and python-pdal
    ```bash
    conda install -c conda-forge pdal python-pdal
    ```
  * Install usgslidar
    ```bash
    pip install usgslidar
    ```
</p>

<h3 id="usage"> Usage </h3>
<h3 id="starting"> Getting started </h3>
<h3 id="example"> Example notebook </h3>
demo ipynb
