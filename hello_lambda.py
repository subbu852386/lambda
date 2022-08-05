import os


def lambda_handler(event, context):
    return "{} from Subbu!!!".format(os.environ['greeting'])
