import requests
from html.parser import HTMLParser
from google_maps_api_key import API_KEY

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


# A Google Maps Directions API request takes the following form:
# https://maps.googleapis.com/maps/api/directions/output?parameters

# Example:
# The following request returns driving directions from Toronto, Ontario to Montreal, Quebec:
# https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=YOUR_API_KEY

# Locations
loc1 = '7024 west carol ave Niles IL'.replace(' ', "%20")
loc2 = '9053 Laramie Avenue Skokie'.replace(' ', "%20")

URL = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&key={2}".\
    format(loc1, loc2, API_KEY)

print(URL)

r = requests.get(URL)
obj = r.json()
steps = obj["routes"][0]["legs"][0]["steps"]

print(obj)

for step in steps:
    print(strip_tags(step["html_instructions"]))
