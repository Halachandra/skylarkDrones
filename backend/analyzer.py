import pandas as pd

# ----------------------------
# Deals Board Columns
# ----------------------------

DEAL_VALUE = "Masked Deal value"
SECTOR_DEALS = "Sector/service"
DEAL_STAGE = "Deal Stage"
DEAL_STATUS = "Deal Status"

# ----------------------------
# Work Order Columns
# ----------------------------

SECTOR_WORK = "Sector"
EXECUTION_STATUS = "Execution Status"
BILLING_STATUS = "Billing Status"
COLLECTION_STATUS = "Collection status"
WO_STATUS = "WO Status (billed)"


# ----------------------------
# Deals Analytics
# ----------------------------

def pipeline_summary(deals_df):

    return {
        "total_deals": len(deals_df),
        "total_pipeline": round(deals_df[DEAL_VALUE].sum(), 2),
        "average_deal_size": round(deals_df[DEAL_VALUE].mean(), 2),
    }


def pipeline_by_sector(deals_df):

    return (
        deals_df
        .groupby(SECTOR_DEALS)[DEAL_VALUE]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )


def deal_stage_distribution(deals_df):

    return (
        deals_df[DEAL_STAGE]
        .value_counts()
        .to_dict()
    )


def deal_status_summary(deals_df):

    return (
        deals_df[DEAL_STATUS]
        .value_counts()
        .to_dict()
    )


# ----------------------------
# Work Orders Analytics
# ----------------------------

def active_workorders(work_df):

    active = work_df[
        work_df[EXECUTION_STATUS].str.lower() != "completed"
    ]

    return len(active)


def billing_summary(work_df):

    return (
        work_df[BILLING_STATUS]
        .value_counts()
        .to_dict()
    )


def collection_summary(work_df):

    return (
        work_df[COLLECTION_STATUS]
        .value_counts()
        .to_dict()
    )


def delayed_projects(work_df):

    delayed = work_df[
        work_df[WO_STATUS]
        .astype(str)
        .str.contains("delay", case=False, na=False)
    ]

    return len(delayed)


# ----------------------------
# Dashboard
# ----------------------------

def dashboard(deals_df, work_df):

    return {

    "pipeline": pipeline_summary(deals_df),

    "revenue": revenue_summary(work_df),

    "pipeline_by_sector": pipeline_by_sector(deals_df),

    "deal_stages": deal_stage_distribution(deals_df),

    "deal_status": deal_status_summary(deals_df),

    "billing": billing_summary(work_df),

    "collections": collection_summary(work_df),

    "active_projects": active_workorders(work_df),

    "delayed_projects": delayed_projects(work_df)

}

def revenue_summary(work_df):

    billed = work_df["Billed Value in Rupees (Incl of GST.) (Masked)"].sum()

    collected = work_df["Collected Amount in Rupees (Incl of GST.) (Masked)"].sum()

    receivable = work_df["Amount Receivable (Masked)"].sum()

    total_contract = work_df["Amount in Rupees (Incl of GST) (Masked)"].sum()

    return {
        "total_contract_value": round(total_contract, 2),
        "billed_value": round(billed, 2),
        "collected_value": round(collected, 2),
        "receivable": round(receivable, 2)
    }

