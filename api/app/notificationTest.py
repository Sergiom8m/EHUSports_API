import requests

def notifyAllDevices():

    # Realizar la primera solicitud
    response = requests.get('http://34.71.128.243:8000/tokens/')

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Extraer los tokens de la respuesta JSON
        tokens = [token['token'] for token in response.json()]

        # Realizar la segunda solicitud para cada token
        for token in tokens:
            headers = {
                'Authorization': 'key=AAAAL1w-Z4w:APA91bFg8D5Ks62mfsaY0nDqslwDBpIBTTQCAft_4fin'
                                '-X4mmvXQPnXWBfY0LGpF50APE8UDtI8_qr4HBWCR29eJT5v0zBHoxuNopStEh'
                                '-B3i0Gxymkr9z2jMJpGR2C0r4_5aw2wTi_b',
                'Content-Type': 'application/json',
            }
            data = {
                'to': token,
                'notification': {
                    'body': 'Hoy es un buen día para realizar alguna actividad deportiva.',
                    'title': 'ES MOMENTO DE PONERSE EN FORMA CON EHUSports!'
                }
            }
            response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, json=data)

    else:
        print('Error al realizar la solicitud.')
