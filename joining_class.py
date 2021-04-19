from datetime import datetime
import time
import webbrowser

links = [
    "https://us04web.zoom.us/j/9922162287?pwd=Wkp3TXgySWh5Ylo0bkxtR0FFdXlFZz09",    # dm
    "https://us04web.zoom.us/j/6845247405?pwd=VXVHWWY4RGxVLzFSRzl6NjEzTWdJUT09",    # es
    "https://us04web.zoom.us/j/3848569137?pwd=ZTFtTmM3WndOcFR0YXhPYWEzSjlHUT09",    # pcc
    "https://us04web.zoom.us/j/75820775605?pwd=cXFCR1ZUN2tOcFdQNDBzZ0dYQ3VMQT09",    # ada
    "https://us04web.zoom.us/j/79099639821?pwd=Nk40UkdEdjZnNC9aVWdxb3p6OHVuZz09",    # eh
    "https://us04web.zoom.us/j/76580633198?pwd=R3NOZ3JMaWhaaUVIQlhuZnY2Zmk2dz09",    # iot
]


def joinClass(clsno):
    webbrowser.open(links[clsno], new=1)
    print("Joined Class")
    time.sleep(3000)
    print("Class ended")
    checkforclass()


def checkforclass():

    now = datetime.now()
    currenttime = now.strftime("%H:%M")
    print("Current time is : " + currenttime)
    if(currenttime == classtime[4]):
        joinClass(4)
    elif(currenttime == classtime[3]):
        joinClass(3)
    elif(currenttime == classtime[0]):
        joinClass(0)
    elif(currenttime == classtime[5]):
        joinClass(5)
    elif(currenttime == classtime[2]):
        joinClass(2)
    elif(currenttime == classtime[1]):
        joinClass(1)
    elif(currenttime >= "18:00"):
        print("All the classes are done")
        quit()
    else:
        print("Will join shortly")
        time.sleep(60)
        checkforclass()

# entering class time


classtime = ['pcct', 'adat', 'eht', 'est', 'iott', 'dmt']

for item in classtime:
    print("Enter %s time:" % (item))
    item = input()

print("You have classes at :")
print(classtime)

checkforclass()
