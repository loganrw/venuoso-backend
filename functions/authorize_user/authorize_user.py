import boto3
import json


def lambda_handler(event, context):

    username = event.get("userName")
    confirmCode = event.get("confirmCode")

    client = boto3.client("cognito-idp")

    response = client.confirm_sign_up(
        ClientId="4pnr3uhqa32fnjhrqoc4lqob0n",
        Username=username,
        ConfirmationCode=confirmCode,
    )

    print(response)
