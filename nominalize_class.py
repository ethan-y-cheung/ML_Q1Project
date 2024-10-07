import pandas as pd

csv_file = 'garments_worker_productivity_classification_preprocessed.csv'

df = pd.read_csv(csv_file)

if 'productivity_met' in df.columns:
    df['productivity_met'] = df['productivity_met'].map({1:'yes', 0:'no'})
    df.to_csv(csv_file, index=False)
    print(f"Column 'productivity_met' has been renamed to 'productivity_met_class' in {csv_file}")
