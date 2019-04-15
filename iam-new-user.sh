#!/bin/bash

#Create user
aws iam create-user --user-name <user-name>

#Add user to groups
aws iam add-user-to-group --user-name <user-name> --group-name <team-name>

#Create console login
aws iam create-login-profile --password-reset-required --user-name <user-name> --password <some-random-password>

#Create access key, secret key
aws iam create-access-key --user-name <user-name>
