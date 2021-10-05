import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say voice="alice">hello</Say><</Response>',
                        to='+91XXXXXX',
                        from_='+XXXXXXXXXXXXX'
                    )
                    #
                                                                                                    
print(call.sid)
