# Script derived from https://gist.github.com/dlo/7177249, expanded to output Gcal CSV format.

# must install requests -> http://docs.python-requests.org/en/latest/user/install/
import requests
import json
import datetime
import csv
 
foursquareHistoryAPI = 'https://api.foursquare.com/v2/users/self/checkins?limit=250&oauth_token={}&v=20150108&offset={}'
 
# If you navigate to https://developer.foursquare.com/docs/explore, Foursquare
# will generate an OAuth token for you automatically. Cut and paste that token
# below.
token = ""

#Var's to loop through entire history, 250 at a time.
increment = 250  #static
offset = 0
 
with open("checkins.csv", 'w') as csvfile:
    while True:
        response = requests.get(foursquareHistoryAPI.format(token, offset))
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #Header Row
        csvfile.write("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n")
        

        if len(response.json()['response']['checkins']['items']) == 0:
            break

        for item in response.json()['response']['checkins']['items']:  #only concerned with checkins
        	if 'venue' in item:  #valid checkin
	        	
	        	#Build a array of the CSV items
	        	str_list = []
	        	str_list.append(item['venue']['name'].encode('utf-8'))
	        	str_list.append(datetime.datetime.fromtimestamp(int(item['createdAt'])).strftime('%Y/%m/%d'))
	        	str_list.append(datetime.datetime.fromtimestamp(int(item['createdAt'])).strftime('%I:%M:%S %p'))
	        	str_list.append(datetime.datetime.fromtimestamp(int(item['createdAt'])+3600).strftime('%Y/%m/%d'))
	        	str_list.append(datetime.datetime.fromtimestamp(int(item['createdAt'])+3600).strftime('%I:%M:%S %p'))
	        	str_list.append("False")
	        	str_list.append("https://foursquare.com/v/foursquare-hq/"+item['venue']['id'])
	        	str_list.append(" ".join(item['venue']['location']['formattedAddress']).encode('utf-8'))
	        	str_list.append("True")

	        	#Dump the array out - Not the best way, but it works and I'm being lazy.
	        	spamwriter.writerow([str_list[0],str_list[1],str_list[2],str_list[3],str_list[4],str_list[5],str_list[6],str_list[7],str_list[8]])
 
 		#Grab the next group
        offset += increment
