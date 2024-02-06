#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

import sys
from os.path import abspath, join, dirname

# Obtén la ruta al directorio principal de tu proyecto
project_directory = abspath(join(dirname(__file__), '../../../'))

# Agrega el directorio principal al PYTHONPATH si no está ya presente
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# ReportMdzM3 (JOB)                                       #
#---------------------------------------------------------#

# Mandatory Imports
from core.Contracts.IJob import IJob

# Facades
from core.Facades.Command import Command
from core.Facades.Extract import Extract
from core.Facades.Mail import Mail
from core.Facades.Excel import Excel

# Imports of this JOB
from app.Excel.Generators.ReportMdzM3Excel import ReportMdzM3Excel
from app.ETL.Extract.ReportMdzM3Extratc import ReportMdzM3Extratc
from app.Mail.Senders.ReportMdzM3Sender import ReportMdzM3Sender
from core.Clarity.Logger import Logger
from core.Clarity.File import File

# Job for Cubic Meters report at Mondelez
class ReportMdzM3(IJob):
   
    # ----------------------------------------------------------------------------------------------------#
    # Data extraction process from the corresponding data source (Database, excel, csv, blueprint, etc.)  #
    # ----------------------------------------------------------------------------------------------------#
    def extract(self):
        
        # --// Ejecución Proceso ETL (Extraccion).
        data = Extract(ReportMdzM3Extratc()).response()
                      
        # --// Validar si se tiene datos retornados.
        if(data is not None and data != ''):
            self.data = data
        else:
            Logger().error("Se Detiene Ejecución Por Falta De Datos.")
            raise ("No Existen Datos De Este Registro.")

    # ----------------------------------------------------------------------------------------------------#
    # Data transformation process to be processed                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def transform(self):
        
        # --// Para este reporte solo crearemos un excel que se enviara por correo electronico.
        Excel(ReportMdzM3Excel(self.data))
    
    # ----------------------------------------------------------------------------------------------------#
    # Clean up resources or perform final actions                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def load(self):
        
        # --// Envio De Excel Por Correo Electronico.
        Mail(ReportMdzM3Sender())
        
        # --//Eliminar Archivo Generado
        File.delete('ReporteMdzM3.xlsx')
        

#---------------------------------------------------------#
# Job Execution                                           #
#---------------------------------------------------------#
Command(ReportMdzM3())