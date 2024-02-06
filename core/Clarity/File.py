#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Class For File Manager                                  #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

from core.Clarity.Logger import Logger
import os

class File:
    
    # Initialize the Storage Files
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), '../../storage/Files')
    
    # Path Storage Files
    @staticmethod
    def path():
        return File().path
    
    # Full Path Storage Files With File Name
    @staticmethod
    def routeSave(name):
        return f"{File().path}/{name}"
    
    # Delete File
    @staticmethod
    def delete(name):
        try:
            
            # Route File
            file = f"{File().path}/{name}"
            
            # If Exist File
            if os.path.exists(file):
                os.remove(file)
                
            # Log Registration
            Logger().info(f"File Class: Delete File <{name}>")
        
            return True
        
        except Exception as e:
            
            return False