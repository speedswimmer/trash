import urllib.request
import json

def printResult(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    count = theJSON["metadata"]["count"]
    print (str(count) + " events recorded")

    for i in theJSON["features"]:
        print(i["properties"]["place"], "-", i["properties"]["alert"])
    print("---------------------\n")

    #for i in theJSON["features"]:
    #    if i["properties"]["mag"] 
          
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl = urllib.request.urlopen(urlData)
    print("result code: " + str(weburl.getcode()))
    
    if weburl.getcode() == 200:
        data = weburl.read()
        #print(data)
        printResult(data)
    else:
        print("Received error, cannoct parse results")

if __name__ == "__main__":
    main()
