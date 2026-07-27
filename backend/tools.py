from analyzer import *

def execute_tool(intent, deals_df, work_df):

    if intent == "pipeline":
        return pipeline_summary(deals_df)

    elif intent == "sector":
        return pipeline_by_sector(deals_df)

    elif intent == "revenue":
        return {
        "revenue": revenue_summary(work_df),
        "billing": billing_summary(work_df),
        "collections": collection_summary(work_df)
    }
    elif intent == "workorders":
        return {
            "active_projects": active_workorders(work_df),
            "billing": billing_summary(work_df),
            "collections": collection_summary(work_df)
        }

    elif intent == "leadership":
        return {
            "pipeline": pipeline_summary(deals_df),
            "revenue": revenue_summary(work_df),
            "billing": billing_summary(work_df),
            "collections": collection_summary(work_df),
            "pipeline_by_sector": pipeline_by_sector(deals_df)
        }

    else:
        return dashboard(deals_df, work_df)