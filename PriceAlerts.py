#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
from binance.client import Client
import time

api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)


# In[13]:


from twilio.rest import Client as TwilioClient

account_sid = "AC66d397d7665c4861cb98fb77dbcae46f"
auth_token  = "08142509162c9c54bd89f936740023b8"

twilioclient = TwilioClient(account_sid, auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+6591796311'


# In[21]:


lunatarget = 35
atomtarget = 36.6

while True:
    Luna = client.get_symbol_ticker(symbol="LUNABUSD")
    lunapx = float(Luna['price'])
    lumamsg = "Luna: "+str(lunapx)
    
    Atom = client.get_symbol_ticker(symbol="ATOMBUSD")
    atompx = float(Atom['price'])
    atommsg = "Atom: "+str(atompx)
    
    if lunapx < lunatarget:
        twilioclient.messages.create(body= lumamsg, from_ = from_whatsapp_number, to = to_whatsapp_number)

    if atompx < atomtarget:
        twilioclient.messages.create(body= atommsg, from_ = from_whatsapp_number, to = to_whatsapp_number)
        
    
    time.sleep(120)
    
    

