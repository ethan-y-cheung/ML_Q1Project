import os
import pandas as pd
from sklearn.model_selection import train_test_split

input_dir = "Attribute Selection Datasets"
output_dir = "Splitted Datasets"

dataset_class = 'productivity_met'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_dir, filename)
        df = pd.read_csv(file_path)

        train_df, temp_df = train_test_split(
            df,
            test_size=0.30,
            stratify=df[dataset_class],
            random_state=42
        )

        val_df, test_df = train_test_split(
            temp_df,
            test_size=0.50,
            stratify=temp_df[dataset_class],
            random_state=42
        )

        dataset_directory = os.path.join(output_dir, filename[:-4])
        os.makedirs(dataset_directory, exist_ok=True)

        train_df.to_csv(os.path.join(dataset_directory, "train.csv"), index=False)
        val_df.to_csv(os.path.join(dataset_directory, "validation.csv"), index=False)
        test_df.to_csv(os.path.join(dataset_directory, "test.csv"), index=False)
