#AWS Project - Architect and Build an End-to-End AWS Web Application from Scratch, Step by Step

(YouTube Tutorial)[https://www.youtube.com/watch?v=7m_q1ldzw0U&list=WL&index=43&t=161s]


## Goals:
- Create a to host a webpage
- Invoke the math functionality
- Do some math
- Store the math result
- Handle permissions


## Pre-requisites
- Create a new AWS account with IAM user
- Install the AWS CLI and setup the toolkit in VSCode


## Create a webpage
- Create an `index_original.html` file and zip it
- Open the AWS console and search for `Amplify`
- Select `Host your web app`
- Deploy without git provider
- Upload the zip file
- Name the app
- Enter `dev` for the environment name
- Upload the zip file


## Do some math
- Open up `Lambda` in the AWS console
- Create a new function
- Select `Author from scratch`
- Name the function
- Select `Python 3.9` as the runtime
- Everything else is default, then create function
- Scroll down to the `Code Source` section
- Copy the code from `PowerOfMathFunction - Lambda.py` into the editor
- Test the function
- - Create a new event
- - Name it `PowerOfMathTestEvent`
- - update the dictionary at the bottom to use `base` and `exponent` as the keys and then assign numbers to them
- Save and deploy


## Invoke the math functionality
- Go to the `API Gateway` service in the AWS console
- Select `REST API`
- Select `REST`, `New API`, and name it `PowerOfMathAPI`
- Create API
- Select `Actions` and `Create Method` (Make sure that `Resources` is selected on the left)
- Select `POST` and then `checkmark`
- Select `Lambda Function` and then select the `PowerOfMathFunction` that was created earlier
- Save and see the gateway permission window
- Under the actions menu select `Enable CORS`
- Select `Enable CORS and replace existing CORS headers`
- Select `Actions` and `Deploy API`
-  Select `New Stage` and name it `dev`
- - Save the URL gateway up at the top:  `https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev`
- Select `Resources` on the left and then select the `POST` method
- Select the blue lightning bolt to test the API


## Store the result
- Go to the `DynamoDB` service in the AWS console
- Create table
- Name it `PowerOfMathDatabase`
- Name the partition/primary key `ID` and make it a string
- Select the table that was just created 
- Select `Additional info` under the `General Information` section under `Overview`
- Copy the `ARN` and save it for later:  `arn:aws:dynamodb:us-east-1:123456789012:table/PowerOfMathTable`


## Handle permissions
- Go back the the Lambda function and select `Configuration` then `Permissions`
- Select the role
- Under Permissions policies slect `Add Permission` and then select `Create inline policy`
- Copy in the JSON from `Lambda Function Policy.txt`
- Update the `Resource` to the `ARN` from the DynamoDB table
- Review Policy and then name it `PowerOfMathPolicy`


## Store the result (continued)
- Go to the Code tab in the Lambda function
- Replace the code with the code from `PowerOfMathFunction - Lambda Final`
- Click `Deploy`
- Run the test again and see the result in the DynamoDB table
- - Open the `PowerOfMathTable` and select the `Explore table items` button
- - There should now be a new entry in the table


## Update the webpage with the API
- Copy in the URL from the gateway created earlier into the `index.html` file
- Create a new zip file with the updated `index.html` file
- Go back to the `Amplify` console and reupload the zip file
- The webpage will redeploy on it's own
- The domain should be the same


## Deleting everything
- Do not want any surprise bills
- Go to the `Amplify` console and select `Actions` and `Delete app`
- Go to `DynamoDB`, select the table from the list of tables, and then click `Delete`
- Go to `Lambda`, select the function from the list of functions, and then click `Delete`
- Go to `API Gateway`, click the `Actions` button and select `Delete API`
