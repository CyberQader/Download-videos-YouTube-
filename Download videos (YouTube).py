from pystyle import *
from pytubefix import YouTube
import os
import time


def elite_ui():

    os.system('cls' if os.name == 'nt' else 'clear')

    header = """
    ┌────────────────────────────────────────────────────────┐
    │          A B D   A L Q A D E R   S Y S T E M S         │
    │              -- TERMINAL INTERFACE v5.0 --             │
    └────────────────────────────────────────────────────────┘
    """

    # 3. استخدام التوسيط الديناميكي
    centered_header = Center.Center(header)

    print(Colorate.Horizontal(Colors.blue_to_white, centered_header))

    status_box = f"""
        [●] STATUS: SECURE      [●] SERVER: LOCALHOST
        [●] ENCRYPTION: AES     [●] ACCESS: AUTHORIZED
    """
    print(Colorate.Vertical(Colors.white_to_blue, Center.Center(status_box)))
    print(Center.Center("━" * 58))

    prefix = " [ SYSTEM BOOTING ] "
    Write.Print(prefix.center(80), Colors.blue_to_white, interval=0.01)

    print("\n")
    for i in range(31):
        bar = "▰" * i + "▱" * (30 - i)
        percent = int((i / 30) * 100)
        print(f"       PROGRESS: {bar} {percent}%".center(80), end="\r")
        time.sleep(0.04)

    print("\n\n" + " » READY FOR COMMANDS « ".center(80))


elite_ui()

url = Write.Input('Enter Url Video : ',Colors.blue_to_green,interval=0.1)
place = Write.Input('Enter Folder To Save The Results : ',Colors.blue_to_green,interval=0.1)
YouTube(url).streams.get_highest_resolution().download(place)
Write.Print('\n The Video Saved To : ',Colors.green,interval=0.2)
Write.Print(place + 'Folder',Colors.red,interval=0.2)
input('\n........')