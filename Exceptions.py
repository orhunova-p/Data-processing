"""Prepared by Orgunova Polina K-10"""
class CommandLError(BaseException):
    def __str__(self):
        return "***** Command line error *****"
class Ini_FileError(BaseException):
    def __str__(self):
        return "***** Error reading ini file *****"
class Add_FileError(BaseException):
    def __str__(self):
        return "***** Incorrectly specified json file *****"
class AddError(BaseException):
    def __str__(self):
        return "***** Error reading json file *****"
class Main_Filling(BaseException):
    def __str__(self):
        return "***** Invalid data of csv file *****"
class DateFError(BaseException):
    def __str__(self):
        return "***** A non-existent date has been set *****"
class DateError(BaseException):
    def __str__(self):
        return "***** One date have more than one marks *****"
class KeysError(BaseException):
        def __str__(self):
            return "***** Invalid keys *****"
class FitError(BaseException):
    def __str__(self):
        return "***** Dissimilar information *****"
class OutputError(BaseException):
    def __str__(self):
        return "***** Unable to write output file *****"