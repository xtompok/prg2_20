import rasterio
from pyproj import CRS, Transformer

ll_wgs = (50.08, 14.40)
ur_wgs = (50.10, 14.42)

wgs2jtsk = Transformer.from_crs(4326,5514)

ll_jtsk = wgs2jtsk.transform(*ll_wgs)
ur_jtsk = wgs2jtsk.transform(*ur_wgs)
print(ll_jtsk, ur_jtsk)

# DTM download: https://www.geoportalpraha.cz/cs/data/otevrena-data/609AB233-4F4B-4010-A6E0-011E232E2390
big = rasterio.open("DTM.tif")
print(big.bounds)
print(big.width, big.height)
print(big.crs)
print(big.indexes)

ll_px = big.index(*ll_jtsk)
ur_px = big.index(*ur_jtsk)
print(ll_px, ur_px)

out_meta = big.meta.copy()
out_meta.update({"driver": "GTiff",
                 "height": merged.shape[1],
                 "width": merged.shape[2],
                 "transform": transform,
                 "crs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs "
                 }
                )
with rasterio.open("merged.tiff", "w", **out_meta) as dest:
    dest.write(merged)