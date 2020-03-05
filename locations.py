import pandas as pd

print 'Reading parcels'
parcels = pd.read_csv('parcels.csv').parcel_id
print 'There are %s parcels' % len(parcels)

print 'Reading 3GB CSV in Python, have patience'
trips = pd.read_csv('trips_2014.csv')

trips = trips[trips.opcl.isin(parcels)]
trips = trips[trips.dpcl.isin(parcels)]

trips['count1'] = 1
df = pd.DataFrame(trips.groupby(['hhno', 'pno'])['count1'].sum())

print '%s people are making more than one trip' % len(df[df['count1'] > 1])
