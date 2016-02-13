# Created by Melle Dijkstra
# Just for fun, trying some python
# Description:
#   A simple program that makes a request to an API that sends plain text back as response with ASCII art
#   The response is displayed in the textfield
import requests
from tkinter import *

# the API url for funny fortunes :)
url = "https://thibaultcha-fortunecow-v1.p.mashape.com/random"
# need this header info to get accepted by API
headers = {"X-Mashape-Key": "MlIo1TbdUlmshFVgUWfiIrHtDNS1p1ohqujjsnCN8wtaFisFK7",
           "Accept": "text/plain"}

# init TK
root = Tk()

# A top frame for the button, a bottom frame for the textfield
topFrame = Frame(root, width=200, height=200, padx=10, pady=10)
bottomFrame = Frame(root, width=600, height=500, pady=10)
textfield = Text(bottomFrame)


# This function makes the request to get a fortune to tell then updates the textfield
def displayfortune(element=textfield):
    # make request with headers info
    r = requests.get(url, headers=headers)
    response = r.text

    # remove previous text and set the response in the textfield
    element.delete("0.0", END)
    element.insert("1.0", chars=response)


button = Button(topFrame, fg="white", bg="darkred", text="Click me to get a random fortune", command=displayfortune)

# Add everything to the root window
button.pack()
textfield.pack()
topFrame.pack()
bottomFrame.pack()

root.mainloop()
