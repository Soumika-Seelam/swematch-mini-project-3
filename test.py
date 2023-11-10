import boto3
import json

def lambda_handler(event, context):
    comprehend = boto3.client(service_name="comprehend", region_name="us-east-2")

    text = """
        I love my new clothes!
    """

    comprehend_json_obj = comprehend.detect_sentiment(Text = text, LanguageCode='en')

    json_text = json.dumps(comprehend_json_obj, indent=4)
    print("json_text:", json_text)

    sentiment = comprehend_json_obj['Sentiment']

    return f"sentiment: {sentiment}"

