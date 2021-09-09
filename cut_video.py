import cv2


def cut_frame(number_frame_entry, path_file_entry):
    name_video_file = str(path_file_entry.get())
    cap = cv2.VideoCapture(name_video_file)
    success, image = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)  # number of frames per second
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # number of frames in the movie
    number_frame = int(number_frame_entry.get()) # how many frames do i want to extract from the video
    frames_to_skip = (frame_count - 1) / (number_frame - 1)  # co ile ramek wyciagam kolejna
    count = 0  # the number of the currently processed frame
    frames_taken = 0  # how many frames have already been drawn
    print("Z filmu o długości " + str(frame_count) + " ramek wyciągam " + str(input) + " ramek")
    image_list = []
    while success:
        if (count == round(frames_taken * frames_to_skip)):
            print("Wyciągam " + str(frames_taken + 1) + ". ramkę, w wideo ma numer " + str(count) + " na " + str(
                frame_count - 1))
            milisecond = round(count * 1000 / fps)
            print("Ramka pochodzi z " + str(milisecond) + " milisekundy nagrania")
            frames_taken += 1
            #cv2.imwrite(os.path.join(path,"frame%d.jpg" % count), image)
        success, image = cap.read()
        image_list.append(image)
        count += 1
    cap.release()
    return image_list
