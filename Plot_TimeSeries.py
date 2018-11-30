from opedia import plotTS as TS

tables = ['tblSST_AVHRR_OI_NRT', 'tblAltimetry_REP', 'tblPisces_NRT']    # see catalog.csv  for the complete list of tables and variable names
variables = ['sst', 'sla', 'NO3']                                        # see catalog.csv  for the complete list of tables and variable names
startDate = '2016-03-29'
endDate = '2016-05-29'
lat1, lat2 = 25, 30
lon1, lon2 = -160, -155
depth1, depth2 = 0, 5
fname = 'TS'
exportDataFlag = False      # True if you you want to download data

TS.plotTS(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
