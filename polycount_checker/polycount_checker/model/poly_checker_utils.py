from pymxs import runtime as rt
import importlib
from ..model import poly_checker_variables as pv
importlib.reload(pv)
from typing import Dict


class PolyUtil():
    def __init__(self):
        self.polycount = pv.POLYCOUNT
        self.lod = pv.AVAILABLE_LOD
        self.excluded_obj = self.get_excluded_objects(pv.EXCLUDE)
        self.file_type = pv.BODY_TYPE
        self.invalid_object_list = []

        self.check_results : Dict[str, Dict[str,str]] = {}
        self.count = pv.COUNT
        self.status = pv.STATUS_INT
        self.diff = pv.DIFF

        self.auto_set_file_type()
        self.init_dicts()
        self.sort_objects()
        self.validate = 0

    def init_dicts(self):
        self.scene_object = self.init_scene_dict([])
        self.scene_polycount = self.init_scene_dict(0)

    
    def init_scene_dict(self, init_value: any):
        def value():
            return [] if isinstance(init_value, list) else init_value
        if(self.file_type in (pv.BODY_TYPE,pv.RACER_TYPE)):
            return {
                pv.BODY:{
                    pv.GHR:value(),
                    pv.G0:value(),
                    pv.G1:value(),
                    pv.G2:value()
                },
                pv.ENGINE:{
                    pv.GHR:value(),
                    pv.G0:value(),
                    pv.G1:value(),
                    pv.G2:value()
                },
                pv.WIPERS:{
                    pv.GHR:value(),
                    pv.G0:value(),
                    pv.G1:value(),
                    pv.G2:value()
                }
            }
        elif(self.file_type == pv.INTERIOR_TYPE):
            return {
                pv.INTERIOR:{
                    pv.GHR:value(),
                    pv.G0:value(),
                    pv.G1:value(),
                    pv.G2:value()
                }
            }
        else:
            scene_dict = {pv.RIMS:{}}
            all_objects = self.get_all_objects()
            for obj in all_objects:
                if(pv.TIRE not in obj.name):
                    scene_dict[pv.RIMS][obj.name] = value()
            return scene_dict

    def set_file_type(self, file_type):
        self.file_type = file_type
    
    def get_file_type(self):
        return self.file_type
    
    def auto_set_file_type(self):
        all_objects = self.get_all_objects()
        for obj in all_objects:
            if(pv.RIMS in obj.name and obj.layer.name in self.lod):
                self.set_file_type(pv.RIM_TYPE)
                break
            elif(pv.INTERIOR in obj.name):
                self.set_file_type(pv.INTERIOR_TYPE)
                break
            elif(pv.BODY in obj.name):
                self.set_file_type(pv.BODY_TYPE)
                break
    
    def get_all_objects(self):
        all_objects = []
        for obj in rt.objects:
            if(rt.ClassOf(obj) == rt.Editable_Poly):
                if(obj.name.lower() in pv.SKIP_OBJECTS):
                    print("Skipping:",obj.name)
                all_objects.append(obj)
        return all_objects
    
    def get_parts(func):
        def wrapper(self, obj, *args, **kargs):
            name = obj.name
            name_part = name.split('_')
            return func(self,name_part, *args,**kargs)
        return wrapper
    
    def get_excluded_objects(self, exclude_dict):
        list = []
        for k,v in exclude_dict.items():
            for obj in v:
                list.append(obj)
        return list
    
    @get_parts
    def get_lod_part(self, name_part):
        lod_part = name_part[0]
        try:
            if lod_part in self.lod:
                return lod_part
            else:
                return pv.INVALID
        except Exception as e:
            print(f"detect invalid object: {name_part[-1]}")
            return pv.INVALID
        
    @get_parts
    def get_name_part(self, name_part):
        try:
            return name_part[1]
        except Exception as e:
            print(f"detect invalid object: {name_part[-1]}")
            return name_part[-1]
    
    def sort_objects(self):
        all_objects = self.get_all_objects()
        for obj in all_objects:
            lod_part = self.get_lod_part(obj)
            name_part = self.get_name_part(obj)
            if(lod_part == pv.INVALID):
                self.invalid_object_list.append(obj)
                continue
            if(lod_part != None):
                if(self.file_type == 0 or self.file_type == 1):
                    if(name_part in pv.EXCLUDE[pv.ENGINE]):
                        self.scene_object[pv.ENGINE][lod_part].append(obj)
                    elif(name_part in pv.EXCLUDE[pv.WIPERS]):
                        self.scene_object[pv.WIPERS][lod_part].append(obj)
                    elif(name_part not in pv.EXCLUDE[pv.RIMS]):
                        self.scene_object[pv.BODY][lod_part].append(obj)
                elif(self.file_type == 2):
                    self.scene_object[pv.INTERIOR][lod_part].append(obj)
                else:
                    if(pv.TIRE not in name_part):
                        self.scene_object[pv.RIMS][obj.name].append(obj)
    
    def get_polycount(self):
        #try:
        if(self.file_type == 0 or self.file_type == 1):
            types = [pv.BODY,pv.ENGINE,pv.WIPERS]
        elif(self.file_type == 2):
            types = [pv.INTERIOR]
        else:
            types = [pv.RIMS]
        if(self.file_type == 3):
            self.calculate_rim_polycount(type=types[-1])
        else:
            self.calculate_polycount(types_list=types)
        
       # except Exception as e:
           # print(e)
    def calculate_polycount(self, types_list: list[str]):
        for type in types_list:
            for lod,obj_list in self.scene_object[type].items():
                if len(obj_list) > 0:                        
                    for obj in obj_list:
                        self.scene_polycount[type][lod] += int(obj.numVerts)

    def calculate_rim_polycount(self,type: str):
        for lod,obj_list in self.scene_object[type].items():
            if len(obj_list) > 0:                        
                for obj in obj_list:                        
                    self.scene_polycount[type][obj.name] = int(obj.numVerts)
    def determine_rim_num(self):
        rims = rt.safeExecute("$*G0_Rim*")
        rim = rims[0]
        name_count = rim.name.split("_")
        rim_num = len(rims)
        if(len(name_count) > 3):
            return rim_num
        else:
            return 0
        

    def get_polycount_limit(self, type: str, lod):
        if type == pv.BODY:
            if self.file_type == 0:
                return self.polycount[pv.BODY][pv.STOCK][lod]
            else:
                return self.polycount[pv.BODY][pv.RACER][lod]
        elif type == pv.RIMS:
            rim_num = self.determine_rim_num()
            s = lod.split('_')
            lod = s[0]
            if(rim_num == 2):
                type = pv.RIM_2
            elif(rim_num == 4):
                type = pv.RIM_4
            return self.polycount[type][lod]
        else:
            return self.polycount[type][lod]

    def add_message(func):
        def wrapper(self : "PolyUtil"):
            func(self)
            if(len(self.invalid_object_list) > 0):
                msg = "These objects have no LODs:\n"
                for obj in self.invalid_object_list:
                    msg += f"{obj.name}\n"
                rt.messageBox(msg)
        return wrapper
    
    @add_message
    def check_polycount(self):
        self.reset_polyCount()
        self.sort_objects()
        self.get_polycount()
        for type,lods in self.scene_polycount.items():
            for lod, count in lods.items():
                limit = self.get_polycount_limit(type, lod)
                
                buffLimit = limit + limit * (pv.BUFFER/100)
                key = self.format_key(file_type = type, cur_lod = lod)
                if(count > buffLimit):
                    if(self.validate == 0):
                        self.validate = 1
                    diff = int(count - buffLimit)
                    #msg = f"{str(pv.STATUS[1])} {str(diff)}"
                    self.check_results[key] = {self.count : count,self.diff : diff, self.status : 1}
                else:
                    self.check_results[key] = {self.count : count, self.diff: 0, self.status : 0}

    def format_key(self,file_type: str, cur_lod: str):
        if(self.file_type == pv.RIM_TYPE):
            return f"{str(cur_lod)}"
        else:
            return f"{str(file_type)} {str(cur_lod)}"
                    
        
    def reset_polyCount(self):
        self.check_results.clear()
        self.invalid_object_list.clear()
        self.clear_dict()
        self.init_dicts()

    def clear_dict(self):
        self.scene_object.clear()
        self.scene_polycount.clear()
    
    def toggle_polycount(self):
        rt.execute("""
            fn ToggleViewportPolycount =
            (
                local vp = viewport.activeViewport

                local isOn = viewport.getShowStatistics vp #triangleCount

                viewport.setShowStatistics vp #triangleCount (not isOn)
                viewport.setShowStatistics vp #polygonCount (not isOn)

                completeRedraw()
            )
        """)
        rt.ToggleViewportPolycount()
def validator():
        try:
            util = PolyUtil()
            util.check_polycount()
            polycount = {}
            if(util.validate == 1):
                polycount['Check lai polycount'] = {}
            return polycount
        except Exception as e:
            print(e)
        



                
    
    