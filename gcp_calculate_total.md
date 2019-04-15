To calculate total cost of Google Cloud storage in GBs:

```gcloud compute disks list |grep -v SIZE_GB |awk '{print $3}' | paste -sd+ - | bc```
