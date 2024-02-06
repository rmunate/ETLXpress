from core.Clarity.Console import Console
from core.Clarity.Logger import Logger
from core.Framework.Kernel import Kernel
from core.Framework.App import App
from core.Environment.Env import Env
import argparse
import sys
import os

os.environ['PYTHONBUFFERED'] = '1'

#-----------------------------------------------------#
# ETLXpress.                                          #
# Lightweight framework for managing CronJobs.        #
# Handles ETL, Reporting, and Messaging.              #
# CCL Colombian Logistics Corporation.                #
# Author: Raul Mauricio Uñate                         #
#-----------------------------------------------------#

if __name__ == "__main__":
    
    # Limpiar el ENV
    Env.clear()
    
    # Start message
    Console.info(f"ETLXpress Initialized - Version: {App.version}")
        
    # Inserting Log.
    Logger().info("ETLXpress Execution.")
    
    # CLI Argument Parser
    parser = argparse.ArgumentParser(description="ETLXpress Main Script")
    parser.add_argument("--cron", help="Name of the cronjob to be executed manually immediately.")
    args = parser.parse_args()
    
    # Actualizar SysPath.
    project_directory = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_directory)
    
    # Initialize the Kernel
    kernel = Kernel()
        
    if args.cron:
        # If the --cron argument is provided, execute that cronjob immediately.
        kernel.execute(args.cron)
    else:
        # If --cron argument is not provided, register all cronjobs.
        kernel.register()
