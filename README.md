# ngrok-discord-docker

A Docker image for [ngrok](https://ngrok.com) service to expose a local docker environment or any other local server to the public internet over secure tunnels. The image is built using official python SDK to act as an ngrok agent and publish to a discord webhook the tunnel created.

# A Little About The Project

This project first started to allow the use of minecraft server easy use of [ngrok](https://ngrok.com) free tier.
If you have suggestions for improvements please feel free to open an issue.

## Usage

### Command-line

**Example**  
The example below assumes that you have running minecraft server with exposed port `25565`.
(replace the ngrok_api, webhook_url and ngrok_authtoken with your own values.)

```bash
docker run -t -i --name ngrok-discord -e ngrok_api=<ngrok_api> -e webhook_url=<webhook_url> -e NGROK_AUTHTOKEN=<ngrok_authtoken> -e PORT=25565 -e PROTOCOL=tcp -e server_name=Server -e massage_title=New Server Name samuelgibhin/ngrok-discord:latest 
```

### As part of compose.yml file 

```yaml
version: "3"
services:
    ngrok-discord:
        container_name: ngrok-discord
        network_mode: host
        stdin_open: true
        tty: true
        image: samuelgibhin/ngrok-discord:latest
        restart: unless-stopped
        environment:
          - ngrok_api=<ngrok_api> #replace with your ngrok api
          - webhook_url=<webhook_url> #replace with your webhook url
          - NGROK_AUTHTOKEN=<ngrok_authtoken> #replace with your ngrok authentication token
          - PORT=25565 #replace with your port
          - PROTOCOL=tcp #replace with your protocol
          - server_name=Server #optional
          - massage_title=New Server Name #optional
```

## License

[MIT](../../blob/master/LICENSE)
