import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

instances_to_stop = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name'] 

        name = "No-Name"
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']

        if state == 'stopped':
            print(f"Skipping {name} ({instance_id})")
            continue

        name_lower = name.lower()

        if 'prod' in name_lower:
            continue

        if 'dev' in name_lower or 'test' in name_lower:
            instances_to_stop.append({'Id': instance_id, 'Name': name})

print("\n================ SAFETY SUMMARY ================")
print("The following running instances are scheduled to be stopped:")
for item in instances_to_stop:
    print(f"  • Name: {item['Name']} | Instance ID: {item['Id']}")
print("==================================================")