import pandas as pd
import numpy as np

def clean_dates(df):

    date_columns = [
        col for col in df.columns
        if "date" in col.lower()
        or "month" in col.lower()
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(
            df[col],
            errors="coerce",
            format="mixed"
        )

    return df

def clean_numbers(df):

    number_columns = []

    for col in df.columns:

        lower = col.lower()

        if (
            "value" in lower
            or "amount" in lower
            or "masked" in lower
            or "receivable" in lower
            or "billed" in lower
        ):
            number_columns.append(col)

    for col in number_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "")
        )

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df

def clean_text(df):

    text_cols = df.select_dtypes(include="object").columns

    for col in text_cols:

        df[col] = (
            df[col]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    return df

def fill_missing(df):

    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = df[col].replace("", "Unknown")

        else:

            df[col] = df[col].fillna(0)

    return df

def clean_dataframe(df):

    df = clean_text(df)

    df = clean_dates(df)

    df = clean_numbers(df)

    df = fill_missing(df)

    return df

