#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

import sys
from os.path import abspath, join, dirname

# Obtén la ruta al directorio principal de tu proyecto
project_directory = abspath(join(dirname(__file__), '../../../'))

# Agrega el directorio principal al PYTHONPATH si no está ya presente
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# (CRONJOB)                                               #
#---------------------------------------------------------#

# Mandatory Imports
from core.Facades.Command import Command
from core.Facades.Extract import Extract
from core.Facades.Transform import Transform
from core.Facades.Load import Load
from core.Facades.Mail import Mail
from core.Facades.Excel import Excel
from core.Contracts.IJob import IJob

# Job Name <ExampleJob>
class ExampleJob(IJob):
   
    # ----------------------------------------------------------------------------------------------------#
    # Data extraction process from the corresponding data source (Database, excel, csv, blueprint, etc.)  #
    # ----------------------------------------------------------------------------------------------------#
    def extract(self):
        # --// Your Code.
        pass

    # ----------------------------------------------------------------------------------------------------#
    # Data transformation process to be processed                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def transform(self):
        # --// Your Code.
        pass
        
    
    # ----------------------------------------------------------------------------------------------------#
    # Clean up resources or perform final actions                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def load(self):
        # --// Your Code.
        pass
        

#---------------------------------------------------------#
# Job Execution                                           #
#---------------------------------------------------------#
Command(ExampleJob())