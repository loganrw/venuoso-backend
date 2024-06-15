import boto3
import json


def lambda_handler(event, context):

    first_name = event.get("firstName")
    last_name = event.get("lastName")
    email = event.get("email")
    password = event.get("password")

    client = boto3.client("cognito-idp")

    response = client.sign_up(
        '6gaiajd80v2srhhs1jcj2v8dmc',
        Username=email,
        Password=password,
        UserAttributes=[
            {
                'Name': 'email',
                'Value': email

            },
            {
                'Name': 'custom:first_name',
                'Value': first_name
            },
            {
                'Name': 'custom:last_name',
                'Value': last_name
            }
        ],
    )

    print(response)
