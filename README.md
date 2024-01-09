# **Portfolio API**

AWS Lambda that get data from GitHub using the [GitHub REST API](https://docs.github.com/en/rest)

Has only one GET method with two variants:

 - **/dev/porfoliodata/getrepos** Get all the user repos (The lambda use a environment variable to get the user)
 - **/dev/porfoliodata/getrepos?repo={repository name}** Get the Readme file in base64 and the languages used in the repo that is recieved

# Environment variables:

 - **GITHUB_TOKEN** Used for increase the GitHub API quota
 - **GITHUB_USER** The user name that will be use for get the repository list

# Lambda Layers
This lambda use the version 0.25.2 of **httpx** package. Is implemented by a lambda layer.
To know of create a layer for python lambdas please take a look at this documentation: https://medium.com/brlink/how-to-create-a-python-layer-in-aws-lambda-287235215b79

# GitHub Quota:

The github api have somes quota for his non-authenticate request and authenticate requests as well, take a look at his documentation https://docs.github.com/es/rest/overview/rate-limits-for-the-rest-api?apiVersion=2022-11-28
