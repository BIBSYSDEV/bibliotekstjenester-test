# Scripts for creating mock data for dynamoDB

This folder contains scripts for generating correctly formatted json to write items batch job.
As no better mock data exists than actual data, this is based on importing actual data from production database.
Known issue: does not handle øæå in csv files.


## Requirements for running scripts:
- python 3.9.7
#### IAM policy roles needed by AWS:
- dynamoDB:BatchWriteItem
- dynamoDB:CreateTable
- dynamoDB:DeleteTable
- dynamodb:DescribeTable

### Format required by AWS
See documentation https://docs.aws.amazon.com/cli/latest/reference/dynamodb/batch-write-item.html
```json
{
  "your_table_name": [
    {
      "PutRequest": {
        "Item": {
          "your_attribute_key_1": {"S": "your_attribute_value_1"},
          "your_attribute_key_2": {"S": "your_attribute_value_2"}
        }
      }
    }
  ]
}
```
Note that a single batch job can only handle up to 25 "PutReqest" at a single call


## Generating prepped json file compatible with write batch format:
1. In the aws dynamoDB console select the items you want to download to csv.
   Care should be given not to expose sensitive user data when selecting items, or you can sensor data manually after downloading.
2. Run the script prep_data_for_dynamo_db.py with specified input-, output- filename, and table_name


## create database, run tests, and tear down database in buildspec:
Requires prepared json to be ready.
1. Create database and prepopulate it with data:
```shell
   if [[ $(aws dynamodb create-table --table-name contents --attribute-definitions AttributeName=isbn,AttributeType=S --key-schema AttributeName=isbn,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1) ]]; then echo "created table contents"; fi
```
the AWS create-table may fail if the table already exists, hence the command is wrapped inside if-statement in order to ignore if the table already exists.
```shell
   aws dynamodb batch-write-item --request-items file://prepped.json
   ```
2. Run tests
3. Tear down database:
  ```shell
  aws dynamodb delete-table --table-name your_table_name
  ```
Note: According to AWS documentation: deleting table takes 2-4 minutes.
