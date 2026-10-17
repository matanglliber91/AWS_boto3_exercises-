import boto3

ec2 = boto3.client('ec2')

def find_idle_servers():
    response = ec2.describe_instances()
    stopped_count = 0
    
    print("Stopped Servers:")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'stopped':
                stopped_count += 1
                iid = instance['InstanceId']
                itype = instance['InstanceType']
                name = 'No Name'
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                print(f"ID: {iid} | Name: {name} | Type: {itype}")
                
    print(f"\nTotal stopped machines: {stopped_count}")

find_idle_servers()