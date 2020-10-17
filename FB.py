import requests
import json
token = "EAAiweZAOwyGgBACMVa7cFwk6nOlrdRAy5KMgIdVJaUOHKqPGU58F7B5MUf5p1oZAKv7OCsWflVHyZCaw8YHdapCMlnbPP9dpKjq1eGs6qRKr86Wj5MEqZBaZBcEoaKDCY1ShiJBhhZABPzVmwDkBuIYpKmvn76MHTpxVLVnIFlZAZCIxFZAG4VFyZAZCPEh151eJLQokZBjY4egSUnIRiMAo7i1e2jyyPdxBKNZC2Twa8zJQE8gZDZD"

# 請求時，需要的特別接口參數，請在token值後加入 &及參數
res = requests.get('https://graph.facebook.com/v8.0/me?access_token=%s&fields=id,name,email,gender' %token)

# 查看是否請求成功並打印
print(res)
print(res.text)

# 將資料轉換成json
data = json.loads(res.text) 

# 打印資料
print(data)