#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

import sys
from os.path import abspath, join, dirname

# Obtén la ruta al directorio principal de tu proyecto
project_directory = abspath(join(dirname(__file__), '../../'))

# Agrega el directorio principal al PYTHONPATH si no está ya presente
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Interface Base Class for Jobs                           #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Importing the Abstract Base Class (ABC) from the abc module
from abc import ABC, abstractmethod

class IJob(ABC):

    # Abstract method for extracting data from a source
    @abstractmethod
    def extract(self):
        """Extracts the necessary data for the ETL job."""
        pass
    
    # Abstract method for executing the main data transformation logic
    @abstractmethod
    def transform(self):
        """Executes the transformation of the extracted data."""
        pass
    
    # Abstract method for cleaning up resources or performing final actions, and loading the results
    @abstractmethod
    def load(self):
        """Loads or stores the results of the ETL job."""
        pass
