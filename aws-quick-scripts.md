#### Get private IP given instance ID

```aws ec2 describe-instances --instance-ids $1 --query Reservations[].Instances[].NetworkInterfaces[].PrivateIpAddress --profile production --region us-east-1 |  grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"```


#### New IAM User

Create user: ```aws iam create-user --user-name <user-name>```

Add user to groups: ```aws iam add-user-to-group --user-name <user-name> --group-name <team-name>```

Create console login: ```aws iam create-login-profile --password-reset-required --user-name <user-name> --password <some-random-password>```

Create access key, secret key: ```aws iam create-access-key --user-name <user-name>```

Update password of a user: ```aws iam update-login-profile --user-name <user-name> --password <some-random-password> --password-reset-required```

Delete user: ```aws iam delete-user --user-name <user-name>```
