import requests


class Bot:

    def __init__(self, page_ID, access_token):
        self.access_token = access_token
        self.access_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={0}'.format(access_token)
        self.page_settings_url = 'https://graph.facebook.com/v2.6/{0}/thread_settings?access_token={1}'.format(page_ID, access_token)

    def send_text(self, recipient_id, output):

        recipient = {
            "id": recipient_id
        }
        message = {
            "text": output
        }
        payload = dict()
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.access_url, data=payload).json()

    # Sending local image not functional
    def send_image(self, recipient_id, image_path):

        recipient = {
            "id": recipient_id
        }
        message = {
            "attachment": {
                "type": "image",
                "payload": {
                }
            }
        }
        payload = dict()
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        payload['filedata'] = open(image_path, 'rb')
        return requests.post(self.access_url, data=payload).json()

    def send_image_url(self, recipient_id, url):

        recipient = {
            "id": recipient_id
        }
        message = {
            "attachment": {
                "type": "image",
                "payload":{
                    "url": url
                }
            }
        }
        payload = dict()
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.access_url, data=payload).json()

    def send_buttons_URLS(self, recipient_id, URLs, titles):

        recipient = {
            "id": recipient_id
        }
        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Button Test",
                    "buttons": self.get_buttons(URLs, titles)
                }
            }
        }
        payload = dict()
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.access_url, data=payload).json()

    def send_buttons_postback(self, recipient_id, heading, titles):

        recipient = {
            "id": recipient_id
        }
        buttons = list()
        for i in range(0, len(titles)):
            temp = {
                "type": "postback",
                "title": titles[i],
                "payload": titles[i]

            }
            buttons.append(temp)
        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": heading,
                    "buttons": buttons
                }
            }
        }
        payload = dict()
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.access_url, data=payload).json()

    def get_buttons(self, URLs, titles):
        buttons = list()
        for i in range(0, len(titles)):
            temp = dict()
            if URLs[i] == 0:
                temp['type'] = "postback"
                temp['title'] = titles[i]
                temp['payload'] = titles[i]
            else:
                temp['type'] = "web_url"
                temp['url'] = URLs[i]
                temp['title'] = titles[i]
            buttons.append(temp)
        return buttons

    def send_generic_template(self, recipient_id, *args):

        recipient = {
            "id": recipient_id
        }
        elements = list()
        for i in range(0, len(args)):
            temp = {
                "title": args[i][0],
                "image_url": args[i][1],
                "subtitle": args[i][2],
                "buttons": self.get_buttons(args[i][3], args[i][4])
            }
            elements.append(temp)
        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements
                }
            }
        }
        payload = dict()
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.access_url, data=payload).json()

    def welcome_message(self, msg):
        payload = {
            "setting_type": "call_to_actions",
            "thread_state": "new_thread",
            "call_to_actions": [
                {
                    "message": {
                        "text": msg
                    }
                }
            ]
        }
        return requests.post(self.page_settings_url, data=payload).json()




