import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC2d9b8d775c96813a62abded01b5c5120'
auth_token = '36962f21e324450d02699507007ceba3'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say voice="alice">Hiii Surucha arora, you are my love darling. </Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        to='+919466735758',
                        from_='+12564154635'
                    )
                    #
                                                                                                    
print(call.sid)
