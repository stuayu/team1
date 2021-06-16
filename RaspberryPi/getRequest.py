import requests

response = requests.get('http://localhost:8000/db/student')
print(response.status_code)    # HTTPのステータスコード取得
print(response.text)    # レスポンスのHTMLを文字列で取得