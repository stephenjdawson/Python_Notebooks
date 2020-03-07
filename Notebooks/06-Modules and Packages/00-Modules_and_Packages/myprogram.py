#importing Module
from mymodule import my_func
#importing package
from MyMainPackage import mainscript
#importing subpackage
from MyMainPackage.SubPackage import mysubscript

#Can also import specific functions from packages and subpackages if you do not want to pring in whole package. 
#make sure to have an __init__.py file in your package and subpackage directory so Python knows they are there. 

#Call function from Module
my_func()
#Call function in package
mainscript.report_main()
#call function in subpackage
mysubscript.sub_report()
