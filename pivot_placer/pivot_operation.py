from pymxs import runtime as rt
import pymxs
class PivotOperation():
    def __init__(self):
        self.source_list = []
        self.target_list = []
        self.store_source_pos = {}
    def get_selected_object(self):
        return rt.selection
    def get_source_objects(self):
        try:
            self.source_list.clear()
            selected_obj = self.get_selected_object()
            for obj in selected_obj:
                self.source_list.append(obj)
        except Exception as e:
            print(e)
    def get_target_objects(self):
        try:
            self.target_list.clear()
            selected_obj = self.get_selected_object()
            for obj in selected_obj:
                self.target_list.append(obj)
        except Exception as e:
            print(e)
    def get_all_object(self):
        geo = [obj for obj in rt.geometry if rt.classof(obj) == rt.Editable_Poly]
        return geo
    def transfer_pivot(self):
        with pymxs.undo(True):
            try:
                target_map = {self.get_object_name(obj) : obj for obj in self.target_list} #Key = name of obj, value = obj in the target list
                for source_obj in self.source_list:
                        source_name = self.get_object_name(source_obj)
                        if(source_name in target_map):
                            target_obj = target_map[source_name]
                            self.copy_pivot(source_obj, target_obj)
                rt.redrawViews()
            except Exception as e:
                    print(str(e))
    def copy_pivot(self, src, tgt):
        rt.src = src
        rt.tgt = tgt
        rt.execute("""
        rot = tgt.rotation - src.rotation
        brot = inverse(rot as quat)
        tgt.pivot = src.pivot
        in coordsys local tgt.rotation *= brot
        tgt.objectoffsetrot *= brot
        tgt.objectoffsetpos *= brot
        """)
        rt.redrawViews()
        
    def get_object_name(self, object):
        res = object.name.split('_')
        return res[1]
    def rotate_pivot(self, src, tgt):
        rot = tgt.rotation - src.rotation
        brot = rt.Inverse(rot)
        print(brot)
        tgt.pivot = src.pivot
        with rt.SetRefCoordSys('local'):
            tgt.rotation *=brot
            tgt.objectoffsetrot *= brot
            tgt.objectoffsetpos *=brot