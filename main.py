import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
import pyttsx3
import time

attempts = 0
max_attempts = 5

def check_password():
    global attempts
    login_window = Toplevel()
    login_window.geometry("400x600")
    login_window.resizable(False, False)
    login_window.title("Login")
    login_window.configure(bg="#2c3e50")

    try:
        login_icon = PhotoImage(file="image_icon/lock.png")
    except Exception as e:
        print(f"Error loading login icon: {e}")

    login_window.iconphoto(False, login_icon)

    def verify_password():
        global attempts
        password = password_entry.get()
        if password == "2707":
            login_window.destroy()
            root.deiconify()
        else:
            attempts += 1
            if attempts >= max_attempts:
                login_window.destroy()
                messagebox.showwarning(
                    "Warning",
                    "Exceeded maximum attempts. Please try again in 10 seconds."
                )
                time.sleep(10)
                attempts = 0
                check_password()
            else:
                messagebox.showerror("Error", f"Password is incorrect. You have {max_attempts - attempts} attempts left.")

    def on_enter(event=None):
        verify_password()

    try:
        lock_image = PhotoImage(file="image_icon/lock.png")
    except Exception as e:
        print(f"Error loading lock image: {e}")

    lock_label = Label(login_window, image=lock_image, bg="#2c3e50")
    lock_label.image = lock_image
    lock_label.pack(pady=50)

    Label(login_window, text="Enter Password", font="arial 20 bold", bg="#2c3e50", fg="white").pack(pady=20)
    password_entry = Entry(login_window, font="arial 20", show="*", width=20)
    password_entry.pack(pady=20)
    
    # Bind the Enter key to the on_enter function
    login_window.bind("<Return>", on_enter)

    Button(login_window, text="Login", font="arial 15 bold", command=verify_password, bg="green", fg="white").pack(pady=20)

root = Tk()
root.withdraw()

check_password()

root.title("TEXT TO SPEECH")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="#2c3e50")

engine = pyttsx3.init()

def set_voice_and_speed(gender, speed):
    voices = engine.getProperty('voices')
    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    if speed == 'Fast':
        engine.setProperty('rate', 250)
    elif speed == 'Normal':
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 50)

def speaknow():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    set_voice_and_speed(gender, speed)
    engine.say(text)
    engine.runAndWait()

def download_audio():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    set_voice_and_speed(gender, speed)
    filename = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
    if filename:
        engine.save_to_file(text, filename)
        engine.runAndWait()

try:
    image_icon = PhotoImage(file="image_icon/megaphone_7883139.png")
except Exception as e:
    print(f"Error loading main icon: {e}")

root.iconphoto(False, image_icon)

TOP_frame = Frame(root, bg="white", width=900, height=100)
TOP_frame.place(x=0, y=0)

try:
    Logo = PhotoImage(file="image_icon/businessman_1533231.png")
except Exception as e:
    print(f"Error loading logo: {e}")

Label(TOP_frame, image=Logo, bg="white").place(x=10, y=5)
Label(TOP_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#2c3e50", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#2c3e50", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Slow', 'Normal'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

try:
    imageicon = PhotoImage(file="image_icon/volume_11825714.png")
except Exception as e:
    print(f"Error loading speak button icon: {e}")

btn = Button(root, text="Speak", command=speaknow, image=imageicon, width=130, font="aril 14 bold", compound=LEFT)
btn.place(x=550, y=280)

try:
    imageicon2 = PhotoImage(file="image_icon/arrow_13725770.png")
except Exception as e:
    print(f"Error loading save button icon: {e}")

save = Button(root, text="Save", command=download_audio, image=imageicon2, width=130, font="aril 14 bold", compound=LEFT)
save.place(x=730, y=280)

root.mainloop()
