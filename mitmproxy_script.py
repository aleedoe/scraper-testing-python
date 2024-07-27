from mitmproxy import http

# Nama file log
log_file = 'response-history.txt'

def log_to_file(message: str) -> None:
    with open(log_file, 'a') as f:
        f.write(message + '\n')

def request(flow: http.HTTPFlow) -> None:
    if flow.request.headers.get("X-Requested-With") == "XMLHttpRequest" or "fetch" in flow.request.headers.get("User-Agent", "").lower():
        log_to_file(f"Fetch/XHR Request URL: {flow.request.url}")
    
def response(flow: http.HTTPFlow) -> None:
    if flow.response.headers.get("Content-Type", "").startswith("application/json"):
        response_text = flow.response.text
        log_to_file(f"Response JSON URL: {flow.request.url}")
        log_to_file(response_text)
