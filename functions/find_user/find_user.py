import boto3
import json


def lambda_handler(event, context):

    email = event.get("email")

    client = boto3.client("cognito-idp")

    response = client.list_users(
        UserPoolId="us-east-1_Pthgjauzw",
        Limit=10,
        Filter='email = "' + email + '"',
    )

    return json.dumps(response, default=str)
