import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class Emails:
    @staticmethod
    def registration_email(recipient, firstName, lastName, accountType):

        sender_email = "gowerstsurgery.adm@gmail.com"
        admin = sender_email
        password = "19_Healthcare_97"

        rec = recipient

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Registration Confirmation"
        msg['From'] = admin
        msg['To'] = rec

        # Create the body of the message.
        text = "Hi " + firstName + " " + lastName + " thank you for registering with Gower St. Surgery" \
               "the e-health management service.\n \n Your account has been successfully set up with " + accountType \
               + " " \
               "priviledges. You can 1. Login \n 2. Book appointments \n 3. Reschedule appointments \n" \
               "4. Cancel appointments \n 5. Book a session with one of our external specialists \n" \
               " \n \n Log back into the application begin </p>\n "

        html = """\
        <html lang="en">
        <head>
            <meta http-equiv="content-type" content="text/html; charset=UTF-8">
            <title>Register as a new patient/GP</title>
        </head>
        <body bgcolor="#EBEBEB" link="#B64926" vlink="#FFB03B">
        <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#EBEBEB">
        <tr>
        <td>
        <table width="600" align="center" border="0" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF">
        <tr>
        <td style="padding-top: 0.5em">
        <h1 style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #0E618C; text-align:
        center">Welcome to Gower St. Surgery<br>--e-health management service--<br></h1>
        </td>
        </tr>
        <tr>
        <td align="center">
        <img src="cid:image1" alt="Logo" style="width:225px;height:200px;"><br>
        </td>
        </tr>
        <tr>
        <td style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #1B1B1B;
         font-size: 14px; padding: 1em">
        </td>
        </tr>
        <tr>
        <td style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #1b1b1b; 
        font-size: 14px; padding: 1em">
        <p>Hi <b>""" + str(firstName) + """  """ + str(lastName) + """</b>, thank you for registering with Gower St. Surgery,
        the e-health management service. <br><br>
        Your account has been successfully set up with <b>""" + str(accountType) + """</b> privileges. You can: <br><br>
        1. Login <br>
        2. Book appointments <br>
        3. Reschedule/cancel appointments <br>
        4. Book a session with one of our external specialists <br>
        5. View your prescriptions and medical history <br><br> Log back into the application to begin </p>
        </td>
        </tr>
        </table>
        </td>
        </tr>
        </table>
        </body>
        </html>
        """

        #text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container
        msg.attach(part1)
        msg.attach(part2)

        fp = open('logo.png', 'rb')
        msgimage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID
        msgimage.add_header('Content-ID', '<image1>')
        msg.attach(msgimage)

        # Send the message
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email, password)
        mail.sendmail(admin, rec, msg.as_string())
        mail.quit()

    @staticmethod
    def appointment_summary_email(recipient, patient_name, appointment_summary_plain, appointment_summary_html):
        sender_email = "gowerstsurgery.adm@gmail.com"
        admin = sender_email
        password = "19_Healthcare_97"

        rec = recipient

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Appointment Summary"
        msg['From'] = admin
        msg['To'] = rec

        # Create the body of the message.
        text = appointment_summary_plain

        html = f"""\
        <html lang="en">
        <table border="0" width="100%" cellspacing="0" cellpadding="0" bgcolor="#EBEBEB">
        <tbody>
        <tr>
        <td>
        <table border="0" width="600" cellspacing="0" cellpadding="0" align="center" bgcolor="#FFFFFF">
        <tbody>
        <tr>
        <td style="padding-top: 0.5em;">
        <h1 style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #0e618c; text-align: center;">Gower St. Surgery<br />--e-health management service--</h1>
        </td>
        </tr>
        <tr>
        <td align="center"><img style="width: 225px; height: 200px;" src="cid:image1" alt="Logo" /></td>
        </tr>
        <tr>
        <td style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #1b1b1b; font-size: 14px; padding: 1em;">&nbsp;</td>
        </tr>
        <tr>
        <td style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #1b1b1b; font-size: 14px; padding: 1em;">
        <p>Hi <strong>{patient_name}</strong>, thank you for attending your 
        recent appointment with Gower St. Surgery, the e-health management service. <br /><br />We have included 
        below a summary of your appointment: <br /><br />{appointment_summary_html} <br /><br />We're here to help. Log back into the 
        application at any time to book another appointment.</p> </td> </tr> </tbody> </table> </td> </tr> </tbody> 
        </table> </html> """

        # text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container
        msg.attach(part1)
        msg.attach(part2)

        fp = open('logo.png', 'rb')
        msgimage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID
        msgimage.add_header('Content-ID', '<image1>')
        msg.attach(msgimage)

        # Send the message
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email, password)
        mail.sendmail(admin, rec, msg.as_string())
        mail.quit()

    @staticmethod
    def appointment_confirmation_email(recipient, patient_name, appointment_summary_plain, appointment_summary_html):
        sender_email = "gowerstsurgery.adm@gmail.com"
        admin = sender_email
        password = "19_Healthcare_97"

        rec = recipient

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Your appointment request"
        msg['From'] = admin
        msg['To'] = rec

        # Create the body of the message.
        text = appointment_summary_plain

        html = f"""\
            <html lang="en">
            <table border="0" width="100%" cellspacing="0" cellpadding="0" bgcolor="#EBEBEB">
            <tbody>
            <tr>
            <td>
            <table border="0" width="600" cellspacing="0" cellpadding="0" align="center" bgcolor="#FFFFFF">
            <tbody>
            <tr>
            <td style="padding-top: 0.5em;">
            <h1 style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #0e618c; text-align: center;">Gower St. Surgery<br />--e-health management service--</h1>
            </td>
            </tr>
            <tr>
            <td align="center"><img style="width: 225px; height: 200px;" src="cid:image1" alt="Logo" /></td>
            </tr>
            <tr>
            <td style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #1b1b1b; font-size: 14px; padding: 1em;">&nbsp;</td>
            </tr>
            <tr>
            <td style="font-family: 'Lucida Grande', 'Lucida Sans Unicode', Verdana, sans-serif; color: #1b1b1b; font-size: 14px; padding: 1em;">
            <p>Hi <strong>{patient_name}</strong>, we have some news about your recent appointment request. <br /><br />{appointment_summary_html} <br /><br />We're here to help. Log back into the 
            application at any time to book another appointment.</p> </td> </tr> </tbody> </table> </td> </tr> </tbody> 
            </table> </html> """

        # text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container
        msg.attach(part1)
        msg.attach(part2)

        fp = open('logo.png', 'rb')
        msgimage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID
        msgimage.add_header('Content-ID', '<image1>')
        msg.attach(msgimage)

        # Send the message
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email, password)
        mail.sendmail(admin, rec, msg.as_string())
        mail.quit()