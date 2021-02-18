users = {
    'Alan': {
        'online': False
    },
    'Jeff': {
        'online': True
    },
    'Sarah': {
        'online': False
    }
}


def count_online(users):
    return sum(user['online'] for user in users.values())


print(count_online(users))