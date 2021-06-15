import skmob

import pandas as pd

from skmob.preprocessing import detection

url = skmob.utils.constants.GEOLIFE_SAMPLE

df = pd.read_csv(url, sep=',', compression='gzip')

tdf = skmob.TrajDataFrame(df, latitude='lat', longitude='lon', user_id='user', datetime='datetime')

print(tdf)


stdf = detection.stops(tdf, stop_radius_factor=0.5, minutes_for_a_stop=20.0, spatial_radius_km=0.2, leaving_time=True)

print(stdf.head())


print(stdf.parameters)

print('Points of the original trajectory:\t%s'%len(tdf))

print('Points of stops:\t\t\t%s'%len(stdf))

print(pd.to_datetime(1490195805, unit='s'))
