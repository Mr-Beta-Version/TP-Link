import requests

cookies = {
    'sysauth': '7bba74753457eac8c16bdbea2b4d8493',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://192.168.0.1',
    'Referer': 'http://192.168.0.1/webpages/index.html',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'form': 'white_list',
}

data = {
    'sign': '231e8d3ed72c628de8d93038db4c34f80f19a8a37bf0454deeb938757b42e7aa099f924280d83dd781e9b7a7dcb399457c4344cb3dd2f0b56067d8e059d4859a',
    'data': 'JFBUC9u1FKdalbLozddfs1h4jbzB/TmtPdFAJ/q7YaF1AEivL5SgN5Ja/cUCZ9QxWzhH6yWz7q5AZCVXPuXjG2SeTOEqowaHpowxkLcv/pS7hFG2VOCe5ykAdCrn8VlJmpl6Q59HQTyDzEhADgwcwqNg1mXyoXU+3aclqg0bfuc=',
}

response = requests.post(
    'http://192.168.0.1/cgi-bin/luci/;stok=dd972c1bfc08b531d0d44de5583ec8cf/admin/access_control',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
