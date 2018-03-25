# http://oco-carbon.com/coding/wunderground-data-to-csv/

import csv
import datetime
import os

import requests # this library makes html requests much simpler


# add your API key (from wunderground) here
api_key = "e074ea046bda0f94"
station_ids = ["VA/Charlottesville", ] # add more stations here if required


for station_id in station_ids:
	print "Fetching data for station ID: %s" % station_id
	# initialise your csv file
	with open('wunderground.csv', 'wb') as outfile:
		writer = csv.writer(outfile)
		headers = ['date','temperature','precipm'] # edit these as required
		writer.writerow(headers)

		# enter the first and last day required here
		start_date = datetime.date(2017,01,01)
		end_date = datetime.date(2017,12,31)

		date = start_date
		while date <= end_date:
			print(date)
			# format the date as YYYYMMDD
			date_string = date.strftime('%Y%m%d')
			# build the url
			url = ("http://api.wunderground.com/api/%s/history_%s/q/%s.json" %
					  (api_key, date_string, station_id))
			# make the request and parse json
			data = requests.get(url).json()
			# build your row
			for history in data['history']['observations']:
				row = []
				row.append(str(history['date']['pretty']))
				row.append(str(history['tempm']))
				row.append(str(history['precipm']))       
				writer.writerow(row)
			# increment the day by one
			date += datetime.timedelta(days=1)

print "Done!"
