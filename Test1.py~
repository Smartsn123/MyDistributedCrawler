import boto3
import datetime
client = boto3.client('ec2')
response = client.request_spot_instances(
    DryRun=False,
    SpotPrice='0.10',
    ClientToken='string',
    InstanceCount=1,
    Type='one-time',
    LaunchSpecification={
        'ImageId': 'ami-fce3c696',
        'KeyName': 'awskey.pem',
        'SecurityGroups': ['sg-709f8709'],
        'InstanceType': 'm4.large',
        'Placement': {
            'AvailabilityZone': 'us-east-1a',
        },
        'BlockDeviceMappings': [
            {
                'Ebs': {
                    'SnapshotId': 'snap-f70deff0',
                    'VolumeSize': 100,
                    'DeleteOnTermination': True,
                    'VolumeType': 'gp2',
                    'Iops': 300,
                    'Encrypted': False
                },
            },
        ],

        'EbsOptimized': True,
        'Monitoring': {
            'Enabled': True
        },
        'SecurityGroupIds': [
            'sg-709f8709',
        ]
    }
)
