# iag-devops-work-problem2

## Prerequisities install aws-sam-cli & aws-cli (mandatory) 

## 1. Create bucket to upload sam package file:
$ aws s3 mb  s3://pdf-extension-check-2c5ade5af868-ap-southeast-2 --region ap-southeast-2
$ aws s3 mb  s3://pdf-extension-check-2c5ade5af868-ap-southeast-2-timestamp --region ap-southeast-2


## sam build
$ sam build

## 2. sam package file and upload to s3 bucket as artefacts
$ sam package package \
    --s3-bucket "pdf-extension-check-2c5ade5af868-ap-southeast-2" \
    --output-template-file output.yaml

## 3. sam deploy lambda function which will run every minutes to show the status which you would be able to see the corresponding Cloudwatch log file: 
$ aws cloudformation deploy --template-file $(pwd)/output.yaml \
    --stack-name pdf-extension-check \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND