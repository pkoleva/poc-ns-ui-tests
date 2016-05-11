from Lib import Common
import unittest
import os
import sys

cwd = os.getcwd()


class BasicAppsTests(unittest.TestCase):
    global cwd
    def setUp(self):
        print "Start of test " + self._testMethodName

    def tearDown(self):
        print "End of test " + self._testMethodName
        name = cwd + "\\" + self._testMethodName + ".png"
        if sys.exc_info() == (None, None, None):
            Common.capture_screen(name)
            os.remove(name)

    def test001(self):
        res = Common.execute_command("tns --version")
        print res
        assert 1 == 1

    def test002(self):
        assert 1 == 2, "Not equal"
