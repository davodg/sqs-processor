from core.sqs_record_processor import SQSRecordProcessor

def main(event, context):
    for record in event['Records']:
        sqs_record_processor = SQSRecordProcessor(record)
        sqs_record_processor.process()
