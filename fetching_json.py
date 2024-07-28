# mitmproxy_script.py
from mitmproxy import http
import json

# Daftar URL yang ingin diambil respons JSON-nya
target_urls = [
    "https://gql.tokopedia.com/graphql/ShopProducts"
]

def response(flow: http.HTTPFlow) -> None:
    if flow.request.url in target_urls and flow.response.headers.get("Content-Type") == "application/json":
        try:
            response_data = json.loads(flow.response.text)
            print(f"Response JSON for {flow.request.url}:")
            print(json.dumps(response_data, indent=2))
        except json.JSONDecodeError:
            print(f"Failed to decode JSON from {flow.request.url}")
