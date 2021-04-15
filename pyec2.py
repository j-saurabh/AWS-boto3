#!/bin/python3

import boto3

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
        Filters=[{'Name':'instance-state-name', 'Values':['running']}])

for instance in instances:
    print("Instance ID:" + instance.id + "\tInstance type:" + instance.instance_type) 

