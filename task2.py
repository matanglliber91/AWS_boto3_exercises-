# Exercise 2 — Start a Stopped Server
# Create a function called <b>start_instance(instance_id)</b>.
# • The function receives an EC2 Instance ID and starts the machine only if it is currently
# stopped.
# Print a clear message describing what happened.
# • If the instance is already running, do not start it again.
# • Use describe_instances before changing the state.
# Return a useful status message.
 
import boto3
 
client = boto3.client('ec2')
 
def start_instance(instance_id):
    response = client.describe_instances(InstanceIds=[instance_id])
    instance = response["Reservations"][0]["Instances"][0]
    state = instance["State"]["Name"]
 
    if state == "stopped":
        client.start_instances(InstanceIds=[instance_id])
    else:
        print(instance_id, "Cannot be started because the current state is:", state)
        
 
start_instance("i-06679819cb2400253")