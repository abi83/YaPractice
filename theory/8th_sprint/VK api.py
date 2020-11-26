import requests

def get_friends(user_id):
    access_token = 'some_secret_token'  # temporary token
    url = 'https://api.vk.com/method/friends.get'
    data = {
        'user_id': user_id,
        'v': 5.52,
        'access_token': access_token,
    }
    r = requests.post(url, data)
    friends_list = r.json()['response']['items']
    return friends_list

user_id=531301803
print(get_friends(user_id))