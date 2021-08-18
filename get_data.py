import pdal
import json
import geopandas
from pyproj import Transformer

PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

REGION = "USGS_LPC_CO_SoPlatteRiver_Lot5_2013_LAS_2015/"

MINX, MINY, MAXX, MAXY = [-93.756155, 41.918015, -93.747334, 41.921429]
BOUNDS = f"({[MINX,MAXX]},{[MINY,MAXY]})"
BOUNDS = "([-11669524, -11666600.8],[4776607.3, 4778714.4])"


transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
xmin, ymax = transformer.transform(MINX, MAXY)
xmax, ymin = transformer.transform(MAXX, MINY)
pdal_aoi_bounds = f"([{xmin}, {xmax}], [{ymin}, {ymax}])"


PUBLIC_ACCESS_PATH = PUBLIC_DATA_PATH+REGION+"ept.json"

OUTPUT_FILENAME_LAZ = "laz/SoPlatteRiver.laz"
OUTPUT_FILENAME_TIF = "tif/SoPlatteRiver.tif"

PIPELINE_PATH = "get_data.json"


def get_raster_terrain(bounds: str, region: str, PUBLIC_ACCESS_PATH: str = PUBLIC_ACCESS_PATH,
                       OUTPUT_FILENAME_LAZ: str = OUTPUT_FILENAME_LAZ, OUTPUT_FILENAME_TIF: str = OUTPUT_FILENAME_TIF,
                       PIPELINE_PATH: str = PIPELINE_PATH
                       ) -> None:
    with open(PIPELINE_PATH) as json_file:
        the_json = json.load(json_file)

    the_json['pipeline'][0]['bounds'] = bounds

    the_json['pipeline'][0]['filename'] = PUBLIC_ACCESS_PATH

    the_json['pipeline'][2]['filename'] = OUTPUT_FILENAME_LAZ
    the_json['pipeline'][3]['filename'] = OUTPUT_FILENAME_TIF

    pipeline = pdal.Pipeline(json.dumps(the_json))

    try:

        pipe_exec = pipeline.execute()
        metadata = pipeline.metadata

    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    get_raster_terrain(bounds=BOUNDS, region=REGION)
