import pandas as pd
from db.db import collection
from typing import BinaryIO

def parse_and_upload_excel(file: BinaryIO) -> dict:
    try:
        df = pd.read_excel(file)
        df = df.where(pd.notnull(df), None)
        records = df.to_dict(orient="records")

        if not records:
            return {"status": "No records found in the Excel file."}

        collection.insert_many(records)
        return {
            "status": "Success",
            "inserted_records": len(records)
        }

    except Exception as e:
        return {
            "status": "Failed",
            "error": str(e)
        }
