import requests
from requests.api import request

response = requests.get('http://localhost:8000/db/student_all')
print(response.status_code)    # HTTPのステータスコード取得
print(response.text)    # レスポンスのHTMLを文字列で取得

#data引数に、postパラメータを渡す
payload = {'ID': 'value1','IDm':'value2'}
res =  requests.post('http://localhost:8000/db/student_all',data=payload)


