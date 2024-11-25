import pandas as pd

def flatten_dict(nested_dict, parent_key='', sep='_'):
    items = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for idx, item in enumerate(v):
                items.extend(flatten_dict({f"{new_key}_{idx}": item}).items())
        else:
            items.append((new_key, v))
    return dict(items)

def normalize_to_single_table(dataset):
    normalized_data = [flatten_dict(record) for record in dataset]
    return pd.DataFrame(normalized_data)
