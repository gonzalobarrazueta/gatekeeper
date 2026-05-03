import pandas as pd
import pytest

@pytest.fixture
def user_data():
    return pd.read_csv("users.csv")

def test_no_null_emails(user_data):
    """Gate 1: Ensures every user has an email."""
    null_emails = user_data["email"].isna()
    assert null_emails.sum() == 0, f"User ids with no emails: {user_data.loc[null_emails == True, "user_id"].to_list()}"

def test_age_is_positive(user_data):
    """Gate 2: Ensures all user ages are positive."""
    positive_ages = user_data["age"] > 0
    assert positive_ages.sum() == len(positive_ages), f"Users with negative ages: {user_data.loc[positive_ages == False, "user_id"].to_list()}"

