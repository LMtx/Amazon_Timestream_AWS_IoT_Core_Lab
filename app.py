#!/usr/bin/env python3
import aws_cdk as cdk
from timestream_lab_stack.timestream_lab_stack import TimestreamLabStack

app = cdk.App()

timestream_lab_stack = TimestreamLabStack(app, "TimestreamLabStack")

app.synth()
