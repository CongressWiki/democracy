# AWS Automation

Stand up the physical layer of this application on AWS.

## :rocket: Quick Start

1. Install Python packages

  ```shell
  pyton3 -m pip install -r requirements.txt
  ```

2. Deploy resources on AWS

  ```shell
  python3 -m setup
  ```

## Deploy AWS

1. Create base stack

```shell
aws cloudformation create-stack --stack-name Democracy-BaseStack --template-body file://cloudformation-templates/vpc-stack.yml --parameters file://cloudformation-templates/vpc-params.json
```

2. Copy base stack output values into the `cloudformation-templates/*-config.json` files

3. Create deploy pipeline

```shell
aws cloudformation create-stack --stack-name Democracy-CodePipeline --template-body file://codepipeline-cfn-codebuild.yml --parameters file://codepipeline-cfn-codebuild.json --capabilities CAPABILITY_NAMED_IAM
```

## TODO

- [ ] Automate deployment of backend (EC2 for python migration)
- [ ] Automate deployment of Lambdas to invoke python migrations
- [ ] Automate deployment of S3 bucket for bill migration data
- [ ] Automate deployment of front end
