import boto3
import json
# To create default session:

def create_customized_session(aws_access_key, aws_secret_key, aws_token,
                           region_name=None,profile_name=None):
    session = boto3.session.Session(aws_access_key_id=aws_access_key,
                                   aws_secret_access_key=aws_secret_key,
                                   aws_session_token = aws_token,
                                   region_name=region_name,
                                   profile_name = profile_name)
    print(session)
    return session

awskey = 'ASIAUMIZT'
awsseckey = 'AjlRYJGMKqt2T4G4Lv11'
awsst = 'IQoJb3JpZ2luX2VjEF4aCXVFr4MptW6/+TXUgxKtnpKMOvVQDtrowrPKNYvj4ZgeL2FLtqxtvMwOHSppTvo5iiTIg1asxiZy/abhxfSuVn2xWA4jLInU2MO/+zlfs89DiX1xbSM75m1lM0btOqA9rEkAnfkAbnHhP0gu4ZwwrER3QLpW+wbei8bvZc7hj8aZq6Fl7wEzHKyn/Fq5WFEf113MPkgdTkWTWG6vmgt0IAdwFu9dDWEj0N/0Hk7Cce2huBWjz0U6NPXyTdNQPZUQOBftcAeQwLMQfvQ1yK/8q/IFVkDRsvJEt0ZDYqoNMqmZ4P8ctKJVNc5ncTxRQ4RnhZnDlPcEfuq7pJXysILf4Rq2uHCrU/RfK3G1P3zah3kxS68NZonQMBEVMMCVQd+z6AnzYu/Bnk/bKnclnmGhK2xortj4mpohFlN1xhlMEi7KEoNyCZJBGB5m8cLL29NE4xQ6WUmHhQe6rk4PvH+A+vdO+JPl323oQfQzCmwsChBjqmAZzvIFxFE/tkNYHTPlR7F5RErYilMPMdBhT436G7Vl1+yzGpy+y/BuDyCbo4JwI6AP0LS+zgvX+yqugEfwLdSGpBRJHS5Yvt75NOhjiIuDeNFF2R4yD7gwU6RirDQ4k1jpNjcdAEWDJUdfkTiivqNmF7B+AJRV8QtmsvTDoavzbCZE5AihDIyKIfjgTkfY5zxAyjlWNP+GUwwBbr2adk1cZVw+fea48='
session = create_customized_session(aws_access_key=awskey, aws_secret_key=awsseckey, aws_token=awsst)
sfn_client = session.client('stepfunctions')

state_machine_arn = 'arn:aws:states:us-east-1:316248692088:stateMachine:cip-sftp-step-function'
response = sfn_client.start_execution(
    stateMachineArn=state_machine_arn,
    name='test1',
    input=json.dumps({
                     "Comment": "a8136c57-5572-7caa-9d26-ad2c7f5bfd0f"
                    })
)
print(response)
