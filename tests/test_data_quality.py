import great_expectations as gx
import pandas as pd
import pytest

@pytest.fixture
def user_data():
    return pd.read_csv("users.csv", dtype={"user_id": "Int64", "email": "string", "age": "Int64"}, parse_dates=["birth_date"])

@pytest.fixture
def batch():
    context = gx.get_context()
    data_source = context.data_sources.add_pandas(name="data_source")
    data_asset = data_source.add_dataframe_asset(name="users_asset")
    batch_definition = data_asset.add_batch_definition_whole_dataframe("batch")
    batch_parameters = {"dataframe": pd.read_csv("users.csv", dtype={"user_id": "Int64", "email": "string", "age": "Int64"}, parse_dates=["birth_date"])}

    return batch_definition.get_batch(batch_parameters=batch_parameters)

@pytest.mark.parametrize("col", [
    ("user_id"),
    ("email"),
    ("age"),
    ("birth_date")
])
def test_table_schema(col, user_data):
    assert col in user_data.columns, f"{col} is not present in the table"

@pytest.mark.parametrize("col, check_dtype_func", [
    ("user_id", pd.api.types.is_integer_dtype),
    ("email", pd.api.types.is_string_dtype),
    ("age", pd.api.types.is_integer_dtype),
    ("birth_date", pd.api.types.is_datetime64_any_dtype)
])
def test_column_types(col, check_dtype_func, user_data):
    assert check_dtype_func(user_data[col]) == True, f"{col} ({user_data[col].dtype}) doesn't comply with defined column type."

def test_no_null_emails(user_data):
    """Gate 1: Ensures every user has an email."""
    null_emails = user_data["email"].isna()
    assert null_emails.sum() == 0, f"User ids with no emails: {user_data.loc[null_emails == True, "user_id"].to_list()}"

def test_age_is_positive(user_data):
    """Gate 2: Ensures all user ages are positive."""
    positive_ages = user_data["age"] > 0
    assert positive_ages.sum() == len(positive_ages), f"Users with negative ages: {user_data.loc[positive_ages == False, "user_id"].to_list()}"
