import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head(10))

df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)


fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Strength vs. Frequency",
)

fig.write_html("wind.html")
