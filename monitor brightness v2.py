import screen_brightness_control as sbc

#Creates class with terminal text color options
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Creates and Prints strings with the name of each monitor
monitor_names = sbc.list_monitors()
#print(monitor_names)

#Creates objects for the brightness level of each monitor
g14_internal_display = sbc.get_brightness(display='BOE Display Technology 0A1D')[0]
sceptre_y27 = sbc.get_brightness(display='Sceptre Y27')[0]
asus_pro_art = sbc.get_brightness(display='None Generic Monitor')[0]

#Prints current brightness levels of all monitors
print("G14 Internal display brightness is currently set to " + str(g14_internal_display) + '%')
print("Sceptre Y27 display brightness is currently set to " + str(sceptre_y27) + '%')
print("Asus Pro Art display brightness is currently set to " + str(asus_pro_art) + '%')

for monitor in monitor_names:
    brightness = input("What brightness level would you like {} to be set to?".format(monitor))
    while True:
        try:
            monitor_brightness = int(brightness)
            if monitor_brightness < 0 or monitor_brightness > 100:
                raise Exception
            else:
                break
        except:
            print(bcolors.FAIL + "ERROR: Brightness must be an integer between 0 and 100! {} does not qualify!".format(brightness) + bcolors.ENDC)
            brightness = input("What brightness level would you like {} to be set to?".format(monitor))
    sbc.set_brightness(brightness, display=monitor)
    print(bcolors.WARNING + "{} brightness has been set to {}%!".format(monitor, str(brightness)) + bcolors.ENDC)

#sbc.set_brightness(25, display='BOE Display Technology 0A1D')
#sbc.set_brightness(25, display='None Generic Monitor')
#sbc.set_brightness(50, display='Sceptre Y27')

