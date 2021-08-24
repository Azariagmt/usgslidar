import numpy as np
import laspy as lp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# from get_data import get_geopandas_dataframe
import geopandas as gpd
from .logs import log
import os

if (not os.path.isdir('./logs')):
    os.mkdir("./logs")

logs_path = "./logs/visualize.logs"
if not os.path.exists(logs_path):
    with open(logs_path, "w"):
        global logger
        logger = log(path="./logs/", file="visualize.logs")
        logger.info("Starts Visualize script")
else:
    logger = log(path="./logs/", file="visualize.logs")
    logger.info("Starts Visualize script")


input_path = "../data/laz/"
dataname = "SoPlatteRiver"

point_cloud = lp.read(input_path+dataname+".las")

colors = np.vstack((point_cloud.red, point_cloud.green,
                   point_cloud.blue)).transpose()


def plot_3d_map(df=None):
    """Plots 3d map of input dataframe

    Arguments: df, takes in dataframe 
    return: None

    """
    if df['elevation'][0] != None:
        gdf = df
        gdf.crs = "epsg:4326"
        print(gdf)

    x = gdf.geometry.x
    y = gdf.geometry.y
    z = gdf.elevation
    points = np.vstack((x, y, z)).transpose()
    factor = 160
    decimated_points = points[::]
    decimated_colors = colors[::]
    print(len(decimated_colors))
    print(decimated_colors)
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax = plt.axes(projection='3d')
    ax.scatter(decimated_points[:, 0], decimated_points[:, 1],
               decimated_points[:, 2],  s=0.01, color=decimated_colors/255)
    plt.show()
