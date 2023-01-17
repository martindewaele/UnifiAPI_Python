import requests
from http.cookiejar import MozillaCookieJar
import json
import urllib3
urllib3.disable_warnings()

class UnifiAPI:
    def __init__(self, apiUrl:str, apiAccount:str, apiPassword:str) -> None:
        self.apiAccount     = apiAccount,
        self.apiPassword    = apiPassword
        self.apiUrl         = apiUrl
        self.headers = {"Accept": "application/json","Content-Type": "application/json"}
        json_data       = {
                            'username': self.apiAccount[0],
                            'password': self.apiPassword
            }
        self.s          = requests.Session()  
        response        = self.s.post(f'https://{self.apiUrl}/api/auth/login', json=json_data, headers = self.headers, verify=False)
        self.token      = response.json()['ssoAuth']['value']

    def logout(self):
        return self.s.post(f'https://{self.apiUrl}/api/logout')

    def getSites(self):
        return self.s.get(
            f'https://{self.apiUrl}/proxy/network/api/self/sites'
            ).json()['data']
    
    def getClients(self, siteName:str ='default') -> dict:
        return self.s.get(
            f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/stat/sta'
            ).json()['data']
        
    def getUnifiSiteDevices(self, siteName:str ='default') -> dict:
        return self.s.get(
            f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/stat/device'
            ).json()['data']

    def getRoutes(self, siteName:str ='default') -> dict:
        return self.s.get(
            f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/stat/routing'
            ).json()['data']

    def getPortProfiles(self, siteName:str ='default') -> dict:
        return self.s.get(
            f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/rest/portconf'
            ).json()['data']

    def getAdmins(self, siteName:str ='default') -> dict:
        return self.s.post(
            f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/cmd/<sitemgr>',
            json={'cmd': 'get-admins'}
            ).json()
    
    def getSpeedtestResults(self, siteName:str ='default') -> dict:
        return self.s.post(
            f'https://{self.apiUrl}/proxy/network/api/s/{siteName}/cmd/devmgr',
            json={'cmd': 'speedtest-status'}
            ).json()
