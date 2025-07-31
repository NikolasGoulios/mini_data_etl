import pandas as pd
import os
import config

# === Load ===
def load_data(path):
	print(f"Loading data from {path}...")
	return pd.read_csv(path)

# === Clean ===
def clean_data(df):
	print("Cleaning data...")

	# Drop columns with more than 95% missing values, potential risk of data accuracy
	missing_ratio = df.isnull().mean()
	columns_to_drop = missing_ratio[missing_ratio > 0.95].index
	df = df.drop(columns=columns_to_drop)

	# Dropping rows with missing values in important columns
	df = df.dropna(subset=config.IMPORTANT_COLUMNS).copy()

	# Normalize price field, remove $ and ,, and convert to numeric (float)
	df['price'] = df['price'].astype(str) \
                         .str.replace('$', '', regex=False) \
                         .str.replace(',', '', regex=False)
	df['price'] = pd.to_numeric(df['price'], errors='coerce')
	df = df.dropna(subset=['price'])

	# Drop duplicates
	df = df.drop_duplicates()

	return df

# === Save ===
def save_data(df, path):
	os.makedirs(os.path.dirname(path), exist_ok=True)
	df.to_csv(path, index=False)
	print(f"Saved cleaned data to {path}")

# === Main ===
def main():
	df = load_data(config.RAW_DATA_PATH)
	cleaned_df = clean_data(df)
	save_data(cleaned_df, config.CLEAN_DATA_PATH)
	print("Original rows:", len(df))
	print("Cleaned rows:", len(cleaned_df))

if __name__ == "__main__":
	main()