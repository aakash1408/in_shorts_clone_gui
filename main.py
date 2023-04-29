import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import io
import webbrowser


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

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
    def display_news_items(self,index):
        self.clear()

        try:
            img_url = self.data["articles"][index]["urlToImage"]
            raw = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = "https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg"
            raw = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image = photo)
        label.pack()

        headline = Label(self.root, text = self.data["articles"][index]["title"], bg = "black", fg = "white", wraplength=350, justify="center")
        headline.pack(pady=(10,5))
        headline.config(font=('verdana',15))

        content = Label(self.root, text = self.data["articles"][index]["description"], bg = "black", fg = "white", wraplength=350, justify="center")
        content.pack(pady=(0,5))
        content.config(font=('verdana',12))
 
        frame = Frame(self.root, bg = "black")
        frame.place(relx=0.5, rely=1.0, anchor="s", width=350)


        if index != 0:
            prev = Button(frame, text = "Prev", width=16,height=3,command=lambda :self.display_news_items(index-1))
            prev.pack(side=LEFT)
        
        read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data["articles"])-1:
            next = Button(frame, text = "Next", width=16,height=3,command=lambda :self.display_news_items(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)  

        
news = Newsapp()