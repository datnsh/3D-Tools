from pymxs import runtime as rt
import importlib, copy
import model.poly_checker_variables as pv
importlib.reload(pv)


class PolyUtil():
    def __init__(self):
        self.polycount = pv.POLYCOUNT
        self.LOD = pv.AVAILABLELOD
        self.excludedObj = self.getExcludedObjects(pv.EXCLUDE)
        self.fileType = self.getFileType()
        self.invalidObjectList = []
        
        self.polyDict = copy.deepcopy(pv.POLYDICT)
        self.objDict = copy.deepcopy(pv.OBJECTDICT)
        self.checkResults = {}
        self.sortObjects()

    def getFileType(self):
        all_objects = self.getAllObjects()
        for obj in all_objects:
            if(pv.RIMS in obj.name and obj.layer.name in self.LOD):
                return 3
            elif(pv.INTERIOR in obj.name):
                return 2
        return 0
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
            print(f"detect invalid object: {namePart[-1]}")
            return pv.INVALID
        
    @getParts
    def getNamePart(self, namePart):
        try:
            return namePart[1]
        except Exception as e:
            print(f"detect invalid object: {namePart[-1]}")
            return namePart[-1]
    
    def sortObjects(self):
        allObjects = self.getAllObjects()
        for obj in allObjects:
            lodPart = self.getLODPart(obj)
            namePart = self.getNamePart(obj)
            if(lodPart == pv.INVALID):
                self.invalidObjectList.append(obj)
                continue
            if(lodPart != None):
                if(self.fileType == 0):
                    if(namePart in pv.EXCLUDE[pv.ENGINE]):
                        self.objDict[pv.ENGINE][lodPart].append(obj)
                    elif(namePart in pv.EXCLUDE[pv.WIPERS]):
                        self.objDict[pv.WIPERS][lodPart].append(obj)
                    elif(namePart not in pv.EXCLUDE[pv.RIMS]):
                        self.objDict[pv.BODY][lodPart].append(obj)
                elif(self.fileType == 1):
                    self.objDict[pv.INTERIOR][lodPart].append(obj)
                else:
                    self.objDict[pv.RIMS][lodPart].append(obj)
    
    def getPolycount(self):
        #try:
        if(self.fileType == 0 or self.fileType == 1):
            types = [pv.BODY,pv.ENGINE,pv.WIPERS]
        elif(self.fileType == 2):
            types = [pv.INTERIOR]
        else:
            types = [pv.RIMS]
        for type in types:
            for lod,objList in self.objDict[type].items():
                if len(objList) > 0:                        
                    for obj in objList:
                        self.polyDict[type][lod] += int(obj.numVerts)

       # except Exception as e:
           # print(e)
        
    def getPolycountLimit(self, type, lod):
        if type == pv.BODY:
            if self.fileType == 0:
                return self.polycount[pv.BODY][pv.STOCK][lod]
            else:
                return self.polycount[pv.BODY][pv.RACER][lod]
        else:
            return self.polycount[type][lod]

    def addMessage(func):
        def wrapper(self):
            func(self)
            if(len(self.invalidObjectList) > 0):
                msg = "These objects have no LODs:\n"
                for obj in self.invalidObjectList:
                    msg += f"{obj.name}\n"
                rt.messageBox(msg)
        return wrapper
    
    @addMessage
    def checkPolycount(self):
        for type,lods in self.polyDict.items():
            for lod, count in lods.items():
                limit = self.getPolycountLimit(type, lod)
                
                buffLimit = limit + limit * (pv.BUFFER/100)
                key = f"{str(type)} {str(lod)}"
                
                if((type == pv.BODY and (self.fileType != 0 and self.fileType != 1)) or
                   (type == pv.RIMS and self.fileType != 3) or 
                   (type == pv.INTERIOR and self.fileType != 2)
                   ):
                    continue
                if(count > buffLimit):
                    msg = str(pv.STATUS[1]) + str(buffLimit - count)
                    self.checkResults[key] = [count,msg]
                else:
                    self.checkResults[key] = [count,str(pv.STATUS[0])]
                    
        
    def resetPolyCount(self):
        self.checkResults.clear()
        self.invalidObjectList.clear()
        self.clearDict(self.objDict)
        self.clearDict(self.polyDict)

    def clearDict(self, d : dict):
        for key, value in d.items():
            if isinstance(value, dict):
                self.clearDict(value)
            elif isinstance(value, list):
                value.clear()
            else:
                d[key] = 0



                
    
    