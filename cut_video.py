import cv2


def cut_frame(number_frame_entry, path_file_entry):
    cap = cv2.VideoCapture(path_file_entry)
    success, image = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)  # number of frames per second
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # number of frames in the movie
    number_frame = int(number_frame_entry.get())  # how many frames do i want to extract from the video
    frames_to_skip = (frame_count - 1) / (number_frame - 1)  # count frame
    count = 0  # the number of the currently processed frame
    frames_taken = 0  # how many frames have already been drawn
    print("From a movie of length " + str(frame_count) + " number of frame " + str(input) + " frame")
    image_list = []
    while success:
        if (count == round(frames_taken * frames_to_skip)):
            print("TO take " + str(frames_taken + 1) + ". Frame, in video has number " + str(count) + " on " + str(
                frame_count - 1))
            milisecond = round(count * 1000 / fps)
            print("Frame from " + str(milisecond) + " milliseconds of recording")
            image_list.append(image)
            frames_taken += 1
        success, image = cap.read()
        count += 1
    cap.release()
    return image_list
