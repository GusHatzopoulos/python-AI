import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200