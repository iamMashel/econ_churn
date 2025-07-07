from pathlib import Path
from typing import Optional, List
import pandas as pd
import duckdb
import logging

# --- Logging setup ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Base Paths ---
PROJECT_ROOT = Path(__file__).parents[2].resolve()
DEFAULT_RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DEFAULT_PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# --- File Path Resolver ---
def get_csv_path(filename: str, data_dir: Path) -> Path:
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory does not exist: {data_dir}")
    return data_dir / filename

# --- CSV Loader ---
def load_csv(
    filename: str,
    data_dir: Optional[Path] = None,
    source: str = "raw",
    verbose: bool = True,
    **kwargs
) -> Optional[pd.DataFrame]:
    if data_dir is None:
        if source == "raw":
            data_dir = DEFAULT_RAW_DATA_DIR
        elif source == "processed":
            data_dir = DEFAULT_PROCESSED_DATA_DIR
        else:
            raise ValueError("source must be 'raw' or 'processed'")
    try:
        csv_path = get_csv_path(filename, data_dir)
        df = pd.read_csv(csv_path, **kwargs)
        if verbose:
            logger.info(f"✅ CSV loaded: {csv_path}")
        return df
    except Exception as e:
        logger.error(f"❌ Failed to load CSV: {e}")
        return None

# --- Excel Loader ---
def load_excel(
    filename: str,
    sheet_name: str = 0,
    data_dir: Optional[Path] = None,
    source: str = "raw",
    verbose: bool = True,
    **kwargs
) -> Optional[pd.DataFrame]:
    if data_dir is None:
        data_dir = DEFAULT_RAW_DATA_DIR if source == "raw" else DEFAULT_PROCESSED_DATA_DIR
    try:
        path = get_csv_path(filename, data_dir)
        df = pd.read_excel(path, sheet_name=sheet_name, **kwargs)
        if verbose:
            logger.info(f"📘 Excel loaded: {path}")
        return df
    except Exception as e:
        logger.error(f"❌ Failed to load Excel: {e}")
        return None

# --- Parquet Loader ---
def load_parquet(filename: str, data_dir: Optional[Path] = None, source: str = "processed") -> Optional[pd.DataFrame]:
    if data_dir is None:
        data_dir = DEFAULT_PROCESSED_DATA_DIR if source == "processed" else DEFAULT_RAW_DATA_DIR
    try:
        path = get_csv_path(filename, data_dir)
        return pd.read_parquet(path)
    except Exception as e:
        logger.error(f"❌ Failed to load Parquet: {e}")
        return None

# --- Save CSV ---
def save_csv(
    df: pd.DataFrame,
    filename: str,
    data_dir: Optional[Path] = None,
    index: bool = False,
    verbose: bool = True
) -> None:
    if data_dir is None:
        data_dir = DEFAULT_PROCESSED_DATA_DIR
    try:
        data_dir.mkdir(parents=True, exist_ok=True)
        path = data_dir / filename
        df.to_csv(path, index=index)
        if verbose:
            logger.info(f"💾 Saved CSV to: {path.resolve()}")
    except Exception as e:
        logger.error(f"❌ Failed to save CSV: {e}")

# --- DuckDB Loader ---
def duckdb_read_csv(
    filename: str,
    data_dir: Optional[Path] = None,
    delim: str = ',',
    source: str = "raw",
    verbose: bool = True,
    **kwargs
) -> Optional[pd.DataFrame]:
    if data_dir is None:
        data_dir = DEFAULT_RAW_DATA_DIR if source == "raw" else DEFAULT_PROCESSED_DATA_DIR
    try:
        csv_path = get_csv_path(filename, data_dir)
        query = f"SELECT * FROM read_csv_auto('{csv_path.as_posix()}', delim='{delim}')"
        df = duckdb.query(query).to_df()
        if verbose:
            logger.info(f"🦆 DuckDB loaded: {csv_path}")
        return df
    except Exception as e:
        logger.error(f"❌ DuckDB failed: {e}")
        return None

# --- CSV File Lister ---
def list_csv_files(data_dir: Optional[Path] = None, source: str = "raw") -> List[str]:
    if data_dir is None:
        data_dir = DEFAULT_RAW_DATA_DIR if source == "raw" else DEFAULT_PROCESSED_DATA_DIR
    if not data_dir.exists():
        logger.warning(f"❌ Data directory does not exist: {data_dir}")
        return []
    files = [f.name for f in data_dir.glob('*.csv')]
    if files:
        logger.info(f"📄 Found CSV files: {files}")
    else:
        logger.warning(f"⚠️ No CSV files found in: {data_dir}")
    return files

# --- Schema Validator ---
def validate_columns(df: pd.DataFrame, required_cols: List[str]) -> None:
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"❌ Missing required columns: {missing}")
    logger.info(f"✅ All required columns present: {required_cols}")

# --- File Exists Shortcut ---
def file_exists(filename: str, source: str = "raw") -> bool:
    base = DEFAULT_RAW_DATA_DIR if source == "raw" else DEFAULT_PROCESSED_DATA_DIR
    return (base / filename).exists()
