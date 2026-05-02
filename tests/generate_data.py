import pandas as pd

def create_mock_data():
    data = {
        "user_id": [1, 2, 3, 4, 5],
        "email": ["alice@example.com", "bob@example.com", "charlie@example.com", None, "eve@example.com"],
        "age": [25, 30, -5, 40, 22]
    }

    df = pd.DataFrame(data)
    df.to_csv("processed_users.csv", index=False)
    print("Mock data generated: processed_users.csv")

if __name__ == "__main__":
    create_mock_data()