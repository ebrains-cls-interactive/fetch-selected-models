
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

def display_dropdown(models, prop='name', prop_name='Name'):
  import ipywidgets as widgets
  from IPython.display import display

  model_selected = widgets.Dropdown(
      options=[m[prop] for m in models],
      description=prop_name,
      layout={'width': 'max-content'},
      disabled=False,
  )
  display(model_selected)
  return model_selected
