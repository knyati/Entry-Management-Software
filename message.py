def vmessage(body,vphone):
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'AC6247dc46c20b404b8d9dd8a2f30accb5'
    auth_token = 'b1e36783788f71b90642060f42050b77'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='+919119388593',
                                body =body,
                                to = str(vphone)
                            )

    print("Message sent to the visitor")
    return 0

def hmessage(body,hphone):
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'AC6247dc46c20b404b8d9dd8a2f30accb5'
    auth_token = 'b1e36783788f71b90642060f42050b77'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_='+18593401868',
                                body = body,
                                to = '+919119388593'
                            )

    print("Message sent to the Host")
    return 0

