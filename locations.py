import pandas as pd

print 'Reading parcels'
parcels = pd.read_csv('parcels.csv').parcel_id
print 'There are {:,} parcels'.format(len(parcels))

print 'Reading 3GB CSV in Python, have patience'
trips = pd.read_csv('trips_2014.csv')
print 'There are {:,} total trips'.format(len(trips))

trips = trips[trips.opcl.isin(parcels)]
trips = trips[trips.dpcl.isin(parcels)]
print 'There are {:,} trips contained within the specififed parcels'.format(len(trips))

trips['count1'] = 1
df = pd.DataFrame(trips.groupby(['hhno', 'pno'])['count1'].sum())

print '{:,} people are making more than one trip'.format(len(df[df['count1'] > 1]))
print '{:,} people are making exactly one trip'.format(len(df[df['count1'] == 1]))
print '{:,} people are making zero trips'.format(len(df[df['count1'] == 0]))
