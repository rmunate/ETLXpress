#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Facade ETL Load                                      #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
from core.Clarity.Logger import Logger

# Facade Load execution
class Load:
    
    # ----------------------------------------------------------------------------------------------------#
    # Execute Command Without Reponse                                                                     #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self, etlprocessclass):
        
        # Log Registration
        Logger().info(f"Load Classs Executed: {etlprocessclass.__class__.__name__}")
        
        # Ejecucion del Metodo del Proceso.
        self.data = etlprocessclass.handle()
    
    # ----------------------------------------------------------------------------------------------------#
    # Reponse Data Las Process                                                                            #
    # ----------------------------------------------------------------------------------------------------#
    def response(self):
        return self.data
        