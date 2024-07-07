import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import streamlit
from streamlit_option_menu import option_menu
import plotly.express as px
import os
import requests
import json
from PIL import Image
#***************************************************************************************************************************

# DF creation

#sqlConnection
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'phonepe_data.db')
mydb = sqlite3.connect(db_path)
cursor = mydb.cursor()



#Aggregated_insurance
cursor.execute("""select * from aggregated_insurance
                  Order by States ;""")
mydb.commit()
table1 = cursor.fetchall()
Aggre_insurance = pd.DataFrame(table1,columns = ("States", "Years", "Quarter", "Transaction_type", "Transaction_count",
                                                 "Transaction_amount"))



#Aggregated_transaction
cursor.execute("""SELECT * FROM aggregated_transaction
                  ORDER BY States ;""")
mydb.commit()
table2 = cursor.fetchall()
Aggre_transaction = pd.DataFrame(table2,columns = ("States", "Years", "Quarter", "Transaction_type", "Transaction_count"
                                                   ,"Transaction_amount"))



#Aggregated_user
cursor.execute("""SELECT * FROM aggregated_user
                  ORDER BY States ;""")
mydb.commit()
table3 = cursor.fetchall()
Aggre_user = pd.DataFrame(table3,columns = ("States", "Years", "Quarter", "Brands", "Transaction_count","Percentage"))



#Map_insurance
cursor.execute("select * from map_insurance ORDER BY States")
mydb.commit()
table4 = cursor.fetchall()
Map_insurance = pd.DataFrame(table4,columns = ("States", "Years", "Quarter", "Districts", "Transaction_count",
                                               "Transaction_amount"))



#Map_transaction
cursor.execute("select * from map_transaction ORDER BY States")
mydb.commit()
table5 = cursor.fetchall()
Map_transaction = pd.DataFrame(table5,columns = ("States", "Years", "Quarter", "Districts", "Transaction_count",
                                                 "Transaction_amount"))



#Map_user
cursor.execute("select * from map_user ORDER BY States")
mydb.commit()
table6 = cursor.fetchall()
Map_user = pd.DataFrame(table6,columns = ("States", "Years", "Quarter", "Districts", "RegisteredUser", "AppOpens"))



#Top_insurance
cursor.execute("select * from top_insurance ORDER BY States")
mydb.commit()
table7 = cursor.fetchall()
Top_insurance = pd.DataFrame(table7,columns = ("States", "Years", "Quarter", "Pincodes", "Transaction_count",
                                               "Transaction_amount"))



#Top_transaction
cursor.execute("select * from top_transaction ORDER BY States")
mydb.commit()
table8 = cursor.fetchall()
Top_transaction = pd.DataFrame(table8,columns = ("States", "Years", "Quarter", "Pincodes", "Transaction_count",
                                                 "Transaction_amount"))



#Top_user
cursor.execute("select * from top_user ORDER BY States")
mydb.commit()
table9 = cursor.fetchall()
Top_user = pd.DataFrame(table9, columns = ("States", "Years", "Quarter", "Pincodes", "RegisteredUser"))


def transaction_amount_count_by_year(df,year):

  tran_amount_count_by_year = df [df["Years"] == year]
  tran_amount_count_by_year.reset_index(drop=True,inplace=True)

  tran_amount_count_by_year_group = tran_amount_count_by_year.groupby("States")[["Transaction_count",
                                                                                 "Transaction_amount"]].sum()
  tran_amount_count_by_year_group.reset_index(inplace=True)

  colmp1,colmp2 = st.columns(2)

  with colmp1:
      plot_amount = px.bar(tran_amount_count_by_year_group, x = "States",y = "Transaction_amount",
                           title = f"{year} TRANSACTION AMOUNT",
                           color_discrete_sequence = ['#58C753'],height = 600,width= 700 )
      st.plotly_chart(plot_amount)

  with colmp2:
      plod_count = px.bar(tran_amount_count_by_year_group, x = "States",y = "Transaction_count",
                          title = f"{year} TRANSACTION COUNT",
                          color_discrete_sequence = px.colors.sequential.Aggrnyl_r,height = 600,width= 700)
      st.plotly_chart(plod_count)

  lat_lang_of_ind_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
  responce = requests.get(lat_lang_of_ind_url)
  json_data1 = json.loads(responce.content)

  states_list = []
  for itam in json_data1['features']:
      states_list.append(itam['properties']['ST_NM'])

  states_list.sort()

  colmp1, colmp2 = st.columns(2)
  with colmp1:
      fig_india_1 = px.choropleth(tran_amount_count_by_year_group, geojson=json_data1, locations="States",
                                  featureidkey="properties.ST_NM",
                                  color="Transaction_amount", color_continuous_scale="Rainbow",
                                  range_color=(tran_amount_count_by_year_group["Transaction_amount"].min(),
                                               tran_amount_count_by_year_group["Transaction_amount"].max()),
                                  hover_name="States", title=f"{year} TRANSACTION AMOUNT", fitbounds="locations",
                                  height=600, width=600)
      fig_india_1.update_geos(visible=False)

      st.plotly_chart(fig_india_1)

  with colmp2:
      fig_india_2 = px.choropleth(tran_amount_count_by_year_group, geojson=json_data1, locations="States",
                                  featureidkey="properties.ST_NM",
                                  color="Transaction_count", color_continuous_scale="Rainbow",
                                  range_color=(tran_amount_count_by_year_group["Transaction_count"].min(),
                                               tran_amount_count_by_year_group["Transaction_count"].max()),
                                  hover_name="States", title=f"{year} TRANSACTION COUNT", fitbounds="locations",
                                  height=600, width=600)
      fig_india_2.update_geos(visible=False)

      st.plotly_chart(fig_india_2)

  return tran_amount_count_by_year


def transaction_amount_count_by_year_quarter(df,quarter):

  tran_amount_count_by_year1 = df [df["Quarter"] == quarter]
  tran_amount_count_by_year1.reset_index(drop=True,inplace=True)

  tran_amount_count_by_year_group1 = tran_amount_count_by_year1.groupby("States")[["Transaction_count",
                                                                                   "Transaction_amount"]].sum()
  tran_amount_count_by_year_group1.reset_index(inplace=True)

  colmp1,colmp2 = st.columns(2)

  with colmp1:
      plot_amount = px.bar(tran_amount_count_by_year_group1, x = "States",y = "Transaction_amount",
                title = f"YEAR{ tran_amount_count_by_year1 ['Years'].unique()} QUARTER {quarter} : TRANSACTION AMOUNT",
                color_discrete_sequence = ['#58C753'],height = 600,width= 700 )
      st.plotly_chart(plot_amount)

  with colmp2:
      plod_count = px.bar(tran_amount_count_by_year_group1, x = "States",y = "Transaction_count",
                title = f"YEAR{ tran_amount_count_by_year1 ['Years'].unique()} QUARTER {quarter} : TRANSACTION COUNT",
                color_discrete_sequence = px.colors.sequential.Aggrnyl_r,height = 600,width= 700)
      st.plotly_chart(plod_count)


  lat_lang_of_ind_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
  responce = requests.get(lat_lang_of_ind_url)
  json_data1 = json.loads(responce.content)

  states_list = []
  for itam in json_data1['features']:
    states_list.append(itam['properties']['ST_NM'])

  states_list.sort()
  colmp1,colmp2 = st.columns(2)

  with colmp1:
    fig_india_1= px.choropleth(tran_amount_count_by_year_group1, geojson= json_data1,
                locations= "States",
                featureidkey= "properties.ST_NM",
                color= "Transaction_amount",
                color_continuous_scale= "Rainbow",
                range_color= (tran_amount_count_by_year_group1["Transaction_amount"].min(),
                              tran_amount_count_by_year_group1["Transaction_amount"].max()),
                hover_name= "States",
                title= f"YEAR{ tran_amount_count_by_year1 ['Years'].unique()} QUARTER {quarter} : TRANSACTION AMOUNT",
                fitbounds= "locations",
                height= 600,width= 600)
    fig_india_1.update_geos(visible= False)



    st.plotly_chart(fig_india_1)

  with colmp2:
    fig_india_2= px.choropleth(tran_amount_count_by_year_group1, geojson= json_data1,
                locations= "States",
                featureidkey= "properties.ST_NM",
                color= "Transaction_count",
                color_continuous_scale= "Rainbow",
                 range_color= (tran_amount_count_by_year_group1["Transaction_count"].min(),
                               tran_amount_count_by_year_group1["Transaction_count"].max()),
                hover_name= "States",
                title= f"YEAR{ tran_amount_count_by_year1 ['Years'].unique()} QUARTER {quarter} : TRANSACTION COUNT",
                fitbounds= "locations",
                height= 600,width= 600)
    fig_india_2.update_geos(visible= False)


    st.plotly_chart(fig_india_2)

  return tran_amount_count_by_year1

# transaction type
def aggre_Transaction_type(df, state):
    tacby = df[df["States"] == state]
    tacby.reset_index(drop=True, inplace=True)

    tacbyg = tacby.groupby("Transaction_type")[["Transaction_count", "Transaction_amount"]].sum()
    tacbyg.reset_index(inplace=True)

    custom_colors = {
        "Type1": "#636EFA",
        "Type2": "#EF553B",
        "Type3": "#00CC96",
        "Type4": "#AB63FA",
        "Type5": "#FFA15A",

    }

    col1, col2 = st.columns(2)
    with col1:
        fig_pie_1 = px.pie(data_frame=tacbyg, names="Transaction_type", values="Transaction_amount",
                           width=600, title=f"{state.upper()} TRANSACTION AMOUNT", hole=0, color="Transaction_type",
                           color_discrete_map=custom_colors)

        st.plotly_chart(fig_pie_1)

    with col2:
        fig_pie_2 = px.pie(data_frame=tacbyg, names="Transaction_type", values="Transaction_count",
                           width=600, title=f"{state.upper()} TRANSACTION COUNT", hole=0, color="Transaction_type",
                           color_discrete_map=custom_colors)

        st.plotly_chart(fig_pie_2)


# Aggre_User_analysis_1
def Aggre_user_plot_1(df, year):
    auy= df[df["Years"]== year]
    auy.reset_index(drop= True, inplace= True)

    auyg= pd.DataFrame(auy.groupby("Brands")["Transaction_count"].sum())
    auyg.reset_index(inplace= True)

    fig_bar_1= px.bar(auyg, x= "Brands", y= "Transaction_count", title= f"{year}  TRANSACTION COUNT BASED ON BRANDS",
                    width= 1000, color_discrete_sequence= px.colors.sequential.Jet, hover_name= "Brands")
    st.plotly_chart(fig_bar_1)

    return auy

#Aggre_user_Analysis_2
def Aggre_user_plot_2(df, quarter):
    auyq= df[df["Quarter"]== quarter]
    auyq.reset_index(drop= True, inplace= True)

    auyqg= pd.DataFrame(auyq.groupby("Brands")["Transaction_count"].sum())
    auyqg.reset_index(inplace= True)

    fig_bar_1= px.bar(auyqg, x= "Brands", y= "Transaction_count", title=  f"TRANSACTION COUNT BASED ON BRANDS BY QUARTER {quarter}",
                    width= 1000, color_discrete_sequence= px.colors.sequential.Magenta_r, hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return auyq


#Aggre_user_alalysis_3
def Aggre_user_plot_3(df, state):
    auyqs= df[df["States"] == state]
    auyqs.reset_index(drop= True, inplace= True)

    fig_line_1= px.line(auyqs, x= "Brands", y= "Transaction_count", hover_data= "Percentage",
                        title= f"{state.upper()} BRANDS, TRANSACTION COUNT, PERCENTAGE",width= 1000, markers= True)
    st.plotly_chart(fig_line_1)


# district vice map insure
def map_insurance_districts(df, state):
    macby = df[df["States"] == state]
    macby.reset_index(drop=True, inplace=True)

    macbyg = macby.groupby("Districts")[["Transaction_count", "Transaction_amount"]].sum()
    macbyg.reset_index(inplace=True)


    col1, col2 = st.columns(2)
    with col1:
        fig_bar_1 = px.bar(macbyg, x="Transaction_amount", y="Districts", orientation="h", height=750,
                           title=f"STATE :{state.upper()} ( DISTRICT VICE TRANSACTION AMOUNT )",
                           color_discrete_sequence=px.colors.sequential.Mint_r)
        st.plotly_chart(fig_bar_1)


    with col2:
        fig_bar_2= px.bar(macbyg, x= "Transaction_count", y= "Districts", orientation= "h", height= 750,
                        title= f"STATE :{state.upper()} ( DISTRICT VICE TRANSACTION COUNT )",
                        color_discrete_sequence= px.colors.sequential.Bluered_r)
        st.plotly_chart(fig_bar_2)


# map_user_plot_1
def map_user_plot_1_ruao_y(df, year):
    muby= df[df["Years"]== year]
    muby.reset_index(drop= True, inplace= True)

    mubyg= muby.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    mubyg.reset_index(inplace= True)

    colm1,colm2 = st.columns(2)

    with colm1:
        fig_line_1= px.line(mubyg, x = "States", y = "RegisteredUser", title= f"{year} REGISTERED USER",
                               width= 1000, height= 800, markers= True)
        st.plotly_chart(fig_line_1)
    with colm2:
        fig_line_2= px.line(mubyg, x = "States", y = "AppOpens", title= f"{year} APPOPENS",
                               width= 1000, height= 800, markers= True)
        st.plotly_chart(fig_line_2)


    return muby

# map_user_plot_2
def map_user_plot_2_ruao_yq(df, quarter):
    mubyq= df[df["Quarter"]== quarter]
    mubyq.reset_index(drop= True, inplace= True)

    mubyqg= mubyq.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    mubyqg.reset_index(inplace= True)
    colm1,colm2 = st.columns(2)

    with colm1:
        fig_line_1= px.line(mubyqg, x= "States", y= "RegisteredUser",
                            title= f" YEAR: {df['Years'].min()} QUARTER: {quarter} , REGISTERED USER",width= 1000, height= 800, markers= True,
                            color_discrete_sequence= px.colors.sequential.Rainbow_r)
        st.plotly_chart(fig_line_1)
    with colm2:

        fig_line_2= px.line(mubyqg, x= "States", y= "AppOpens",
                            title= f" YEAR: {df['Years'].min()} QUARTER: {quarter} , APPOPENS",width= 1000, height= 800, markers= True,
                            color_discrete_sequence= px.colors.sequential.Rainbow_r)
        st.plotly_chart(fig_line_2)

    return mubyq

#map_user_plot_3
def map_user_plot_3_rud_yq(df, states):
    mubyqsd= df[df["States"]== states]
    mubyqsd.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_map_user_bar_1= px.bar(mubyqsd, x= "RegisteredUser", y= "Districts", orientation= "h",
                                title= f"{states.upper()} REGISTERED USER", height= 800, color_discrete_sequence= px.colors.sequential.Rainbow_r)
        st.plotly_chart(fig_map_user_bar_1)

    with col2:

        fig_map_user_bar_2= px.bar(mubyqsd, x= "AppOpens", y= "Districts", orientation= "h",
                                title= f"{states.upper()} APPOPENS", height= 800, color_discrete_sequence= px.colors.sequential.Rainbow)
        st.plotly_chart(fig_map_user_bar_2)

def Top_in_pin_plot_1(df, state):
    tiy= df[df["States"]== state]
    tiy.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_top_insur_bar_1= px.bar(tiy, x= "Quarter", y= "Transaction_amount", hover_data= "Pincodes",
                                title= "TRANSACTION AMOUNT", height= 650,width= 600,
                                    color_discrete_sequence= px.colors.sequential.GnBu_r)
        st.plotly_chart(fig_top_insur_bar_1)

    with col2:

        fig_top_insur_bar_2= px.bar(tiy, x= "Quarter", y= "Transaction_count", hover_data= "Pincodes",
                                title= "TRANSACTION COUNT", height= 650,width= 600,
                                    color_discrete_sequence= px.colors.sequential.Darkmint_r)
        st.plotly_chart(fig_top_insur_bar_2)


def top_user_plot_1(df, year):
    tuy= df[df["Years"]== year]
    tuy.reset_index(drop= True, inplace= True)

    tuyg= pd.DataFrame(tuy.groupby(["States", "Quarter"])["RegisteredUser"].sum())
    tuyg.reset_index(inplace= True)

    fig_top_plot_1= px.bar(tuyg, x= "States", y= "RegisteredUser", color= "Quarter", width= 1000, height= 800,
                        color_discrete_sequence= px.colors.sequential.Burgyl, hover_name= "States",
                        title= f"{year} REGISTERED USERS")
    st.plotly_chart(fig_top_plot_1)

    return tuy

# top_user_plot_2
def top_user_plot_2(df, state):
    tuys= df[df["States"]== state]
    tuys.reset_index(drop= True, inplace= True)

    fig_top_pot_2= px.bar(tuys, x= "Quarter", y= "RegisteredUser", title= "REGISTEREDUSERS, PINCODES, QUARTER",
                        width= 1000, height= 800, color= "RegisteredUser", hover_data= "Pincodes",
                        color_continuous_scale= px.colors.sequential.Magenta)

    st.plotly_chart(fig_top_pot_2)

# Top Chart

def top_chart_transaction_amount(table_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'phonepe_data.db')
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()

    # plot_1
    query1 = f'''SELECT states, SUM(Transaction_amount) AS Transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_amount DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1 = cursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table_1, columns=("States", "Transaction_amount"))

    col1, col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(df_1, x="States", y="Transaction_amount", title="TOP 10 OF TRANSACTION AMOUNT",
                            hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height=650, width=600)
        st.plotly_chart(fig_amount)

    # plot_2
    query2 = f'''SELECT states, SUM(Transaction_amount) AS Transaction_amount
                FROM {table_name}
                GROUP BY States
                ORDER BY Transaction_amount
                LIMIT 10;'''

    cursor.execute(query2)
    table_2 = cursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table_2, columns=("States", "Transaction_amount"))

    with col2:
        fig_amount_2 = px.bar(df_2, x="States", y="Transaction_amount", title="LAST 10 OF TRANSACTION AMOUNT",
                              hover_name="States",
                              color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height=650, width=600)
        st.plotly_chart(fig_amount_2)

    # plot_3
    query3 = f'''SELECT States, AVG(Transaction_amount) AS Transaction_amount
                FROM {table_name}
                GROUP BY States
                ORDER BY Transaction_amount;'''

    cursor.execute(query3)
    table_3 = cursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table_3, columns=("States", "Transaction_amount"))

    fig_amount_3 = px.bar(df_3, y="States", x="Transaction_amount", title="AVERAGE OF TRANSACTION AMOUNT",
                          hover_name="States", orientation="h",
                          color_discrete_sequence=px.colors.sequential.Bluered_r, height=800, width=1000)
    st.plotly_chart(fig_amount_3)


def top_chart_transaction_count(table_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'phonepe_data.db')
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()

    #plot_1
    query1= f'''SELECT states, SUM(transaction_count) AS transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_count DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table_1, columns=("states", "transaction_count"))

    col1,col2= st.columns(2)
    with col1:
        fig_amount= px.bar(df_1, x="states", y="transaction_count", title="TOP 10 OF TRANSACTION COUNT", hover_name= "states",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)

    #plot_2
    query2= f'''SELECT states, SUM(transaction_count) AS transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_count
                LIMIT 10;'''

    cursor.execute(query2)
    table_2= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table_2, columns=("states", "transaction_count"))

    with col2:
        fig_amount_2= px.bar(df_2, x="states", y="transaction_count", title="LAST 10 OF TRANSACTION COUNT", hover_name= "states",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount_2)

    #plot_3
    query3= f'''SELECT states, AVG(transaction_count) AS transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_count;'''

    cursor.execute(query3)
    table_3= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table_3, columns=("states", "transaction_count"))

    fig_amount_3= px.bar(df_3, y="states", x="transaction_count", title="AVERAGE OF TRANSACTION COUNT", hover_name= "states", orientation= "h",
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount_3)


def top_chart_registered_user(table_name, state):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'phonepe_data.db')
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()

    #plot_1
    query1= f'''SELECT districts, SUM(registereduser) AS registereduser
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY registereduser DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table_1, columns=("districts", "registereduser"))

    col1,col2= st.columns(2)
    with col1:
        fig_amount= px.bar(df_1, x="districts", y="registereduser", title="TOP 10 OF REGISTERED USER", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)

    #plot_2
    query2= f'''SELECT districts, SUM(registereduser) AS registereduser
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY registereduser
                LIMIT 10;'''

    cursor.execute(query2)
    table_2= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table_2, columns=("districts", "registereduser"))

    with col2:
        fig_amount_2= px.bar(df_2, x="districts", y="registereduser", title="LAST 10 REGISTERED USER", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount_2)

    #plot_3
    query3= f'''SELECT districts, AVG(registereduser) AS registereduser
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY registereduser;'''

    cursor.execute(query3)
    table_3= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table_3, columns=("districts", "registereduser"))

    fig_amount_3= px.bar(df_3, y="districts", x="registereduser", title="AVERAGE OF REGISTERED USER", hover_name= "districts", orientation= "h",
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount_3)


def top_chart_appopens(table_name, state):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'phonepe_data.db')
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()

    #plot_1
    query1= f'''SELECT districts, SUM(appopens) AS appopens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY appopens DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table_1, columns=("districts", "appopens"))


    col1,col2= st.columns(2)
    with col1:

        fig_amount= px.bar(df_1, x="districts", y="appopens", title="TOP 10 OF APPOPENS", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
        st.plotly_chart(fig_amount)

    #plot_2
    query2= f'''SELECT districts, SUM(appopens) AS appopens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY appopens
                LIMIT 10;'''

    cursor.execute(query2)
    table_2= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table_2, columns=("districts", "appopens"))

    with col2:

        fig_amount_2= px.bar(df_2, x="districts", y="appopens", title="LAST 10 APPOPENS", hover_name= "districts",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
        st.plotly_chart(fig_amount_2)

    #plot_3
    query3= f'''SELECT districts, AVG(appopens) AS appopens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY appopens;'''

    cursor.execute(query3)
    table_3= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table_3, columns=("districts", "appopens"))

    fig_amount_3= px.bar(df_3, y="districts", x="appopens", title="AVERAGE OF APPOPENS", hover_name= "districts", orientation= "h",
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
    st.plotly_chart(fig_amount_3)


def top_chart_registered_users(table_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'phonepe_data.db')
    mydb = sqlite3.connect(db_path)
    cursor = mydb.cursor()

    # plot_1
    query1 = f'''SELECT states, SUM(RegisteredUser) AS registeredusers
                FROM {table_name}
                GROUP BY states
                ORDER BY registeredusers DESC
                LIMIT 10;'''

    cursor.execute(query1)
    table_1 = cursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table_1, columns=("states", "registeredusers"))

    col1, col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(df_1, x="states", y="registeredusers", title="TOP 10 OF REGISTERED USERS",
                            hover_name="states",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height=650, width=600)
        st.plotly_chart(fig_amount)

    # plot_2
    query2 = f'''SELECT states, SUM(registereduser) AS registeredusers
                FROM {table_name}
                GROUP BY states
                ORDER BY registeredusers
                LIMIT 10;'''

    cursor.execute(query2)
    table_2 = cursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table_2, columns=("states", "registeredusers"))

    with col2:
        fig_amount_2 = px.bar(df_2, x="states", y="registeredusers", title="LAST 10 REGISTERED USERS",
                              hover_name="states",
                              color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height=650, width=600)
        st.plotly_chart(fig_amount_2)

    # plot_3
    query3 = f'''SELECT states, AVG(registereduser) AS registeredusers
                FROM {table_name}
                GROUP BY states
                ORDER BY registeredusers;'''

    cursor.execute(query3)
    table_3 = cursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table_3, columns=("states", "registeredusers"))

    fig_amount_3 = px.bar(df_3, y="states", x="registeredusers", title="AVERAGE OF REGISTERED USERS",
                          hover_name="states", orientation="h",
                          color_discrete_sequence=px.colors.sequential.Bluered_r, height=800, width=1000)
    st.plotly_chart(fig_amount_3)



#Streamlit

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .title {
        color: #9933BD;
        font-size: 36px; /* Adjust the size as needed */
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the title with the custom style
st.markdown('<h1 class="title">PHONEPE DATA VISUALIZATION AND EXPLORATION</h1>', unsafe_allow_html=True)
#st.title("PHONEPE DATA VISUALIZATION AND EXPLORATION")

with st.sidebar:
    select = option_menu("Main Menu", ["HOME", "DATA EXPLORATION", "TOP CHARTS"])

if select == "HOME":
    col1, col2, = st.columns(2)

    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("****Credit & Debit card linking****")
        st.write("****Bank Balance check****")
        st.write("****Money Storage****")
        st.write("****PIN Authorization****")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.image(Image.open(r"C:\Users\sabar\PycharmProjects\phonePe\images\phonepe1.png"), width=550)

    col3, col4,  = st.columns(2)

    with col3:
        st.image(Image.open(r"C:\Users\sabar\PycharmProjects\phonePe\images\PhonePe_Logo-450x450.png"), width=400)

    with col4:
        st.write("****Easy Transactions****")
        st.write("****One App For All Your Payments****")
        st.write("****Your Bank Account Is All You Need****")
        st.write("****Multiple Payment Modes****")
        st.write("****PhonePe Merchants****")
        st.write("****Multiple Ways To Pay****")
        st.write("****1.Direct Transfer & More****")
        st.write("****2.QR Code****")
        st.write("****Earn Great Rewards****")

    col5, col6 = st.columns(2)

    with col5:


        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("****No Wallet Top-Up Required****")
        st.write("****Pay Directly From Any Bank To Any Bank A/C****")
        st.write("****Instant & Free****")


    st.image(Image.open(r"C:\Users\sabar\PycharmProjects\phonePe\images\PhonePe-Offers-700x266.png"), width=1050)


elif select == "DATA EXPLORATION":
    tab1, tab2, tab3 = st.tabs(["Aggregated Data Analysis", "Map Data Analysis", "Top Data Analysis"])

    with tab1:

        method1 = st.radio("Analyze",["Transaction Data  (AGRTD)","Insurance Data  (AGRTD)", "User Data  (AGRTD)"])

        if method1 == "Insurance Data  (AGRTD)":
            colms1,colms2 = st.columns(2)
            with colms1:
                years = st.slider("Select the year",Aggre_insurance["Years"].min(),Aggre_insurance["Years"].max(),
                                  Aggre_insurance["Years"].min())
            tacby_i = transaction_amount_count_by_year(Aggre_insurance,years)

            colm,colm2 = st.columns(2)

            with colm:
                quarter = st.slider("Select the quarter", tacby_i["Quarter"].min(),
                                    tacby_i["Quarter"].max(),tacby_i["Quarter"].min())

            transaction_amount_count_by_year_quarter(tacby_i, quarter)



        elif method1 == "Transaction Data  (AGRTD)" :
            colms1, colms2 = st.columns(2)
            with colms1:
                years = st.slider("Select the year", Aggre_transaction["Years"].min(), Aggre_transaction["Years"].max(),
                                  Aggre_transaction["Years"].min())
            tacby_t = transaction_amount_count_by_year(Aggre_transaction, years)

            colms1, colms2 = st.columns(2)
            with colms1:
                state = st.selectbox("SELECT THE STATE",tacby_t['States'].unique())
            aggre_Transaction_type(tacby_t,state)

            colm,colm2 = st.columns(2)

            with colm:
                quarter = st.slider("Select the quarter", tacby_t ["Quarter"].min(),
                                    tacby_t ["Quarter"].max(),tacby_t ["Quarter"].min())

            tacbyq_t = transaction_amount_count_by_year_quarter(tacby_t , quarter)

            colms1, colms2 = st.columns(2)
            with colms1:
                state = st.selectbox("CHOOSE THE STATE",tacby_t['States'].unique())
            aggre_Transaction_type(tacbyq_t,state)

        elif method1 == "User Data  (AGRTD)":
            colms1, colms2 = st.columns(2)
            with colms1:
                years = st.slider("Select the year [Brands details (2022-2Q to Now) Not available due to some reasons]", Aggre_user["Years"].min(), Aggre_user["Years"].max(),
                                  Aggre_user["Years"].min())
            tacby_u = Aggre_user_plot_1(Aggre_user, years)

            colm,colm2 = st.columns(2)

            with colm:
                quarter = st.selectbox("Select the quarter",tacby_u["Quarter"].unique())
            tacbyq_u = Aggre_user_plot_2(tacby_u , quarter)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State", tacbyq_u["States"].unique())

            Aggre_user_plot_3(tacbyq_u, states)



    with tab2:

        method2 = st.radio("Analyze",["Transaction Data  (MAP)","Insurance Data  (MAP)", "User Data  (MAP)"])

        if method2 == "Insurance Data  (MAP)":

            colms1, colms2 = st.columns(2)
            with colms1:
                years = st.slider("Select the year", Map_insurance["Years"].min(), Map_insurance["Years"].max(),
                                  Map_insurance["Years"].min())
            tacby_m = transaction_amount_count_by_year(Map_insurance, years)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State Year Vice", tacby_m["States"].unique())

            map_insurance_districts(tacby_m, states)

            colm,colm2 = st.columns(2)

            with colm:
                quarter = st.selectbox("Select the quarter ", tacby_m ["Quarter"].unique())

            tacbyq_m = transaction_amount_count_by_year_quarter(tacby_m , quarter)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State Quater Vice", tacbyq_m["States"].unique())

            map_insurance_districts(tacbyq_m, states)

        elif method2 == "Transaction Data  (MAP)" :

            col1, col2 = st.columns(2)
            with col1:

                years = st.slider("Select The Year", Map_transaction["Years"].min(), Map_transaction["Years"].max(),
                                  Map_transaction["Years"].min())
            tacby_m = transaction_amount_count_by_year(Map_transaction, years)

            col1, col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State Year Vice", tacby_m["States"].unique())
            map_insurance_districts(tacby_m,states)

            col1,col2= st.columns(2)
            with col1:

                quarters= st.slider("Select The Quarter",tacby_m["Quarter"].min(), tacby_m["Quarter"].max(),tacby_m["Quarter"].min())
            tacbyq_m= transaction_amount_count_by_year_quarter(tacby_m, quarters)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State Quater Vice", tacbyq_m["States"].unique())

            map_insurance_districts(tacbyq_m, states)

        elif method2 == "User Data  (MAP)":
            col1, col2 = st.columns(2)
            with col1:

                years = st.slider("Select The Year", Map_user["Years"].min(), Map_user["Years"].max(),
                                  Map_user["Years"].min())
            uby_m = map_user_plot_1_ruao_y(Map_user, years)

            col1, col2 = st.columns(2)
            with col1:

                quarters = st.slider("Select The Quarter", uby_m["Quarter"].min(), uby_m["Quarter"].max(),
                                     uby_m["Quarter"].min())
            ubyq_m = map_user_plot_2_ruao_yq(uby_m, quarters)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State", ubyq_m["States"].unique())

            map_user_plot_3_rud_yq(ubyq_m, states)

    with tab3:

        method3 = st.radio("Analyze",["Transaction Data  (TOP)","Insurance Data  (TOP)", "User Data  (TOP)"])

        if method3 == "Insurance Data  (TOP)":
            col1, col2 = st.columns(2)
            with col1:

                years = st.slider("Select The Year", Top_insurance["Years"].min(), Top_insurance["Years"].max(),
                                  Top_insurance["Years"].min())
            tacby_t = transaction_amount_count_by_year(Top_insurance, years)

            col1,col2= st.columns(2)
            with col1:
                states= st.selectbox("Select The State", tacby_t["States"].unique())
            Top_in_pin_plot_1(tacby_t, states)

            col1,col2= st.columns(2)
            with col1:

                quarters= st.slider("Select The Quarter  ",tacby_t["Quarter"].min(), tacby_t["Quarter"].max(),tacby_t["Quarter"].min())
            tit_y_q= transaction_amount_count_by_year_quarter(tacby_t, quarters)


        elif method3 == "Transaction Data  (TOP)" :
            col1, col2 = st.columns(2)
            with col1:

                years = st.slider("Select The Year  ", Top_transaction["Years"].min(), Top_transaction["Years"].max(),
                                  Top_transaction["Years"].min())
            tttY = transaction_amount_count_by_year(Top_transaction, years)

            col1, col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State  ", tttY["States"].unique())

            Top_in_pin_plot_1(tttY, states)

            col1, col2 = st.columns(2)
            with col1:

                quarters = st.slider("Select The Quarter ",tttY["Quarter"].min(),
                                     tttY["Quarter"].max(), tttY["Quarter"].min())
            tttY_Q = transaction_amount_count_by_year_quarter(tttY, quarters)


        elif method3 == "User Data  (TOP)":
            col1, col2 = st.columns(2)
            with col1:

                years = st.slider("Select The Year  ", Top_user["Years"].min(), Top_user["Years"].max(),
                                  Top_user["Years"].min())
            top_user_Y = top_user_plot_1(Top_user, years)

            col1, col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State    ", top_user_Y["States"].unique())

            top_user_plot_2(top_user_Y, states)

elif select == "TOP CHARTS":
    question = st.selectbox("Select the Question", ["1. Transaction Amount and Count of Aggregated Insurance",
                                                    "2. Transaction Amount and Count of Map Insurance",
                                                    "3. Transaction Amount and Count of Top Insurance",
                                                    "4. Transaction Amount and Count of Aggregated Transaction",
                                                    "5. Transaction Amount and Count of Map Transaction",
                                                    "6. Transaction Amount and Count of Top Transaction",
                                                    "7. Transaction Count of Aggregated User",
                                                    "8. Registered users of Map User",
                                                    "9. App opens of Map User",
                                                    "10. Registered users of Top User",
                                                    ])

    if question == "1. Transaction Amount and Count of Aggregated Insurance":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("aggregated_insurance")

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("aggregated_insurance")

    elif question == "2. Transaction Amount and Count of Map Insurance":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("map_insurance")

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("map_insurance")

    elif question == "3. Transaction Amount and Count of Top Insurance":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("top_insurance")

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("top_insurance")

    elif question == "4. Transaction Amount and Count of Aggregated Transaction":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("aggregated_transaction")

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("aggregated_transaction")

    elif question == "5. Transaction Amount and Count of Map Transaction":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("map_transaction")

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("map_transaction")

    elif question == "6. Transaction Amount and Count of Top Transaction":

        st.subheader("TRANSACTION AMOUNT")
        top_chart_transaction_amount("top_transaction")

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("top_transaction")

    elif question == "7. Transaction Count of Aggregated User":

        st.subheader("TRANSACTION COUNT")
        top_chart_transaction_count("aggregated_user")

    elif question == "8. Registered users of Map User":

        states = st.selectbox("Select the State", Map_user["States"].unique())
        st.subheader("REGISTERED USERS")
        top_chart_registered_user("map_user", states)

    elif question == "9. App opens of Map User":

        states = st.selectbox("Select the State", Map_user["States"].unique())
        st.subheader("APPOPENS")
        top_chart_appopens("map_user", states)

    elif question == "10. Registered users of Top User":

        st.subheader("REGISTERED USERS")
        top_chart_registered_users("top_user")

