__author__ = 'root'

import json
from Metadata import Metadata
import sys
from settings import settings

class Protocol:
    def __init__(self,test = None):
        self.test = False
        if test != None:
            self.test = True

    def protocol(self,params):
        aux = json.loads(params)
        type = aux["type"]
        lista = aux["lista"]
        creds = None

        if aux.has_key('credentials'):
            creds = {'oauth':{'consumer_key':'' + str(aux['credentials']['oauth']['consumer_key']) + '','consumer_secret':'' + str(aux['credentials']['oauth']['consumer_secret']) + '','token_key':'' + str(aux['credentials']['oauth']['token_key']) + '','token_secret':'' + str(aux['credentials']['oauth']['token_secret']) + ''}}

        result = False

        self.configDb(type,creds)

        if type == "insert":
            result = self.insert(lista)
        elif type == "select":
            result = self.select(lista[0])
        elif type == "update":
            result = self.update(lista)
        elif type == "delete":
            result = self.delete(lista)
        elif type == "parent":
            result = self.getParent(lista[0])
        elif type == "deleteFolder":
            result = self.deleteFolder(lista[0])
        elif type == "deleteMetadataUser":
            result = self.deleteMetadataUser(lista)
        elif type == "selectMetadataUser":
            result = self.selectMetadataUser(lista[0]['user_eyeos'])
        elif type == "rename":
            result = self.renameMetadata(lista[0])
        elif type == "insertDownloadVersion":
            result = self.insertDownloadVersion(lista[0])
        elif type == "updateDownloadVersion":
            result = self.updateDownloadVersion(lista[0])
        elif type == "deleteDownloadVersion":
            result = self.deleteDownloadVersion(lista[0]['id'],lista[0]['user_eyeos'])
        elif type == "getDownloadVersion":
            result = self.getDownloadVersion(lista[0])
        elif type == "recursiveDeleteVersion":
            result = self.recursiveDeleteVersion(lista[0])
        elif type == "deleteEvent":
            result = self.deleteEvent(lista)
        elif type == "updateEvent":
            result = self.updateEvent(lista)
        elif type == "selectEvent":
            result = self.selectEvent(lista[0]['type'],lista[0]['user_eyeos'],lista[0]['calendar'])
        elif type == "insertEvent":
            result = self.insertEvent(lista)
        elif type == "insertCalendar":
            result = self.insertCalendar(lista)
        elif type == "deleteCalendar":
            result = self.deleteCalendar(lista)
        elif type == "selectCalendar":
            result = self.selectCalendar(lista[0])
        elif type == "updateCalendar":
            result = self.updateCalendar(lista)
        elif type == "deleteCalendarUser":
            result = self.deleteCalendarUser(lista[0]['user_eyeos'])
        elif type == "selectCalendarsAndEvents":
            result = self.selectCalendarsAndEvents(lista[0]['user_eyeos'])
        elif type == "getMetadataFile":
            result = self.getMetadataFile(lista[0]['id'],lista[0]['cloud'])
        elif type == "lockFile":
            result = self.lockFile(lista[0])
        elif type == "updateDateTime":
            result = self.updateDateTime(lista[0])
        elif type == "unLockFile":
            result = self.unLockFile(lista[0])

        return json.dumps(result)

    def insert(self, lista):
        self.metadata.insert(lista)
        return True

    def select(self, lista):
        return self.metadata.select(lista)

    def update(self, lista):
        self.metadata.update(lista)
        return True

    def delete(self, lista):
        self.metadata.delete(lista)
        return True

    def getParent(self, lista):
        return self.metadata.getParent(lista)

    def deleteFolder(self, lista):
        self.metadata.deleteFolder(lista)
        return True

    def deleteMetadataUser(self, lista):
        self.metadata.deleteMetadataUser(lista)
        return True

    def selectMetadataUser(self,user):
        return self.metadata.selectMetadataUser(user)

    def renameMetadata(self, metadata):
        self.metadata.renameMetadata(metadata)
        return True

    def insertDownloadVersion(self,metadata):
        self.metadata.insertDownloadVersion(metadata)
        return True

    def updateDownloadVersion(self,metadata):
        self.metadata.updateDownloadVersion(metadata)
        return True

    def deleteDownloadVersion(self,id,user):
        self.metadata.deleteDownloadVersion(id,user)
        return True

    def getDownloadVersion(self, lista):
        return self.metadata.getDownloadVersion(lista)

    def recursiveDeleteVersion(self,lista):
        self.metadata.recursiveDeleteVersion(lista)
        return True

    def deleteEvent(self,lista):
        self.metadata.deleteEvent(lista)
        return True

    def updateEvent(self,lista):
        self.metadata.updateEvent(lista)
        return True

    def selectEvent(self,type,user,calendarid):
        return self.metadata.selectEvent(type,user,calendarid)

    def insertEvent(self,lista):
        self.metadata.insertEvent(lista)
        return True

    def insertCalendar(self,lista):
        self.metadata.insertCalendar(lista)
        return True

    def deleteCalendar(self,lista):
        self.metadata.deleteCalendar(lista)
        return True

    def selectCalendar(self,data):
        return self.metadata.selectCalendar(data)

    def updateCalendar(self,lista):
        self.metadata.updateCalendar(lista)
        return True

    def deleteCalendarUser(self,user):
        self.metadata.deleteCalendarUser(user)
        return True

    def selectCalendarsAndEvents(self,user):
        return self.metadata.selectCalendarsAndEvents(user)

    def getMetadataFile(self,id,cloud):
        return self.metadata.getMetadataFile(id,cloud)

    def lockFile(self,data):
        return self.metadata.lockFile(data)

    def updateDateTime(self,data):
        return self.metadata.updateDateTime(data)

    def unLockFile(self,data):
        self.metadata.unLockFile(data)
        return True

    def configDb(self,type,creds = None):
        if self.test == True:
            name = "test.u1db"
            name2 = "test1.u1db"
        else:
            name = "metadata.u1db"
            name2 = None
            if type == "deleteEvent" or type == "updateEvent" or type == "selectEvent" or type == "insertEvent" or type == "insertCalendar" or type == "deleteCalendar" or type == "selectCalendar" or type == "updateCalendar" or type == 'deleteCalendarUser' or type == 'selectCalendarsAndEvents':
                name = "calendar.u1db"
            elif type == "insertDownloadVersion" or type == "updateDownloadVersion" or type == "deleteDownloadVersion" or type == "getDownloadVersion":
                name = "downloadfile.u1db"
            elif type == "recursiveDeleteVersion" or type == "deleteMetadataUser":
                name2 = "downloadfile.u1db"
            elif type == "getMetadataFile" or type == "lockFile" or type == "updateDateTime" or type == "unLockFile":
                name = "lockfile.u1db"

        self.metadata = Metadata(name,creds,name2)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        protocol = Protocol()
        print (protocol.protocol(str(sys.argv[1])))
    else:
        print ('false')

