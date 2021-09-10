import os
import cv2
import tkinter as tk
from tkinter import filedialog as fd
from cut_video import cut_frame


#windows for dialog file
def save_file(imageList):
    wybrany_folder = fd.askdirectory()
    if wybrany_folder:
        number_frame = 0
        for image in imageList:
            cv2.imwrite(os.path.join(wybrany_folder, "frame-namei%d.jpg" %  number_frame), image)
            number_frame += 1

#check enter to str
def printmessage(check_entry_numer, check_entry_path):
    if check_entry_numer == True and check_entry_path == True:
        done_label.setvar("Your frames was saved in desktop")
    if check_entry_numer == False:
        done_label.setvar("please enter the number again")
    if check_entry_path == False:
        done_label.setvar("please enter the path file again")
    else:
        done_label.setvar("please enter the values again")


#check enter  to number
def check_entry_numer(input_entry):
    if input_entry:
        try:
            return int(input_entry) >= 2
        except ValueError:
            return False
    else:
        return False

#check enter to str
def check_entry_path(input_entry):
    if input_entry:
        try:
            str(input_entry)
            return True
        except:
            return False
    else:
        return False

def start():
    check_number = check_entry_numer(number_frame_entry.get())
    check_path = check_entry_path(path_file_entry.get())
    printmessage(check_number, check_path)
    imageList = cut_frame(number_frame_entry, path_file_entry)
    #save_file(imageList.count(), imageList)

root = tk.Tk()
root.geometry("350x200")
root.title("Cut video")

# declaring string variable
# for storing name and password
count_frame = tk.StringVar()
path_file = tk.StringVar()
massage_text = tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen

def submit():
    c_frame = count_frame.get()
    p_file = path_file.get()

    c_frame.set("")
    p_file.set("")
    massage_text.set("zxdfghjkl")

number_frame_label = tk.Label(root, text='Number of frames', font=('helvetica', 14, 'normal'))

number_frame_entry = tk.Entry(root, textvariable=count_frame, font=('helvetica', 14, 'normal'))

path_file_label = tk.Label(root, text='File path', font=('helvetica', 14, 'normal'))

path_file_entry = tk.Entry(root, textvariable=path_file, font=('helvetica', 14, 'normal'))

start_button = tk.Button(root, text='Start', command=start)

done_label = tk.Label(root, textvariable=massage_text, font=('helvetica', 14, 'normal'))


number_frame_label.grid(row=0, column=0, sticky = 'W', padx=20,pady=5)
number_frame_entry.grid(row=0, column=1)
path_file_label.grid(row=1, column=0, sticky = 'W',  padx=20, pady=5)
path_file_entry.grid(row=1, column=1)
start_button.grid(row=2, column=1)
done_label.grid(row=3, column=1, pady=5)


root.mainloop()
done_label.pack()

