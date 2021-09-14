import os
import cv2
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from cut_video import cut_frame


# windows for dialog file
def save_files(imageList):
    wybrany_folder = fd.askdirectory()
    if wybrany_folder:
        number_frame = 0
        for image in imageList:
            cv2.imwrite(os.path.join(wybrany_folder, "frame-%d.jpg" % (number_frame + 1)), image)
            number_frame += 1


selected_file = ""


def select_file():
    filetypes = [("Video file", '*.mp4')]
    global selected_file
    selected_file = fd.askopenfilename(
        title="Open a file",
        initialdir='/',
        filetypes=filetypes,
    )
    if (selected_file != ""):
        file_name = selected_file[(selected_file.rfind('/') + 1):]
        select_file_label.config(text=file_name)
    else:
        select_file_label.config(text='File not chosen')


# check enter to str
def printmessage(check_entry_numer, check_entry_path):
    if check_entry_numer == True and check_entry_path == True:
        done_label.config(text="Processing...")
    elif check_entry_numer == False and check_entry_path == True:
        done_label.config(text="Please enter a correct number")
    elif check_entry_numer == True and check_entry_path == False:
        done_label.config(text="Please choose a file")
    else:
        done_label.config(text="Please choose a file and enter a correct number")
    pass


# check enter to number
def check_entry_numer(input_entry):
    try:
        return int(input_entry) >= 2
    except ValueError:
        return False


def start():
    is_number_correct = check_entry_numer(number_frame_entry.get())
    is_video_chosen = selected_file != "" and selected_file != None
    printmessage(is_number_correct, is_video_chosen)
    if (is_number_correct and is_video_chosen):
        imageList = cut_frame(number_frame_entry, selected_file)
        mb.showinfo(title="Message", message="Choose file saving location")
        save_files(imageList)
        done_label.config(text="Done!")


root = tk.Tk()
root.geometry("390x180")
root.title("Cut video")
root.resizable(False, False)

number_frame_label = tk.Label(root, text='Number of frames', font=('helvetica', 14, 'normal'))

number_frame_entry = tk.Entry(root, textvariable=tk.StringVar(), font=('helvetica', 14, 'normal'))

select_file_label = tk.Label(root, text='File not chosen', font=('helvetica', 12, 'normal'))

select_file_button = tk.Button(root, text='Choose file', highlightbackground="blue", highlightthickness=2,
                               command=select_file)

start_button = tk.Button(root, text='Start', highlightbackground="blue", highlightthickness=2, command=start)

done_label = tk.Label(root, text="", font=('helvetica', 14, 'normal'))

number_frame_label.grid(row=0, column=0, sticky='W', padx=20, pady=10)
number_frame_entry.grid(row=0, column=1, padx=10)
select_file_button.grid(row=1, column=0, padx=20, pady=5)
select_file_label.grid(row=1, column=1, sticky='W', padx=10, pady=5)
start_button.grid(row=2, column=1, padx=10, pady=5)
done_label.grid(row=3, column=0, columnspan=2, padx =20, pady =20)

root.mainloop()