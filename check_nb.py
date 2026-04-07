import os
import json
import requests

def check_file_size(filepath):
    if os.path.exists(filepath):
        print(f"File {filepath} exists, size: {os.path.getsize(filepath)} bytes")
    else:
        print(f"File {filepath} not found")

def analyze_notebook(nb_path):
    if not os.path.exists(nb_path):
        print(f"Notebook {nb_path} not found")
        return
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    for i, cell in enumerate(nb['cells']):
        source = "".join(cell.get('source', []))
        if 'DecisionTreeClassifier' in source:
            print(f"--- Cell {i} (Code) ---")
            print(source)
            print("-" * 20)
        # Also look for preprocessing
        if 'dataset.drop' in source or 'preprocessing' in source.lower():
             if i < 20: # Just first few segments
                print(f"--- Cell {i} (Preprocessing) ---")
                print(source)
                print("-" * 20)

if __name__ == "__main__":
    check_file_size('DataCoSupplyChainDataset.csv')
    analyze_notebook('comparison-of-classification-regression-rnn.ipynb')
