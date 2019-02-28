EMAIL_TEMPLATE = """
<html><body>
Dear <b>{name}</b>,
<p>
Thanks for registration your application has been pending for approval. But you can still able to login and update your profile and business information. Below are your login Detail
</p>
<p>Username : {email}<br/>
Password : {password}
</p>
<p>
Kindly find below detail for your service.
</p>
ExampleCo Listing - 1 Year/s (06/03/2019 - 05/03/2020) Rs. 1400<br/>
------------------------------------------------------<br/>
Sub Total: Rs. 1400<br/>
Credit: Rs. 0.00<br/>
Total: Rs. 1400<br/>
------------------------------------------------------<br/>
</p>
<p>
Payment Method<br/>
Wire Transfer/NEFT : You can Wire Transfer funds to the following account:<br/>
<br/>
Bank Name - ICICI<br/>
Name - Technologies Pvt. Ltd.<br/>
Account Type - Current<br/>
A/c No - 084305000654<br/>
IFSC - ICIC0000843
</p>
<p>
Online Payment Link :  <a href="https://payments.example.com/pay/EXAMPLE">Click here</a> or copy below link and paste it in your browser<br/>
  https://payments.example.com/pay/EXAMPLE
</p>
Please let us know with transaction id so that we can notify your payment and list your business in ExampleCo. Please feel free to ask if you have any query regarding this.
<p>
ExampleCo Team<br/>
Support No : 0000000000<br/>
Email : info@example.com<br/>
Web : https://www.example.com<br/>
Example Pvt. Ltd<br/><br/>
<img src='https://www.example.com/static/mail_logo/logo.png' />
</p>
</body></html>
"""
replace_dict = {"name":"Surendra shukla", "email":"","password":""}
print(EMAIL_TEMPLATE.format(**replace_dict))