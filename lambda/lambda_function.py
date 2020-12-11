#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import base64
import boto3


def lambda_handler(event, context):
    chestxrayimage = event["xrayimage"]
    decoded_xrayimage = base64.b64decode(chestxrayimage)
    return predictCovid19(decoded_xrayimage)


def predictCovid19(image):
    client = boto3.client("sagemaker-runtime")
    try:
        response = client.invoke_endpoint(
            EndpointName="FinalEndpoint",
            ContentType="application/octet-stream",
            Body=image,
        )
        result = response["Body"].read()
        result = json.loads(result)
        maxResult = result.index(max(result))
        if maxResult == 0:
            responseMessage = "Detected Normal"
        elif maxResult == 1:
            responseMessage = "Detected Covid-19"
        elif maxResult == 2:
            responseMessage = "Detected Viral"
        else:
            responseMessage = "Not able to determine"

    except client.exceptions.ModelError as e:
        responseMessage = "Not able to determine"

    return {"statusCode": 200, "body": json.dumps(responseMessage)}
