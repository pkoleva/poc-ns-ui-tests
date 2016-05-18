import org.sikuli.script.SikulixForJython
from sikuli import *
import os
import sys
import unittest
from Lib import Common
from Common import *
from ImageLibrary import *


cwd = os.getcwd()


class CommandLine_Tests(unittest.TestCase):
    global cwd

    def setUp(self):
        print "Start of test " + self._testMethodName

    def tearDown(self):
        print "End of test " + self._testMethodName
        name = cwd + "\\" + self._testMethodName + ".png"
        if sys.exc_info() != (None, None, None):
            capture_screen(name)
            os.remove(name)

    # def test001(self):
    #     start_console()
    #     typeInField(Pattern(Common.consoleWindow).similar(0.9), "tns create TestApp")
    #     type(Key.ENTER)
    #     wait(Common.projectCreated, 10)
    #     typeInField(Pattern(Common.consoleWindow).similar(0.9), "cd TestApp")

    # def test100_LaunchAndroidEmulator_VerifyStarted(self):
    #     wait_to_load(Common.debugTab, 2)
    #     if not exists(Common.debugLbl):
    #         click(Common.debugTab)
    #         wait_to_load(Common.debugLbl, 2)
    #     if exists(Pattern(Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(Common.launchAndroidEmuLbl)

    # def test110_AttachAndroidEmulator_VerifyStarted(self):
    #     wait_to_load(ImageLibrary.Common.debugTab, 2)
    #     if not exists(ImageLibrary.Common.debugLbl):
    #         click(ImageLibrary.Common.debugTab)
    #         wait_to_load(ImageLibrary.Common.debugLbl, 2)
    #     if exists(Pattern(ImageLibrary.Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(ImageLibrary.Common.attachAndroidEmulatorLbl)

    # def test200_LaunchAndroidDevice_VerifyStarted(self):
    #     wait_to_load(ImageLibrary.Common.debugTab, 2)
    #     if not exists(ImageLibrary.Common.debugLbl):
    #         click(ImageLibrary.Common.debugTab)
    #         wait_to_load(ImageLibrary.Common.debugLbl, 2)
    #     if exists(Pattern(ImageLibrary.Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(ImageLibrary.Common.launchAndroidDeviceLbl)

    # def test210_AttachAndroidDevice_VerifyStarted(self):
    #     wait_to_load(ImageLibrary.Common.debugTab, 2)
    #     if not exists(ImageLibrary.Common.debugLbl):
    #         click(ImageLibrary.Common.debugTab)
    #         wait_to_load(ImageLibrary.Common.debugLbl, 2)
    #     if exists(Pattern(ImageLibrary.Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(ImageLibrary.Common.attachAndroidDeviceLbl)

    # def test300_LaunchiOSEmulator_VerifyStarted(self):
    #     wait_to_load(Common.debugTab, 2)
    #     if not exists(Common.debugLbl):
    #         click(Common.debugTab)
    #         wait_to_load(Common.debugLbl, 2)
    #     if exists(Pattern(Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(Common.launchiOSEmulatorLbl)

    # def test310_AttachiOSEmulator_VerifyStarted(self):
    #     wait_to_load(ImageLibrary.Common.debugTab, 2)
    #     if not exists(ImageLibrary.Common.debugLbl):
    #         click(ImageLibrary.Common.debugTab)
    #         wait_to_load(ImageLibrary.Common.debugLbl, 2)
    #     if exists(Pattern(ImageLibrary.Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(ImageLibrary.Common.attachiOSEmulatorLbl)

    # def test400_LaunchiOSDevice_VerifyStarted(self):
    #     wait_to_load(ImageLibrary.Common.debugTab, 2)
    #     if not exists(ImageLibrary.Common.debugLbl):
    #         click(ImageLibrary.Common.debugTab)
    #         wait_to_load(ImageLibrary.Common.debugLbl, 2)
    #     if exists(Pattern(ImageLibrary.Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(ImageLibrary.Common.launchiOSDeviceLbl)

    # def test410_AttachiOSDevice_VerifyStarted(self):
    #     wait_to_load(ImageLibrary.Common.debugTab, 2)
    #     if not exists(ImageLibrary.Common.debugLbl):
    #         click(ImageLibrary.Common.debugTab)
    #         wait_to_load(ImageLibrary.Common.debugLbl, 2)
    #     if exists(Pattern(ImageLibrary.Common.settingsNewBtn).similar(0.9)):
    #         generate_debug_configurations()
    #     run_configuration(ImageLibrary.Common.attachiOSDeviceLbl)
