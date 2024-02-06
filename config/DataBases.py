import sys
from os.path import abspath, join, dirname

# Obtén la ruta al directorio principal de tu proyecto
project_directory = abspath(join(dirname(__file__), '../'))

# Agrega el directorio principal al PYTHONPATH si no está ya presente
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#---------------------------------------------#
# Database Connection Data                    #
#---------------------------------------------#

# Importaciones De Modulo
from core.Environment.Env import Env

# Base de Datos De Integracion PBI
class DB_ORACLE_PBI:
    name = "BPI"
    tns = Env.get("DB_TNS_PBI")
    username = Env.get("DB_USERNAME_PBI")
    password = Env.get("DB_PASSWORD_PBI")
    encoding = Env.get("DB_ENCODING_PBI")
    nencoding = Env.get("DB_NENCODING_PBI")