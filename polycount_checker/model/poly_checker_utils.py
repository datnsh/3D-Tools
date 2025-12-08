from pymxs import runtime as rt
import model.poly_checker_variables as pv

class PolyUtil():
    def __init__(self):
        self.polycountDict = pv.POLYCOUNT
        self.LOD = pv.AVAILABLELOD
        self.excludedObj = self.getExcludedObjects(pv.EXCLUDE)
        self.polycountTypeDict = self.getPolycountTypeDict(-1)
        self.fileType = -1
        
        self.polyDict = {k : 0 for k in self.LOD}
        self.objDict = {k : [] for k in self.LOD}

        self.sortObjects()

    def getAllObjects(self):
        return rt.objects
    def getParts(func):
        def wrapper(self, obj, *args, **kargs):
            name = obj.name
            namePart = name.split('_')
            return func(self,namePart, *args,**kargs)
        return wrapper
    def getExcludedObjects(self, excludeDict):
        list = []
        for k,v in excludeDict.items():
            for obj in v:
                list.append(obj)
        return list
    @getParts
    def getLODPart(self, namePart):
        lodPart = namePart[0]
        try:
            if lodPart in self.LOD:
                return lodPart
            else:
                return pv.INVALID
        except Exception as e:
            print(e)
            return pv.INVALID
        
    @getParts
    def getNamePart(self, namePart):
        try:
            return namePart[1]
        except Exception as e:
            print(e)
            return namePart[-1]
    
    def sortObjects(self):
        allObjects = self.getAllObjects()
        for obj in allObjects:
            lodPart = self.getLODPart(obj)
            namePart = self.getNamePart(obj)
            if(lodPart != None):
                if(self.fileType == -1 and (namePart not in self.excludedObj)):
                    self.objDict[lodPart].append(obj)
                elif(self.fileType == 3 and (namePart in pv.EXCLUDE[pv.ENGINE])):
                    self.objDict[lodPart].append(obj)
                elif(self.fileType == 2 and (namePart in pv.EXCLUDE[pv.WIPERS])):
                    self.objDict[lodPart].append(obj)
    def getPolycount(self):
        for key in self.LOD:
            for obj in self.objDict[key]:
                try:
                    self.polyDict[key] += obj.numVerts
                    print(f"Add {obj.name} to {key}")
                except Exception as e:
                    print(e)
                    continue

    def getPolycountTypeDict(self, type = int()):
        if type == 0:
            return self.polycountDict[pv.BODY][pv.RACER]
        elif type == 1:
            return self.polycountDict[pv.INTERIOR]
        elif type == 2:
            return self.polycountDict[pv.WIPERS]
        elif type == 3:
            return self.polycountDict[pv.ENGINE]
        else:
            return self.polycountDict[pv.BODY][pv.STOCK]
        # match(type):
        #     case 0:
        #         return self.polycountDict[pv.BODY][pv.RACER]
        #     case 1:
        #         return self.polycountDict[pv.INTERIOR]
        #     case 2:
        #         return self.polycountDict[pv.WIPERS]
        #     case 3:
        #         return self.polycountDict[pv.ENGINE]
        #     case _:
        #         return self.polycountDict[pv.BODY][pv.STOCK]

    def checkPolycount(self, k, v):
        if(k == pv.INVALID):
            if(v > 0):
                return pv.STATUS[4]
            else:
                return pv.STATUS[0]
        if(v > self.polycountTypeDict[k]):
            limit = self.polycountTypeDict[k]
            buffLimit = limit + limit*(20/100)
            print(buffLimit)
            if(v > buffLimit):
                status = pv.STATUS[1]
            else:
                status = pv.STATUS[2]
            status += str(v - buffLimit)
            return status
        else:
            return pv.STATUS[0]
        
    def resetPolyCount(self):
        self.polyDict = {key: 0 for key in self.polyDict}



                
    
    