# coding=utf-8
#**********************************************************************************
#    This Class will store the info for the Cisco ACI Repository and perform      #
#	 the Post for creation                                                        #
#    The Class will usage the following information:                              #
#		Annotation                                                                #
#		Authentication Type                                                       #
#		Description                                                               #
#		Distinguished Name                                                        #
#		Host IP Address                                                           #
#		Repository Name                                                           #
#		Repository Alias Name                                                     #
#		Protocol (SFTP, FTP, SCP)                                                 #
#		Backup Server Remote Path                                                 #
#		Backup Server Remote Port                                                 #
#	    Backup Server UserName                                                    #
#**********************************************************************************

import requests

#################
#Class Definition
#################

class Repository:
    
    def __init__ (sefl, annotation, authType, descr, dn, host, name, nameAlias, protocol, remotePath, remotePort, userName):
        sefl.__annotation = annotation
        sefl.__authType = authType
        sefl.__descr = descr
        sefl.__dn = dn
        sefl.__host = host
        sefl.__name = name
        sefl.__nameAlias = nameAlias
        sefl.__protocol = protocol
        sefl.__remotePath = remotePath
        sefl.__remotePort = remotePort
        sefl.__userName = userName

    ######################
    #Attributes Definition
    ######################


    #Annotation for remote backup server
    __annotation = ""

    #Authentication type for remote backup server
    __authType = ""

    #Description for remote backup server
    __descr = ""

    #Fabric path for remote backup server
    __dn = ""

    #Host IP Address for backups
    __host = ""

    #Name of the repository
    __name = ""

    #Alias for the Repository
    __nameAlias = ""

    #Protocol for remote backup server
    __protocol = ""

    #Path Directory for Backup Server
    __remotePath = ""

    #Remote port remote backup server
    __remotePort = ""

    #Username remote backup server
    __userName = ""

    #######################
    #Get Methods definition
    #######################

    #Get Annotation Method
    def getAnnotation(self):
        return self.__annotation
    
    #Get Authentication Type Method
    def getAuthType(self):
        return self.__authType

    #Get Description Method
    def getDescription(self):
        return self.__descr

    #Get Distinguished Name Method
    def getDN(self):
        return self.__dn

    #Get Host Method
    def getHost(self):
        return self.__host

    #Get Name Method
    def getName(self):
        return self.__name

    #Get Name Alias Method
    def getNameAlias(self):
        return self.__nameAlias

    #Get Protocol Method
    def getProtocol(self):
        return self.__protocol

    #Get Remote Path Method
    def getRemotePath(self):
        return self.__remotePath

    #Get Remote Port Method
    def getRemotePort(self):
        return self.__remotePort

    #Get User Name Method
    def getUserName(self):
        return self.__userName

    ############
    #Main Method
    ############

    #def repoCreation(self, ip, node, interface, cookie):
    def repoCreation(self, APIC, Cookie):
        #URL Generation 
        URL = "https://%s/api/node/mo/uni/fabric/path-%s.json" % (APIC, self.__name)

        #Payload generation with RepoConstant.py values
        payload = '{"totalCount":"1","imdata":[{"fileRemotePath":{"attributes":{"annotation":"%s","authType":"%s","descr":"%s","dn":"%s","host":"%s","name":"%s","nameAlias":"%s","protocol":"%s","remotePath":"%s","remotePort":"%s","userName":"%s"}}}]}' % (self.__annotation, self.__authType, self.__descr, self.__dn, self.__host, self.__name, self.__nameAlias, self.__protocol, self.__remotePath, self.__remotePort, self.__userName)

        error = False
        
        #Hearder Type Json format
        headers = {'Content-Type': 'application/json'}
        
        #Post Method
        xmlpost = requests.post(URL, data=payload, cookies=Cookie, verify=False, headers=headers)
        
        #We Check the Script Result after the post method
        #If result is 200 everything work fine
        #if the results is not 200 was a problem in the post
        if xmlpost.status_code == 200:
            print ("\t[OK] Repository %s Created" % self.__name)
        else:
            print ("\t[FAILED] Creating %s Repository" % self.__name)
            print (xmlpost.text)
            error = True
        return error