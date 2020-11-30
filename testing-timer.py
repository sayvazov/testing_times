import requests
import re
import csv
from datetime import datetime
from pdfminer.high_level import extract_text

print ("Downloading file.")

url = "https://hhinternet.blob.core.windows.net/wait-times/testing-wait-times.pdf"
r = requests.get(url)

pdf_path = "newest.pdf"
with open (pdf_path, "wb") as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

# Read file
text = extract_text("newest.pdf")
lines = text.splitlines()
lines = [a for a in lines if a]
start_index = lines.index("Select a Two-Hour Window")

# Get the two hour time window start.
date_string = (lines[start_index + 2])
date_string = date_string[:date_string.index("-") - 1]

date_object = datetime.strptime(date_string, "%m/%d/%Y | %H:%M %p")

 

#Parse each pair as a location/business
locations = []
for location_index in range(start_index+3, len(lines), 2):
    location = lines[location_index]
    # Need to remove parenthetical metadata
    location = re.sub("\(.*\)", "", location)
    busyness = lines[location_index +1]
    locations.append([location, busyness])

with open(f"output{date_object.__str__()}.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(locations)

#print (locations)