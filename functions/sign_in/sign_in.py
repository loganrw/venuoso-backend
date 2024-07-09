import boto3
import json


def lambda_handler(event, context):
    password = event.get("password")
    username = event.get("userName")

    client = boto3.client("cognito-idp")

    response = client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"username": username, "password": password},
        ClientId="4pnr3uhqa32fnjhrqoc4lqob0n",
    )

    return response
