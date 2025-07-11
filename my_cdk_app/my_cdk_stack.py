from aws_cdk import Stack, aws_s3 as s3
from constructs import Construct

class MyCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self,
            "MyFirstBucket-76473546465636",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,  # NOT for production!
            auto_delete_objects=True                   # Needs permissions
        )
