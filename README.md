# fetch-selected-models

### Install
```
pip install -q --upgrade git+https://github.com/ebrains-cls-interactive/fetch-selected-models.git@dev#egg=fetch_selected_models
```

### Usage
```
from fetch_selected_models import fetcher
models = fetcher.get_model_dict('morphology', 'morphologyAnalysis')
morph_selected = fetcher.display_dropdown(models) # displays the dropdown
```

Where **morphology** is the **category id** and **morphologyAnalysis** is the **usecase id** (from [usecases-info.json](https://github.com/ebrains-cls-interactive/usecases-info/blob/main/usecases-info.json#L214))

### Get selected value
```
selected = morph_selected.value
```

### Extra options
```
models = fetcher.get_model_dict(category_id, usecase_id, propertie, propertie_name)
```
**propertie**: which propertie of the models.json to show
**propertie_name** which text to show in the widget
