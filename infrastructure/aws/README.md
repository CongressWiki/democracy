# AWS Automation

Stand up layers 1-5 of the Democracy application on AWS.

## :rocket: Quick Start

1. Create VPC base stack

```shell
aws cloudformation create-stack --stack-name Democracy-Test-VPC --template-body file://base-stack/vpc.yml --capabilities CAPABILITY_NAMED_IAM
```

2. Create PostgreSQL Database for each environment [Test, UAT, Production]

```shell
# Test
aws cloudformation create-stack --stack-name Democracy-Test-VPC --template-body file://database/postgresql.yml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=EnvironmentName,ParameterValue=test

# UAT
aws cloudformation create-stack --stack-name Democracy-UAT-VPC --template-body file://database/postgresql.yml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=EnvironmentName,ParameterValue=uat

# Production
aws cloudformation create-stack --stack-name Democracy-Prod-VPC --template-body file://database/postgresql.yml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=EnvironmentName,ParameterValue=prod
```

3. Create codepipeline

```shell
aws cloudformation create-stack --stack-name Democracy-CodePipeline --template-body file://development/codepipeline.yml --capabilities CAPABILITY_NAMED_IAM
```

## TODO

- [ ] Automate deployment of backend (EC2 for python migration)
- [ ] Automate deployment of Lambdas to invoke python migrations
- [ ] Automate deployment of S3 bucket for bill migration data
- [ ] Automate deployment of front end
