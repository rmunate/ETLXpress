#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Facade ETL Extract                                      #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
from core.Clarity.Logger import Logger
from core.Notify.Email import Email

# Facade Extract execution
class Mail:
    
    # ----------------------------------------------------------------------------------------------------#
    # Execute Command Without Reponse                                                                     #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self, email):
        
        # Log Registration
        Logger().info(f"Email Class Executed: {email.__class__.__name__}")
        
        # Create an instance of the email class
        notify = Email()
        
        # Set the email subject
        eSubject = email.subject()
        notify.subject(eSubject)
        
        # Set the email recipients
        eTo = email.to()
        notify.to(eTo)
        
        # Define the body type
        eBody = email.body()
        if eBody['type'] == "html":
            notify.template(eBody['template'], eBody.get('replacements', {}))
        else:
            notify.textPlain(eBody['template'])
        
        # Add attachments
        eFiles = email.attachments()
        for file in eFiles:
            notify.file(file)
        
        # Send Email
        self.data = notify.send()
    
    # ----------------------------------------------------------------------------------------------------#
    # Response of email sending                                                                           #
    # ----------------------------------------------------------------------------------------------------#
    def response(self):
        return self.data
        