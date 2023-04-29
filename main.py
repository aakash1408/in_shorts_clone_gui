import requests
from tkinter import *

class Newsapp:

    def __init__(self):

        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce159becf640549315f01724aa10dd").json()
        #load gui
        self.load_gui()
        #display news items
        self.display_news_items(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.title("inshorts_clone")
        self.root.configure(background="black")
        
    
    def display_news_items(self,index):
        headline = Label(self.root, text = self.data["articles"][index]["title"], bg = "black", fg = "white", wraplength=350, justify="center")
        headline.pack()

        self.root.mainloop()

news = Newsapp()