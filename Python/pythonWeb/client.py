import requests

response = requests.get('http://http://127.0.0.1:5000/status')
print(response.status_code)
print(response.text)
print(response.json())

message = {'username': '0','text': '123'}
response = requests.post('http://http://127.0.0.1:5000/send', json=message)
print(response.status_code)
print(response.text)
print(response.json())


def send_message(username, text):
    message = {'username': username, 'text': text}
    response = requests.post('http://127.0.0.1:5000/send', json=message)
    return response.status_code == 200


username = input('Введите имя: ')
while True:
    text = input('Введите сообщение: ')
    result = send_message(username, text)
    if result is False:
        print('Error')