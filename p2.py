import boto3

def main():
    instances = boto3.resource('ec2').instances.all()
    for instance in instances:
        for vol in instance.volumes.all():
            for tag in instance.tags:
                prefix = tag["Key"][:4]
                if prefix != 'aws:':
                    print("Applying KEY/VALUE pair: ", tag["Key"],"/",tag["Value"], " to volume ID: ", vol.volume_id)
                    vol.create_tags(
                        Tags = [
                            {
                                'Key': tag["Key"],
                                'Value': tag["Value"]
                            },
                        ]
                    )

if __name__ == '__main__':
	main()

