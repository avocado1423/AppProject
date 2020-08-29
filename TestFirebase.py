import requests
from kivy.lang import Builder
import json
from kivy.app import App

class MyFirebase():
    wAPI = "AIzaSyAJpmixuiEAB5MzNHuYhqYBtOijnCLxHkI"

    def sign_up(self, email, password, first, last):
        app = App.get_running_app()
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wAPI
        signup_payload = {"email": email, "password": password, "first": first, "last": last, "returnSecureToken": True}
        signup_requests = requests.post(signup_url, data=signup_payload)
        print(signup_requests.ok)
        print(signup_requests.content.decode())
        signup_data = json.loads(signup_requests.content.decode())
        print(signup_data)

        if signup_requests.ok == True:

            refresh_token = signup_data["refreshToken"]
            localID = signup_data["localId"]
            idToken = signup_data["idToken"]
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

            app.local_id = localID
            app.idToken = idToken

            my_data = f'"email": "{email}", "password": "{password}", "first": "{first}", "last": "{last}"'
            print(my_data)

            post_request = requests.patch("https://kivy-rtdb.firebaseio.com/" + localID + ".json?auth=" + idToken,
                           data=my_data)
            print(post_request.ok)
            print(json.loads(post_request.content.decode()))


        if signup_requests.ok == False:
            pass

    def exchange_refresh_token(self):
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=" + self.wAPI
        refresh_payload = '{"grant_type": "refresh_token, "refresh_token": "%s"}'% refresh_token
        refresh_req = requests.post(refresh_url, data=refresh_payload)
        print("REFRESH OK?", refresh_req.ok)
        print(refresh_req.json())



    def sign_in(self):
        pass

