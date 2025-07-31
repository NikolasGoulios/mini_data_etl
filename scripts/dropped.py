import pandas as pd
import os
import config



def load_data(path):
	print(f"Loading data from {path}...")
	return pd.read_csv(path)

def extract_dropped_data(df):
	print(f"Extracting dropped data...")
	df_dropped = df[df[config.IMPORTANT_COLUMNS].isnull().any(axis=1)]
	return df_dropped

def save_dropped_data(df, path):
	os.makedirs(os.path.dirname(path), exist_ok=True)
	df.to_csv(path, index=False)
	print(f"Saved {len(df)} dropped data to {path}")

def main():
	df = load_data(config.RAW_DATA_PATH)
	df_dropped = extract_dropped_data(df)
	save_dropped_data(df_dropped, config.DROPPED_PATH)

if __name__ == "__main__":
	main()