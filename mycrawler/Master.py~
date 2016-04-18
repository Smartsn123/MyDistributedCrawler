# from fabric.api import *
# from fabric.colors import green as _green, yellow as _yellow
from boto.ec2.connection import EC2Connection

import time
 
# def start_machine(ami='xyz'):
#'''Launch a single instance of the provided ami'''

aws_access_key_id = 'Cf7...'
aws_secret_access_key = 'Av7h....'

# Basic Information
instance_name = 'Name-Of-My-Machine'
instance_type='t2.micro'
key_name = 'My-SSH-Key-Name'
#placement='us-east-1d'
image_id = 'ami-d7a...'
min_count = 1
max_count = 1

# Network
security_group_ids = ['sg-7fh...']
monitoring_enabled = True
subnet_id = 'subnet-f77...'
private_ip_address = '192.168.30.1'

# Specific Machine
kernel_id = None
ramdisk_id = None
user_data = None

print('Connecting to AWS API...')
conn = EC2Connection(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

print('Creating New Machine "'+instance_name+'"...')
reservation = conn.run_instances(
									image_id=image_id,
									key_name = key_name,
									min_count = min_count, 
									max_count = min_count,
									monitoring_enabled = monitoring_enabled,
									security_group_ids = security_group_ids,
									instance_type = instance_type,
									kernel_id = kernel_id,
									ramdisk_id = ramdisk_id,
									subnet_id = subnet_id,
									private_ip_address = private_ip_address,
									user_data = user_data
								)

instance = reservation.instances[0]
conn.create_tags([instance.id], {"Name": instance_name})

print('Waiting for instance to start...')
# Check up on its status every so often
status = instance.update()
while status == 'pending':
	time.sleep(5)
	status = instance.update()
	print str(status) + '...'
if status == 'running':
	print('New instance "' + instance.id + '" is running... waiting for complete start.')

	reservations = conn.get_all_instance_status(instance_ids=instance.id)
	instance = reservations[0]

	while instance.system_status.status != 'ok' and instance.instance_status.status != 'ok':
		time.sleep(20)

		reservations = conn.get_all_instance_status(instance_ids=instance.id)
		instance = reservations[0]

		print instance.system_status.status + '/' + instance.instance_status.status + '...'
		
else:
	print('Failed to create instance "'+instance.id+'" - status: ' + status)
