import boto3

def create_new_instances():
    instances = ec2.create_instances(
        ImageId='ami-0a40efd5228d5c9a1',
        MinCount=1,
        MaxCount=2,
        InstanceType='t2.micro',
        KeyName='ec2-keypair'
    )

def create_new_keypair():
    outfile = open('ec2-keypair.pem', 'w')

    key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

    KeyPairOut = str(key_pair.key_material)
    print(KeyPairOut)
    outfile.write(KeyPairOut)


if __name__ == '__main__':
    ec2 = boto3.resource('ec2')
    ec2client = boto3.client('ec2')

    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance)
            print("You can access the server public IP Address from here: " + instance["PublicIpAddress"] + "\n\n\n")

    # create_new_keypair()
    # create_new_instances()
