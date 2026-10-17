import boto3

client = boto3.client('ec2')
response = client.describe_instances()

for reservation in response['Reservations']:
  for instance in reservation['Instances']:
    instance_id = instance['InstanceId']
    state = instance['State']['Name']
    private_ip = instance.get('PrivateIpAddress', 'N/A')

    
    instance_name = 'No Name'
    if 'Tags' in instance:
      for tag in instance['Tags']:
        if tag['Key'] == 'Name':
          instance_name = tag['Value']

    print(
        f'ID: {instance_id} | Name: {instance_name} | State: {state} | IP:'
        f' {private_ip}'
    )