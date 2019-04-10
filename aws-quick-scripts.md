
Get private IP given instance ID

```aws ec2 describe-instances --instance-ids $1 --query Reservations[].Instances[].NetworkInterfaces[].PrivateIpAddress --profile production --region us-east-1 |  grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"```
