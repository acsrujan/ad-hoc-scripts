To calculate total cost of Google Cloud storage in GBs:

```gcloud compute disks list |grep -v SIZE_GB |awk '{print $3}' | paste -sd+ - | bc```

To calculate total vCPUs and GBs:

This gives a list of all machines with their types or custom types.. take this output to a spreadsheet or excel and add the columns CPU and RAM.. for standard instance types, add the corresponding CPU and RAM and for rest, add as per custom.

Add the column values.

ToDo: Make the above mess to some bash script.

```gcloud compute instances list --sort-by=MACHINE_TYPE --format="table(name,machineType,status)" --filter="(status=RUNNING)"``` 
