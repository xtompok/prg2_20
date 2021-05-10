import rasterio
import rasterio.merge
from rasterio.plot import show

#SRTM download: https://step.esa.int/auxdata/dem/SRTMGL1/
srtm1 = rasterio.open("N50E014.hgt")
srtm2 = rasterio.open("N50E015.hgt")
print(srtm1)
print(srtm1.width,srtm1.height)
print(srtm1.bounds)
print(srtm1.crs)
print(srtm1.indexes)
print(srtm2)
print(srtm2.width,srtm1.height)
print(srtm2.bounds)
print(srtm2.crs)
print(srtm2.indexes)
merged,transform = rasterio.merge.merge((srtm1,srtm2))
show(merged,cmap='terrain')
out_meta = srtm1.meta.copy()
out_meta.update({"driver": "GTiff",
                 "height": merged.shape[1],
                 "width": merged.shape[2],
                 "transform": transform,
                 "crs": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs "
                 }
                )
with rasterio.open("merged.tiff", "w", **out_meta) as dest:
    dest.write(merged)

merged2 = rasterio.open("merged.tiff")
print(merged2.bounds, merged2.crs)