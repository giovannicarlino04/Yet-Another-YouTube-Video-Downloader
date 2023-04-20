import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def download():
    link = entry1.get()
    yt = YouTube(link)
    yt.streams.get_highest_resolution().download()
    print("downloaded", link)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="YT Video Downloader")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Video Link")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master = frame, text="Download", command=download)
button.pack(pady=12, padx=10)

root.mainloop()