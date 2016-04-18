from pprint import pprint
import boto3


"""
Upload a file to a remote directory using SFTP. All parameters except
for "instance" are strings. The instance parameter should be a
boto.ec2.instance.Instance object.
 
instance        An EC2 instance to upload the files to.
key             The file path for a valid SSH key which can be used to
log in to the EC2 machine.
username        The username to log in as.
local_filepath  The path to the file to upload.
remote_filepath The path where the file should be uploaded to.
"""
def upload_file(instance, key, username, local_filepath, remote_filepath):
    ssh_client = boto3.manage.cmdshell.sshclient_from_instance(
        instance,
        key,
        user_name=username
    )
    ssh_client.put_file(local_filepath, remote_filepath)


#create new instances
ec2 = boto3.resource('ec2')
#myinst = ec2.create_instances(ImageId='ami-005b0352', MinCount=2, MaxCount=2)

for inst in myinst:
   inst.update()
   while 1:
      if inst.status == 'running ':
        break;

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)




