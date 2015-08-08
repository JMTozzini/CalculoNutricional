#! /usr/bin/python

from model import Model
from exception import MyException
from consoleView import  ConsoleView
import traceback

if __name__ == '__main__' :
    
    try :
        gModel = Model()
        gView = ConsoleView(gModel)
        gView.run()
        print("FIM")
        
    except MyException as myExc:
        print(myExc)
    
    except:
        traceback.print_exc()
        
    