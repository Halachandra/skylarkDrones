import requests
import pandas as pd
from config import MONDAY_API_KEY
from cleaner import clean_dataframe

URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": MONDAY_API_KEY,
    "Content-Type": "application/json",
}

def get_board_items(board_id):

    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            id
            name
            column_values {{
              column {{
                title
              }}
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        URL,
        json={"query": query},
        headers=HEADERS,
    )

    data = response.json()
    print(data)

    items = data["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:

        row = {"Item Name": item["name"]}

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    df = pd.DataFrame(rows)
    df = clean_dataframe(df)
    return df

from config import DEALS_BOARD_ID

def get_deals():

    return get_board_items(DEALS_BOARD_ID)

from config import WORKORDERS_BOARD_ID

def get_work_orders():

    return get_board_items(WORKORDERS_BOARD_ID)
