import config
import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': config.PHONE,
  'message': 'Hello world',
  'key': config.KEY,
})
print(resp.json())