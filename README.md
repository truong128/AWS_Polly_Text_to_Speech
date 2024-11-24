# AWS_Polly_Text_to_Speech
This code snippet is used to generate the "Speech" from "Text" using AWS Polly services.

# GenAI_AWS_Polly
This code snippet is used to generate the "Speech" from "Text" using AWS Polly services.
# Here is the step-by-step to run
## Step 1: Create an AWS account
## Step 2: Prepare any input "Text"
## Step 3: Run on AWS CLI or API (need AWS configure if running API from local machine)
## Step 4: Run the Python script above

# Troubleshooting: If you encounter any errors related to permissions or models, you need to go to your account to set them up.
## 1. Go to the AWS Management Console
## 2. Search for "IAM" and go to the IAM service
## 3. Click on "Users" in the left sidebar
## 4. Find and click on your user "your IAM user"
## 5. Click on "Add permissions" button
## 6. Choose "Attach existing policies directly"
## 7. In the search box, type "Polly"
## 8. Look for and select AmazonPollyFullAccess
## 9. Click "Next" and then "Add permissions"

# -> Alternatively, if you prefer using AWS CLI (AWS console), you can run:
aws iam attach-user-policy \
    --user-name aws.ai.ml.truongnguyen_01 \
    --policy-arn arn:aws:iam::aws:policy/AmazonPollyFullAccess
