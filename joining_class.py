from datetime import datetime
import time
import webbrowser


class links:
    dm = "https://us04web.zoom.us/j/9922162287?pwd=Wkp3TXgySWh5Ylo0bkxtR0FFdXlFZz09"
    es = "https://us04web.zoom.us/j/6845247405?pwd=VXVHWWY4RGxVLzFSRzl6NjEzTWdJUT09"
    pcc = "https://zoom.us/j/3848569137?pwd=ZTFtTmM3WndOcFR0YXhPYWEzSjlHUT09"
    ada = "https://us04web.zoom.us/j/75820775605?pwd=cXFCR1ZUN2tOcFdQNDBzZ0dYQ3VMQT09"
    eh = "https://us04web.zoom.us/j/79099639821?pwd=Nk40UkdEdjZnNC9aVWdxb3p6OHVuZz09"
    iot = "https://us04web.zoom.us/j/76580633198?pwd=R3NOZ3JMaWhaaUVIQlhuZnY2Zmk2dz09"


def checkforclass():

    now = datetime.now()
    currenttime = now.strftime("%H:%M")
    print("Current time is : " +currenttime)

    if(currenttime == classtime[4]):
        webbrowser.open(links.iot,new=1)
        print("Joined Class")
        time.sleep(3000)
        print("Class ended")
        checkforclass()

    elif(currenttime == classtime[3]):
        webbrowser.open(links.es,new=1)
        print("Joined Class")
        time.sleep(3000)
        print("Class ended")
        checkforclass()
    
    elif(currenttime == classtime[0]):
        webbrowser.open(links.pcc,new=1)
        print("Joined Class")
        time.sleep(3000)
        print("Class ended")
        checkforclass()

    elif(currenttime == classtime[5]):
        webbrowser.open(links.dm,new=1)
        print("Joined Class")
        time.sleep(3000)
        print("Class ended")
        checkforclass()
    
    elif(currenttime == classtime[2]):
        webbrowser.open(links.eh,new=1)
        print("Joined Class")
        time.sleep(3000)
        print("Class ended")
        checkforclass()

    elif(currenttime == classtime[1]):
        webbrowser.open(links.ada,new=1)
        print("Joined class")
        time.sleep(3000)
        print("Class ended")
        checkforclass()

    elif(currenttime >= "18:00"):
        print("All the classes are done")

    else:
        print("Will join shortly")
        time.sleep(60)
        checkforclass()


#entering class time

pcct=input("Enter PCC time : ")
adat=input("Enter ADA time : ")
eht=input("Enter EH time : ")
est=input("Enter ES time : ")
iott=input("Enter IOT time : ")
dmt=input("Enter DM time : ")

classtime=[pcct,adat,eht,est,iott,dmt]
print("You have classes at :")
print(classtime)

checkforclass()