#import subprocess
#from pexpect import popen_spawn
import os
import socket
import time
#import urllib2


#user = 'dashemsec'

def update_git():
    print("GIT CONFIG")
    cmd = 'git -C /home/pi/github/rpidata/ config user.email "<emailid>"'
    os.system(cmd)
    cmd = 'git -C /home/pi/github/rpidata/ config user.name "<name>"'
    os.system(cmd)

    print("GIT ADD")
    cmd = "git -C /home/pi/github/rpidata/ add ifconfig.txt" 
    os.system(cmd)

    print("GIT COMMIT")
    cmd = 'git -C /home/pi/github/rpidata/ commit -m "system update"'
    os.system(cmd)

    print("GIT PUSH")
    cmd = "git -C /home/pi/github/rpidata/ push https://<user>:<token>@github.com/dashemsec/rpidata.git"
    os.system(cmd)

    print('end of commands')

def print_xyz():
    print("TEST")

def update_ifconfig_file():
    print("UPDATING IFCONFIG FILE...")
    cmd = "ifconfig > /home/pi/github/rpidata/ifconfig.txt"
    os.system(cmd)
    cmd = "date >> /home/pi/github/rpidata/ifconfig.txt"
    os.system(cmd)

def internet_off():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            #print('Clossing socket')
            sock.close
        return False
    except OSError:
        pass
    return True

def check_internet_is_down():
   return internet_off()

def wait_for_internet():
    while internet_off() is True:
        print("INTERNET IS DOWN")
        time.sleep(1)
    print("INTERNET IS UP :)")

def main():

    if check_internet_is_down() is False:
        print("INTERNET IS UP :)")
        update_ifconfig_file()
        update_git()
        #print_xyz()

    while 1:
        internet_down = check_internet_is_down()
        if internet_down:
            print("INTERNET IS DOWN...")
            wait_for_internet()
            update_ifconfig_file()
            update_git()

        time.sleep(10)

    exit()

if __name__ == "__main__":
    main()
