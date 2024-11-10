-- Adjusted script to handle multiple styles and ensure compatibility
SELECT band_name,
       COALESCE(YEAR(split) - YEAR(formed), YEAR(CURDATE()) - YEAR(formed)) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', REPLACE(style, ' ', '')) > 0
ORDER BY lifespan DESC;
