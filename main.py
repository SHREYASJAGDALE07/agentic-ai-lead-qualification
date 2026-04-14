import pandas as pd
from agent import lead_agent
from model import train_model

data = pd.read_csv("data/leads_dataset.csv")

data["Agent_Action"] = data.apply(lead_agent, axis=1)

model = train_model("data/leads_dataset.csv")

data.to_csv("data/output.csv", index=False)

print("Process Completed!")
