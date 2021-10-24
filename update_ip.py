import os
import socket
import time



def update_git():

    cmd = "git add ifconfig.txt" 
    os.system(cmd)

    cmd = 'git commit -m "system update"'
    os.system(cmd)

    cmd = "git push https://<user>:<token>@github.com/dashemsec/rpidata.git"
    os.system(cmd)

    print('end of commands')

def print_xyz():
    print("TEST")

def update_ifconfig_file():
    cmd = "ifconfig > ifconfig.txt"
    os.system(cmd)
    cmd = "date >> ifconfig.txt"
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
