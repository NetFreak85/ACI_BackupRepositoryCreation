# coding=utf-8
#***********************************************************************************************************************#
#    This script will help you to create a Backup Repository in  Application Centric Infrastructure (ACI)               #
#	 The script will create a new repository with the following information:                                            #
#		Annotation                                                                                                      #
#		Authentication Type                                                                                             #
#		Description                                                                                                     #
#		Distinguished Name                                                                                              #
#		Host IP Address                                                                                                 #
#		Repository Name                                                                                                 #
#		Repository Alias Name                                                                                           #
#		Protocol (SFTP, FTP, SCP)                                                                                       #
#		Backup Server Remote Path                                                                                       #
#		Backup Server Remote Port                                                                                       #
#	    Backup Server UserName                                                                                          #
#                                                                                                                       #
#   --usage:                                                                                                            #
#             ./RepositoryCreation.py                                                                                   #
#         or  python RepositoryCreation.py                                                                              #
#                                                                                                                       #
# date:  13/09/2021 Created                                                                                             #
#***********************************************************************************************************************#

import requests
import json
import getCookie
import Constant
import RepoConstant
from Repository import Repository

#Get Resquest to APICs and return a json object
def get_request(url, cookie):
	r = requests.get(url, cookies=cookie, verify=False)
	json_obj = json.loads(r.content)
	return json_obj

#Create Repository via Class Repository
def createRepository(APIC, Cookie):
    repo = Repository (RepoConstant.annotation, RepoConstant.authType, RepoConstant.descr, RepoConstant.dn, RepoConstant.host, RepoConstant.name, RepoConstant.nameAlias, RepoConstant.protocol, RepoConstant.remotePath, RepoConstant.remotePort, RepoConstant.userName) 
    repo.repoCreation(APIC, Cookie)

#Main program
if __name__ == '__main__':
    Cookie = getCookie.get_cookie(Constant.apic, Constant.User, Constant.Password)
    createRepository(Constant.apic,Cookie)