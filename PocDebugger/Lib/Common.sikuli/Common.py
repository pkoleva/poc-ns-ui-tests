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
    sshproc = subprocess.Popen([command],
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


def type_infield(field, string):
    click(field)
    type(string)


def wait_to_load(image, counter):
    n = counter
    a = False
    while n != 0:
        if exists(image):
            print("Found image" + repr(image))
            a = True
            break
        else:
            wait(1)
        n -= 1
    print("Waited for " + repr(counter-n) + " seconds")
    return a

# def open_tab(tab):


def generate_debug_configurations():
    click(ImageLibrary.Common.settingsNewBtn)
    wait_to_load(ImageLibrary.Common.selectEnvironmentLbl,2)
    click(ImageLibrary.Common.nativeScriptLbl)


def run_configuration(configuration):
    click(Pattern(ImageLibrary.Common.settingsBtn).targetOffset(-50, 0))
    wait(configuration)
    click(Pattern(configuration).similar(0.9))
    click(ImageLibrary.Common.startDebugButton)

