#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Load (ET *L*)                                           #
#---------------------------------------------------------#

# ETL Load Name <ExampleLoad>
class ExampleLoad:
    
    # ----------------------------------------------------------------------------------------------------#
    # Connection to the Database, Load Data and/or Add Additional Dependencies                            #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self):
        # --// Your Code.
        pass
        
    # ----------------------------------------------------------------------------------------------------#
    # Complete Load Process                                                                               #
    # ----------------------------------------------------------------------------------------------------#
    def handle(self):
        # --// Your Code.
        pass
