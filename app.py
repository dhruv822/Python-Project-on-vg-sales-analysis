import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df  = pd.read_csv('vgsales (1).csv')
df['Publisher'].fillna('Unknown', inplace=True)

ts = df ['Global_Sales'].sum()
tg = df.shape[0]
tp = len(df['Publisher'].unique())

st.sidebar.title('Sales Dashboard.')
st.sidebar.image('https://media.kasperskydaily.com/wp-content/uploads/sites/92/2020/02/17105257/game-ratings-featured.jpg')
st.sidebar.markdown('---')
inp = st.sidebar.radio("Select Analysis.",['Overview.',
                                           'Year wise Analysis.',
                                           'Genre wise Analysis.',
                                           'Platform wise Analysis.',
                                           'Publisher wise Analysis.'])

#overview
if inp == 'Overview.':
    st.title('VIDEO GAMES DATA ANALYSIS🎮')
    st.markdown('---')
    st.image('https://vgsalesanalysis-sky.streamlit.app/~/+/media/7a0f1eab9f4e725f24e02b3f5dd702770cbea1491244d5ed496155f6.png')
    st.markdown('---')
    c1,c2,c3 = st.columns([1,1,1])
    c1.metric('Total Sales.', value=ts, delta=+30)
    c2.metric('Total Games Released.', value=tg,delta=+10)
    c3.metric('Total Pulishers.', value=tp, delta= +20 )
    st.markdown('---')
    st.markdown("""
    ### ※ Columns in the data along with their description.
- `Rank:` The ranking position of the game in terms of global sales.
- `Name:` The name of the video game.
- `Platform:` The gaming platform (console or system) on which the game was released.
- `Year:` The year when the game was released.
- `Genre:` The genre or category of the game (e.g., action, adventure, sports).
- `Publisher:` The company or entity responsible for publishing and distributing the game.
- `NA_Sales:` Sales of the game in North America (in millions of units).
- `EU_Sales:` Sales of the game in Europe (in millions of units).
- `JP_Sales:` Sales of the game in Japan (in millions of units).
- `Other_Sales:` Sales of the game in regions other than North America, Europe, and Japan (in millions of units).
- `Global_Sales:` Total global sales of the game (sum of sales across all regions, in millions of units).
""")
    st.markdown('---')
    st.header('The data of all games..')
    st.dataframe(df)

    st.sidebar.markdown('---')
    games = df['Name'].unique()
    game = st.sidebar.selectbox('Select a Game', games)
    temp = df[df['Name'] == game]
    btn = st.sidebar.button('Click to view data')
    st.markdown('---')
    if btn:
        st.header(f'Info of {game}.')
        st.dataframe(temp)

# Year wise analysis
elif inp == 'Year wise Analysis.':
    st.title("Yearwise  Analysis.")
    st.header('Year  wise Sales')
    temp = df.groupby('Year')['Global_Sales'].sum().reset_index()
    fig = px.line(temp, x='Year', y='Global_Sales')
    st.plotly_chart(fig)

    st.markdown('---')

    st.header("Games Released Per Year.")
    temp = df['Year'].value_counts().sort_index()
    fig = px.bar(temp, x = temp.index, y = temp, text_auto=True)
    st.plotly_chart(fig)

#  Genre wise analysis
elif inp =='Genre wise Analysis.':
    st.title("Genre wise Analysis")
    temp = df['Genre'].value_counts().reset_index()
    fig = px.pie(temp, names = 'Genre', values='count',
                 hover_name='Genre',title='Genre Popularity',
                 height = 700,)
    st.plotly_chart(fig)

    st.markdown('---')

    st.header("Genre wise Sales.")
    temp = df.groupby('Genre')['Global_Sales'].sum()
    fig = px.bar(temp, x= temp.index, y =temp, title='Genre Sales')
    st.plotly_chart(fig)

# Platform wise analysis
elif inp =='Platform wise Analysis.':
    st.title("Platform Wise Analysis.")
    st.markdown("---")
    st.header("Genre Wise Sales.")
    temp = df.groupby("Platform")['Global_Sales'].sum().sort_values()
    fig = px.bar(temp, x=temp.index,y =temp)
    st.plotly_chart(fig)

    st.header('Best selling Game at every platform')
    temp = (df.groupby('Platform').apply(lambda x:x.nlargest(1,'Global_Sales')).reset_index(drop=True))
    st.dataframe(temp[['Platform','Name']])

# Publisher wise Analysis
elif inp =='Publisher wise Analysis.':
    st.title("Publisher wise Analysis.")
    st.header('Top Publishers...')
    temp = (df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index())
    fig = px.bar(temp, x='Publisher', y='Global_Sales')
    st.plotly_chart(fig)
    st.markdown("---")
    st.header("Contribution of Publishers.")
    fig = px.pie(temp, names='Publisher', values='Global_Sales', hover_name='Publisher')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

