# DeadMansSwitch
*Guide on setting up an uptime monitoring/alert system.*

Why would you want this? If the program your running is sensitive and you need an alert when it either:\
A. Crashes, B. Computer restarts/loses power, C. Loses internet

The solution is simple, a C# program (or any program you want) sends heartbeats to AWS.\
If heartbeats stop coming in after X minutes then an email is sent to you.

Tools used:\
Free Tier of AWS, C#, Python

Provided is the python script to be run in the Lambda Function, and the C# function that I am using.

Also listing some videos that could be helpful for this project, if you are new to AWS/Lambda/EventBridge.

### Links:
- Setting up event schedular on AWS using EventBride https://www.youtube.com/watch?v=uUhEKtLrGvo 
- Setting up a Lambda Function on AWS https://www.youtube.com/watch?v=0jsty3XKQYI
- Setting up a Gmail App Password https://support.google.com/accounts/answer/185833?hl=en
- Setting up Amazon SDK for C# https://aws.amazon.com/sdk-for-net/
