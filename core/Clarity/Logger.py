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
# Log System                                              #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Importaciones De Modulo
from datetime import datetime
import logging
import os

class Logger:
    
    # Init Logger
    def __init__(self):
        
        # Get Current Date
        currentDate = datetime.now()
        dateNameLogFile = currentDate.strftime("%Y_%m_%d")
        
        # Get the current directory of the script
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Set the path for the log file
        path_log = os.path.join(current_directory, f"../../storage/logs/ETLXpress_{dateNameLogFile}.log")

        # Configure logging with encoding specification
        logging.basicConfig(filename=path_log, level=logging.INFO,
                            format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8')

    # Log an informational message
    @staticmethod
    def info(message):
        logging.info(message)

    # Log an error message
    @staticmethod
    def error(message):
        logging.error(message)
