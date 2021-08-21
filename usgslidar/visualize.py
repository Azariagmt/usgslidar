import numpy as np
import laspy as lp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from get_data import get_geopandas_dataframe
import geopandas as gpd
from logs import log

logger = log(path="../logs/", file="visualize.logs")
logger.info("Starts Visualize script")

input_path="../data/laz/"
dataname="SoPlatteRiver"

point_cloud = lp.read(input_path+dataname+".las")

colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

def plot_3d_map():
    try:
        gdf = gpd.read_file("../data/elevation.csv")
        gdf.crs = "epsg:4326"
        logger.info("Dataframe loaded successfully")
    except RuntimeError as e:
        logger.exception("Dataframe couldn't be loaded.")
    x = gdf.geometry.x
    y = gdf.geometry.y
    z = gdf.elevation
    points = np.vstack((x, y, z)).transpose()
    factor=160
    decimated_points = points[::factor]
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax = plt.axes(projection='3d')
    ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2],  s=0.01, color="blue")
    plt.show()

# get the points and colors from point cloud data
# points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()


# ax = plt.axes(projection='3d')
# ax.scatter(points[:,0], points[:,1], points[:,2], c = colors/255, s=0.01)
# plt.show()

if __name__ == "__main__":
    plot_3d_map()


# print(len(points))
# factor=160
# decimated_points = points[::factor]
# print(len(decimated_points))

# voxel_size=6
# nb_vox=np.ceil((np.max(points, axis=0) - np.min(points, axis=0))/voxel_size)

# non_empty_voxel_keys, inverse, nb_pts_per_voxel = np.unique(((points - np.min(points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True, return_counts=True)
# idx_pts_vox_sorted=np.argsort(inverse)

# voxel_grid={}
# grid_barycenter,grid_candidate_center=[],[]
# last_seen=0

# for idx,vox in enumerate(non_empty_voxel_keys):
#     voxel_grid[tuple(vox)]= points[idx_pts_vox_sorted[last_seen:last_seen+nb_pts_per_voxel[idx]]]
#     grid_barycenter.append(np.mean(voxel_grid[tuple(vox)],axis=0))
#     grid_candidate_center.append(voxel_grid[tuple(vox)][np.linalg.norm(voxel_grid[tuple(vox)] - np.mean(voxel_grid[tuple(vox)],axis=0),axis=1).argmin()])
#     last_seen+=nb_pts_per_voxel[idx]


# decimated_colors = colors[::factor]
# ax = plt.axes(projection='3d')
# ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2], c = decimated_colors/65535, s=0.01)
# plt.show()
