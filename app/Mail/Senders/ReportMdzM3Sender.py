#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#---------------------------------------------------------#
# ReportMdzM3Sender (Email)                               #
#---------------------------------------------------------#

class ReportMdzM3Sender:
    
    # ----------------------------------------------------------------------------------------------------#
    # Email Subject                                                                                        #
    # ----------------------------------------------------------------------------------------------------#
    def subject(self):
        return "Mondelez Cubic Meters Report"
    
    # ----------------------------------------------------------------------------------------------------#
    # Destination Email Addresses                                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def to(self):
        return [
            "arbey.vivas@mdlz.com",
            "alexander.loza@mdlz.com",
            "alejandramaria.rodriguez@mdlz.com",
            "maricel.cordoba@mdlz.com",
            "coorinventarioscl@ccl.com.co",
            "gerenteopeclo@ccl.com.co",
            "franklin.amaya@mdlz.com",
            "andres.cardona@mdlz.com",
            "jrobayo@ccl.com.co",
            "runate@ccl.com.co",
            "jarevalo@ccl.com.co",
            "wsanchez@ccl.com.co"
        ]
    
    # ----------------------------------------------------------------------------------------------------#
    # Body Type {'type' : 'plain/html', 'template' : 'text/template'}                            #
    # ----------------------------------------------------------------------------------------------------#
    def body(self):
        return {
            'type': 'html',               # html/plain
            'template': 'ReportMdzM3',    # template (HTML template name) / Plain Text
            'replacements' : {}           # Key, value, find the key and replace it with the value
        }

    # ----------------------------------------------------------------------------------------------------#
    # Attachments                                                                                          #
    # ----------------------------------------------------------------------------------------------------#  
    def attachments(self):
        return [
            'ReporteMdzM3.xlsx'
        ]