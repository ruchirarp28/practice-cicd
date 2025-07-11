#!/usr/bin/env python3

import aws_cdk as cdk
from my_cdk_app.my_cdk_stack import MyCdkStack

app = cdk.App()
MyCdkStack(app, "MyCdkStack")
app.synth()
