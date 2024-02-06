#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#---------------------------------------------------------#
# ReportMdzM3 (Excel)                                     #
#---------------------------------------------------------#

# Mandatory Imports
from core.Contracts.IExport import IExport

class ReportMdzM3Excel(IExport):

    # Custom Propierties
    data = None
    
    # ----------------------------------------------------------------------------------------------------#
    # Received data through the constructor (Not Mandatary)                                               #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self, data):
        self.data = data
        
    # ----------------------------------------------------------------------------------------------------#
    # Name Excel File                                                                                     #
    # ----------------------------------------------------------------------------------------------------#
    def filename(self):
        return "ReporteMdzM3.xlsx"
    
    # ----------------------------------------------------------------------------------------------------#
    # SheetName                                                                                           #
    # ----------------------------------------------------------------------------------------------------#
    def title(self):
        return "Reporte M3"
        
    # ----------------------------------------------------------------------------------------------------#
    # Excel Styles - Define styles for the Excel report.                                                  #
    # ----------------------------------------------------------------------------------------------------#
    def styles(self):
        return {
            'backgroundColorHeader' : '002040',
            'textColorHeader' : 'ffffff',
            'textBoldHeader' : True
        }
        
    # ----------------------------------------------------------------------------------------------------#
    # Excel Headings - Extracts headers for the Excel report from the provided data.                      #
    # ----------------------------------------------------------------------------------------------------#
    def headings(self):
        return self.data["headers"]
        
    # ----------------------------------------------------------------------------------------------------#
    # Excel Rows - Extracts rows for the Excel report from the provided data.                             #
    # ----------------------------------------------------------------------------------------------------#
    def rows(self):
        return self.data["rows"]