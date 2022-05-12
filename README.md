# DeadMansSwitch
*Guide on setting up an uptime monitoring/alert system.*

Why would you want this? If the program your running is sensitive and you need an alert when it either:\
A. Crashes, B. Computer restarts/loses power, C. Loses internet

The solution is simple, a C# program (or any program you want) updates a timestamp in a file on AWS S3.\
Then a Lambda Function written in Python gets triggered by AWS EventBridge every X mins.\
If the Lambda detects the timeStamp in the file is older then X minutes it means the program has not been reporting in.
When the Lambda detects there has not been a file update in X mins, it then sends an email to you alerting you your program has gone offline/disconnected/computer restarted etc.

Tools used:\
Free Tier of AWS, C#, Python

Provided is the python script to be run in the Lambda Function, and the C# function that I am using.

Also listing some links that could be helpful for this project, if you are new to AWS/Lambda/EventBridge/GoogleAppPassword.

### Links:
- Setting up event schedular on AWS using EventBride https://www.youtube.com/watch?v=uUhEKtLrGvo 
- Setting up a Lambda Function on AWS https://www.youtube.com/watch?v=0jsty3XKQYI
- Setting up a Gmail App Password https://support.google.com/accounts/answer/185833?hl=en
- Setting up Amazon SDK for C# https://aws.amazon.com/sdk-for-net/
