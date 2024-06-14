import boto3

client = boto3.client("cognito-idp")


response = client.admin_create_user(
    UserPoolId="string",
    Username="string",
    UserAttributes=[
        {"Name": "string", "Value": "string"},
    ],
    ValidationData=[
        {"Name": "string", "Value": "string"},
    ],
    TemporaryPassword="string",
    ForceAliasCreation=True | False,
    MessageAction="RESEND" | "SUPPRESS",
    DesiredDeliveryMediums=[
        "EMAIL",
    ],
    ClientMetadata={"string": "string"},
)
