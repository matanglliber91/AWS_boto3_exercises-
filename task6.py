import boto3
 
client = boto3.client("ec2")
 
 
def list_instances():
    response = client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"],"|",instance["State"]["Name"])
 
def start_instance(instance_id):
    client.start_instances(InstanceIds=[instance_id])
    print("Start request sent.")
 
def stop_instance(instance_id):
    client.stop_instances(InstanceIds=[instance_id])
    print("Stop request sent.")
 
def reboot_instance(instance_id):
    client.reboot_instances(InstanceIds=[instance_id])
    print("Reboot request sent.")
 
 
def main():
    while True:
        print("\n====== EC2 Mangment Menu ======")
        print("1. List instances")
        print("2. Start instance")
        print("3. Stop instance")
        print("4. Reboot instance")
        print("5. Exit")
 
        choice = input("Please pick an option: ")
 
        if choice == "1":
            print("-------------------------")
            list_instances()
        elif choice == "2":
            instance_id = input("Instance ID: ")
            start_instance(instance_id)
        elif choice == "3":
            instance_id = input("Instance ID: ")
            stop_instance(instance_id)
        elif choice == "4":
            instance_id = input("Instance ID: ")
            reboot_instance(instance_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input please pick a number between 1-5")
 
main()