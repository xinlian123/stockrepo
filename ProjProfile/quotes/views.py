from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    import os
    import time
    os.environ['no_proxy'] = 'investors-exchange-iex-trading.p.rapidapi.com'

    url = "https://qaaccess.creditacceptance.com:8443/openam/json/authenticate"

    headers = {
        'Accept-Language': "en-US,en;q=0.5",
        'Content-Type': "application/json",
        'x-openam-password': "Xiaobai25",
        'x-openam-username': "xlian",
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "qaaccess.creditacceptance.com:8443",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    api_response = requests.request("POST", url, headers=headers)
    try:
        response = json.loads(api_response.content)

    except:
        response = 'error..'

    return render(request, 'home.html', {'response': response})

def about(request):
    return render(request, 'about.html', {})
