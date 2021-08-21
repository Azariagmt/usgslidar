import pdal
import json
import geopandas as gpd
from pyproj import Transformer
from logs import log
from shapely.geometry import Polygon, Point


logger = log(path="../logs/", file="get_data.logs")
logger.info("Starts Get data script")

PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

REGION = "IA_FullState/"

MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
BOUNDS = f"({[MINX,MAXX]},{[MINY,MAXY]})"
BOUNDS = "([-11669524, -11666600.8],[4776607.3, 4778714.4])"

PUBLIC_ACCESS_PATH = PUBLIC_DATA_PATH+REGION+"ept.json"

# TODO ask user to input filename
OUTPUT_FILENAME_LAZ = "../data/laz/SoPlatteRiver.las"
OUTPUT_FILENAME_TIF = "../data/tif/SoPlatteRiver.tif"

PIPELINE_PATH = "get_data.json"


def get_polygon_boundaries(polygon: Polygon, input_epsg : int = 3857, output_epsg :int = 4326):
    """Gets the required polygon boundaries

    Arguments:
        Polygon -- A shapely polygon
                   https://shapely.readthedocs.io/en/stable/manual.html
        Input epsg -- The input CRS reference system
                      default -- 3857
        Output epsg -- The output CRS reference system
                      default -- 26915
    
    Returns: A tuple of lists containing rectangular boundary
            ([minx, maxx],[miny,maxy]) &
            the initial user polygon input
    
    """
    polygon_df = gpd.GeoDataFrame([polygon], columns=['geometry'])

    polygon_df.set_crs(epsg=output_epsg, inplace=True)
    polygon_df['geometry'] = polygon_df['geometry'].to_crs(
        epsg=input_epsg)
    minx, miny, maxx, maxy = polygon_df['geometry'][0].bounds

    polygon_input = 'POLYGON(('

    xcord, ycord = polygon_df['geometry'][0].exterior.coords.xy
    for x, y in zip(list(xcord), list(ycord)):
        polygon_input += f'{x} {y}, '
    polygon_input = polygon_input[:-2]
    polygon_input += '))'
    
    print(polygon_input)

    return f"({[minx, maxx]},{[miny,maxy]})", polygon_input


def get_raster_terrain(polygon: list, region: str, PUBLIC_ACCESS_PATH: str = PUBLIC_ACCESS_PATH,
                       OUTPUT_FILENAME_LAZ: str = OUTPUT_FILENAME_LAZ, OUTPUT_FILENAME_TIF: str = OUTPUT_FILENAME_TIF,
                       PIPELINE_PATH: str = PIPELINE_PATH
                       ) -> None:
    """Initializes the PDAL pipeline and gets bound for entire region

    Arguments: 
        Polygon (list of x,y coordinate tuples) -- sets boundary
        region (string) -- region
    
    Optional Arguments:
        PIPELINE_PATH (string) -- path to new PDAL pipeline

    Returns:
        Arrays from the PDAL pipeline
    """
    try:
        input_polygon = Polygon(polygon)
        MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
        input_polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
        logger.info("Polygon input success!")
    except RuntimeError as e:
        logger.exception("Polygon input error")
        
    try:
        bounds, polygon_input = get_polygon_boundaries(input_polygon)
        logger.info("Rectangular input extracted successfully")
    except RuntimeError as e:
        logger.exception("Polygon extraction error")


    # TODO convert CRS to 3857

    try:
        with open(PIPELINE_PATH) as json_file:
            the_json = json.load(json_file)
 

        the_json['pipeline'][0]['bounds'] = bounds
        the_json['pipeline'][0]['filename'] = PUBLIC_ACCESS_PATH

        the_json['pipeline'][1]['polygon'] = polygon_input

        # TODO replace 4326 with out_srs
        # the_json['pipeline'][4]['out_srs'] = "EPSG:4326" 
        
        the_json['pipeline'][4]['filename'] = OUTPUT_FILENAME_LAZ
        # the_json['pipeline'][6]['filename'] = OUTPUT_FILENAME_TIF

        pipeline = pdal.Pipeline(json.dumps(the_json))

        logger.info("pipeline initiated")
    except RuntimeError as e:
        logger.exception("failed to initiate pipeline")
    try:
        pipe_exec = pipeline.execute()
        print(pipe_exec)
        # TODO all the comments
        # list df numpy arrays...x, y and z bounds
        # laz file contains a lot of info
        # interested in elevation point
        # z is the elevation
        metadata = pipeline.metadata
        print(metadata)
        logger.info("Pipeline executed and metadata generated successfully")
    except RuntimeError as e:
        logger.exception("Failed to generate metadata and execute pipeline")

    try:
        print("PIPE EXEC return")
        pipeline_arrays =  pipeline.arrays
        print(pipeline_arrays)
        logger.info("Pipeline arrays successfully returned.")
        return pipeline_arrays
    except RuntimeError as e:
        logger.exception("Failed to retrieve pipeline arrays")



def get_elevetion(array_data, crs_epgs=4326): 
    """Returns the elevation of each point in the point_cloud data
    
    """  
    if array_data:
        for i in array_data:
            geometry_points = [Point(x, y) for x, y in zip(i["X"], i["Y"])]
            elevetions = i["Z"]
            df = gpd.GeoDataFrame(columns=["elevation", "geometry"])
            df['elevation'] = elevetions
            df['geometry'] = geometry_points
            df = df.set_geometry("geometry")
            df.set_crs(epsg=crs_epgs, inplace=True)
        print(df)
        df.to_file("../data/elevation.geojson", driver='GeoJSON')
        return df

    return None

def get_geopandas_dataframe():
    """
    
    """
    pipeline_arrays = get_raster_terrain(polygon=[(-93.756155, 41.918015),( -93.747334, 41.921429), (-93.756155, 41.918015), (-93.756155, 41.918015) ], region="IA_FullState")
    elevation_df = get_elevetion(pipeline_arrays)
    return elevation_df


if __name__ == "__main__":
    parrays = get_raster_terrain(polygon=[(-93.756155, 41.918015),( -93.747334, 41.921429), (-93.756155, 41.918015), (-93.756155, 41.918015) ], region="IA_FullState")
    get_elevetion(parrays)
