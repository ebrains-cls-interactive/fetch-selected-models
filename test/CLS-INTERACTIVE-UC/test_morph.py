
import sys
sys.path.append("../..")

from fetch_selected_models import fetcher

CATEGORY = 'morphology'
SUB_CATEGORY = 'morphologyAnalysis'
models = fetcher.get_model_dict(CATEGORY, SUB_CATEGORY)
print(models)
