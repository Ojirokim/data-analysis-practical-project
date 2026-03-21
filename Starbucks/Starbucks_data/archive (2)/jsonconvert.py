import pandas as pd
import json

# load json
with open('transcript.json') as f:
    data = json.load(f)

# normalize (flatten)
df = pd.json_normalize(data)

# save as csv
df.to_csv('transcript_clean.csv', index=False)