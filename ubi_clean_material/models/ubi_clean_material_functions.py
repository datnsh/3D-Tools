from pymxs import runtime as rt

EXCLUDE = ["Z1","Z2","Z3","Z4","Z5","Z6","Z7"]
class MaterialCleaner():
    def get_used_id(self, obj):
        used_ids = set()
        if rt.classOf(obj) == rt.Editable_Poly:
            num_faces = rt.polyop.getNumFaces(obj)
            for f in range(1, num_faces + 1):
                used_ids.add(rt.polyop.getFaceMatID(obj,f))
        return used_ids

    def find_the_multimaterial(self):
        multi_mats = []
        for m in rt.sceneMaterials:
            if rt.classOf(m) == rt.Multimaterial:
                multi_mats.append(m)
        if len(multi_mats) == 0:
            print("No Multi/Sub-Object material found in the scene.")
            return None
        if len(multi_mats) > 1:
            print("Warning: found more than one Multi-Material, using the first one:", multi_mats[0].name)
        return multi_mats[0]
        
    def get_unused_id(self, target_mat, used_id):
        id_list = target_mat.materialIDList
        name_list = target_mat.names
        remove_id = set()
        for i in range(len(id_list) - 1):
            if id_list[i] not in used_id and (name_list[i] not in EXCLUDE):
                remove_id.add(id_list[i])
        if len(remove_id) > 0:
            print(remove_id)
        else:
            print("No Unused Material")
        return remove_id
        
    def create_new_material(self, target_mat, unused_id):
        new_ids = rt.Array()
        new_mats = rt.Array()
        new_names = rt.Array()
        for i in range(len(target_mat.materialIDList)):
            mat_id = target_mat.materialIDList[i]
            if mat_id in unused_id:
                print(f"Removing ID {mat_id} ({target_mat.names[i]})")
            else:
                rt.append(new_ids, mat_id)
                rt.append(new_mats, target_mat.materialList[i])
                rt.append(new_names, target_mat.names[i])
        return new_ids, new_mats, new_names
        
    def clean_scene_multimaterial(self):
        target_mat = self.find_the_multimaterial()
        if target_mat is None:
            return

        used_id = set()
        for obj in rt.objects:
            used_id.update(self.get_used_id(obj))
        print("Used Material IDs:", used_id)
        
        unused_id = self.get_unused_id(target_mat,used_id)
        new_ids, new_mats, new_names = self.create_new_material(target_mat, unused_id)
        
        target_mat.materialList = new_mats
        target_mat.materialIDList = new_ids
        target_mat.names = new_names