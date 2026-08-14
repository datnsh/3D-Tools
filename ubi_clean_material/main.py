import sys, os
path = os.path.dirname(__file__)
print(path)
if path not in sys.path:
    sys.path.append(path)
from models.ubi_clean_material_functions import MaterialCleaner

def main():
    cleaner = MaterialCleaner()
    cleaner.clean_scene_multimaterial()

if __name__ == "__main__":
    main()
