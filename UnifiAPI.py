import requests
from http.cookiejar import MozillaCookieJar
import json

class UnifiAPI:
    def __init__(self, apiUrl, apiAccount, apiPassword):
        self.apiAccount     = apiAccount,
        self.apiPassword    = apiPassword
        self.apiUrl         = apiUrl
        self.headers = {"Accept": "application/json","Content-Type": "application/json"}
        json_data       = {
                            'username': self.apiAccount[0],
                            'password': self.apiPassword
            }
        self.s = requests.Session() 
        response        = self.s.post(f'https://{self.apiUrl}/api/auth/login', json=json_data, headers = self.headers, verify=False)
        print(response.status_code)

    def getSites(self):
        return self.s.get(f'https://{self.apiUrl}/proxy/network/api/self/sites',headers = self.headers, verify=False).json()['data']
    
    def getClients(self, siteName):
        return self.s.get(f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/stat/sta').json()['data']
        
    def getUnifiSiteDevices(self, siteName):
        return self.s.get(f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/stat/device').json()['data']
