import requests
import os
import logging
import ngrok
from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        body = bytes("Hello", "utf-8")
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)
        
def get_ngrok_tunnel() -> str:
    ngrok_api = os.environ.get('ngrok_api', None)
    if ngrok_api is None:
        raise Exception("ngrok_api not set")
    
    headers = {
        'Authorization': f'Bearer {ngrok_api}',
        'Ngrok-Version': '2',
    }

    tunnels = requests.get('https://api.ngrok.com/tunnels', headers=headers)
    
    try:
        tunnel = tunnels.json()['tunnels'][0]["public_url"]
    except Exception as e:
        print(e)
        tunnel = ''

    print(f"{tunnel = }")
    
    return tunnel
        
def update_webhook(tunnel: str) -> None:
    webhook_url = os.environ.get('webhook_url', None)

    if webhook_url is None:
        raise Exception("webhook_url not set")

    embed = {
        "description": f'{tunnel.split("//")[1]}',
        "title": "New Server Name"
    }
    
    data = {
        "content": "message content",
        "username": "Server",
        "embeds": [
            embed
        ],
    }

    result = requests.post(webhook_url, json=data)
    if 200 <= result.status_code < 300:
        print(f"Webhook sent {result.status_code}")
    else:
        print(f"Not sent with {result.status_code}, response:\n{result.json()}")

def main():

    port = int(os.environ.get("PORT", 25565))
    protocol = os.environ.get("PROTOCOL", "tcp")

    logging.basicConfig(level=logging.INFO)
    server = HTTPServer(("localhost", 8080), HelloHandler)
    listener = ngrok.forward(port, protocol, authtoken_from_env=True)
    update_webhook(get_ngrok_tunnel())
    server.serve_forever()

if __name__ == "__main__":
    main()