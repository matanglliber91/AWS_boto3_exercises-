# Exercise 1 — EC2 Inventory Map
# Build a Python script that creates a simple inventory of all EC2 instances in a chosen AWS
# region.
# For every instance, print: Instance ID, Name tag (if it exists), instance type, state, private IP,
# and public IP.
# • At the end, print how many instances are running, stopped, and in other states.
# • Use boto3 and the EC2 client.
# • Do not manually enter instance IDs.
# • Handle instances that do not have a Name tag or public IP.
 
import boto3
 
client = boto3.client('ec2')
 
response = client.describe_instances()
 
running = 0
stopped = 0
 
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
 
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"]
        instance_type = instance["InstanceType"]
        public_ip = instance.get("PrivateIpAddress")
        private_ip = instance.get("PublicIpAddress")
 
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]
 
 
        print("-------------------------")
        print("instance ID:" , instance_id)
        print("instance name:" , name)
        print("instance state:" , state)
        print("instance type:" , instance_type)
        print("instance public ip:" , public_ip)
        print("instance private ip:" , private_ip)
 
        if state == "running":
            running += 1
        elif state == "stopped":
            stopped += 1
 
 
print("-------------------------")
print("Running instances: " ,running)
print("Stopped instances: " ,stopped)                         