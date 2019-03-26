# Given a csv convert that to raster form that can be used in qgis

library(raster)

# example data
temp <- read.csv("method_each_season_4.csv", header=TRUE)


# if these are points on a regular raster, you can do
x <- rasterFromXYZ(temp[, c('lon', 'lat', 'spike')])

# in your case (no need to compute rows/colums):
#x <- raster(xmn=70.5, xmx=100.5, ymn=5.5, ymx=50.5, res=1.0, crs="+proj=longlat +datum=WGS84")
v <- getValues(x)
print(v)
writeRaster(x, "waves/s4_heat.grd")
#us_fire <- rasterize(temp[, c('Longitude', 'Latitude')], x, temp[, 'std'], fun=mean)
#plot(us_fire)