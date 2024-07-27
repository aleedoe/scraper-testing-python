# mitmproxy_script.py
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.headers.get("X-Requested-With") == "XMLHttpRequest" or "fetch" in flow.request.headers.get("User-Agent", "").lower():
        print(f"Fetch/XHR Request URL: {flow.request.url}")
