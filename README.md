Base of this script was derived from: [this page](https://gist.github.com/dlo/7177249)

# Instructions
1. Install python library [Requests](http://docs.python-requests.org/en/latest/user/install/)

2. Get your foursquare auth [token](https://developer.foursquare.com/docs/explore)

3. After inserting your token into the script, run with `python run.py`

4. For good measure, verify the CSV output (in same directory) looks right: `head checkins.csv`

5. Create a new calendar in Google. **You can bulk import, but you CANNOT bulk delate without deleting the entire calendar.**

6. Do the import. `Other Calendars -> Import Calendar`. Select the calendar name you want to load and the CSV file. 

