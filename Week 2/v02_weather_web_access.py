import urllib, json

city_name = raw_input("What city would you like to know about? ")
api_url = "http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric" % urllib.quote(city_name)

try: 
    response = urllib.urlopen(api_url)
    json_tree = json.loads(response.read())
    
    if json_tree['cod'] == 200:
        temperature = json_tree["main"]["temp"]
        description = json_tree["weather"][0]["description"]
        
        print "It is " + str(temperature) +  " degrees in " + city_name 
        print "The weather can be described as \"" + description + "\"."
    else:
        print "The service doesn't know that city."

except Exception:
    print "Couldn't connect to the openweathermap service."
