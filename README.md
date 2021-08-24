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
Full Documentation for usgslidar package can be found <a href="https://usgslidar.readthedocs.io/en/latest/?">here</a>.
<h3 id="starting"> Getting started </h3>
Lets view an example of visualizing a point cloud data on a farm in Iowa
<p>

  * From the get_data module lets import the get_geopandas_dataframe module
      ```python
      from usgslidar.get_data import get_geopandas_dataframe
      ```
    
  * We will get back the elevation and geometry dataframe when we call the get_geopandas_dataframe function
    ```python
    elevation_df = get_geopandas_dataframe()
    ```
    
  * Lets now import the plot_3d_map function from the visualize module to help us plot the 3d map
    ```python
    from usgslidar.visualize import plot_3d_map
    ```
    
  * We can now plot the 3d map calling the function and passing in the elevation dataframe we got above
    ```python
    plot_3d_map(df=elevation_df)
    ```
    
  * We will get an output of a 3d plot like below that we can play around with
    
  ![output](https://user-images.githubusercontent.com/56393921/130657829-826d2fe0-3857-4da6-a722-2ccd2875f985.png)
  
    
</p>

<h3 id="example"> Examples </h3>
Example notebooks with specific purposes can be found <a href="https://github.com/Azariagmt/usgslidar/tree/main/demo-notebooks">here.</a>
