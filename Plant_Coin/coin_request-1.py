
import json
import requests

webhook_url = 'https://hooks.slack.com/services/T70HH0URF/BBQPBTMHR/Dj3UytrtfjCenk6TYusSIAs'# enter your own web hook url
slack_data = {'text': "Thirsty Now!!😞, water me and get plant coins", "attachments": [
        {
            "text": "Water plants and earn plant coin",
            "fallback": "Plant coin needs a another try!!",
            "callback_id": "plant_coin",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "water",
                    "text": "Water me",
                    "type": "button",
                    "value": "plant coin"
                }
            ]
        }
    ]}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
