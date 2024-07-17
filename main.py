import psutil
import ctypes
import os
import subprocess
import time

wallpaper_changed = False
music_playing = False
music_process = None

def change_wallpaper(path):
    global wallpaper_changed
    if os.name == 'nt': 
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        print("Шпалери змінено!")
def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent

def play_music(file):
    global music_playing, music_process
    if not music_playing:
        if os.name == 'nt':
            music_process = subprocess.Popen(['start', '', file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        music_playing = True
        print("Музика почала грати.")

def stop_music():
    global music_playing, music_process
    if music_playing and music_process:
        music_process.kill()  
        music_playing = False
        print("Музика зупинена.")

def main():
    wallpaper_1 = "D:\\users\\Desktop\\script\\image (1).png"
    wallpaper_2 = "D:\\users\\Desktop\\script\\image.png"
    music_file = "D:\\users\\Desktop\\script\\DOBRYVA_Svitlo_ye_chi_nema.mp3"

    while True:
        global wallpaper_changed
        battery = psutil.sensors_battery()
        if battery.power_plugged:
            if wallpaper_changed:
                change_wallpaper(wallpaper_2)
                wallpaper_changed = False
          
        else:
            if not wallpaper_changed:
                change_wallpaper(wallpaper_1)
                wallpaper_changed = True
            play_music(music_file) 

        time.sleep(10)  

if __name__ == "__main__":
    main()
