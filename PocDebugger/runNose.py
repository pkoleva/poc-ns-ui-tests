import nose
import sys

print sys.argv[1]
nose.run(argv=['nosetests','-v','--with-doctest',sys.argv[1]])
