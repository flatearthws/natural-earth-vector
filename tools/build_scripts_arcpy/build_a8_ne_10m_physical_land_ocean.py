# ---------------------------------------------------------------------------
# build_a8_ne_10m_physical_land_ocean.py
# Created on: Tue Oct 08 2013 01:10:43 AM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
ne_10m_land_ocean_seams_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land_ocean_seams.shp"
ne_10m_minor_islands_coastline_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_minor_islands_coastline.shp"
ne_10m_coastline_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_coastline.shp"
ne_10m_physical_building_blocks_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\intermediate\\ne_10m_physical_building_blocks.shp"
ne_10m_land_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land_scale_rank.shp"
ne_10m_land_ocean_label_points_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land_ocean_label_points.shp"
ne_10m_ocean_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_ocean_scale_rank.shp"
ne_10m_ocean_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_ocean.shp"
ne_10m_land_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land.shp"
ne_10m_admin_0_map_subunits_test_shp__4_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_ocean.shp"
ne_10m_ocean = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_ocean.shp"
ne_10m_admin_0_map_subunits_test_shp__7_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_ocean.shp"
ne_10m_admin_0_map_subunits_test_shp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land.shp"
ne_10m_ocean__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land.shp"
ne_10m_admin_0_map_subunits_test_shp__3_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land.shp"

# Process: Feature To Polygon...
gp.FeatureToPolygon_management("C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_coastline.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_minor_islands_coastline.shp;C:\\ProjectFiles\\NaturalEarth\\nev_version_2d1d0\\10m_physical\\ne_10m_land_ocean_seams.shp", ne_10m_physical_building_blocks_shp, "", "ATTRIBUTES", ne_10m_land_ocean_label_points_shp)

# Process: Select (3)...
gp.Select_analysis(ne_10m_physical_building_blocks_shp, ne_10m_ocean_scale_rank_shp, "\"featurecla\" = 'Ocean'")

# Process: Dissolve...
gp.Dissolve_management(ne_10m_ocean_scale_rank_shp, ne_10m_ocean_shp, "featurecla", "scalerank MIN", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Field (2)...
gp.AddField_management(ne_10m_ocean_shp, "scalerank", "SHORT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__4_, "scalerank", "[MIN_scaler]", "VB", "")

# Process: Delete Field...
gp.DeleteField_management(ne_10m_ocean, "MIN_scaler")

# Process: Select...
gp.Select_analysis(ne_10m_physical_building_blocks_shp, ne_10m_land_scale_rank_shp, "\"featurecla\" = 'Land'")

# Process: Dissolve (2)...
gp.Dissolve_management(ne_10m_land_scale_rank_shp, ne_10m_land_shp, "featurecla", "scalerank MIN", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Field (3)...
gp.AddField_management(ne_10m_land_shp, "scalerank", "SHORT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__2_, "scalerank", "[MIN_scaler]", "VB", "")

# Process: Delete Field (2)...
gp.DeleteField_management(ne_10m_ocean__2_, "MIN_scaler")

