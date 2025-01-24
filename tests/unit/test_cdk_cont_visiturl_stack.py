import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_cont_visiturl.cdk_cont_visiturl_stack import CdkContVisiturlStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_cont_visiturl/cdk_cont_visiturl_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkContVisiturlStack(app, "cdk-cont-visiturl")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
