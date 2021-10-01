#a simple tkinter and python program for youtube downloader by Adarsh G Dnaiel
import tkinter as tk
from pytube import YouTube
from tkinter import filedialog

#the tkinter window 
window = tk.Tk()
window.title('AGD Youtube Downloader')
window.geometry('500x400')
window.iconbitmap('c:/Users/Adarsh G Daniel/Desktop/AGD Youtube Downloader/Icon/logo.ico')
window.configure(bg = '#ff4d4d')


#right click pop up
global m
m = tk.Menu(window, tearoff=0)
m.add_command(label="Cut")
m.add_command(label="Copy")
m.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    m.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    m.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    m.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    m.tk.call("tk_popup", m, e.x_root, e.y_root)

#Final Download button
def downloadvid():
    global E1
    string = E1.get()
    if string != " " and 'youtu.be' in string:
        window.geometry('500x650')
        yt = YouTube(str(string))
        videos = yt.streams.all()
        global folder_path
        s = 1
        w = tk.Label(window, text = "Select your Choice of quality", fg = "white", bg= '#ff4d4d', font = ('Arial', 15))
        w.pack()
        l = tk.Listbox(window, width = 10, bd = 0, bg = '#262626', fg = "white", font = ('Arial', 12))
        for v in videos:
            print(v)
            if '"video/mp4"' in str(v) and 'progressive="False"' in str(v):
                c = str(v).split(' ')
                for i in c:
                    if i.startswith('res'):
                        l.insert(str(s) , i[5:-1])
                        l.pack()
                        s += 1
        
        def browse_button():             #browse for the location
            filename = filedialog.askdirectory()
            folder_path.set(filename)
            print(filename)

        def downloadvid1():             #getting the resolution details
                data = ''
                n = 0
                for i in l.curselection():
                    data = str(l.get(i))
                    print(data)
                for v in videos:
                    if str(data) in str(v) and 'progressive="False"' in str(v) and 'video/mp4' in str(v):
                        print(v)
                        d = n
                        break
                    n += 1
                print(d)
                n = int(d)
                vid = videos[n+1]
                destination = str(folder_path.get())
                vid.download(destination)            
                w = tk.Label(window, text = yt.title+"\n has been downloaded", fg = "white", bg= '#ff4d4d', font = ('Arial', 10))           #final message
                w.pack()
        #other blanks which call the functions
        w = tk.Label(window, text = "Enter your destination", fg = "white", bg= '#ff4d4d', font = ('Arial', 13))
        w.pack()
        folder_path = tk.StringVar()
        lbl1 = tk.Label(master=window,textvariable=folder_path, width = 0, fg = "white", bg= '#ff4d4d',)
        lbl1.pack()
        button2 = tk.Button(text="Browse", command=browse_button, fg = "white", bg= '#262626', bd = 0)
        button2.pack(pady = 5, ipadx = 10, ipady = 5)
        button = tk.Button(window, text = "Download",  fg = "white", bg= '#262626',  bd = 0, command = downloadvid1)
        button.pack(pady = 10, ipadx = 10, ipady = 5)
    else:
        w1 = tk.Label(window, text = "Enter a valid link", fg = "white", bg= '#ff4d4d')
        w1.pack()

    


#Starting main window
w = tk.Label(window, text = "Youtube Downloader", fg = "white", bg= '#ff4d4d', font = ('Arial', 25))
w.pack(pady = 20)

w = tk.Label(window, text = "Enter your link here", fg = "white", bg= '#ff4d4d', font = ('Arial', 16))
w.pack(pady = 10)


E1 = tk.Entry(window, width = 60, fg = "#262626", bd = 0, font = ('Arial', 10))
E1.pack(side = tk.TOP)
E1.bind('<Button-3>',show_menu)


button = tk.Button(window, text = "Done", fg = "white", bg= '#262626', command = downloadvid, bd = 0)
button.pack(pady = 10, ipadx = 10, ipady = 5)

w = tk.Label(window, text = "Created by Adarsh G Daniel", fg = "white", bg= '#ff4d4d', font = ('Arial', 10))
w.pack(side = tk.BOTTOM)



window.mainloop()
