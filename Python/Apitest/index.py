import requests

# example: list of fake posts
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()  # list of dicts
    for post in posts[:5]:  # print first 5
        print(f"Post {post['id']} Title: {post['title']}")
else:
    print("Error:", response.status_code)
