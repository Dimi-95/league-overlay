from riotwatcher import LolWatcher, ApiError
import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context #use this to bypass the SSL error from the HTTP request

api_key = "RGAPI-c4c24621-36f1-4bc6-b03a-f7b7fe5b5cb2"
watcher = LolWatcher(api_key) #main interaction point of the League Api


player_name = urllib.request.urlopen("https://127.0.0.1:2999/liveclientdata/activeplayername") #open the URL/Data end point of RIOT

#----READ AND GET INFRO FROM URL---------

data = player_name.read() #read the URL
encoding = player_name.info().get_content_charset("utf8") #Turn the acquired information into readable characters
result = json.loads(data.decode(encoding)) #turn everything into a readable format (show basically the end result)


#---- SKILLS being used ----
#while True:
player_active = urllib.request.urlopen("https://127.0.0.1:2999/liveclientdata/activeplayer")


data_skills = player_active.read()
encoding_2 = player_active.info().get_content_charset("utf8")
result_2 = json.loads(data_skills.decode(encoding))

skills = result_2["fullRunes"]

print(skills)