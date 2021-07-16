import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    data = json.loads(event["Records"][0]["body"])
    s3.put_object(Bucket = "sns-to-sqs-to-lambda-to-s3", Key = "data.json", Body = json.dumps(data))

    return {
        'statusCode' : 200,
        'body' : json.dumps('Hello from Lambda!')
    }
