#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Extract (*E* TL)                                        #
#---------------------------------------------------------#

# ETL Extract Name <ExampleExtract>
class ExampleExtract:
    
    # ----------------------------------------------------------------------------------------------------#
    # Connection to the Database and/or Add Additional Dependencies                                       #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self):
        # --// Your Code.
        pass
        
    # ----------------------------------------------------------------------------------------------------#
    # Complete Extraction Process                                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def handle(self):
        # --// Your Code.
        pass
