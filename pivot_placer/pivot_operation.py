from pymxs import runtime as rt
import pymxs
class PivotOperation():
    def __init__(self):
        self.source_list = []
        self.target_list = []
<<<<<<< HEAD
<<<<<<< HEAD
=======
    def clear_all_list(self):
        self.source_list.clear()
        self.target_list.clear()
>>>>>>> 199e902 (Fix bug and add gitignore)
=======
    def clear_all_list(self):
        self.source_list.clear()
        self.target_list.clear()
>>>>>>> 199e9028648d759506ba93e98e1e0e80b3ca6d5e
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
<<<<<<< HEAD
<<<<<<< HEAD
                print(str(e))
    def copy_pivot(source, target):
        source_position = source.pivot
        source_rotation = source.rotation
        target.rotation = source_rotation

        target.objectoffsetrot *= source_rotation
        target.pivot = source_position
=======
                    print("At transfer_pivot: " + str(e))
>>>>>>> 199e9028648d759506ba93e98e1e0e80b3ca6d5e
    
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
        
    def get_object_name(self, object):
        res = object.name.split('_')
        obj_name = res[1] + res[2]
        return obj_name

<<<<<<< HEAD
if __name__ == "__main__":
    po = PivotOperation()
    po.transfer_pivot()
=======
                    print("At transfer_pivot: " + str(e))
    
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
        
    def get_object_name(self, object):
        res = object.name.split('_')
        obj_name = res[1] + res[2]
        return obj_name

=======
>>>>>>> 199e9028648d759506ba93e98e1e0e80b3ca6d5e
    def rotate_pivot(self, src, tgt):
        rot = tgt.rotation - src.rotation
        brot = rt.Inverse(rot)
        print(brot)
        tgt.pivot = src.pivot
        with rt.SetRefCoordSys('local'):
            tgt.rotation *=brot
            tgt.objectoffsetrot *= brot
<<<<<<< HEAD
            tgt.objectoffsetpos *=brot
>>>>>>> 199e902 (Fix bug and add gitignore)
=======
            tgt.objectoffsetpos *=brot
>>>>>>> 199e9028648d759506ba93e98e1e0e80b3ca6d5e
