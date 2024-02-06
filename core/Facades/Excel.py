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
from core.Clarity.Excel import Excel as ExcelFile
from core.Clarity.File import File

# Facade Excel Generator execution
class Excel:
    
    # ----------------------------------------------------------------------------------------------------#
    # Execute Command Without Reponse                                                                     #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self, export):
        
        # Log Registration
        Logger().info(f"Excel Generator Classs Executed: {export.__class__.__name__}")
        
        # Instance of the Excel to Create
        excel = ExcelFile()
                
        # Styles
        eStyles = export.styles()
        excel.setBackgroundColorHeader(eStyles.get('backgroundColorHeader', 'FFFFFF'))
        excel.setTextBoldHeader(eStyles.get('textBoldHeader', False))
        excel.setTextColorHeader(eStyles.get('textColorHeader','000000'))
        
        # Sheet Name
        eTitle = export.title()
        excel.setSheetName(eTitle)
        
        # Headings
        eHeaders = export.headings()
        excel.headers(eHeaders)
        
        # Body
        eRows = export.rows()
        excel.rows(eRows)
        
        # Save
        eRoute = File.routeSave(export.filename())
        excel.save(eRoute)
        
        # Route File
        self.route = eRoute
    
    # ----------------------------------------------------------------------------------------------------#
    # Reply The Contents of Excel                                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def response(self):
        with open(self.route, 'r') as file:
            content = file.read()
        return content
        