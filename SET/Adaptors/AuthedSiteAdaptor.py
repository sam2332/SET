from SET.core import Core


class AuthedSiteAdaptor:
    loggedIn = False

    def __init__(self, core=None):
        if core is None:
            core = Core()
        self.core = core
        self.driver = self.core.getDriver()
        if self.driver is None:
            self.core.startSession()
            self.driver = self.core.getDriver()
        self._tick()

    def _isLoggedIn(self):
        pass

    def _login(self):
        pass

    def get(self, url):
        self._tick()
        self.core.get(url)
        return self.core

    def _tick(self):
        if self._isLoggedIn():
            self.loggedIn = True
            return True
        else:
            self.loggedIn = self._login()
            return self.loggedIn
