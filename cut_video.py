import cv2
import tkinter as tk
import os
import time
import pathlib


def start():
    check_number = check_entry_numer(number_frame_entry.get())
    check_path = check_entry_path(path_file_entry.get())
    printmessage(check_number, check_path)
    cut_frame(number_frame_entry, path_file_entry)

def cut_frame(number_frame, name_video_file):
    name_video_file = str(path_file_entry.get())
    cap = cv2.VideoCapture(name_video_file)
    success, image = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)  # number of frames per second
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # number of frames in the movie
    ##number_frame_entry.config(int(str(count_frame)))
    number_frame = int(number_frame_entry.get())  # how many frames do i want to extract from the video
    frames_to_skip = (frame_count - 1) / (number_frame - 1)  # co ile ramek wyciagam kolejna
    count = 0  # the number of the currently processed frame
    frames_taken = 0  # how many frames have already been drawn
    print("Z filmu o długości " + str(frame_count) + " ramek wyciągam " + str(input) + " ramek")

    #createFile()
    while success:
        if (count == round(frames_taken * frames_to_skip)):
            print("Wyciągam " + str(frames_taken + 1) + ". ramkę, w wideo ma numer " + str(count) + " na " + str(
                frame_count - 1))
            milisecond = round(count * 1000 / fps)
            print("Ramka pochodzi z " + str(milisecond) + " milisekundy nagrania")
            frames_taken += 1
            cv2.imwrite("frame%d.jpg" % count, image)
        success, image = cap.read()
        count += 1
    cap.release()
    print("Done!: "+ str(input))
    #done_label.set("Done")


##interface
root = tk.Tk()

# setting the windows size
root.geometry("350x200")

# declaring string variable
# for storing name and password
count_frame = tk.StringVar()
path_file = tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    c_frame = count_frame.get()
    p_file = path_file.get()

    print("How much print the frame: " + c_frame)
    print("Path file : " + p_file)

    c_frame.set("")
    p_file.set("")


# creating a label for number of frame
# name using widget Label
number_frame_label = tk.Label(root, text='Number of frames', font=('helvetica', 14, 'normal'))

# creating a entry for number_frame
# name using widget Entry
number_frame_entry = tk.Entry(root, textvariable=count_frame, font=('helvetica', 14, 'normal'))

# creating a label for path_file_
path_file_label = tk.Label(root, text='File path', font=('helvetica', 14, 'normal'))

# creating a entry for path_file_
path_file_entry = tk.Entry(root, textvariable=path_file, font=('helvetica', 14, 'normal'))

# creating a button using the widget
# Button that will call the start function
start_button = tk.Button(root, text='Start', command=start)

done_label = tk.Label(root, text='', font=('helvetica', 14, 'normal'))


# placing the label and entry in
# the required position using grid
# method
number_frame_label.grid(row=0, column=0, sticky = 'W', padx=20,pady=5)
number_frame_entry.grid(row=0, column=1)
path_file_label.grid(row=1, column=0, sticky = 'W',  padx=20, pady=5)
path_file_entry.grid(row=1, column=1)
start_button.grid(row=2, column=1)
done_label.grid(row=3, column=1, pady=5)
# performing an infinite loop
# for the window to display
root.mainloop()


#create directory on desktop and save all phote, directory called date
def createFile():
    os.mkdir(time.strftime("/%Y/%m/%d"))
    ##pathlib.Path(__file__).parent.resolve()

#check enter to str
def printmessage(check_entry_numer, check_entry_path):
    if check_entry_numer == True and check_entry_path == True:
        done_label.set("Your frames was saved in desktop")
    if check_entry_numer == False:
        done_label.set("please enter the number again")
    if check_entry_path == False:
        done_label.set("please enter the path file again")
    else:
        done_label.set("please enter the values again")

#check enter  to number
def check_entry_numer(input_entry):
    input_entry.get()
    if input_entry:
        try:
            int(input_entry)
            return True
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
