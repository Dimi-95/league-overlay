from tkinter import *
import os
from PIL import Image, ImageDraw, ImageFont
import win32api, win32gui
from time import time
import urllib.request
import ssl
import json
from riotwatcher import LolWatcher, ApiError

ssl._create_default_https_context = ssl._create_unverified_context
api_key = [API KEY FROM RIOT]
watcher = LolWatcher(api_key)
my_region = "euw1"
fnt = ImageFont.truetype('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\fonts\\Friz Quadrata Regular.ttf', 22)


player_name = urllib.request.urlopen("https://127.0.0.1:2999/liveclientdata/activeplayername") #open the URL/Data end point of RIOT

#----READ AND GET INFRO FROM URL---------

data = player_name.read() #read the URL
encoding = player_name.info().get_content_charset("utf8") #Turn the acquired information into readable characters
live_player_name = json.loads(data.decode(encoding)) #turn everything into a readable format (show basically the end result)

me = watcher.summoner.by_name(my_region, f"{live_player_name}")
my_ranked_stats = watcher.league.by_summoner(my_region, me["id"])

tier = my_ranked_stats[0]["tier"]
rank = my_ranked_stats[0]["rank"]
wins = my_ranked_stats[0]["wins"]
losses = my_ranked_stats[0]["losses"]
lp = my_ranked_stats[0]["leaguePoints"] # add "LP" at the end of it
wr = round(wins/(wins+losses)*100) # add "%" at the end of it


#------------find and store the | x,y and widthxheight | of a window---------------------------

save = win32gui.FindWindow(None, "League of Legends (TM) Client") #Finds the window - if it is online

(x, y, width, heigth) = win32gui.GetWindowRect(save) #saves the coordinates

position = (x, y, width, heigth) 

print(position)

#----------------------------------------

root = Tk()
root.title("Dimi")
root.iconbitmap() #the icon next to the label/title
root.geometry(f"{width}x{heigth}+{x-480}+{y+5}") #Wide screen
#root.geometry(f"{width}x{heigth}+{x}+{y}") #Normal screen
root.wm_attributes('-topmost', 1, '-transparentcolor', '#abcdef') # topmost and the number next to it make sure that the window stays on top of other windows | transparentcolor make the window transparent
root.attributes("-alpha", 0.9)
root.config(bg='#abcdef')
root.overrideredirect(1) #removes the frame of the window, making it headless


#--------------Get runes from game and feed them to get the right picture

player_active = urllib.request.urlopen("https://127.0.0.1:2999/liveclientdata/activeplayer")


data_skills = player_active.read()
encoding_2 = player_active.info().get_content_charset("utf8")
result_2 = json.loads(data_skills.decode(encoding_2))

live_runes = result_2["fullRunes"]

live_keystone = live_runes["generalRunes"][0]["displayName"] # from 0-5 for all runes, in their respective order
live_rune_1 = live_runes["generalRunes"][1]["displayName"]
live_rune_2 = live_runes["generalRunes"][2]["displayName"]
live_rune_3 = live_runes["generalRunes"][3]["displayName"]

live_rune_4 = live_runes["generalRunes"][4]["displayName"]
live_rune_5 = live_runes["generalRunes"][5]["displayName"]

live_shard_1 = live_runes["statRunes"][0]["rawDescription"]
live_shard_2 = live_runes["statRunes"][1]["rawDescription"] 
live_shard_3 = live_runes["statRunes"][2]["rawDescription"]  #Cycle through 0-2 for the statMods

remove = str.maketrans(":'", 2*" ") 
new_live_keystone = live_keystone.translate(remove)
new_live_rune_2 = live_rune_2.translate(remove)
new_live_shard_2 = live_shard_2.translate(remove)

print(new_live_rune_2)

#----------------- create a picture --------------------

#-------------BACKROUND-------------------------------
filename1 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\bg.png"
bg = Image.open(filename1, 'r')

#-------------KEYSTONE--------------------------------
filename2 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Keystones2\\{new_live_keystone}.png"
new_live_keystone = Image.open(filename2, "r")

#-------------RUNES (1)-------------------------------
filename3 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\{live_rune_1}.png"
live_rune_1 = Image.open(filename3, "r")

filename4 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\{new_live_rune_2}.png"
new_live_rune_2 = Image.open(filename4, "r")

filename5 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\{live_rune_3}.png"
live_rune_3 = Image.open(filename5, "r")

#-------------RUNES (2)-------------------------------
filename6 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\{live_rune_4}.png"
live_rune_4 = Image.open(filename6, "r")

filename7 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\{live_rune_5}.png"
live_rune_5 = Image.open(filename7, "r")

#-------------SHARDS----------------------------------
filename8 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Rune Shards\\{live_shard_1}.png"
live_shard_1 = Image.open(filename8, "r")

filename9 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Rune Shards\\{new_live_shard_2}.png"
new_live_shard_2 = Image.open(filename9, "r")

filename10 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Rune Shards\\{live_shard_3}.png"
live_shard_3 = Image.open(filename10, "r")

#------------------- Ranked Emblem ---------------

filename11 = f"C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\RankedEmblems2\\{tier}.png"
ranked_emblem = Image.open(filename11, "r")


#-------------PASTING OF PICTURES/COLLAGE-------------
text_img = Image.new('RGBA', (1177,62), (0, 0, 0, 0))
text_img.paste(bg, (0,0))

text_img.paste(new_live_keystone, (500, -5), mask=new_live_keystone )

text_img.paste(live_rune_1, (600, 7), mask=live_rune_1 )
text_img.paste(new_live_rune_2, (665, 7), mask=new_live_rune_2 )
text_img.paste(live_rune_3, (730, 7), mask=live_rune_3 )

text_img.paste(live_rune_4, (840, 7), mask=live_rune_4 )
text_img.paste(live_rune_5, (895, 7), mask=live_rune_5 )

text_img.paste(live_shard_1, (990, 15), mask=live_shard_1 )
text_img.paste(new_live_shard_2, (1030, 15), mask=new_live_shard_2 )
text_img.paste(live_shard_3, (1070, 15), mask=live_shard_3 )


text_img.paste(ranked_emblem, (50,-30), mask=ranked_emblem)




text_img.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\output.png", format="png")

#-------------------------------------------------------

image = Image.open("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\output.png")

draw = ImageDraw.Draw(image)

draw.text((220-1,10-3), f"{tier} {rank}", font=fnt, fill=(0,0,0))
draw.text((220,10), f"{tier} {rank}", font=fnt, fill=(255,220,0))



draw.text((225-1,30-3), f"{wins}W - {losses}L", font=fnt, fill=(0,0,0))
draw.text((225,30), f"{wins}W - {losses}L", font=fnt, fill=(255,220,0))

draw.text((380-1,25-3), f"WR:", font=fnt, fill=(0,0,0))
draw.text((380,25), f"WR:", font=fnt, fill=(255,220,0))

if wr > 50:
    draw.text((425-1,22-3), f"{wr}%", font=fnt, fill=(0,0,0))
    draw.text((425,22), f"{wr}%", font=fnt, fill=(10,199,48))
elif wr < 50:
    draw.text((425-1,22-3), f"{wr}%", font=fnt, fill=(0,0,0))
    draw.text((425,22), f"{wr}%", font=fnt, fill=(199,44,20))
elif wr == 50:
    draw.text((425-1,22-3), f"{wr}%", font=fnt, fill=(0,0,0))
    draw.text((425,22), f"{wr}%", font=fnt, fill=(255,255,255))




image.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\output.png")


#-------- take that picture and project it onto the transparent and headless window


t_img = PhotoImage(file="C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\output.png")

myimage = Label(image=t_img)
myimage.pack()

start = time()

root.after(7000, root.destroy)

root.mainloop()

 
