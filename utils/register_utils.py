"""
Module for utility functions related to user registration.
"""

def email_verified_success_html(link):
    """
    Generates the HTML content for the email verification success page.
    
    Args:
        link (str): The URL to the login page.
    
    Returns:
        str: The HTML content for the email verification success page.
    """
    html_head = """
<!DOCTYPE html>
<html>
<head>
    <title>Email Confirmed</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }
        .container {
            padding: 50px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .heading {
            font-size: 24px;
            color: #333333;
            margin-bottom: 20px;
        }
        .message {
            font-size: 18px;
            color: #555555;
            margin-bottom: 30px;
        }
        .button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
"""
    html_body = f"""
    <body>
    <div class="container">
        <div class="logo">
            <img src="https://www.bluetickconsultants.com/images/bluetick-consultants.png" alt="Company Logo" width="150">
        </div>
        <br/><br/>
        <div class="heading">Email Successfully Verified</div>
        <div class="message">Thank you for verifying your email. You're now ready to start using BluetickPDF.</div>
        <a href="{link}" class="button">Log In and Get Started</a>
    </div>
    </body>
</html>  
    """

    return html_head + html_body

def create_verification_email_body(link):
    """
    Generates the HTML content for the email verification email.
    
    Args:
        link (str): The URL to the email verification endpoint.
    
    Returns:
        str: The HTML content for the email verification email.
    """
    html_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Email Verification</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
  }
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  }
  .logo {
    display: block;
    margin: 20px auto;
    text-align: center;
  }
  .button-container {
    text-align: center;
    margin-top: 30px;
  }
  .verify-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007bff;
    color: #ffffff !important;
    text-decoration: none;
    border-radius: 5px;
  }
  .footer {
    text-align: center;
    margin-top: 20px;
    font-size: 12px;
    color: #999999;
  }
</style>
</head>'''
    html_body = f'''
<body>
  <div class="container">
    <div class="logo">
      <img src="https://www.bluetickconsultants.com/images/bluetick-consultants.png" alt="Company Logo" width="150">
    </div>
    <h2>Email Verification</h2>
    <p>Dear user,</p>
    <p>Thank you for registering with BluetickPDF. </p>
    <p>To complete the registration process, please click the "Verify Email" button below:</p>
    <div class="button-container">
      <a href={link} class="verify-button">Verify Email</a>
    </div>
  </div>
  <div class="footer">
    Bluetick Consulatants LLP &bull; Bangalore, India &bull;  <a href="https://www.bluetickconsultants.com">www.bluetickconsultants.com</a>
  </div>
</body>
</html>
'''
    
    return html_head + html_body
