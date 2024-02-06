#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

# Module Imports
import os
from core.Clarity.Console import Console
from core.Clarity.Logger import Logger

# Class Create Files For CLI
class Maker:
    
    # General Configuration
    def __init__(self, type, name):
        
        # Log Registration
        Logger().info(f"Maker CLI Class: Initialized")
        
        self.type = type
        self.name = name
        
    # Make File
    def execute(self):
        
        # Start Execution
        Console.success(f"Starting batch process for creating command: {self.name}")
        
        # Create - Command
        if (self.type == 'command'):
                
            stub_file = os.path.join(os.path.dirname(__file__), '../Stubs/Command.stub')
            command_file = os.path.join(os.path.dirname(__file__), f"../../app/Console/Commands/{self.name}.py")
            
            # Check if File Already Exists
            if os.path.exists(command_file):
                Console.danger(f"The command to create already exists: {command_file}")
                sys.exit()

            # Open Stub File
            with open(stub_file, 'r') as f:
                content = f.read()

            # Apply Command Name
            output = content.replace('{{file-name}}', self.name)

            # Create New File
            with open(command_file, 'w') as f:
                f.write(output)

            # Console Alert
            Console.success(f"Command created successfully: {command_file}")
            
            # Log Registration
            Logger().info(f"Maker CLI Class: Create File <{command_file}>")
            
            # Close Process
            sys.exit()
            
        # Create - Excel
        if (self.type == 'excel'):
                
            stub_file = os.path.join(os.path.dirname(__file__), '../Stubs/Excel.stub')
            excel_file = os.path.join(os.path.dirname(__file__), f"../../app/Excel/Generators/{self.name}.py")
            
            # Check if File Already Exists
            if os.path.exists(excel_file):
                Console.danger(f"The Excel to create already exists: {excel_file}")
                sys.exit()

            # Open Stub File
            with open(stub_file, 'r') as f:
                content = f.read()

            # Apply Excel Name
            output = content.replace('{{file-name}}', self.name)

            # Create New File
            with open(excel_file, 'w') as f:
                f.write(output)

            # Console Alert
            Console.success(f"Excel created successfully: {excel_file}")
            
            # Log Registration
            Logger().info(f"Maker CLI Class: Create File <{excel_file}>")
            
            # Close Process
            sys.exit()
            
        # Create - Extract
        if (self.type == 'extract'):
                
            stub_file = os.path.join(os.path.dirname(__file__), '../Stubs/Extract.stub')
            extract_file = os.path.join(os.path.dirname(__file__), f"../../app/ETL/Extract/{self.name}.py")
            
            # Check if File Already Exists
            if os.path.exists(extract_file):
                Console.danger(f"The Extract to create already exists: {extract_file}")
                sys.exit()

            # Open Stub File
            with open(stub_file, 'r') as f:
                content = f.read()

            # Apply Extract Name
            output = content.replace('{{file-name}}', self.name)

            # Create New File
            with open(extract_file, 'w') as f:
                f.write(output)

            # Console Alert
            Console.success(f"Extract created successfully: {extract_file}")
            
            # Log Registration
            Logger().info(f"Maker CLI Class: Create File <{extract_file}>")
            
            # Close Process
            sys.exit()
            
        # Create - Transform
        if (self.type == 'transform'):
                
            stub_file = os.path.join(os.path.dirname(__file__), '../Stubs/Transform.stub')
            transform_file = os.path.join(os.path.dirname(__file__), f"../../app/ETL/Transform/{self.name}.py")
            
            # Check if File Already Exists
            if os.path.exists(transform_file):
                Console.danger(f"The Transform to create already exists: {transform_file}")
                sys.exit()

            # Open Stub File
            with open(stub_file, 'r') as f:
                content = f.read()

            # Apply Transform Name
            output = content.replace('{{file-name}}', self.name)

            # Create New File
            with open(transform_file, 'w') as f:
                f.write(output)

            # Console Alert
            Console.success(f"Transform created successfully: {transform_file}")
            
            # Log Registration
            Logger().info(f"Maker CLI Class: Create File <{transform_file}>")
            
            # Close Process
            sys.exit()

        # Create - Load
        if (self.type == 'load'):
                
            stub_file = os.path.join(os.path.dirname(__file__), '../Stubs/Load.stub')
            load_file = os.path.join(os.path.dirname(__file__), f"../../app/ETL/Load/{self.name}.py")
            
            # Check if File Already Exists
            if os.path.exists(load_file):
                Console.danger(f"The Load to create already exists: {load_file}")
                sys.exit()

            # Open Stub File
            with open(stub_file, 'r') as f:
                content = f.read()

            # Apply Load Name
            output = content.replace('{{file-name}}', self.name)

            # Create New File
            with open(load_file, 'w') as f:
                f.write(output)

            # Console Alert
            Console.success(f"Load created successfully: {load_file}")
            
            # Log Registration
            Logger().info(f"Maker CLI Class: Create File <{load_file}>")
            
            # Close Process
            sys.exit()
        
        # Create - Sender
        if (self.type == 'sender'):
                
            stub_file = os.path.join(os.path.dirname(__file__), '../Stubs/Sender.stub')
            sender_file = os.path.join(os.path.dirname(__file__), f"../../app/Mail/Senders/{self.name}.py")
            
            # Check if File Already Exists
            if os.path.exists(sender_file):
                Console.danger(f"The Sender to create already exists: {sender_file}")
                sys.exit()

            # Open Stub File
            with open(stub_file, 'r') as f:
                content = f.read()

            # Apply Load Name
            output = content.replace('{{file-name}}', self.name)

            # Create New File
            with open(sender_file, 'w') as f:
                f.write(output)

            # Console Alert
            Console.success(f"Sender created successfully: {sender_file}")
            
            # Log Registration
            Logger().info(f"Maker CLI Class: Create File <{sender_file}>")
            
            # Close Process
            sys.exit()
        
        Console.danger("The type of file to be created is not a framework standard, check that the type of file to be created is written correctly.")