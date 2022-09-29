# This is a sample Python script.
import json

import jsonpath
import requests

if __name__ == '__main__':
    # b = 'https://www.googleapis.com/blogger/v3/blogs/920308070457707190/posts?key=AIzaSyA9sQzsGZ_C35C0crbzH8Dx3zQdg7hzcZo'
    b2 = 'https://www.googleapis.com/blogger/v3/blogs/920308070457707190?key=AIzaSyA9sQzsGZ_C35C0crbzH8Dx3zQdg7hzcZo'

    search = 'https://www.googleapis.com/blogger/v3/blogs/920308070457707190/posts/search?q=dummy&key=AIzaSyA9sQzsGZ_C35C0crbzH8Dx3zQdg7hzcZo'

    add_n = 'https://www.googleapis.com/blogger/v3/blogs/920308070457707190/posts'
    myobj = {
        "kind": "blogger#post",
        "blog": {
            "id": "920308070457707190"
        },
        "title": "A new post",
        "content": "With <b>exciting</b> content..."
    }



    key = {
        'Authorization': 'Bearer ya29.a0Aa4xrXMPW2keZ_khpx_pVgHHDQMnhT2EBPdzYrxE72AcBzgNXWhiidBkpNeoz3WMj99_JYvyhWc3mvF1Al0X_jEnPh9TiNk1JObscX97Z87cIZS7_xPmmpF3Ze4fV5xfSG-Ch4EVWqVUPMCvz4Fxnx7KDM_8aCgYKATASARMSFQEjDvL9w16xRjCsWtubANEoZwzJ4Q0163',
        'content-Type': 'application/json'
    }
    res = requests.post(add_n, json=myobj, headers=key)
    # print(json.dumps(res.json(), indent=4))
    print(res.text)
    # a = jsonpath.jsonpath(json.loads(res.text), 'posts.totalItems')
    # print(jsonpath.jsonpath(json.loads(res.text), 'name'))

    # print(res.headers.get("Content-Type"))
    # abc = json.loads(res.text)
    # xyz = jsonpath.jsonpath(abc, 'items[0].blog')
    # print(xyz)
    # print(type(abc))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print(res.headers["Content-Type"])
