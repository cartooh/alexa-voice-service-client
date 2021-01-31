import argparse

from alexa_client import AlexaClient


def main(client_id, secret, refresh_token, locales):
    alexa_client = AlexaClient(
        client_id=client_id,
        secret=secret,
        refresh_token=refresh_token,
    )

    with alexa_client.connect():  # authenticate and other handshaking steps
        alexa_client.send_locales_changed(locales)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--client-id', help='AVS client ID', required=True
    )
    parser.add_argument(
        '-s', '--client-secret', help='AVS client secret', required=True
    )
    parser.add_argument(
        '-r', '--refresh-token', help='AVS refresh token', required=True
    )
    parser.add_argument(
        '-l', '--locales', help='locales', nargs='+', required=True
    )
    parsed = parser.parse_args()
    main(
        client_id=parsed.client_id,
        secret=parsed.client_secret,
        refresh_token=parsed.refresh_token,
        locales=parsed.locales
    )
