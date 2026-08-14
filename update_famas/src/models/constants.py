from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

class ConfigKeys:
    OLDEST_DROP = "oldest_drop"
    SOURCE_FOLDER = "source_path"
    DESTINATION_FOLDER = "destination_path"
    ARCHIVE_FOLDER = "archived_path"
    DATABASE_FOLDER = "database_path"
    OUTPUT_FOLDER = "output_path"

class FileNames:
    CONFIG = "config.json"

class Excel:
    HEADERS = {"A1": "Stt",
                "B1" : "AssetName",
                "C1" : "Artist",
                "D1" : "Map"
    }
    
class Paths:
    ASSETS = Path("assets")
    CONFIG = PROJECT_ROOT/ ASSETS / FileNames.CONFIG
