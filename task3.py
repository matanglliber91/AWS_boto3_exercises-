import boto3


def stop_instance(instance_id):
  client = boto3.client('ec2')

  response = client.describe_instances(InstanceIds=[instance_id])

  for reservation in response['Reservations']:
    for instance in reservation['Instances']:
      current_state = instance['State']['Name']
      print(f'Current state: {current_state}')

      if current_state == 'stopped':
        print('This instance is already stopped! No action taken.')
        return

      confirmation = input(
          "Type 'YES' to confirm stopping this instance: "
      )

      if confirmation == 'YES':
        client.stop_instances(InstanceIds=[instance_id])
        print('Stopping instance...')
      else:
        print('Action cancelled.')
        
        stop_instance('i-07ba9f5ce7251ddbc')
