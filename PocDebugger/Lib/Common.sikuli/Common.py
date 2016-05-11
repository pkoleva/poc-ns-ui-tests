import org.sikuli.script.SikulixForJython
from sikuli import *
import subprocess
import os
import os.path
from Lib import ImageLibrary

screen = Screen()


def start_console():
    subprocess.Popen(["start cmd /k"],
                     shell=True,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE
                     )


def execute_command(command):
    sshproc = subprocess.Popen(["start cmd /c " + command],
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
    stdout_value, stderr_value = sshproc.communicate('through stdin to stdout')
    print "####################"
    print repr(stdout_value)
    if stderr_value != None:
        print "####################"
        print repr(stderr_value)


def capture_screen(name):
    print "Capturing screenshot"
    file_name = screen.capture(screen.getBounds())
    if os.path.isfile(name):
        os.remove(name)
    os.rename(file_name, name)


def typeInField(field,string):
    click(field)
    type(string)
