import pandas as pd
import pytest

@pytest.fixture
def user_data():
    return pd.read_csv("users.csv")

def test_no_null_emails(users_df):
    """Gate 1: Ensures every user has an email."""
    null_emails = users_df["email"].isna()
    assert null_emails.sum() == 0, f"User ids with no emails: {users_df.loc["user_id", null_emails].to_list()}"

