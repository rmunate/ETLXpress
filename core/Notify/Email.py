#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#----------------------------------------------#
# Email Sending                               #
#----------------------------------------------#

import os
import smtplib
from os.path import abspath, join, dirname
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from core.Clarity.File import File
from core.Environment.Env import Env
from core.Clarity.Logger import Logger

class Email:
    
    # Initialize email sending class.
    def __init__(self, subject='Notification ETLXpress'):
        
        # Log Registration
        Logger().info(f"Email Class: Initialized")
        
        self.subjectEmail = subject
        self.toAddresses = None
        self.html = None
        self.text = None
        self.attachments = []
        
        # Define connection data
        self.server = Env.get("MAIL_HOST")
        self.port = Env.get("MAIL_PORT")
        self.username = Env.get("MAIL_USERNAME")
        self.password = Env.get("MAIL_PASSWORD")
        self.fromAddress = Env.get("MAIL_FROM_ADDRESS")
    
    
    # Set email subject
    def subject(self, subject):
        
        # Log Registration
        Logger().info(f"Email Class: Subject <{subject}>")
        
        #Subject
        self.subjectEmail = subject
    
    # Email recipients
    def to(self, to):
        
        # Log Registration
        Logger().info(f"Email Class: Subject <{to}>")
        
        # To
        self.toAddresses = to
    
    # HTML Template
    def template(self, templateHTML, replaces={}):
        template_path = os.path.join(os.path.dirname(__file__), f"../../app/Mail/Templates/{templateHTML}.html")
        
        if os.path.exists(template_path):
            
            # Log Registration
            Logger().info(f"Email Class: Template <{template_path}>")
        
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
                
                for search, replace in replaces.items():
                    template_content = template_content.replace(search, replace)
                    
            self.html = template_content
        else:
            raise FileNotFoundError(f"Template Mail '{templateHTML}' Not Found")

    # Plain Text without template
    def textPlain(self, text):
        
        # Log Registration
        Logger().info(f"Email Class: Text Plain <{text}>")
        
        # Text
        self.text = text
    
    # Attach File
    def file(self, file):
        file = os.path.join(os.path.dirname(__file__), f"{File.path()}/{file}")
        if os.path.exists(file):
            
            # Log Registration
            Logger().info(f"Email Class: Add File <{file}>")
            
            self.attachments.append(file)
        else:
            raise FileNotFoundError("File Not Found")
    
    # Send email
    def send(self):
        email = MIMEMultipart()
        email["From"] = self.fromAddress
        email["To"] = ", ".join(self.toAddresses)
        email["Subject"] = self.subjectEmail
        
        if self.html is not None and self.html != '':
            email.attach(MIMEText(self.html, "html", "utf-8"))
        else:
            email.attach(MIMEText(self.text, "plain", "utf-8"))
            
        for archivo in self.attachments:
            nombre_adjunto = os.path.basename(archivo)

            parte_adjunta = MIMEBase("application", "octet-stream")
            parte_adjunta.set_payload(open(archivo, "rb").read())
            encoders.encode_base64(parte_adjunta)
            parte_adjunta.add_header("Content-Disposition", f"attachment; filename= {nombre_adjunto}")
            email.attach(parte_adjunta)

        with smtplib.SMTP(self.server, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(email)
            
        # Log Registration
        Logger().info(f"Email Class: Send")
