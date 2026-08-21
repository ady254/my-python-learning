from threading import Thread
from time import sleep, time

def download(file_name):
    print("downloading...",file_name)
    sleep(0.5)
    print("All Download completed")

if __name__ == "__main__":

    files = ["video.mp4", "image.png", "data.csv"]

    start = time()

    for f in files:
        download(f)


    end = time()

    print(f"serial time {end - start:.2f} seconds")

     