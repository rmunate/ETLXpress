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
# Interface Base Class for Excel Export                   #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Importing the Abstract Base Class (ABC) from the abc module
from abc import ABC, abstractmethod

class IExport(ABC):

    # Name File
    @abstractmethod
    def filename(self):
        pass
    
    # SheetName
    @abstractmethod
    def title(self):
        pass
    
    # Excel Styles - Define styles for the Excel report.
    @abstractmethod
    def styles(self):
        pass
    
    # Excel Headings - Extracts headers for the Excel report from the provided data.
    @abstractmethod
    def headings(self):
        pass
    
    # Excel Rows - Extracts rows for the Excel report from the provided data.
    @abstractmethod
    def rows(self):
        pass