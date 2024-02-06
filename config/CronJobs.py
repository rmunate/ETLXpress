import sys
from os.path import abspath, join, dirname

# Obtén la ruta al directorio principal de tu proyecto
project_directory = abspath(join(dirname(__file__), '../'))

# Agrega el directorio principal al PYTHONPATH si no está ya presente
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#-----------------------------------------#
#   List Of CronJobs                      #
#-----------------------------------------#

cronjobs = [
    {
        'name': 'Report_Mondelez_M3',
        'schedule': '0 0 * * *',
        'command': 'python -B app/Console/Commands/ReportMdzM3.py',
    },
]
