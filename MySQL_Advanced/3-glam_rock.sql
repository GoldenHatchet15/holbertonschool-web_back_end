-- Script to list Glam rock bands ranked by their longevity
SELECT band_name,
       IFNULL(YEAR(split) - YEAR(formed), YEAR(CURDATE()) - YEAR(formed)) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
