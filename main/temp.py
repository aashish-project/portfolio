import requests

data_requests = requests.get('https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending')
print(data_requests.request.headers)