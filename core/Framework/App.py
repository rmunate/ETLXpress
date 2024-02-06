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
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
class App:

    # Framework Name
    name = "ETLXpress"

    # Framework Version
    version = '1.0.0'

    # Version Date
    date = '2024-02-05'
