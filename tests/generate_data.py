import pandas as pd

def create_mock_data():
    data = {
        "user_id": [1, 2, 3, 4, 5],
        "email": ["alice@example.com", "bob@example.com", "charlie@example.com", "elle@example.com", "eve@example.com"],
        "age": [25, 30, 15, 40, 22],
        "birth_date": ["2000-10-09", "2003-12-11", "2000-10-20", "2000-03-03", "2000-10-23"]
    }

    df = pd.DataFrame(data)
    df.to_csv("users.csv", index=False)
    print("Mock data generated: users.csv")

if __name__ == "__main__":
    create_mock_data()