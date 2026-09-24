import json
import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_key = event["Records"][0]["s3"]["object"]["key"]

    response = s3.get_object(
        Bucket=bucket_name,
        Key=file_key
    )

    file_data = json.loads(response["Body"].read())

    valid_requests = []

    for request in file_data["requests"]:
        if (
            request.get("requestId")
            and request.get("customerName")
            and request.get("requestType")
            and request.get("createdAt")
        ):
            valid_requests.append(request)
        else:
            print(f"Invalid request: {request}")

    output = {
        "sourceFile": file_key,
        "requests": valid_requests
    }

    output_key = file_key.replace("incoming/", "processed/")

    s3.put_object(
        Bucket=bucket_name,
        Key=output_key,
        Body=json.dumps(output, indent=2),
        ContentType="application/json"
    )

    print(f"Processed {len(file_data['requests'])} requests.")
    print(f"Valid requests: {len(valid_requests)}")
    print(
        f"Invalid requests: "
        f"{len(file_data['requests']) - len(valid_requests)}"
    )

    return {
        "statusCode": 200,
        "body": "Processing complete"
    }