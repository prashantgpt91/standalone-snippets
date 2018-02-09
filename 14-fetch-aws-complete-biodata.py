#!/usr/bin/env python2
import botocore.session
from datetime import datetime, tzinfo, timedelta
import json

class SimpleUtc(tzinfo):
    def tzname(self):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.utcnow().replace(tzinfo=SimpleUtc()).isoformat()

        return json.JSONEncoder.default(self, o)

def clean_response(resp):
    del resp['ResponseMetadata']
    return resp

def details(region):
    ec2 = session.create_client('ec2', region_name=region)
    print("Executing ec2 describe-instances")
    output['ec2'] = clean_response(ec2.describe_instances())
    print("Executing ec2 describe-security-groups")
    output['securitygroup'] = clean_response(ec2.describe_security_groups())
    print("Executing ec2 describe-subnet")
    output['subnets'] = clean_response(ec2.describe_subnets())
    print("Executing ec2 describe-network-acls")
    output['acls'] = clean_response(ec2.describe_network_acls())
    print("Executing ec2 describe-vpcs")
    output['vpc'] = clean_response(ec2.describe_vpcs())
    print("Executing ec2 describe-volumes")
    output['ebs'] = clean_response(ec2.describe_volumes())
    print("Executing elb describe-load-balancers")
    output['elb'] = clean_response(session.create_client('elb', region_name=region).describe_load_balancers())
    elbv2 = session.create_client('elbv2', region_name=region)
    output['elbv2'] = {}
    output['elbv2']['TargetHealthDescriptions'] = {}
    print("Executing elbv2 describe-load-balancers")
    output['elbv2']['LoadBalancers'] = elbv2.describe_load_balancers()['LoadBalancers']
    print("Executing elbv2 describe-target-groups")
    output['elbv2']['TargetGroups'] = elbv2.describe_target_groups()['TargetGroups']
    print("Executing elbv2 describe-target-health")
    for target_group_arn in [target_group['TargetGroupArn'] for target_group in output['elbv2']['TargetGroups']]:
        output['elbv2']['TargetHealthDescriptions'][target_group_arn] = elbv2.describe_target_health(TargetGroupArn=target_group_arn)['TargetHealthDescriptions']
    print("Executing autoscaling describe-auto-scaling-groups")
    output['autoscale'] = clean_response(session.create_client('autoscaling', region_name=region).describe_auto_scaling_groups())
    print("Executing autoscaling describe-launch-configurations")
    output['launchconfig'] = clean_response(session.create_client('autoscaling', region_name=region).describe_launch_configurations())
    print("Executing s3api list-buckets")
    output['s3buckets'] = clean_response(session.create_client('s3', region_name=region).list_buckets())
    print("Executing rds describe-db-instances")
    output['rds'] = clean_response(session.create_client('rds', region_name=region).describe_db_instances())
    print("Executing cloudfront describe-db-instances")
    output['cloudfront'] = clean_response(session.create_client('cloudfront', region_name=region).list_distributions())

    print("Executing sns list-topics")
    sns = session.create_client('sns', region_name=region)
    topic_resp = sns.list_topics()
    print("Executing sns get-topic-attributes")
    output['sns'] = [clean_response(sns.get_topic_attributes(TopicArn = t['TopicArn'])) for t in topic_resp.get('Topics',[])]

    print("Executing sqs list-queues")
    sqs = session.create_client('sqs', region_name=region)
    queue_resp = sqs.list_queues()

    print("Executing sqs get-queue-attributes")
    urls = queue_resp.get('QueueUrls',[])
    output['sqs'] = {'Queues': [clean_response(sqs.get_queue_attributes(AttributeNames=['All'], QueueUrl = url)) for url in urls]}

    output['importMetaData'] = {'region': region, 'timeStamp': datetime.now()}

    with open(region + '.json', 'w') as f:
        json.dump(output, f, cls=DateTimeEncoder)

if __name__ == '__main__':

    region_virginia = 'us-east-1'
    region_ohio = 'us-east-2'
    region_california = 'us-west-1'
    region_oregon = 'us-west-2'
    region_mumbai = 'ap-south-1'
    region_seoul = 'ap-northeast-2'
    region_singapore = 'ap-southeast-1'
    region_sydney = 'ap-southeast-2'
    region_tokyo = 'ap-northeast-1'
    region_canada = 'ca-central-1'
    #region_beijing = 'cn-north-1'
    region_frankfurt = 'eu-central-1'
    region_ireland = 'eu-west-1'
    region_london = 'eu-west-2'
    region_paris = 'eu-west-3'
    region_saopaulo = 'sa-east-1'


    region_list = [region_seoul, region_california, region_canada, region_frankfurt, region_ireland, region_london, region_mumbai, region_ohio, region_oregon, region_paris, region_saopaulo, region_singapore, region_sydney, region_tokyo, region_virginia]

    output = {}
    session = botocore.session.get_session()
    for i in region_list:
        details(region=i)


