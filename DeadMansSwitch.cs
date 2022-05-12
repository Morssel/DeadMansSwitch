using System;
using System.Threading
using Amazon;
using Amazon.Auth;
using Amazon.Runtime;
using Amazon.S3;
using Amazon.Util;
using Amazon.S3.Model;

namespace DeadMansSwitch
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            // Link to better/different ways of triggering a func every x mins
            //https://stackoverflow.com/questions/13019433/calling-a-method-every-x-minutes
            while (true)
            {
                UpdateDeadMansSwitch();
                Thread.Sleep(5000); // 5 Seconds
            }
        }

        public static async void UpdateDeadMansSwitch()
        {
            IAmazonS3 client = new AmazonS3Client("accessKeyID", "SecretAccessKey", RegionEndpoint.USEast1);
            String timeStamp = "";
            
            var utcTime = DateTime.UtcNow; // 2022-01-13T16:25:35

            string timeString = utcTime.ToString("s");
            
            var putRequest = new PutObjectRequest
            {
                BucketName = "deadmansbucket",
                Key = "DeadMansSwtichFile.txt",
                ContentBody = timeString
            };

            Console.WriteLine("Attempting to upload utc time to S3: " + timeString);

            try
            {
                var response = await client.PutObjectAsync(putRequest);
                Console.WriteLine("response2.HttpStatusCode " + response.HttpStatusCode);
            }
            catch
            {
                Console.WriteLine("Failed PutObjectAsync()");
            }
        }

    }
}
