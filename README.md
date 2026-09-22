# Assignment 2: Yarrow-Mullein Bank Event-Driven Ingestion Pipeline

## Student Information

- **Name:**
- **Date completed:**
- **GitHub repository URL:**

## Architecture Diagram

<!-- Insert your diagram showing the S3 upload event, Lambda function, and processed S3 output. -->

Your diagram should show `incoming/` as the input prefix, `processed/` as the output prefix, the `ObjectCreated` event, and CloudWatch logging.

## Implementation Summary

Briefly explain how your pipeline validates Yarrow-Mullein Bank customer service requests and writes processed output.

<!-- Your summary. -->

## Required Evidence

### S3 Bucket and Prefixes

<!-- Add evidence of the private bucket and incoming/ and processed/ prefixes. -->

### Lambda Function and Permissions

<!-- Add evidence of function configuration, source code, and the pre-configured LabRole attachment. Discuss least-privilege permissions in Reflection Questions 3 and 5; do not claim LabRole is least privilege. -->

### S3 Trigger

<!-- Add evidence that only incoming/ JSON uploads trigger the function. -->

### Valid Request Processing

<!-- Add evidence of input data and processed output for at least eight valid service requests. -->

### Invalid Request Handling

<!-- Add evidence that at least two invalid requests are logged while valid requests are processed. -->

### JSON Data Shape

<!-- Add or describe your valid and invalid JSON files. Together they must contain at least 10 unique request objects. -->

### Negative Trigger Tests

<!-- Add evidence or an explanation for an object outside incoming/, a non-JSON object, and the processed output not retriggering the function. -->

## Reflection Questions

### 1. What event causes the Lambda function to run?

<!-- Your answer. -->

### 2. Why should the function validate a customer service request before creating the processed output?

<!-- Your answer. -->

### 3. What S3 and CloudWatch permissions does the Lambda execution role require, and why?

<!-- Your answer. -->

### 4. How would you prevent the Lambda function from being triggered by its own output files?

<!-- Your answer. -->

### 5. If you were deploying outside AWS Academy, how would you scope the Lambda permissions to only the `incoming/` and `processed/` prefixes?

<!-- Your answer should identify S3 read/write actions and resources, CloudWatch Logs permissions, and prefix-scoped ARNs. -->
