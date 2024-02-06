#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Class for printing values to the console.               #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
from core.Clarity.Logger import Logger

class Console:

    # Color Palette.
    default = '\033[0m'
    info_color = '\033[34m'
    danger_color = '\033[91m'
    warning_color = '\033[93m'
    success_color = '\033[92m'

    # Print value and exit execution.
    @staticmethod
    def dump(value):
               
        # Print Value
        print(value)
        sys.exit()
        
    # Print value to the console without formatting.
    @staticmethod
    def write(message=''):
        
        # Execution
        print(f"{Console.default}{message}{Console.default}")
        
    # Print information value.
    @staticmethod
    def info(message=''):
        
        # Execution
        print(f"{Console.info_color}{message}{Console.default}")
        
    # Print error value.
    @staticmethod
    def danger(message=''):
        
        # Execution
        print(f"{Console.danger_color}{message}{Console.default}")
        
    # Print warning value.
    @staticmethod
    def warning(message=''):
        
        # Execution
        print(f"{Console.warning_color}{message}{Console.default}")
        
    # Print successful value.
    @staticmethod
    def success(message=''):
        
        # Execution
        print(f"{Console.success_color}{message}{Console.default}")
