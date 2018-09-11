import boto3
import sys

def main(tag, toggle):
	client = boto3.client('ec2')
	response = client.describe_instances(
	    Filters=[
	        {
	            'Name': 'tag:Tag',
	            'Values': [
	                tag,
	            ]
	        },
	    ]
	)
	responseInstanceId = response["Reservations"][0]["Instances"][0]["InstanceId"]
	if toggle == "Stop":
		#TODO check if instance not running, exit loop.
		print("Stopping Instance ", responseInstanceId)
		response = client.stop_instances(
    			InstanceIds=[
       				responseInstanceId,
    			]
    		)
	elif toggle == "Start":
		print("Starting Instance ", responseInstanceId)
		#TODO check if instance running, exit loop.
		response = client.start_instances(
    			InstanceIds=[
        			responseInstanceId,
    			]
		)
	else:
		print("Please enter a valid command: Start or Stop")

if __name__ == '__main__':
	tag = sys.argv[1]
	toggle = sys.argv[2]
	main(tag, toggle)

