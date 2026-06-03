from pymxs import runtime as rt
class PivotOperation():
    def __init__(self):
        self.source_list = []
        self.target_list = []
<<<<<<< HEAD
=======
    def clear_all_list(self):
        self.source_list.clear()
        self.target_list.clear()
>>>>>>> 199e902 (Fix bug and add gitignore)
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
        n = len(self.source_list)
        for i in range(n):
            try:
                print(f"Copy {self.source_list[i].name} pivot to {self.target_list[i].name}")
                PivotOperation.copy_pivot(self.source_list[i],self.target_list[i])
                print("completed")
            except Exception as e:
<<<<<<< HEAD
                print(str(e))
    def copy_pivot(source, target):
        source_position = source.pivot
        source_rotation = source.rotation
        target.rotation = source_rotation

        target.objectoffsetrot *= source_rotation
        target.pivot = source_position
    

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

    def rotate_pivot(self, src, tgt):
        rot = tgt.rotation - src.rotation
        brot = rt.Inverse(rot)
        print(brot)
        tgt.pivot = src.pivot
        with rt.SetRefCoordSys('local'):
            tgt.rotation *=brot
            tgt.objectoffsetrot *= brot
            tgt.objectoffsetpos *=brot
>>>>>>> 199e902 (Fix bug and add gitignore)
