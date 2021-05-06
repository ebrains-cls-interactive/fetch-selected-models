
import sys
sys.path.append("../..")

from fetch_selected_models import fetcher

category = 'morphology'
sub_category = 'morphologyAnalysis'
models = fetcher.get_model_dict(category, sub_category)
print(models)
