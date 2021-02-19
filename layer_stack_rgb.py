Created on Thu Feb 18 21:07:45 2021

@author: pyada
"""

import rasterio
import rasterio.crs
import rasterio.warp

r=r'path to your red_band.tif'
g=r'path to your green_band.tif'
b=r'path to your blue_band.tif'
stacked_path = r'path to your layer stacked rgb.tif' 

def layer_stack_rgb(r,g,b,stacked_path):
    
    file_list = [r, g, b]
    

    # Read metadata of first file
    with rasterio.open(file_list[0]) as src0:
        meta = src0.meta

    # Update meta to reflect the number of layers
    meta.update(count = len(file_list))

    # Read each layer and write it to stack
    with rasterio.open(stacked_path, 'w', **meta) as dst:
        for id, layer in enumerate(file_list, start=1):
            with rasterio.open(layer) as src1:
                dst.write_band(id, src1.read(1))
    raster = rasterio.open(stacked_path)
    raster.crs
    raster.transform
    raster_arr = raster.read()
    print(raster_arr.shape)

layer_stack_rgb(r,g,b,stacked_path)
