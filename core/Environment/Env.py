#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)
    
#---------------------------------------------------------#
# Singleton Class for Loading the ENV                     #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Importaciones De Modulo
from core.Clarity.Logger import Logger
from dotenv import load_dotenv
import os

# Environment Class
class Env:
    
    # Instance of the ENV
    _instance = None

    # Unique loading of the ENV
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Env, cls).__new__(cls)
            cls._instance._loaded = False
        return cls._instance

    # Method to load the Env
    @staticmethod
    def load_env():
        if not hasattr(Env._instance, '_loaded') or not Env._instance._loaded:
            
            # Load ENV
            env_path = os.path.join(os.path.dirname(__file__), '../../.env')
            load_dotenv(env_path)
            Env._instance._loaded = True
            
            # Log Registration
            Logger().info(f"Environment: Initialized")

    # Method to get the value from Env
    @staticmethod
    def get(key):
        
        # Load ENV
        Env().load_env()
        
        # Data Value
        value = os.getenv(key)
        
        # Empty Or Null Value
        if value is None:
            
            # Log Registration
            Logger().error(f"Environment: Key '{key}' not found in environment variables.")
        
            raise (f"Environment: Key '{key}' not found in environment variables.")
        
        return value
    
    # Method to get the value from Env
    @staticmethod
    def clear():
        
        # Log Registration
        Logger().info(f"Environment: Clear")
        
        # Clear ENV
        Env._instance = None
