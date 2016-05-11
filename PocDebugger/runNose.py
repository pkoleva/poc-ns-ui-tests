import nose
import sys

print sys.argv[1]
if __name__ == '__main__':
    arguments = ['nosetests', '-v', '-s', '--with-doctest', '--with-xunit']
    for i in sys.argv:
        arguments.append(str(i))
    nose.run(argv=arguments)
