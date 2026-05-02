import pandas as pd
import pytest

@pytest.fixture
def user_data():
    return pd.read_csv("users.csv")

def test_no_null_emails(user_data):
    """Gate 1: Ensures every user has an email."""
    null_emails = user_data["email"].isna()
    assert null_emails.sum() == 0, f"User ids with no emails: {user_data.loc[null_emails == True, "user_id"].to_list()}"

