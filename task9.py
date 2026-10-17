import boto3


def get_name(instance):
  for tag in instance.get("Tags", []):
    if tag["Key"] == "Name":
      return tag["Value"]
  return "No Name"


def start_environment(environment):
  ec2 = boto3.client("ec2")
  response = ec2.describe_instances()

  started_count = 0
  skipped_count = 0

  print(f"Scanning for environment '{environment}' to start...")

  for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
      instance_id = instance["InstanceId"]
      state = instance["State"]["Name"]
      name = get_name(instance).lower()

      if environment.lower() in name:
        if state == "stopped":
          print(f"Starting stopped instance: {instance_id} (Name: {name})")
          ec2.start_instances(InstanceIds=[instance_id])
          started_count += 1
        else:
          print(
              f"Skipping instance: {instance_id} (Name: {name}) - Current state"
              f" is '{state}'"
          )
          skipped_count += 1

  
  print("\n--- Summary ---")
  print(f"Total machines started: {started_count}")
  print(f"Total machines skipped: {skipped_count}")


start_environment("dev")