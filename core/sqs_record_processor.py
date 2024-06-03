import logging
import boto3
import json
import traceback
from services.fesa_api import FesaAPI
from models.user import UserModel
from config import Config

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

sns_client = boto3.client('sns', endpoint_url='http://localstack:4566')


class SQSRecordProcessor(object):
    def __init__(self, record: dict):
        self.record = record
        self.body = record.get('body').replace("'", '"')
        self.user = UserModel(json.loads(self.body))
        self.message_id = self.record.get('MessageId')
        self.message_attributes = self.record.get('MessageAttributes')
        self.fesa_api = FesaAPI()
        self.config = Config()
    
    def process(self):
        LOGGER.info(f"Processing message {self.body}")
        try:
            self._create_user()
            self._save_message_to_db()

            self._send_message_to_sns()
        except Exception as e:
            self._save_message_to_db(status='failed', traceback=traceback.format_exc())
            LOGGER.error(f"Error processing message {self.message_id}: {e}")
            raise Exception(e)
        LOGGER.info(f"Message {self.message_id} processed successfully")
        return True

    def _create_user(self):
        self.fesa_api.post('/users', self.user.to_dict())
    
    def _send_message_to_sns(self):
        sns_client.publish(
            TopicArn=self.config.sns_topic_arn,
            Message=f"Message {self.message_id} processed successfully"
        )

    def _save_message_to_db(self, status='processed', traceback=None):
        message = {
            "status": status,
            "error": traceback,
            "text": self.user.to_dict(),
        }
        self.fesa_api.post('/messages', message)
