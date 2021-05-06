
from pathlib import Path
import re
import json

UC_FOLDER_NAME = 'CLS-INTERACTIVE-UC' 
MODELS_FOLDER_NAME = 'CLS-INTERACTIVE-MODELS'
MODELS_FILE_NAME = 'models.json'

def _get_model_path_():
  regex = rf"(.+){UC_FOLDER_NAME}"
  m = re.match(regex, str(Path.cwd()))
  base_collab = m.groups()[0]
  base_model = Path(base_collab) / MODELS_FOLDER_NAME / MODELS_FILE_NAME
  return base_model

def get_model_dict(category_id, use_case_id):
  path = _get_model_path_()
  with open(path) as json_file:
      data = json.load(json_file)
  models = data[category_id][use_case_id]
  return models
