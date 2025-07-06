from pathlib import Path
from typing import Optional, List
import pandas as pd
import duckdb

# Automatically resolve project root based on this file's location
DEFAULT_RAW_DATA_DIR = (Path(__file__).parents[2] / "data" / "raw").resolve()
DEFAULT_PROCESSED_DATA_DIR = (Path(__file__).parents[2] / "data" / "processed").resolve()


def get_csv_path(filename: str, data_dir: Optional[Path] = None) -> Path:
    """
    Returns the full path to a CSV file in the data/raw directory.
    """
    if data_dir is None:
        data_dir = DEFAULT_RAW_DATA_DIR
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory does not exist: {data_dir}")
    return data_dir / filename


def load_csv(filename: str, data_dir: Optional[Path] = None, **kwargs) -> Optional[pd.DataFrame]:
    """
    Loads a CSV file using pandas.
    """
    try:
        csv_path = get_csv_path(filename, data_dir)
        df = pd.read_csv(csv_path, **kwargs)
        print(f"✅ CSV loaded: {csv_path}")
        return df
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
        return None


def duckdb_read_csv(filename: str, data_dir: Optional[Path] = None, delim: str = ',', **kwargs) -> Optional[pd.DataFrame]:
    """
    Loads a CSV file using DuckDB's read_csv_auto.
    """
    try:
        csv_path = get_csv_path(filename, data_dir)
        query = f"SELECT * FROM read_csv_auto('{csv_path.as_posix()}', delim='{delim}')"
        df = duckdb.query(query).to_df()
        print(f"✅ DuckDB loaded: {csv_path}")
        return df
    except Exception as e:
        print(f"❌ DuckDB failed: {e}")
        return None
      
def save_csv(
    df: pd.DataFrame,
    filename: str,
    data_dir: Optional[Path] = None,
    index: bool = False,
    verbose: bool = True
) -> None:
    """
    Saves a DataFrame as CSV to the /data/processed directory by default.

    Args:
        df (pd.DataFrame): The DataFrame to save
        filename (str): Name of the CSV file to save (e.g., 'orders_clean.csv')
        data_dir (Optional[Path]): Custom target directory. Defaults to /data/processed
        index (bool): Whether to write row indices (default: False)
        verbose (bool): If True, print a success message
    """
    if data_dir is None:
        data_dir = DEFAULT_PROCESSED_DATA_DIR
    try:
        data_dir.mkdir(parents=True, exist_ok=True)
        file_path = data_dir / filename
        df.to_csv(file_path, index=index)
        if verbose:
            print(f"💾 Saved CSV to: {file_path.resolve()}")
    except Exception as e:
        print(f"❌ Failed to save CSV: {e}")


def list_csv_files(data_dir: Optional[Path] = None) -> List[str]:
    """
    Lists all CSV files in the data/raw directory.
    """
    if data_dir is None:
        data_dir = DEFAULT_RAW_DATA_DIR
    if not data_dir.exists():
        print(f"❌ Data directory does not exist: {data_dir}")
        return []
    files = [f.name for f in data_dir.glob('*.csv')]
    if files:
        print(f"📄 Found CSV files: {files}")
    else:
        print(f"⚠️ No CSV files found in: {data_dir}")
    return files

