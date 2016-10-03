import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning, SNIMissingWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)
import ast

from config_settings import ConfigSettings as CS

class LibraryTest:
    urlconfig=CS(r'./libraryTest.ini')
    def __init__(self,rest_ip):
        self.rest_ip=rest_ip
        self.basic_url="http://"+self.rest_ip+":5000"
        self.ok_flag=True
    def checkAPI (self):
        for api in self.urlconfig.Config.sections():
            method=self.urlconfig.get(api,"method")
            expected_result = self.urlconfig.get(api,"expected_result")
            result_type = self.urlconfig.get(api,"result_type")
            url=self.urlconfig.get(api,"url")
            url=self.basic_url+url
            try:
                if method=='GET':
                    response=requests.get(url)
                elif method=='POST':
                    response=requests.post(url)
                elif method=='PUT':
                     response=requests.put(url)
                elif method=='DELETE':
                     response=requests.delete(url)
                else:
                    print "not a valid method for %s. skip" %(url)
                    continue
                if result_type == 'value':
                    if ast.literal_eval(response._content) <> ast.literal_eval(expected_result):
                        print colurs.FAIL+ "response code:%s ,for request:%s and response: %s" %(response.status_code,url, response._content ) +colurs.ENDC
                        if self.ok_flag:
                            self.ok_flag=False
                    else:
                        print colurs.OKGREEN + "%s %s OK" %(method,url) +colurs.ENDC
                else:
                    if response.status_code <> int(expected_result):
                        print colurs.FAIL+ "response code:%s ,for request:%s and response: %s" %(response.status_code,url, response._content ) +colurs.ENDC
                        if self.ok_flag:
                            self.ok_flag=False
                    else:
                        print colurs.OKGREEN + "%s %s OK" %(method,url) +colurs.ENDC
            except requests.ConnectionError:
                    print "connection error to request:%s" %(url)

class colurs:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

if __name__ == "__main__":
    san=LibraryTest(sys.argv[1])
    print "begin REST Service sanity check"
    san.checkAPI()
    if san.ok_flag:
        print colurs.OKGREEN+ "Library test completed successfully!"+colurs.ENDC
    else:
        print colurs.FAIL+ "REST test completed with errors"+colurs.ENDC
