import aws_cdk as core
import aws_cdk.assertions as assertions

from sqs_fn_dlq_infra.sqs_fn_dlq_infra_stack import SqsFnDlqInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sqs_fn_dlq_infra/sqs_fn_dlq_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SqsFnDlqInfraStack(app, "sqs-fn-dlq-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
