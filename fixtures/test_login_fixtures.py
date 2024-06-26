#
# # tests/test_login_fixtures.py
# import pytest
# import requests
#
# BASE_URL = "http://192.168.30.39:5000/api/v1/"
# AUTH_URL = "http://192.168.30.39:5000/api/v1/users/login"
#
# @pytest.fixture(scope="session")
# def base_url():
#     return BASE_URL
#
# @pytest.fixture(scope="function")
# def api_client():
#     return requests.Session()
#
# # @pytest.fixture(scope="session")
# def auth_token():
#     auth_data = {
#         "action": "login",
#         "username": "admin",
#         "password": "admin"
#     }
#     response = requests.post(AUTH_URL, json=auth_data)
#     data = response.json()['data']
#     headers = {}
#     if 'access_token' in data:
#         headers['X-Access-Token'] = data['access_token']
#     assert response.status_code == 200, "Failed to obtain access token"
#     return headers
# auth_token()
#
