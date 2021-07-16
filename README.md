# CloudFormation
Cloudformation template

The template for Cloudformation creates A SNS Topic, subscription to the topic whose endpoint is a SQS queue, a Lambda function which gets triggered when a message is available in the queue. The data of the message is then saved to a s3 bucket.
