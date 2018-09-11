import boto3
import sys

def main(resizeInstanceId, newInstanceSize):
	print("Resizing...")
	client = boto3.client('ec2')
	
	my_instance = resizeInstanceId
	
	# Stop the instance
	client.stop_instances(InstanceIds=[my_instance])
	waiter=client.get_waiter('instance_stopped')
	waiter.wait(InstanceIds=[my_instance])
	
	# Change the instance type
	client.modify_instance_attribute(InstanceId=my_instance, Attribute='instanceType', Value=newInstanceSize)
	
	# Start the instance
	client.start_instances(InstanceIds=[my_instance])
	
def displayInstances():
	print("Current Instances")
	instances = boto3.resource('ec2').instances.all()
	for instance in instances:
		print(instance.instance_id, instance.instance_type)
		
if __name__ == '__main__':
	try:
		resizeInstanceId = sys.argv[1]
		newInstanceSize  = sys.argv[2]
		main(resizeInstanceId, newInstanceSize)
	except Exception as e:
		displayInstances()