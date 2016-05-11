# poc-ns-ui-tests
PoC on how to structure a UI Tests project

# Prerequisites
You should have the following dependencies to run the project
- python (v 2.7.0)
- jython (v 2.7.0)
- Sikuli (v 1.1.0)
- noserunner (v 1.3.7) (only for running through the command line)

# How to run the tests
## Via PyCharm IDE
- Open the folder of the project with PyCharm
- In File>Settings>Project>Project Interpreter select 2.7.0 jython (if you can't find the interpreter you'll need to add it)
- In Run/Debug Configurations create a new Python Unittest configuration and in Environment variables add CLASSPATH to sikulixapi.jar and JYTHONPATH to C:\Program Files (x86)\JetBrains\PyCharm Community Edition 5.0.4\helpers\pydev; or where the pydev plugin is
Run the tests with the newly made configuration

## Using other IDEs
Basically the same - add jython interpreter, add sikulixapi.jar to the classpath of the project, configure running and execute tests

## Using the command line
- add sikulixapi.jar to CLASSPATH env variable 
- if everything is set correctly you just need to go to the project folder and run "jython runNose.py Tests"
