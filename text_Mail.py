import os
from datetime import datetime

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.Subject = 'Service XYZ has planned maintenance'
mail.To = "solomon.paul.kancharla@sap.com"

mail.HTMLBody = r"""
Dear Colleague,<br><br>
Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET
<br><br>
Thanks & Regards,
<br><br>
Team XYZ
"""
mail.Send()
