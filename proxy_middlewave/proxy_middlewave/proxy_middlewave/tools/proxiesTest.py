import requests
from tools.proxyTool import get_proxy


def proxy():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    proxy = get_proxy()
    response = requests.get(url='https://weibo.com/login.php',
                            headers=headers,
                            proxies={"http": proxy},
                            timeout=5
                            )
    print(response.status_code)

proxy()