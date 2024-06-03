import os

class Config:
    def __init__(self):
        self.fesa_api_host = os.getenv('FESA_API_HOST')
        self.sns_topic_arn = os.getenv('SNS_TOPIC_ARN')