from services.drop_scanner import DropScanner
from services.excel_exporter import ExcelExporter
from services.config_manager import ConfigManager
from models.constants import Paths, Excel
from services.famas_updater import FamasUpdater
from services.famas_optimizer import FamasOptimizer
print("Assets path:",Paths.ASSETS)
print("Config path:",Paths.CONFIG)
famas_updater = FamasUpdater(ConfigManager(), DropScanner(), ExcelExporter())
famas_optimize = FamasOptimizer(DropScanner())
famas_optimize.optimize_car_list()
