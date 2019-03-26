Independent-Study-Project

Data given:

a) Max Temperature

b) Min temperature

c) Average Tempersture


Step 1 -:  To visualize data in arcgis and gstat integrated with qgis. Clean data using python libraries.

Step 2 -:  Interpolation Technique

"Gridded Data" for precip is obtained by interpolation from rain gage data perhaps as spatial averages, in that case you need to know what interpolation method was used and how it was used. Likewise temperature is usually observed at point locations and you only get gridded data by interpolation.

    Spatial Interpretation: Estiamting the value of properties at unsampled space within area covered by observations.
    
    methods:
    
           Point baswd interpolation techniques
           
           a) IDW inverse distance interpolation
           
           b) Spline Interpolation Technique
           
           c) Kriging Interpolation technique
   
Step 3-: Find Threshold and Cluster based on some algorithm

Step4: Find Correlation, risk and Intensity between grids as well along with population data. like what is the frequency of heat waves in that grid. What is intensity and how grids are correlated.

Referemces:

https://www.google.com/amp/s/www.researchgate.net/post/What_is_an_appropriate_spatial-interpolation_method_for_temperature/amp

https://m.youtube.com/watch?v=FJAiJ1fVljo

http://www.gisresources.com/types-interpolation-methods_3/


## Challenges:

Extremeties:

It is always taken that for atleast 6 days if temperature exceed 90% percentile its heat wave and if its less than 10% its cold wave.

But For India, It depend on grid.


For threshold temperature:

a) For each grid, set temperature as Mean +/- 3* Std. Cons: It also depend on nearby areas. It might ignore temperature of surrounding areas.

b) we have to find different threshold of days and temperature for each grid. One approach is we have temperature, lattitude, longitude,dates: we find spatial clusters inside india. Clusters should take distance into account. After finding clusters, we set threshold for each cluster by finding mean and Std. It takes surrounding areas into account and temperature acoss full data.


Specs to be considered( for presentation and workflows) -:
a) Intensity
b) Co-relation
c) Frequency 
d) Vulnerability
e) Population projection




## Studies:

https://www.sarahinscience.com/blog/whats-the-right-way-to-measure-heatwaves

https://www.researchgate.net/publication/270292252_The_Excess_Heat_Factor_A_Metric_for_Heatwave_Intensity_and_Its_Use_in_Classifying_Heatwave_Severity

