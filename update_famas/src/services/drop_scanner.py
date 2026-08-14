import re
from pathlib import Path
import math
from services.config_manager import ConfigManager
from models.constants import ConfigKeys
class DropScanner():
	def __init__(self):
		self.drop_pattern = re.compile(r"Drop_(\d+)$")

	def check_drop(self, source_folder: Path, destination_folder: Path) -> tuple[int, int]:
		source_item = self.get_latest_file(source_folder)
		destination_item = self.get_latest_file(destination_folder)
		source_drop = self.get_drop_number(source_item)
		destination_drop = self.get_drop_number(destination_item)
		return source_drop, destination_drop

	def check_drop_difference(self,source_folder: Path, destination_folder:Path) -> tuple[int,int]:
		source_item = self.get_first_drop(source_folder)
		destination_item = self.get_first_drop(destination_folder)
		source_drop = self.get_drop_number(source_item)
		destination_drop = self.get_drop_number(destination_item)
		return source_drop, destination_drop
	
	def get_latest_file(self, path : Path):
		latest_time = None
		latest_item = None
		for item in path.iterdir():
			if self.drop_pattern.match(item.stem):
				birthtime = item.stat().st_birthtime
				if latest_time is None or birthtime > latest_time:
					latest_item = birthtime
					latest_item = item
		return latest_item

	def get_drop_number(self, item : Path):
		number = 0
		match = re.search(r"(\d+)$",item.stem)
		if match:
			number = int(match.group())
		return number
	
	def get_drop_car_list(self, drop_number : int, folder_path: Path):
		car_list = []
		drop_folder = folder_path / f"Drop_{drop_number}"
		if drop_folder.exists() and drop_folder.is_dir():
			for item in drop_folder.iterdir():
				if item.is_dir():
					if "feature" in item.name.lower() or "update" in item.name.lower():
						for inner_item in item.iterdir():
							car_list.append(inner_item.name)
					else:
						car_list.append(item.name)
			return car_list
		else:
			return []

	def get_first_drop(self, path: Path):
		oldest_drop_num = math.inf
		oldest_item = None
		for item in path.iterdir():
			if self.drop_pattern.match(item.stem):
				item_drop_num = self.get_drop_number(item)
				if oldest_drop_num > item_drop_num:
					oldest_drop_num = item_drop_num
					oldest_item = item
		return oldest_item