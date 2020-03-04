import os
import time
def clear():
    os.system("clear")
cho=input("(1)PolyBar Refresh\n(2)Pacman And Pamac\n(3)Battery:")
if cho == "1":
    clear()
    os.system("sh /home/efe/.config/polybar/launch.sh")
    time.sleep(0.15)
    os.system("clear")
elif cho == "2":
    clear()
    pa=input("(1)Pacman\n(2)Pamac:")
    if pa == "1":
        clear()
        pac=input("(1)Install\n(2)Search\n(3)Remove")
        if pac == "1":
            clear()
            pacin=input("What Do You Want To Install? :")
            os.system("sudo pacman -Syyu "+pacin)
        elif pac == "2":
            clear()
            pacse=input("What Do You Want To Search? :")
            os.system("sudo pacman -Ss "+pacse)
        elif pac == "3":
            clear()
            pacre=input("What Do You Want To Remove? :")
            os.system("sudo pacman -Rs "+pacre)
    elif pa == "2":
        clear()
        pam=input("(1)Install\n(2)Search\n(3)Remove")
        if pam == "1":
            clear()
            pamin=input("What Do You Want To Install? :")
            os.system("pamac install "+pamin)
        elif pam == "2":
            clear()
            pamse=input("What Do You Want To Search? :")
            os.system("pamac search "+pamse)
        elif pam == "3":
            clear()
            pamre=input("What Do You Want To Remove? :")
            os.system("pamac remove "+pamre)
elif cho == "3":
    clear()
    os.system("upower -i /org/freedesktop/UPower/devices/battery_BAT0")
