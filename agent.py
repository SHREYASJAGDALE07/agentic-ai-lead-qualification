def lead_agent(row):
    if row["Converted"] == 1:
        return "High Priority – Call Immediately"
    elif row["Time_Spent_on_Site"] > 5:
        return "Follow-up Needed"
    else:
        return "Low Interest – Ignore"
