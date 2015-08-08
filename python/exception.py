class MyException(Exception):
    """Exception class of the application for customs exceptions"""
    
    def __init__(self, iMsg):
        self.__message = iMsg
        
    def __str__(self):
        return repr(self.__message)