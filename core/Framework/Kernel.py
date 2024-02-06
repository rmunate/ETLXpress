#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#---------------------------------------------------------#
# Kernel: Framework Initialization                        #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Importaciones De Modulo
from config.CronJobs import cronjobs
from core.Clarity.Console import Console
from core.Clarity.Logger import Logger
import subprocess
import logging
import sys

# Check if the operating system is Linux
if sys.platform.startswith('linux'):
    from crontab import CronTab
else:
    import schedule
    import time

class Kernel:

    # Execute a specific cronjob once without scheduling
    def execute(self, cron_name):
        
        # Buscar el CronJob
        for job in cronjobs:
            
            # Si se encuentra el Cron
            if job['name'] == cron_name:
                
                # Intentar Ejecución
                try:
                    
                    # Imprimir mensaje de Info
                    Console.info(f"Start Process Succesfull")
                    
                    # Crear Registro en el Log
                    Logger().info(f"Start Job, Name: {cron_name}.")
                                        
                    # Ejecutar el Cron
                    subprocess.run(job['command'], shell=True, check=True)
                    
                except subprocess.CalledProcessError as e:
                    
                    # Imprimir Error En Pantalla
                    Console.danger(f"Error Execute")
                    
                    # Registrar Los De Error
                    Logger().info(f"Fail Job, Name: {cron_name}, Error: {e}.")
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    # Run the cronjob immediately
    def run_cronjob(self, job):
        """
        Run a cronjob immediately.

        Args:
            job (dict): Cronjob configuration.
        """
        # Perform the actions specified in the cronjob
        try:
            # Execute the cronjob command
            subprocess.run(job['command'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing cronjob '{job['name']}': {e}")

    # Register and schedule the jobs
    def register(self):
        """
        Register and schedule the defined cronjobs.
        """
        # Check if the operating system is Linux
        if sys.platform.startswith('linux'):
            self.register_linux()
        else:
            self.register_windows()

    # Register and schedule cronjobs for Linux
    def register_linux(self):
        cron = CronTab(user=True)
        for job in cronjobs:
            cron_job = cron.new(command=job['command'])
            cron_job.setall(job['schedule'])
            cron_job.set_comment(job['name'])
            cron_job.enable()
        cron.write()

    # Register and schedule cronjobs for Windows
    def register_windows(self):
        for job in cronjobs:
            # Pass the environment configuration to the cronjob
            job['env_config'] = self.env_config

            # Schedule the cronjob
            schedule.every().day.at(job['schedule']).do(self.run_cronjob, job)

        # Keep the script running to allow scheduled tasks to execute
        while True:
            schedule.run_pending()
            time.sleep(1)
