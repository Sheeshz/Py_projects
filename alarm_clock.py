import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "py_beginner/alarm.mp3"
    running = True
    
    while running:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        
        if now == alarm_time:
            print("Wake Up!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        
            running = False
        
        time.sleep(1)

if __name__=="__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)