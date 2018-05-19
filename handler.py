import json
import boto3
import csv

def hello(event, context):
    if event == {}:
        raise Exception('Noooooooooooooo eventtttttttttt.')
    else:
        return world(event)


def world(event):
    v = event.get('hello')
    if v is not None:
        return 'hello world.'
    else:
        raise Exception('Erroooooooooooooooooooor.')

    # try:
    #     v = event.get('hello')
    #     if v is not None:
    #         return 'hello world.'
    #     else:
    #         raise Exception('Erroooooooooooooooooooor.')
    # except Exception:
    #     raise


def dlq_message_handler(event, context):
    sqs = boto3.resource('sqs')
    queue_name = 'dlq-tutorial'
    q = sqs.get_queue_by_name(QueueName=queue_name)
    messages = []
    while True:
        q_messages = q.receive_messages(AttributeNames=['All'],
                                        MessageAttributeNames=['All'],
                                        MaxNumberOfMessages=10)
        if q_messages:
            for qm in q_messages:
                attr = qm.attributes
                body = qm.body
                msga = qm.message_attributes

                sent_time_stamp = attr.get('SentTimestamp')
                error_message = msga['ErrorMessage']['StringValue']

                message = {}
                message['SentTimestamp'] = sent_time_stamp
                message['ErrorMessage'] = error_message
                message['EventBody'] = str(json.loads(body))
                messages.append(message)

                qm.delete()
        else:
            break

    if len(messages) > 0:
        write_csv_file(messages)
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


def write_csv_file(messages):
    header = messages[-1].keys()
    with open('example.csv', 'w', newline='') as csvfile:
        fieldnames = header
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for row in messages:
            writer.writerow(row)

def write_excel_file(records):
    wb = openpyxl.Workbook()
    ws = wb.active

    for row in records:
        ws.append(row)

    wb.save('example.xlsx')
