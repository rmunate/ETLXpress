#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#---------------------------------------------------------#
# Data Framework                                          #
# Last Modification: 06-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
from core.Clarity.Logger import Logger

# Facade JOB execution
class Command:

    # ----------------------------------------------------------------------------------------------------#
    # Execute Command Without Reponse                                                                     #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self, command):
        
        # Log Registration
        Logger().info(f"--------------- START JOB <{command.__class__.__name__}> ---------------")

        # Execute ETL command: Extract, Transform, Load
        command.extract()
        command.transform()
        self.data = command.load()

        # Log the completion of the JOB
        Logger().info(f"---------------  END JOB  <{command.__class__.__name__}> ---------------")

    # ----------------------------------------------------------------------------------------------------#
    # Reponse Data Las Process                                                                            #
    # ----------------------------------------------------------------------------------------------------#
    def response(self):
        return self.data