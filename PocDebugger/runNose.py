import unittest
import nose
import sys

sys.path.append("C:\jenkins\tools\jython\SikuliX\sikuli-java.jar")
sys.path.append("C:\jenkins\tools\jython\SikuliX\sikuli-script.jar")
sys.path.append("C:\jenkins\tools\jython\SikuliX\libs")
print "sys.path=" + repr(sys.path)


print sys.argv[1]
nose.run(argv=['nosetests','-v','--with-doctest',sys.argv[1]])
