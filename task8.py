import boto3


def get_name(instance):
  for tag in instance.get('Tags', []):
    if tag['Key'] == 'Name':
      return tag['Value']
  return 'No Name'


ec2 = boto3.client('ec2')
response = ec2.describe_instances()

environments = {'prod': [], 'dev': [], 'test': [], 'other': []}

for reservation in response['Reservations']:
  for instance in reservation['Instances']:
    instance_id = instance['InstanceId']
    name = get_name(instance).lower()  
    
    if 'prod' in name:
      environments['prod'].append(instance_id)
    elif 'dev' in name:
      environments['dev'].append(instance_id)
    elif 'test' in name:
      environments['test'].append(instance_id)
    else:
      environments['other'].append(instance_id)

for env, ids in environments.items():
  print(f"Environment: {env.upper()} (Total machines: {len(ids)})")
  for i_id in ids:
    print(f'  - ID: {i_id}')
  print('-' * 30)