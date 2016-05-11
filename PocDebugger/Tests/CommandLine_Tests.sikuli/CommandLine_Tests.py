import org.sikuli.script.SikulixForJython
from sikuli import *
import os
import sys
import unittest
from Lib import Common
from Lib import ImageLibrary
from Common import *
from ImageLibrary import *


cwd = os.getcwd()


class CommandLineTests(unittest.TestCase):
    global cwd

    def setUp(self):
        print "Start of test " + self._testMethodName

    def tearDown(self):
        print "End of test " + self._testMethodName
        name = cwd + "\\" + self._testMethodName + ".png"
        if sys.exc_info() != (None, None, None):
            capture_screen(name)
            os.remove(name)

    def test001(self):
        start_console()
        typeInField(Pattern(Common.consoleWindow).similar(0.9), "tns create TestApp")
        type(Key.ENTER)
        wait(Common.projectCreated, 10)
