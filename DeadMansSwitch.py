from datetime import datetime, timedelta
import smtplib
import boto3

bucket = 'yourBucketName'
key = 'DeadMansSwitchFile.txt'
timedeltathreshold = 11


def lambda_handler(event, context):
    print("Starting DeadMansSwitch Func")
    # Get File
    s3 = boto3.client('s3')

    response = s3.get_object(Bucket=bucket, Key=key)

    content = response["Body"].read().decode('utf-8')

    print("File contents: " + content)

    # Process File
    try:
        filedate = datetime.fromisoformat(content)
    except Exception as e:
        print("Error: ", str(e))
        return "Error can't process string into DateTime"

    if (datetime.utcnow() - filedate) > timedelta(minutes=timedeltathreshold):
        print("MORE then " + timedeltathreshold + " minutes have passed, email sent")
        send_email()
    else:
        print("LESS then " + timedeltathreshold + " minutes have passed")

    return "200 Lambda Complete"


def send_email():
    email_address = "yourEmail@gmail.com"
    subject = "Dead Man's Switch: Program Went Offline"
    body = "Dead Man's Switch was triggered for Program"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, "yourGoogleAppPasswordHere")
        server.sendmail("email_address", email_address, "Subject: {}\n\n{}".format(subject, body))

        # If an email was sent then replace the file contents with `empty`
        #   so no more emails are generated until computer makes a new heartbeat
        s3_resource = boto3.resource('s3')
        s3_resource.Bucket(bucket).put_object(Key=key, Body="Empty")
    except Exception as e:
        print("Error: ", str(e))
        return "Error can't process server gmail request"
    finally:
        if server is not None:
            server.quit()
