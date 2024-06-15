import boto3
import json


def lambda_handler(event, context):

    email = event.get("email")
    password = event.get("password")
    username = event.get("userName")

    client = boto3.client("cognito-idp")

    response = client.sign_up(
        ClientId='4pnr3uhqa32fnjhrqoc4lqob0n',
        Username=username,
        Password=password,
        UserAttributes=[
            {
                'Name': 'email',
                'Value': email

            }
        ],
    )

    print(response)
