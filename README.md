# League Overlay

---
Modules used: tkinter, os, PIL, win32api, time, urllib.request, ssl, json, riotwatcher
---

A Program that locates the "League of Legends (TM) Client", which is the ongoing game.

After doing so, it fixates a window onto it, by using the location that is being taken through the "win32api" module.

![Image of the window](https://media.discordapp.net/attachments/719464131220078602/780492262965510174/unknown.png)


From left to right, this window contains: 

- The Ranked Emblem, the current player has achieved.
- The Tier and the Rank 
- Beneath the Tier and the Rank are the Wins and Losses
- The Win Ratio, which is being calculated by using the Wins and Losses
- The Runes the current player is using

The Data to generate this picture is being taken from the [RIOT LIVE CLIENT API](https://developer.riotgames.com/docs/lol#game-client-api_live-client-data-api)

Desired information is being saved into variables, which get assigned into specific positions on the canvas. Using tkinter, a transparent window is being created, showing off
only the generated image, while being headless ( no cancel or minimize to tray button )

The program runs on a timer, closing after 7 seconds.

The Pictures that are being used are saved into folder, which the program has access to. The Background itself is a stylized pre-existing template. 

**[Video](https://youtu.be/XzXLDRQI-bQ)** example of the program running

---
Additional programs and Folder that got uploaded to this repository: 

- Folder with all the images needed 

- resize images.py ( Resized all the given icons, that got used to generate the picture, into the same size )
- findWindow.py ( Test run of the program, a windows coordinates, to fixate on it and size itself accordingly )
- createImage.py ( Generates an image, from multiple images, after getting the paths fed into it )
