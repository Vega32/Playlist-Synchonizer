import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
import os.path
import extraction as ex
import pickle
import threading
import time


def set_directory():
    return filedialog.askdirectory() + '/'


def set_playlist(master, data):
    master.selectedPlayListName = data.get("name")
    master.selectedPlayListURL = data.get("url")
    master.selectedPlayListType = data.get("type")
    master.selectedPlayListDirectory = data.get("directory")

    master.SelectedPlaylistLabel.configure(text=data.get("name"))


def showLoading():
    loading = tk.Toplevel()
    loading.grab_set()
    loading.mainloop()
    while threading.active_count() > 1:
        time.sleep(0.5)
    loading.destroy()


class Root:
    def __init__(self, top):

        top.geometry("600x450")
        top.minsize(600, 475)
        top.maxsize(600, 475)
        # top.resizable(1, 1)
        top.title("MP4/MP3 Downloader")
        top.configure(background="#000000")
        top.configure(cursor="arrow")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")
        # top.resizable(False, False)

        self.top = top
        self.top.update_idletasks()

        self.menubar = tk.Menu(top, font="TkMenuFont", bg="#000000", fg="#00ff00")
        top.configure(menu=self.menubar)

        self.Title = tk.Label(self.top)
        self.Title.place(relx=0.0, rely=0.0, height=90, width=600)
        self.Title.configure(activebackground="#d9d9d9")
        self.Title.configure(activeforeground="black")
        self.Title.configure(background="#000000")
        self.Title.configure(borderwidth="0")
        self.Title.configure(compound='center')
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(font="-family {Lucida Console} -size 48")
        self.Title.configure(foreground="#00ff00")
        self.Title.configure(highlightbackground="#d9d9d9")
        self.Title.configure(highlightcolor="#000000")
        self.Title.configure(padx="10")
        self.Title.configure(pady="10")
        self.Title.configure(text='''DOWNLOADER''')

        self.BasicDownloader = tk.Frame(self.top)
        self.BasicDownloader.place(relx=0.0, rely=0.2, relheight=0.8
                                   , relwidth=1.0)
        self.BasicDownloader.configure(relief="groove")
        self.BasicDownloader.configure(background="#000000")
        self.BasicDownloader.configure(highlightbackground="#d9d9d9")
        self.BasicDownloader.configure(highlightcolor="#000000")

        self.URL_Label = tk.Label(self.BasicDownloader)
        self.URL_Label.place(relx=0.05, rely=0.106, height=35, width=124)
        self.URL_Label.configure(activebackground="#d9d9d9")
        self.URL_Label.configure(activeforeground="black")
        self.URL_Label.configure(background="#000000")
        self.URL_Label.configure(compound='center')
        self.URL_Label.configure(disabledforeground="#a3a3a3")
        self.URL_Label.configure(font="-family {Lucida Console} -size 20")
        self.URL_Label.configure(foreground="#00ff00")
        self.URL_Label.configure(highlightbackground="#d9d9d9")
        self.URL_Label.configure(highlightcolor="#000000")
        self.URL_Label.configure(text='''URL''')

        self.urlEntry = tk.Entry(self.BasicDownloader)
        self.urlEntry.place(relx=0.3, rely=0.106, height=36, relwidth=0.6)
        self.urlEntry.configure(background="#000000")
        self.urlEntry.configure(borderwidth="0")
        self.urlEntry.configure(disabledforeground="#a3a3a3")
        self.urlEntry.configure(font="-family {Lucida Console} -size 12")
        self.urlEntry.configure(foreground="#00ff00")
        self.urlEntry.configure(highlightbackground="#ffffff")
        self.urlEntry.configure(highlightcolor="#ffffff")
        self.urlEntry.configure(highlightthickness="2")
        self.urlEntry.configure(insertbackground="#000000")
        self.urlEntry.configure(selectbackground="#d9d9d9")
        self.urlEntry.configure(selectforeground="black")
        self.urlEntry.configure(insertbackground="#00ff00")

        self.AudioFrame = tk.Frame(self.BasicDownloader)
        self.AudioFrame.place(relx=0.55, rely=0.35, relheight=0.2, relwidth=0.3)
        self.AudioFrame.configure(relief="groove")
        self.AudioFrame.configure(background="#ffffff")
        self.AudioFrame.configure(highlightbackground="#000000")
        self.AudioFrame.configure(highlightcolor="#000000")

        self.AudioButton = tk.Button(self.AudioFrame)
        self.AudioButton.place(x=2, y=2, height=71, width=176)
        self.AudioButton.configure(activebackground="#00ff00")
        self.AudioButton.configure(activeforeground="#000000")
        self.AudioButton.configure(background="#000000")
        self.AudioButton.configure(borderwidth="0")
        self.AudioButton.configure(disabledforeground="#a3a3a3")
        self.AudioButton.configure(font="-family {Lucida Console} -size 30")
        self.AudioButton.configure(foreground="#00ff00")
        self.AudioButton.configure(highlightbackground="#ffffff")
        self.AudioButton.configure(highlightcolor="#000000")
        self.AudioButton.configure(highlightthickness="0")
        self.AudioButton.configure(overrelief="solid")
        self.AudioButton.configure(relief="solid")
        self.AudioButton.configure(text='''AUDIO''')
        self.AudioButton.configure(command=self.downloadAudio)

        self.VideoFrame = tk.Frame(self.BasicDownloader)
        self.VideoFrame.place(relx=0.15, rely=0.35, relheight=0.2, relwidth=0.3)
        self.VideoFrame.configure(relief="groove")
        self.VideoFrame.configure(background="#ffffff")
        self.VideoFrame.configure(highlightbackground="#000000")
        self.VideoFrame.configure(highlightcolor="#000000")

        self.VideoButton = tk.Button(self.VideoFrame)
        self.VideoButton.place(x=2, y=2, height=71, width=176)
        self.VideoButton.configure(activebackground="#00ff00")
        self.VideoButton.configure(activeforeground="#000000")
        self.VideoButton.configure(background="#000000")
        self.VideoButton.configure(borderwidth="0")
        self.VideoButton.configure(disabledforeground="#a3a3a3")
        self.VideoButton.configure(font="-family {Lucida Console} -size 30")
        self.VideoButton.configure(foreground="#00ff00")
        self.VideoButton.configure(highlightbackground="#ffffff")
        self.VideoButton.configure(highlightcolor="#000000")
        self.VideoButton.configure(highlightthickness="0")
        self.VideoButton.configure(overrelief="solid")
        self.VideoButton.configure(relief="solid")
        self.VideoButton.configure(text='''VIDEO''')
        self.VideoButton.configure(command=self.downloadVideo)

        self.PlaylistButtonFrame = tk.Frame(self.BasicDownloader)
        self.PlaylistButtonFrame.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.6)
        self.PlaylistButtonFrame.configure(relief="groove")
        self.PlaylistButtonFrame.configure(background="#ffffff")
        self.PlaylistButtonFrame.configure(highlightbackground="#d9d9d9")
        self.PlaylistButtonFrame.configure(highlightcolor="#000000")

        self.PlaylistPageButton = tk.Button(self.PlaylistButtonFrame)
        self.PlaylistPageButton.place(x=2, y=2, height=71, width=356)
        self.PlaylistPageButton.configure(activebackground="#00ff00")
        self.PlaylistPageButton.configure(activeforeground="black")
        self.PlaylistPageButton.configure(background="#000000")
        self.PlaylistPageButton.configure(borderwidth="0")
        self.PlaylistPageButton.configure(disabledforeground="#a3a3a3")
        self.PlaylistPageButton.configure(font="-family {Lucida Console} -size 24")
        self.PlaylistPageButton.configure(foreground="#00ff00")
        self.PlaylistPageButton.configure(highlightbackground="#d9d9d9")
        self.PlaylistPageButton.configure(highlightcolor="#000000")
        self.PlaylistPageButton.configure(highlightthickness="0")
        self.PlaylistPageButton.configure(text='''Manage Playlist''')
        self.PlaylistPageButton.configure(command=self.showPlaylistDownload)

        self.selectedPlayListName = ""
        self.selectedPlayListURL = ""
        self.selectedPlayListType = 0
        self.selectedPlayListDirectory = ""

        self.PlaylistDownload = tk.Frame(self.top)
        self.PlaylistDownload.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)
        self.PlaylistDownload.configure(relief="groove")
        self.PlaylistDownload.configure(background="#000000")
        self.PlaylistDownload.configure(highlightbackground="#d9d9d9")
        self.PlaylistDownload.configure(highlightcolor="#000000")
        self.PlaylistDownload.lower(self.BasicDownloader)

        self.BackButtonFrame = tk.Frame(self.PlaylistDownload)
        self.BackButtonFrame.place(relx=0.05, rely=0.8, relheight=0.1
                                   , relwidth=0.2)
        self.BackButtonFrame.configure(relief="groove")
        self.BackButtonFrame.configure(background="#ffffff")
        self.BackButtonFrame.configure(highlightbackground="#d9d9d9")
        self.BackButtonFrame.configure(highlightcolor="#000000")

        self.BackButton = tk.Button(self.BackButtonFrame)
        self.BackButton.place(relx=0.008, rely=0.028, height=34, width=118)
        self.BackButton.configure(activebackground="#00ff00")
        self.BackButton.configure(activeforeground="black")
        self.BackButton.configure(background="#000000")
        self.BackButton.configure(borderwidth="0")
        self.BackButton.configure(disabledforeground="#a3a3a3")
        self.BackButton.configure(font="-family {Lucida Console} -size 24")
        self.BackButton.configure(foreground="#00ff00")
        self.BackButton.configure(highlightbackground="#d9d9d9")
        self.BackButton.configure(highlightcolor="#000000")
        self.BackButton.configure(highlightthickness="0")
        self.BackButton.configure(text='''Back''')
        self.BackButton.configure(command=self.hidePlaylistDownload)

        self.Playlist_Label = tk.Label(self.PlaylistDownload)
        self.Playlist_Label.place(relx=0.05, rely=0.1, height=36, width=300)
        self.Playlist_Label.configure(activebackground="#d9d9d9")
        self.Playlist_Label.configure(activeforeground="black")
        self.Playlist_Label.configure(background="#000000")
        self.Playlist_Label.configure(compound='center')
        self.Playlist_Label.configure(disabledforeground="#a3a3a3")
        self.Playlist_Label.configure(font="-family {Lucida Console} -size 20")
        self.Playlist_Label.configure(foreground="#00ff00")
        self.Playlist_Label.configure(highlightbackground="#d9d9d9")
        self.Playlist_Label.configure(highlightcolor="#000000")
        self.Playlist_Label.configure(text='''Selected Playlist :''')

        self.SelectedPlaylistLabel = tk.Label(self.PlaylistDownload)
        self.SelectedPlaylistLabel.place(relx=0.6, rely=0.1, height=36
                                         , width=180)
        self.SelectedPlaylistLabel.configure(activebackground="#d9d9d9")
        self.SelectedPlaylistLabel.configure(activeforeground="black")
        self.SelectedPlaylistLabel.configure(background="#000000")
        self.SelectedPlaylistLabel.configure(compound='left')
        self.SelectedPlaylistLabel.configure(disabledforeground="#a3a3a3")
        self.SelectedPlaylistLabel.configure(font="-family {Lucida Console} -size 16")
        self.SelectedPlaylistLabel.configure(foreground="#00ff00")
        self.SelectedPlaylistLabel.configure(highlightbackground="#d9d9d9")
        self.SelectedPlaylistLabel.configure(highlightcolor="#ffffff")
        self.SelectedPlaylistLabel.configure(highlightthickness="2")

        self.SelectFrame = tk.Frame(self.PlaylistDownload)
        self.SelectFrame.place(relx=0.05, rely=0.3, relheight=0.15, relwidth=0.4)

        self.SelectFrame.configure(relief="groove")
        self.SelectFrame.configure(background="#ffffff")
        self.SelectFrame.configure(highlightbackground="#000000")
        self.SelectFrame.configure(highlightcolor="#000000")

        self.SelectButton = tk.Button(self.SelectFrame)
        self.SelectButton.place(x=2, y=2, height=52, width=236)
        self.SelectButton.configure(activebackground="#00ff00")
        self.SelectButton.configure(activeforeground="#000000")
        self.SelectButton.configure(background="#000000")
        self.SelectButton.configure(borderwidth="0")
        self.SelectButton.configure(disabledforeground="#a3a3a3")
        self.SelectButton.configure(font="-family {Lucida Console} -size 18")
        self.SelectButton.configure(foreground="#00ff00")
        self.SelectButton.configure(highlightbackground="#ffffff")
        self.SelectButton.configure(highlightcolor="#000000")
        self.SelectButton.configure(highlightthickness="0")
        self.SelectButton.configure(overrelief="solid")
        self.SelectButton.configure(relief="solid")
        self.SelectButton.configure(text='''Select Playlist''')
        self.SelectButton.configure(command=self.selectPlaylist)

        self.CreateFrame = tk.Frame(self.PlaylistDownload)
        self.CreateFrame.place(relx=0.55, rely=0.3, relheight=0.15, relwidth=0.4)

        self.CreateFrame.configure(relief="groove")
        self.CreateFrame.configure(background="#ffffff")
        self.CreateFrame.configure(highlightbackground="#000000")
        self.CreateFrame.configure(highlightcolor="#000000")

        self.CreateButton = tk.Button(self.CreateFrame)
        self.CreateButton.place(x=2, y=2, height=52, width=236)
        self.CreateButton.configure(activebackground="#00ff00")
        self.CreateButton.configure(activeforeground="#000000")
        self.CreateButton.configure(background="#000000")
        self.CreateButton.configure(borderwidth="0")
        self.CreateButton.configure(disabledforeground="#a3a3a3")
        self.CreateButton.configure(font="-family {Lucida Console} -size 18")
        self.CreateButton.configure(foreground="#00ff00")
        self.CreateButton.configure(highlightbackground="#ffffff")
        self.CreateButton.configure(highlightcolor="#000000")
        self.CreateButton.configure(highlightthickness="0")
        self.CreateButton.configure(overrelief="solid")
        self.CreateButton.configure(relief="solid")
        self.CreateButton.configure(text='''Create Playlist''')
        self.CreateButton.configure(command=self.showPlaylistForm)

        self.UpdatePlaylistButtonFrame = tk.Frame(self.PlaylistDownload)
        self.UpdatePlaylistButtonFrame.place(relx=0.3, rely=0.55, relheight=0.2, relwidth=0.4)
        self.UpdatePlaylistButtonFrame.configure(relief='groove')
        self.UpdatePlaylistButtonFrame.configure(borderwidth="2")
        self.UpdatePlaylistButtonFrame.configure(relief="groove")
        self.UpdatePlaylistButtonFrame.configure(background="#d9d9d9")
        self.UpdatePlaylistButtonFrame.configure(highlightbackground="#d9d9d9")
        self.UpdatePlaylistButtonFrame.configure(highlightcolor="#000000")

        self.UpdatePlaylistButton = tk.Button(self.UpdatePlaylistButtonFrame)
        self.UpdatePlaylistButton.place(x=2, y=2, height=68, width=233)
        self.UpdatePlaylistButton.configure(activebackground="#00ff00")
        self.UpdatePlaylistButton.configure(activeforeground="#000000")
        self.UpdatePlaylistButton.configure(background="#000000")
        self.UpdatePlaylistButton.configure(borderwidth="0")
        self.UpdatePlaylistButton.configure(disabledforeground="#a3a3a3")
        self.UpdatePlaylistButton.configure(font="-family {Lucida Console} -size 16")
        self.UpdatePlaylistButton.configure(foreground="#00ff00")
        self.UpdatePlaylistButton.configure(highlightbackground="#d9d9d9")
        self.UpdatePlaylistButton.configure(highlightcolor="#000000")
        self.UpdatePlaylistButton.configure(text='''Update Playlist''')
        self.UpdatePlaylistButton.configure(command=self.updatePlaylist)

        self.processing = tk.IntVar(value=threading.active_count())
        self.top.after(100, self.updateThreadCount)
        self.processing.trace('w', lambda *args: self.createLoading())

        self.loadingStyle = ttk.Style()
        self.loadingStyle.theme_use("clam")
        self.loadingStyle.configure("matrix.Horizontal.TProgressbar", forground="#00ff00", background="#00ff00",
                                    activebackground="#000000", highlightbackground="#ffffff", highlightcolor="#ffffff",
                                    highlightthickness="2")
        self.loading = ttk.Progressbar(self.top, style="matrix.Horizontal.TProgressbar", orient="horizontal",
                                       length=200, mode='indeterminate')

    def updateThreadCount(self):
        self.processing.set(threading.active_count())
        self.top.after(1000, self.updateThreadCount)

    def createLoading(self):
        if self.processing.get() == 2:

            self.loading.pack(padx=100, pady=80, ipadx=200, ipady=10)
            self.loading.grab_set()
            self.loading.start(20)
        else:
            self.loading.grab_release()
            self.loading.pack_forget()

    def showPlaylistDownload(self):
        self.PlaylistDownload.lift(self.BasicDownloader)
        self.top.update_idletasks()

    def hidePlaylistDownload(self):
        self.PlaylistDownload.lower(self.BasicDownloader)

    def showPlaylistForm(self):
        self.form = tk.Toplevel()
        self.form.grab_set()
        CreatePlaylistForm(self.form, self)

    def downloadVideo(self):
        if self.urlEntry.get() != "":
            directory = set_directory()
            if directory != "" and directory != "/":
                self.loading.lift(self.BasicDownloader)
                threading.Thread(target=ex.download_video, args=(self.urlEntry.get(), directory)).start()
            else:
                msgbox.showinfo("Error", "Couldn't get directory")
        else:
            msgbox.showinfo("Error", "Empty url field")

    def downloadAudio(self):
        if self.urlEntry.get() != "":
            directory = set_directory()
            if directory != "/" and directory != "":
                self.loading.lift(self.BasicDownloader)
                threading.Thread(target=ex.download_audio, args=(self.urlEntry.get(), directory)).start()
            else:
                msgbox.showinfo("Error", "Couldn't get directory")
        else:
            msgbox.showinfo("Error", "Empty url field")

    def selectPlaylist(self):
        directory = set_directory()
        if ".config.playlist" not in os.listdir(directory):
            msgbox.showinfo("Error", "Invalid playlist. Missing config file")
            return
        else:
            with open(directory + '.config.playlist', 'rb') as f:
                data = pickle.load(f)
                set_playlist(self, data)

    def updatePlaylist(self):
        self.loading.lift(self.PlaylistDownload)
        threading.Thread(target=self.updateThread).start()

    def updateThread(self):
        playlistUpdate = ex.getDataPlaylist(self.selectedPlayListURL)
        currentPlaylist = os.listdir(self.selectedPlayListDirectory)
        for updated in playlistUpdate:
            found = False
            for current in currentPlaylist:
                if current[:-4] == updated[0]:
                    found = True
            if not found:
                if self.selectedPlayListType == 0:
                    ex.download_video(updated[1], self.selectedPlayListDirectory)
                else:
                    ex.download_audio(updated[1], self.selectedPlayListDirectory)

        currentPlaylist = os.listdir(self.selectedPlayListDirectory)
        for current in currentPlaylist:
            found = False
            if current == ".config.playlist" or current[:-4] != ".mp3" and current[:-4] != ".mp4":
                continue
            else:
                for updated in playlistUpdate:
                    if current[:-4] == updated[0]:
                        found = True
            if not found:
                os.remove(self.selectedPlayListDirectory + current)
        print(currentPlaylist)


class CreatePlaylistForm:
    def __init__(self, top, master):

        self.master = master

        top.geometry("400x450")
        # top.minsize(120, 1)
        # top.maxsize(3844, 1061)
        # top.resizable(1, 1)
        top.title("Create Playlist")
        top.configure(background="#000000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")
        top.resizable(False, False)

        self.top = top

        self.urlLabel = tk.Label(self.top)
        self.urlLabel.place(relx=0.05, rely=0.251, height=45, width=80)
        self.urlLabel.configure(activebackground="#d9d9d9")
        self.urlLabel.configure(activeforeground="black")
        self.urlLabel.configure(anchor='w')
        self.urlLabel.configure(background="#000000")
        self.urlLabel.configure(compound='left')
        self.urlLabel.configure(disabledforeground="#a3a3a3")
        self.urlLabel.configure(font="-family {Lucida Console} -size 20")
        self.urlLabel.configure(foreground="#00ff00")
        self.urlLabel.configure(highlightbackground="#d9d9d9")
        self.urlLabel.configure(highlightcolor="#000000")
        self.urlLabel.configure(text='''URL''')

        self.locationLabel = tk.Label(self.top)
        self.locationLabel.place(relx=0.05, rely=0.651, height=45, width=140)
        self.locationLabel.configure(activebackground="#d9d9d9")
        self.locationLabel.configure(activeforeground="black")
        self.locationLabel.configure(anchor='w')
        self.locationLabel.configure(background="#000000")
        self.locationLabel.configure(compound='left')
        self.locationLabel.configure(disabledforeground="#a3a3a3")
        self.locationLabel.configure(font="-family {Lucida Console} -size 20")
        self.locationLabel.configure(foreground="#00ff00")
        self.locationLabel.configure(highlightbackground="#d9d9d9")
        self.locationLabel.configure(highlightcolor="#000000")
        self.locationLabel.configure(text='''Location''')

        self.nameLabel = tk.Label(self.top)
        self.nameLabel.place(relx=0.05, rely=0.051, height=45, width=80)
        self.nameLabel.configure(activebackground="#d9d9d9")
        self.nameLabel.configure(activeforeground="black")
        self.nameLabel.configure(anchor='w')
        self.nameLabel.configure(background="#000000")
        self.nameLabel.configure(compound='left')
        self.nameLabel.configure(disabledforeground="#a3a3a3")
        self.nameLabel.configure(font="-family {Lucida Console} -size 20")
        self.nameLabel.configure(foreground="#00ff00")
        self.nameLabel.configure(highlightbackground="#d9d9d9")
        self.nameLabel.configure(highlightcolor="#000000")
        self.nameLabel.configure(text='''Name''')

        self.NameEntry = tk.Entry(self.top)
        self.NameEntry.place(relx=0.3, rely=0.051, height=45, relwidth=0.6)
        self.NameEntry.configure(background="#000000")
        self.NameEntry.configure(borderwidth="2")
        self.NameEntry.configure(disabledforeground="#a3a3a3")
        self.NameEntry.configure(font="TkFixedFont")
        self.NameEntry.configure(foreground="#00ff00")
        self.NameEntry.configure(highlightbackground="#d9d9d9")
        self.NameEntry.configure(highlightcolor="#ffffff")
        self.NameEntry.configure(highlightthickness="2")
        self.NameEntry.configure(insertbackground="#000000")
        self.NameEntry.configure(relief="solid")
        self.NameEntry.configure(selectbackground="#d9d9d9")
        self.NameEntry.configure(selectforeground="black")
        self.NameEntry.configure(insertbackground="#00ff00")
        self.NameEntry.configure(font="-family {Lucida Console} -size 12")

        self.typeLabel = tk.Label(self.top)
        self.typeLabel.place(relx=0.05, rely=0.451, height=45, width=80)
        self.typeLabel.configure(activebackground="#d9d9d9")
        self.typeLabel.configure(activeforeground="black")
        self.typeLabel.configure(anchor='w')
        self.typeLabel.configure(background="#000000")
        self.typeLabel.configure(compound='left')
        self.typeLabel.configure(disabledforeground="#a3a3a3")
        self.typeLabel.configure(font="-family {Lucida Console} -size 20")
        self.typeLabel.configure(foreground="#00ff00")
        self.typeLabel.configure(highlightbackground="#d9d9d9")
        self.typeLabel.configure(highlightcolor="#000000")
        self.typeLabel.configure(text='''Type''')

        self.type = tk.IntVar(top, 0)

        self.VideoRadioButton = tk.Radiobutton(top)
        self.VideoRadioButton.place(relx=0.3, rely=0.451, height=45, width=100)
        self.VideoRadioButton.configure(text="Video")
        self.VideoRadioButton.configure(variable=self.type)
        self.VideoRadioButton.configure(value=0)
        self.VideoRadioButton.configure(indicatoron=True)
        self.VideoRadioButton.configure(background="#000000")
        self.VideoRadioButton.configure(foreground="#00ff00")
        self.VideoRadioButton.configure(font="-family {Lucida Console} -size 16")
        self.VideoRadioButton.configure(activebackground="#000000")
        self.VideoRadioButton.configure(activeforeground="#00ff00")
        self.VideoRadioButton.configure(selectcolor="#000000")

        self.AudioRadioButton = tk.Radiobutton(top)
        self.AudioRadioButton.place(relx=0.6, rely=0.451, height=45, width=100)
        self.AudioRadioButton.configure(text="Audio")
        self.AudioRadioButton.configure(variable=self.type)
        self.AudioRadioButton.configure(value=1)
        self.AudioRadioButton.configure(indicatoron=True)
        self.AudioRadioButton.configure(background="#000000")
        self.AudioRadioButton.configure(foreground="#00ff00")
        self.AudioRadioButton.configure(font="-family {Lucida Console} -size 16")
        self.AudioRadioButton.configure(activebackground="#000000")
        self.AudioRadioButton.configure(activeforeground="#00ff00")
        self.AudioRadioButton.configure(selectcolor="#000000")

        self.PlaylistUrlEntry = tk.Entry(self.top)
        self.PlaylistUrlEntry.place(relx=0.3, rely=0.251, height=45, relwidth=0.6)
        self.PlaylistUrlEntry.configure(background="#000000")
        self.PlaylistUrlEntry.configure(borderwidth="2")
        self.PlaylistUrlEntry.configure(disabledforeground="#a3a3a3")
        self.PlaylistUrlEntry.configure(font="-family {Lucida Console} -size 12")
        self.PlaylistUrlEntry.configure(foreground="#00ff00")
        self.PlaylistUrlEntry.configure(highlightbackground="#d9d9d9")
        self.PlaylistUrlEntry.configure(highlightcolor="#ffffff")
        self.PlaylistUrlEntry.configure(highlightthickness="2")
        self.PlaylistUrlEntry.configure(insertbackground="#000000")
        self.PlaylistUrlEntry.configure(relief="solid")
        self.PlaylistUrlEntry.configure(selectbackground="#d9d9d9")
        self.PlaylistUrlEntry.configure(selectforeground="black")
        self.PlaylistUrlEntry.configure(insertbackground="#00ff00")

        self.CreateButtonFrame = tk.Frame(self.top)
        self.CreateButtonFrame.place(relx=0.275, rely=0.82, relheight=0.12, relwidth=0.45)
        self.CreateButtonFrame.configure(relief="groove")
        self.CreateButtonFrame.configure(background="#ffffff")
        self.CreateButtonFrame.configure(highlightbackground="#d9d9d9")
        self.CreateButtonFrame.configure(highlightcolor="#000000")

        self.CreateButton = tk.Button(self.CreateButtonFrame)
        self.CreateButton.place(relx=0.011, rely=0.037, height=50, width=176)
        self.CreateButton.configure(activebackground="#00ff00")
        self.CreateButton.configure(activeforeground="black")
        self.CreateButton.configure(background="#000000")
        self.CreateButton.configure(borderwidth="0")
        self.CreateButton.configure(disabledforeground="#a3a3a3")
        self.CreateButton.configure(font="-family {Lucida Console} -size 24")
        self.CreateButton.configure(foreground="#00ff00")
        self.CreateButton.configure(highlightbackground="#d9d9d9")
        self.CreateButton.configure(highlightcolor="#000000")
        self.CreateButton.configure(highlightthickness="0")
        self.CreateButton.configure(text='''Create''')
        self.CreateButton.configure(command=self.submit)

        self.directory = ""

        self.SelectButtonFrame = tk.Frame(self.top)
        self.SelectButtonFrame.place(relx=0.45, rely=0.651, relheight=0.1, relwidth=0.4)
        self.SelectButtonFrame.configure(relief="groove")
        self.SelectButtonFrame.configure(background="#ffffff")
        self.SelectButtonFrame.configure(highlightbackground="#d9d9d9")
        self.SelectButtonFrame.configure(highlightcolor="#000000")

        self.SelectButton = tk.Button(self.SelectButtonFrame)
        self.SelectButton.place(relx=0.013, rely=0.044, height=41, width=156)
        self.SelectButton.configure(activebackground="#00ff00")
        self.SelectButton.configure(activeforeground="black")
        self.SelectButton.configure(background="#000000")
        self.SelectButton.configure(borderwidth="0")
        self.SelectButton.configure(disabledforeground="#a3a3a3")
        self.SelectButton.configure(font="-family {Lucida Console} -size 20")
        self.SelectButton.configure(foreground="#00ff00")
        self.SelectButton.configure(highlightbackground="#d9d9d9")
        self.SelectButton.configure(highlightcolor="#000000")
        self.SelectButton.configure(highlightthickness="0")
        self.SelectButton.configure(relief="solid")
        self.SelectButton.configure(text='''Select''')
        self.SelectButton.configure(command=self.selectDirectory)

    def selectDirectory(self):
        self.directory = set_directory()
        if bool(os.listdir(self.directory)):
            msgbox.showinfo("Error", "Playlist folder must be empty")
            self.directory = ""

    def submit(self):
        name = self.NameEntry.get()
        url = self.PlaylistUrlEntry.get()
        playlistType = self.type.get()

        if name == "":
            msgbox.showinfo("Error", "\"Name\" field is empty")
        elif url == "":
            msgbox.showinfo("Error", "\"URL\" field is empty")
        elif playlistType is None:
            msgbox.showinfo("Error", "No playlist type set")
        elif self.directory == "" or self.directory == "/":
            msgbox.showinfo("Error", "No directory set")
        else:
            data = {'name': name, 'url': url, 'type': playlistType, 'directory': self.directory}
            with open(self.directory + '.config.playlist', 'wb') as f:
                pickle.dump(data, f)
            set_playlist(self.master, data)
            self.top.destroy()


def start_up():
    base = tk.Tk()
    base.configure(height=450, width=600)
    base.maxsize(600, 450)
    # base.resizable(False, False)
    root = Root(base)
    base.mainloop()


if __name__ == '__main__':
    start_up()
