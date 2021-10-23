import subprocess
#from pexpect import popen_spawn
import os


user = 'dashemsec'
password = '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'

cmd = "cd /home/pi/github/rpidata"
#returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git add ." 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "system update"'
subprocess.call(cmd, shell=True)

#cmd = "git remote set-url origin https://github.com/Tehsurfer/git-test.git"
#subprocess.call(cmd, shell=True)

cmd = "git push "
child_process = popen_spawn.PopenSpawn(cmd)
child_process.expect('User')
child_process.sendline(user)
child_process.expect('Password')
child_process.sendline(password)
print('returned value:', returned_value)

print('end of commands')
