# import itertools
#
# process_graph = { "process_graph": {"imagery": {"imagery": {"extent": ["2017-01-01", "2017-01-31"],
#    "imagery": {"extent": {
#      "north": 49.041469,
#      "east": 17.171631,
#      "west": 9.497681,
#      "south": 46.517296,
#      "crs": "EPSG:32632"},
#     "imagery": {"process_id": "get_collection", "name": "s2a_prd_msil1c"},
#     "process_id": "filter_bbox"},
#    "process_id": "filter_daterange"},
#   "nir": "B08",
#   "process_id": "NDVI",
#   "red": "B04"},
#  "process_id": "min_time"}
# }
#
# process_part = [
#      '"north": 49.041469,'
#      '"east": 17.171631,'
#      '"west": 9.497681,'
#      '"south": 46.517296,'
#      '"crs": "EPSG:32632"']
#
# result_list = []
#
# for p1 in range(0, len(process_graph)):
#     buffer_list = []
#     for p2 in range(0, len(process_graph)):
#         buffer_list.append(process_graph[p1])


# import json
# response = '[{"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TQS_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TQS_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TQR_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TQR_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TPT_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TPT_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TPS_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TPS_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TNR_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TNR_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TQT_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TQT_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TNS_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TNS_20170504T101349.zip"}, {"date": "2017-05-04", "name": "S2A_MSIL1C_20170504T101031_N0205_R022_T32TNT_20170504T101349", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TNT_20170504T101349.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TNT_20170507T102319", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TNT_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TPS_20170507T102319", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TPS_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TQT_20170507T102319", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TQT_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TPT_20170507T102319", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TPT_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TNR_20170507T102319", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TNR_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TPR_20170507T102319", "timestamp": "2017-05-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TPR_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TNS_20170507T102319", "timestamp": "2017-05-12", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TNS_20170507T102319.zip"}, {"date": "2017-05-07", "name": "S2A_MSIL1C_20170507T102031_N0205_R065_T32TQS_20170507T102319", "timestamp": "2017-05-12", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TQS_20170507T102319.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TNS_20170514T101125", "timestamp": "2017-05-15", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TNS_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TPR_20170514T101125", "timestamp": "2017-05-15", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TPR_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TQS_20170514T101125", "timestamp": "2017-05-16", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TQS_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TQR_20170514T101125", "timestamp": "2017-05-16", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TQR_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TPS_20170514T101125", "timestamp": "2017-05-17", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TPS_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TPT_20170514T101125", "timestamp": "2017-05-17", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TPT_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TNR_20170514T101125", "timestamp": "2017-05-17", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TNR_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TNT_20170514T101125", "timestamp": "2017-05-17", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TNT_20170514T101125.zip"}, {"date": "2017-05-14", "name": "S2A_MSIL1C_20170514T101031_N0205_R022_T32TQT_20170514T101125", "timestamp": "2017-05-17", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TQT_20170514T101125.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TQT_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TQT_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TQS_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TQS_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TNS_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TNS_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TNT_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TNT_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TPS_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TPS_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TPR_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TPR_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TPT_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TPT_20170517T102352.zip"}, {"date": "2017-05-17", "name": "S2A_MSIL1C_20170517T102031_N0205_R065_T32TNR_20170517T102352", "timestamp": "2017-05-25", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TNR_20170517T102352.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TQS_20170524T101353", "timestamp": "2017-05-26", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TQS_20170524T101353.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TPS_20170527T102301", "timestamp": "2017-05-28", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TPS_20170527T102301.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TPS_20170524T101353", "timestamp": "2017-05-28", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TPS_20170524T101353.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TPT_20170524T101353", "timestamp": "2017-05-28", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TPT_20170524T101353.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TNR_20170524T101353", "timestamp": "2017-05-29", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TNR_20170524T101353.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TPT_20170527T102301", "timestamp": "2017-05-29", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TPT_20170527T102301.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TQS_20170527T102301", "timestamp": "2017-05-30", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TQS_20170527T102301.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TQT_20170524T101353", "timestamp": "2017-06-01", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TQT_20170524T101353.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TNS_20170524T101353", "timestamp": "2017-06-07", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TNS_20170524T101353.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TNT_20170524T101353", "timestamp": "2017-06-07", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TNT_20170524T101353.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TPR_20170524T101353", "timestamp": "2017-06-07", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TPR_20170524T101353.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TQT_20170527T102301", "timestamp": "2017-06-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TQT_20170527T102301.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TNT_20170527T102301", "timestamp": "2017-06-08", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TNT_20170527T102301.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TNS_20170527T102301", "timestamp": "2017-06-09", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TNS_20170527T102301.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TPR_20170527T102301", "timestamp": "2017-06-10", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TPR_20170527T102301.zip"}, {"date": "2017-05-27", "name": "S2A_MSIL1C_20170527T102031_N0205_R065_T32TNR_20170527T102301", "timestamp": "2018-08-10", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TNR_20170527T102301.zip"}, {"date": "2017-05-24", "name": "S2A_MSIL1C_20170524T101031_N0205_R022_T32TQR_20170524T101353", "timestamp": "2018-08-11", "path": "/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TQR_20170524T101353.zip"}]}: s2a_prd_msil1c <data.dependencies.arg_parser.BBox object at 0x7fcb815f4d68> 2017-05-01T00:00:00Z 2017-05-31T23:59:59Z'
# #response2 = "{'file_paths': \"[{'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TQS_20170504T101349_new', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TQS_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TQR_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TQR_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TPT_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TPT_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TPS_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TPS_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TNR_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TNR_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TQT_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TQT_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TNS_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TNS_20170504T101349.zip'}, {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TNT_20170504T101349', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TNT_20170504T101349.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TNT_20170507T102319', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TNT_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TPS_20170507T102319', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TPS_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TQT_20170507T102319', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TQT_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TPT_20170507T102319', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TPT_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TNR_20170507T102319', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TNR_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TPR_20170507T102319', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TPR_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TNS_20170507T102319', 'timestamp': '2017-05-12', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TNS_20170507T102319.zip'}, {'date': '2017-05-07', 'name': 'S2A_MSIL1C_20170507T102031_N0205_R065_T32TQS_20170507T102319', 'timestamp': '2017-05-12', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/07/S2A_MSIL1C_20170507T102031_N0205_R065_T32TQS_20170507T102319.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TNS_20170514T101125', 'timestamp': '2017-05-15', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TNS_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TPR_20170514T101125', 'timestamp': '2017-05-15', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TPR_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TQS_20170514T101125', 'timestamp': '2017-05-16', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TQS_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TQR_20170514T101125', 'timestamp': '2017-05-16', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TQR_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TPS_20170514T101125', 'timestamp': '2017-05-17', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TPS_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TPT_20170514T101125', 'timestamp': '2017-05-17', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TPT_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TNR_20170514T101125', 'timestamp': '2017-05-17', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TNR_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TNT_20170514T101125', 'timestamp': '2017-05-17', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TNT_20170514T101125.zip'}, {'date': '2017-05-14', 'name': 'S2A_MSIL1C_20170514T101031_N0205_R022_T32TQT_20170514T101125', 'timestamp': '2017-05-17', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/14/S2A_MSIL1C_20170514T101031_N0205_R022_T32TQT_20170514T101125.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TQT_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TQT_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TQS_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TQS_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TNS_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TNS_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TNT_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TNT_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TPS_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TPS_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TPR_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TPR_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TPT_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TPT_20170517T102352.zip'}, {'date': '2017-05-17', 'name': 'S2A_MSIL1C_20170517T102031_N0205_R065_T32TNR_20170517T102352', 'timestamp': '2017-05-25', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/17/S2A_MSIL1C_20170517T102031_N0205_R065_T32TNR_20170517T102352.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TQS_20170524T101353', 'timestamp': '2017-05-26', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TQS_20170524T101353.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TPS_20170527T102301', 'timestamp': '2017-05-28', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TPS_20170527T102301.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TPS_20170524T101353', 'timestamp': '2017-05-28', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TPS_20170524T101353.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TPT_20170524T101353', 'timestamp': '2017-05-28', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TPT_20170524T101353.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TNR_20170524T101353', 'timestamp': '2017-05-29', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TNR_20170524T101353.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TPT_20170527T102301', 'timestamp': '2017-05-29', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TPT_20170527T102301.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TQS_20170527T102301', 'timestamp': '2017-05-30', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TQS_20170527T102301.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TQT_20170524T101353', 'timestamp': '2017-06-01', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TQT_20170524T101353.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TNS_20170524T101353', 'timestamp': '2017-06-07', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TNS_20170524T101353.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TNT_20170524T101353', 'timestamp': '2017-06-07', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TNT_20170524T101353.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TPR_20170524T101353', 'timestamp': '2017-06-07', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TPR_20170524T101353.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TQT_20170527T102301', 'timestamp': '2017-06-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TQT_20170527T102301.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TNT_20170527T102301', 'timestamp': '2017-06-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TNT_20170527T102301.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TNS_20170527T102301', 'timestamp': '2017-06-09', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TNS_20170527T102301.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TPR_20170527T102301', 'timestamp': '2017-06-10', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TPR_20170527T102301.zip'}, {'date': '2017-05-27', 'name': 'S2A_MSIL1C_20170527T102031_N0205_R065_T32TNR_20170527T102301', 'timestamp': '2018-08-10', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/27/S2A_MSIL1C_20170527T102031_N0205_R065_T32TNR_20170527T102301.zip'}, {'date': '2017-05-24', 'name': 'S2A_MSIL1C_20170524T101031_N0205_R022_T32TQR_20170524T101353', 'timestamp': '2018-08-11', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/24/S2A_MSIL1C_20170524T101031_N0205_R022_T32TQR_20170524T101353.zip'}]}\""
#
# #response = response.replace("\"", "").replace("'", "\"")
#
# response = response.split("]")[0]+"]"
# #response2 = response2.replace("\"", "").replace("'", "\"")
# #print(response)
# #print(response[12700:12718])
# json_response = json.loads(response)
# json_response2 = json.loads(response)
#
# for file in json_response2:
#     found = False
#     for file2 in json_response:
#         if file["name"] == file2["name"]:
#             found = True
#             break
#     if not found:
#         print("not found {}".format(file))

import openeo
import logging
import time
import psycopg2
import json
# west, south, east, north
testcases = [
#  {"testcase": 1, "west": 10.288696, "south": 45.935871, "east": 12.189331, "north": 46.905246, "crs": "EPSG:4326", "begin": "2017-05-01", "end": "2017-05-31"}, # running example
# {"testcase": 2, "west": 26.330109, "south": -16.023376, "east": 28.171692, "north": -15.253714, "crs": "EPSG:4326", "begin": "2006-03-30", "end": "2006-03-30"}, # http:// dx.doi.org/ 10.3390/ rs8050402 1
# {"testcase": 3, "west": 26.830673, "south": -15.307366, "east": 27.052460, "north": -15.113227, "crs": "EPSG:4326", "begin": "2007-03-30", "end": "2007-03-30"}, # http:// dx.doi.org/ 10.3390/ rs8050402 2
# {"testcase": 4, "west": 25.563812, "south": -14.429360, "east": 26.092529, "north": -13.980713, "crs": "EPSG:4326", "begin": "2006-03-29", "end": "2006-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 3
# {"testcase": 5, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2007-07-23", "end": "2007-07-23"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 1
# {"testcase": 6, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2005-08-22", "end": "2005-08-22"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 2
# {"testcase": 7, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2007-07-23", "end": "2007-07-24"}, # http:// dx.doi.org/ 10.1016/j.jag.2016.12.003 1
# {"testcase": 8, "west": 16.506958, "south": 47.529257, "east": 17.188110, "north": 48.022998, "crs": "EPSG:4326", "begin": "2007-07-23", "end": "2007-07-24"}, # Big Data Infrastructures for Processing Sentinel Data, Wolfgang Wagner
# {"testcase": 9, "west": 104.276733, "south": 8.423470, "east": 106.809082, "north": 11.156845, "crs": "EPSG:4326", "begin": "2007-01-01", "end": "2011-01-01"}, # THE USE OF SAR BACKSCATTER TIME SERIES FOR CHARACTERISING RICE PHENOLOGY, DUY NGUYEN
# {"testcase": 10, "west": 17.078934, "south": 47.691739, "east": 18.022385, "north": 48.039070, "crs": "EPSG:4326",
#      "begin": "2016-05-24", "end": "2016-05-24"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 1
#{"testcase": 11, "west": 5.229492, "south": 36.261992, "east": 19.555664, "north": 46.830134, "crs": "EPSG:4326",
#     "begin": "2017-10-01", "end": "2017-10-31"} # Digital Object Identifier 10.1109/TGRS.2018.2858004 2
# {"testcase": 12, "west": 10.074463, "south": 44.425934, "east": 13.842773, "north": 46.065608, "crs": "EPSG:4326",
#      "begin": "2017-05-07", "end": "2017-05-07"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 3
# {"testcase": 13, "west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
#      "begin": "2017-04-01", "end": "2017-09-30"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 3
# {"testcase": 14, "west": 15.062256, "south": 47.197178, "east": 18.347168, "north": 48.994636, "crs": "EPSG:4326",
#      "begin": "2016-12-01", "end": "2016-12-31"}, #  https://doi.org/10.1080/01431161.2018.1479788 1
# {"testcase": 15, "west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
#      "begin": "2016-05-24", "end": "2016-05-24"}, #  doi:10.3390/rs10071030 1
# {"testcase": 16, "west": 6.855469, "south": 36.279707, "east": 19.291992, "north": 49.296472, "crs": "EPSG:4326",
#      "begin": "2017-10-01", "end": "2017-10-31"}, #  doi:10.3390/rs10071030 2
# {"testcase": 17, "west": 9.063721, "south": 44.190082, "east": 17.973633, "north": 49.253465, "crs": "EPSG:4326",
#      "begin": "2017-07-24", "end": "2017-07-24"}, #  doi:10.3390/rs10071030 3
 {"testcase": 18, "west": 6.350098, "south": 36.120128, "east": 18.830566, "north": 47.025206, "crs": "EPSG:4326",
      "begin": "2017-07-23", "end": "2017-07-23"} #  doi:10.3390/rs10071030 4
]

LOCAL_EODC_DRIVER_URL = "http://openeo.local.127.0.0.1.nip.io"

JOB_COLUMN_QUERY = "SELECT sum(pg_column_size(metrics)) as filesize, count(*) as filerow FROM jobs as t WHERE id = '{}'"
QUERY_TABLE_QUERY = "SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM query as t WHERE query_pid = '{}'"
QUERYJOB_TABLE_QUERY = "SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM queryjob as t WHERE job_id = '{}'"


logging.basicConfig(level=logging.INFO)
logging.info("--- Impact Evaluation ---")
logging.info("Connecting to the local back end {}...".format(LOCAL_EODC_DRIVER_URL))

# Connect to back end
con = openeo.connect(LOCAL_EODC_DRIVER_URL)
processes = con.get_processes()
# Reset back end database


storage_dict = {}
performance_dict = {}

NUMBER_OF_ITERATIONS = 1
MAX_TRY = 10

counter = 1
number_of_testcases = len(testcases)
for testcase in testcases:


    # Choose dataset
    pgA = processes.get_collection(name="s2a_prd_msil1c")
    pgA = processes.filter_daterange(pgA, extent=[testcase["begin"], testcase["end"]])
    pgA = processes.filter_bbox(pgA, west=testcase["west"], south=testcase["south"], east=testcase["east"], north=testcase["north"], crs=testcase["crs"])

    # Choose processes
    pgA = processes.ndvi(pgA, nir="B08", red="B04")
    pgA = processes.min_time(pgA)
    #logging.info("Creating testcase {}/{}...".format(counter, number_of_testcases))

    storage_dict[counter] = []
    performance_dict[counter] = []

    logging.info("Start testcase {}/{}...".format(counter, number_of_testcases))
    #time.sleep(2)
    jobA = con.create_job(pgA.graph)
    if jobA:
        jobA.start_job()
    time.sleep(10)
    for i in range(NUMBER_OF_ITERATIONS):

        logging.info("Reset back end database {}...".format(LOCAL_EODC_DRIVER_URL))
        con.resetdb()
        logging.info("Execution testcase {}/{}...".format(i, NUMBER_OF_ITERATIONS))
        #try:
        jobA = con.create_job(pgA.graph)
        if jobA:
            jobA.start_job()

            desc = jobA.describe_job
            tries = 0
            while desc["status"] == "submitted":
                time.sleep(2)
                desc = jobA.describe_job
                if tries >= MAX_TRY:
                    break
                tries += 1
            pidA = jobA.get_data_pid()
            try:
                connection = psycopg2.connect(user="bg",
                                          password="bg12345",
                                          host="172.30.161.214",
                                          port="5432",
                                          database="jobs")
                cursor = connection.cursor()
                storage_entry = []
                cursor.execute(JOB_COLUMN_QUERY.format(jobA.job_id))
                job_size = cursor.fetchall()
                storage_entry.append(job_size[0])
                cursor.execute(QUERY_TABLE_QUERY.format(pidA))
                query_size = cursor.fetchall()
                storage_entry.append(query_size[0])
                cursor.execute(QUERYJOB_TABLE_QUERY.format(jobA.job_id))
                queryjob_size = cursor.fetchall()
                storage_entry.append(queryjob_size[0])
                storage_dict[counter].append(storage_entry)
                #print(job_size)

            except (Exception, psycopg2.Error) as error:
                print("Error while fetching from PostgreSQL", error)
            finally:
                # closing database connection.
                if (connection):
                    cursor.close()
                    connection.close()
                    #print("PostgreSQL connection is closed")

            logging.info("Status of testcase {}: {}".format(counter, desc["status"]))
            if desc["status"] != "submitted":
                performance_dict[counter].append(desc["status"].split(";"))
        else:
            time.sleep(5)
        #except Exception:
        #    logging.info("Status of testcase {}: exception".format(counter))

    logging.info("Finished testcase {}/{}...".format(counter, number_of_testcases))
    counter += 1
with open('storage_file.json', 'w') as file:
    file.write(json.dumps(storage_dict))
with open('performance_file.json', 'w') as file:
    file.write(json.dumps(performance_dict))

# Get Size of job table:
# SELECT sum(pg_column_size(metrics)) as filesize, count(*) as filerow FROM jobs as t WHERE id = ;
# Get Size of Query table:
# SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM query as t WHERE id = ;
# Get Size of QueryJob table:
# SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM queryjob as t WHERE job_id = ;
