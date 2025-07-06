from pathlib import Path
import shutil
import pytest
import pandas as pd


from src.utils.load_data import (
    load_csv,
    duckdb_read_csv,
    list_csv_files,
    get_csv_path
)

# Setup test directory
TEST_DATA_DIR = Path(__file__).parents[1] / "data" / "raw"
TEST_DATA_DIR.mkdir(parents=True, exist_ok=True)
TEST_FILE = TEST_DATA_DIR / "test_file.csv"

@pytest.fixture(scope="module", autouse=True)
def setup_csv():
    # Create a dummy CSV file
    TEST_FILE.write_text("id,name\n1,Alice\n2,Bob")
    yield
    # Cleanup
    if TEST_FILE.exists():
        TEST_FILE.unlink()

def test_get_csv_path():
    path = get_csv_path("test_file.csv", data_dir=TEST_DATA_DIR)
    assert path.exists()
    assert path.name == "test_file.csv"

def test_load_csv():
    df = load_csv("test_file.csv", data_dir=TEST_DATA_DIR)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["id", "name"]

def test_duckdb_read_csv():
    df = duckdb_read_csv("test_file.csv", data_dir=TEST_DATA_DIR)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 2
    assert "name" in df.columns

def test_list_csv_files():
    files = list_csv_files(data_dir=TEST_DATA_DIR)
    assert "test_file.csv" in files
