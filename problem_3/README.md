# iag-devops-work-problem3

Website status check from: src/website-lists.json;
Adding more site into website-lists.json (follow json syntax)

## 1. Create bucket to upload sam package file:
$ aws s3 mb  s3://website-statuscheck-2c5ade5af868-ap-southeast-2 --region ap-southeast-2

## 2. Create package file and upload to s3 bucket as artefacts
$ aws cloudformation package --template-file template.yaml \
    --s3-bucket "website-statuscheck-2c5ade5af868-ap-southeast-2" \
    --output-template-file output.yaml

## 3. Deploy lambda function which will run every minutes to show the status which you would be able to see the corresponding Cloudwatch log file: 
$ aws cloudformation deploy --template-file $(pwd)/output.yaml \
    --stack-name sam-lambda-deploy-problem3 \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND