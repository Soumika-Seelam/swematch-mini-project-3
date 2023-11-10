import json
import boto3

def lambda_handler(event, context):
    # Initialize AWS Comprehend client
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

    # Assuming the body is JSON and it's a string, it needs to be parsed
    if isinstance(event['body'], str):
        body = json.loads(event['body'])
        text_to_analyze = body.get('text')
    else:
        text_to_analyze = event['body'].get('text')  # If the body is already a dict

    # Perform sentiment analysis
    response = comprehend.detect_sentiment(Text=text_to_analyze, LanguageCode='en')

    # Construct the response with the sentiment analysis result
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Adjust as needed for production
        },
        'body': json.dumps({
            'sentiment': response['Sentiment'],
            'sentimentScore': response['SentimentScore']
        })
    }
