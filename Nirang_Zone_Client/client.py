import requests

URL = 'http://127.0.0.1:8000'

def get_token():

    # get auth token
    url = f'{URL}/api/auth/'
    response = requests.post(url, data={
        'username':'<username>',
        'password':'<password>'
    })
    return response.json()

def get_data():

    urls = f'{URL}/api/users_list/'
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(urls,headers=header)
    users_data = response.json()

    for user in users_data:
        print(user)

def create_new(count):

    urls = f'{URL}/api/users_list/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "id": f'{count}',
        "user_id": f"14MSE100{count}",
        "user_name": "Faf Du Plessis",
        "user_age": 24,
        "user_ranking": 2.5
    }
    response = requests.post(urls,data=data, headers=header)
    print(response.text)

def edit_data(user_id):

    urls = f'{URL}/api/users_list/{user_id}/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "user_name": "Sachin Tendulkar",
        "user_age": 47,
        "user_ranking": 18
    }
    response = requests.put(urls,data=data, headers=header)
    print(response.text)

def delete_data(user_id):

    urls = f'{URL}/api/users_list/{user_id}/'
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(urls, headers=header)
    print(response.status_code)

# here are the commands function calls for API call testing purpose
# 1. to get all the user from the database
# get_data()

# 2. create new user data with different ID
# for i in range(5):
#
#     create_new(i)

# 3. to update any value of a specific user
# edit_data(15)

# 4. delete a range of users randomly
# for j in range(20):
#
#     if j > 10:
#
#         delete_data(e)