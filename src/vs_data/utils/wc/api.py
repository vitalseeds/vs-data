from woocommerce import API
from vs_data.utils.cli import display_table


def get_api(url, key, secret):
    # print(url, key, secret)
    print(url)
    return API(
        url=url, consumer_key=key, consumer_secret=secret, version="wc/v3", timeout=300
    )
