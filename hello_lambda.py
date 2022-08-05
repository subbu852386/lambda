import os


def lambda_handler(event, context):
    return "{} from Github Actions!!!".format(os.environ['greeting'])
