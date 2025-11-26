from pymxs import runtime as rt
import model.poly_checker_variables as pv

class PolyUtil():
    def __init__(self):
        self.objDict = {0:[],1:[],2:[],3:[],4:[]}
        self.polyDict = {0:0, 1:0,2:0,3:0,4:0}
        self.lodDict = pv.LOD
        self.allObjects = self.getAllObjects()
        self.sortObjects(self.allObjects, self.lodDict,self.objDict)
    def getAllObjects(self):
        return rt.objects
    def sortObjects(self,allObjects, lodDict, objDict):
        for obj in allObjects:
            name = obj.name
            nameGroup = name.split('_')
            lodNum = lodDict[nameGroup[0]]
            if(lodNum != None):
                objDict[lodNum].append(obj)
            else:
                objDict[4].append(obj)
    def checkPolycount(self):
        for key, value in self.polyDict.items():
            for obj in self.objDict[key]:
                try:
                    self.polyDict[key] += obj.numVerts
                except Exception as e:
                    print(e)
                    continue
    def resetPolyCount(self):
        self.polyDict = {key: 0 for key in self.polyDict}



                
    
    