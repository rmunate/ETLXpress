#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Extract (*E* TL)                                        #
#---------------------------------------------------------#

# Imports of this ETL
from config.DataBases import DB_ORACLE_PBI
from datetime import datetime, timedelta
from core.Builder.Oracle import Oracle

class ReportMdzM3Extratc:
    
    # ----------------------------------------------------------------------------------------------------#
    # Connection to the Database and/or Add Additional Dependencies                                       #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self):
        self.db = Oracle(DB_ORACLE_PBI)
        
    # ----------------------------------------------------------------------------------------------------#
    # Complete Extraction Process                                                                         #
    # ----------------------------------------------------------------------------------------------------#
    def handle(self):
        
        # --// Fechas del informe
        # Fecha actual
        currentDate = datetime.now()

        # Fecha De Ayer
        newDate = currentDate - timedelta(days=1)

        # Inicio Informe
        startYaer = newDate.year
        startMonth = newDate.month
        startDay = 1

        # Fin de Consulta
        endYaer = newDate.year
        endMonth = newDate.month
        endDay = newDate.day
        
        # Rango
        start = datetime(startYaer, startMonth, startDay)
        end = datetime(endYaer, endMonth, endDay)
        
        # Fechas para el Where
        startWhere = start.strftime('%Y-%m-%d')
        endWhere = end.strftime('%Y-%m-%d')
        
        query = "SELECT OWNER AS PROPIETARIO, SKU, DESCRIPCION, VOLUMEN,"
                
        while start <= end:
            formatted_date = start.strftime('%Y-%m-%d')  # Formato compatible con Oracle
            query += f"MAX(CASE WHEN TRUNC(LIH_DATE) = TO_DATE('{formatted_date}', 'YYYY-MM-DD') THEN CANTIDAD_BODEGA END) AS \"{formatted_date}\", "
            start += timedelta(days=1)
            
        query += f"SUM(CANTIDAD_BODEGA) AS TOTAL_UNIDADES, AVG(CANTIDAD_BODEGA) AS PROMEDIO_UNIDADES, (AVG(CANTIDAD_BODEGA) * VOLUMEN) AS TOTAL_M3 FROM VIEW_REPORT_M3 WHERE LIH_DATE >= TO_DATE('{startWhere}', 'YYYY-MM-DD') AND LIH_DATE <= TO_DATE('{endWhere}', 'YYYY-MM-DD') GROUP BY OWNER, SKU, DESCRIPCION, VOLUMEN"
        
        try:
            return self.db.query(query)
        except ValueError as e:
            raise ValueError("Error De Ejecución.")
