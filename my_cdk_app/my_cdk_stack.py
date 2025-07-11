from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

class MyCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(
            self,
            "MyFirstBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,  # For dev/testing only
            auto_delete_objects=True
        )
