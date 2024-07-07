import os
import json
import pandas as pd
import sqlite3

# AGGREGATED TRANSACTION

aggregated_transaction_list_of_india_path1 = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/aggregated/transaction/country/india/state/"
aggregated_transaction_list_of_india = os.listdir(aggregated_transaction_list_of_india_path1)

coloumns = {"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}
for state in aggregated_transaction_list_of_india:
  create_path_to_state= aggregated_transaction_list_of_india_path1 + state + "/"
  created_path_to_state = os.listdir(create_path_to_state)

  for year in created_path_to_state:
    create_path_to_year = create_path_to_state + year + "/"
    created_path_to_year = os.listdir(create_path_to_year)

    for file in created_path_to_year:
      create_path_to_file = create_path_to_year + file
      file_data_open = open(create_path_to_file, "r")

      a = json.load(file_data_open)

      for i in a['data']['transactionData']:
        name = i['name']
        count =i['paymentInstruments'][0]['count']
        amount = i['paymentInstruments'][0]['amount']
        coloumns['Transaction_type'].append(name)
        coloumns['Transaction_count'].append(count)
        coloumns['Transaction_amount'].append(amount)
        coloumns['States'].append(state)
        coloumns['Years'].append(year)
        coloumns['Quarter'].append(int(file.strip('.json')))


aggregated_transaction_list_of_india_df = pd.DataFrame(coloumns)


aggregated_transaction_list_of_india_df["States"] = aggregated_transaction_list_of_india_df["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggregated_transaction_list_of_india_df["States"] = aggregated_transaction_list_of_india_df["States"].str.replace("-"," ")
aggregated_transaction_list_of_india_df["States"] = aggregated_transaction_list_of_india_df["States"].str.title()
aggregated_transaction_list_of_india_df["States"] = aggregated_transaction_list_of_india_df['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



# AGGREGATED USER

aggregated_user_list_of_india_path2 = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/aggregated/user/country/india/state/"
aggregated_user_list_of_india = os.listdir( aggregated_user_list_of_india_path2)

coloumns_2 = {"States":[],"Years":[],"Quarter":[],'Brand':[],"Transaction_count":[],'Percentage':[]}

for state_u in aggregated_user_list_of_india:
  create_path_to_state2 = aggregated_user_list_of_india_path2 + state_u + "/"
  created_path_to_state2 = os.listdir(create_path_to_state2)

  for year_u in created_path_to_state2:
    create_path_to_year2 = create_path_to_state2 + year_u + "/"
    created_path_to_year2 = os.listdir(create_path_to_year2)

    for file_u in created_path_to_year2:
      create_path_to_file2 = create_path_to_year2 + file_u
      file_data_open2 = open(create_path_to_file2, "r")

      b = json.load(file_data_open2)

    if b['data'].get('usersByDevice') is not None:
        for i in b['data']['usersByDevice']:
            brand = i['brand']
            count = i['count']
            percentage = i['percentage']

            coloumns_2['Brand'].append(brand)
            coloumns_2['Transaction_count'].append(count)
            coloumns_2['Percentage'].append(percentage)
            coloumns_2['States'].append(state_u)
            coloumns_2['Years'].append(year_u)
            coloumns_2['Quarter'].append(int(file_u.strip('.json')))
    else:
        print("usersByDevice is None or does not exist")

aggregated_user_list_of_india_df = pd.DataFrame(coloumns_2)


aggregated_user_list_of_india_df["States"] = aggregated_user_list_of_india_df["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggregated_user_list_of_india_df["States"] = aggregated_user_list_of_india_df["States"].str.replace("-"," ")
aggregated_user_list_of_india_df["States"] = aggregated_user_list_of_india_df["States"].str.title()
aggregated_user_list_of_india_df["States"] = aggregated_user_list_of_india_df['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


# AGGREGATED INSURANCE

aggregated_insurance_list_of_india_path_1_2conti = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/aggregated/insurance/country/india/state/"
aggregated_insurance_list_of_india = os.listdir(aggregated_insurance_list_of_india_path_1_2conti)

columns1_2conti= {"States":[], "Years":[], "Quarter":[], "Insurance_type":[], "Insurance_count":[],"Insurance_amount":[] }

for state_ai in aggregated_insurance_list_of_india:
  create_path_to_state_1_2conti = aggregated_insurance_list_of_india_path_1_2conti + state_ai + "/"
  created_path_to_state_1_2conti = os.listdir(create_path_to_state_1_2conti)

  for year_ai in created_path_to_state_1_2conti:
    create_path_to_year_1_2conti = create_path_to_state_1_2conti + year_ai + "/"
    created_path_to_year_1_2conti = os.listdir(create_path_to_year_1_2conti)

    for file_ai in created_path_to_year_1_2conti:
      create_path_to_file_1_2conti = create_path_to_year_1_2conti + file_ai
      file_data_open_1_2conti = open(create_path_to_file_1_2conti, "r")

      ab_conti = json.load(file_data_open_1_2conti)

      for i in ab_conti["data"]["transactionData"]:
        name = i["name"]
        count = i["paymentInstruments"][0]["count"]
        amount = i["paymentInstruments"][0]["amount"]
        columns1_2conti["Insurance_type"].append(name)
        columns1_2conti["Insurance_count"].append(count)
        columns1_2conti["Insurance_amount"].append(amount)
        columns1_2conti["States"].append(state_ai)
        columns1_2conti["Years"].append(year_ai)
        columns1_2conti["Quarter"].append(int(file_ai.strip(".json")))


aggregated_insurance_list_of_indiadf = pd.DataFrame(columns1_2conti)


aggregated_insurance_list_of_indiadf["States"] = aggregated_insurance_list_of_indiadf["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggregated_insurance_list_of_indiadf["States"] = aggregated_insurance_list_of_indiadf["States"].str.replace("-"," ")
aggregated_insurance_list_of_indiadf["States"] = aggregated_insurance_list_of_indiadf["States"].str.title()
aggregated_insurance_list_of_indiadf['States'] = aggregated_insurance_list_of_indiadf['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


# MAP TRANSACTION

map_transaction_of_india_path3 = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/map/transaction/hover/country/india/state/"
map_transaction_of_india = os.listdir(map_transaction_of_india_path3)

coloumns_3 = {"States":[],"Years":[],"Quarter":[],'District':[],"Transaction_count":[],"Transaction_amount":[]}

for state_mt in map_transaction_of_india:
  create_path_to_state3 = map_transaction_of_india_path3 + state_mt + "/"
  created_path_to_state3 = os.listdir(create_path_to_state3)

  for year_mt in created_path_to_state3:
    create_path_to_year3 = create_path_to_state3 + year_mt + "/"
    created_path_to_year3 = os.listdir(create_path_to_year3)

    for file_mt in created_path_to_year3:
      create_path_to_file3 = create_path_to_year3 + file_mt
      file_data_open3 = open(create_path_to_file3, "r")

      c = json.load(file_data_open3)

      for i in c['data']['hoverDataList']:
        name = i['name']
        count =i['metric'][0]['count']
        amount = i['metric'][0]['amount']
        coloumns_3['District'].append(name)
        coloumns_3['Transaction_count'].append(count)
        coloumns_3['Transaction_amount'].append(amount)
        coloumns_3['States'].append(state_mt)
        coloumns_3['Years'].append(year_mt)
        coloumns_3['Quarter'].append(int(file_mt.strip('.json')))


map_transaction_list_of_india_df = pd.DataFrame(coloumns_3)


map_transaction_list_of_india_df["States"] = map_transaction_list_of_india_df["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_transaction_list_of_india_df["States"] = map_transaction_list_of_india_df["States"].str.replace("-"," ")
map_transaction_list_of_india_df["States"] = map_transaction_list_of_india_df["States"].str.title()
map_transaction_list_of_india_df["States"] = map_transaction_list_of_india_df['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


# MAP USER

map_user_list_of_india_path4 = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/map/user/hover/country/india/state/"
map_user_list_of_india = os.listdir(map_user_list_of_india_path4)

columns4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

for state_mu in map_user_list_of_india:
  create_path_to_state4 = map_user_list_of_india_path4 + state_mu + "/"
  created_path_to_state4 = os.listdir(create_path_to_state4)

  for year_mu in created_path_to_state4:
    create_path_to_year4 = create_path_to_state4 + year_mu + "/"
    created_path_to_year4 = os.listdir(create_path_to_year4)

    for file_mu in created_path_to_year4:
      create_path_to_file4 = create_path_to_year4 + file_mu
      file_data_open4 = open(create_path_to_file4, "r")

      d = json.load(file_data_open4)


      for i in d["data"]["hoverData"].items():
          district = i[0]
          registereduser = i[1]["registeredUsers"]
          appopens = i[1]["appOpens"]
          columns4["Districts"].append(district)
          columns4["RegisteredUser"].append(registereduser)
          columns4["AppOpens"].append(appopens)
          columns4["States"].append(state_mu)
          columns4["Years"].append(year_mu)
          columns4["Quarter"].append(int(file_mu.strip(".json")))


map_user_list_of_indiadf = pd.DataFrame(columns4)


map_user_list_of_indiadf["States"] = map_user_list_of_indiadf["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user_list_of_indiadf["States"] = map_user_list_of_indiadf["States"].str.replace("-"," ")
map_user_list_of_indiadf["States"] = map_user_list_of_indiadf["States"].str.title()
map_user_list_of_indiadf['States'] = map_user_list_of_indiadf['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


# MAP INSURANCE

map_insurance_list_of_india_path3_4conti = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/map/insurance/hover/country/india/state/"
map_insurance_list_of_india = os.listdir(map_insurance_list_of_india_path3_4conti)

columns3_4conti = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Transaction_count":[],"Transaction_amount":[] }

for state_mi in map_insurance_list_of_india:
  create_path_to_state3_4conti = map_insurance_list_of_india_path3_4conti + state_mi + "/"
  created_path_to_state3_4conti = os.listdir(create_path_to_state3_4conti)

  for year_mi in created_path_to_state3_4conti:
    create_path_to_year3_4conti = create_path_to_state3_4conti + year_mi + "/"
    created_path_to_year3_4conti = os.listdir(create_path_to_year3_4conti)

    for file_mi in created_path_to_year3_4conti:
      create_path_to_file3_4conti = create_path_to_year3_4conti + file_mi
      file_data_open3_4conti = open(create_path_to_file3_4conti, "r")

      cd_conti = json.load(file_data_open3_4conti)

      for i in cd_conti["data"]["hoverDataList"]:
        name = i["name"]
        count = i["metric"][0]["count"]
        amount = i["metric"][0]["amount"]
        columns3_4conti["Districts"].append(name)
        columns3_4conti["Transaction_count"].append(count)
        columns3_4conti["Transaction_amount"].append(amount)
        columns3_4conti["States"].append(state_mi)
        columns3_4conti["Years"].append(year_mi)
        columns3_4conti["Quarter"].append(int(file_mi.strip(".json")))


map_insurance_list_of_indiadf = pd.DataFrame(columns3_4conti)


map_insurance_list_of_indiadf["States"] = map_insurance_list_of_indiadf["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_insurance_list_of_indiadf["States"] = map_insurance_list_of_indiadf["States"].str.replace("-"," ")
map_insurance_list_of_indiadf["States"] = map_insurance_list_of_indiadf["States"].str.title()
map_insurance_list_of_indiadf['States'] = map_insurance_list_of_indiadf['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


# TOP TRANSACTION

top_transaction_list_of_india_path5 = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/top/transaction/country/india/state/"
top_transaction_list_of_india = os.listdir(top_transaction_list_of_india_path5)

columns5 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state_tt in top_transaction_list_of_india:
  create_path_to_state5 = top_transaction_list_of_india_path5 + state_tt + "/"
  created_path_to_state5 = os.listdir(create_path_to_state5)

  for year_tt in created_path_to_state5:
    create_path_to_year5 = create_path_to_state5 + year_tt + "/"
    created_path_to_year5 = os.listdir(create_path_to_year5)

    for file_tt in created_path_to_year5:
      create_path_to_file5 = create_path_to_year5 + file_tt
      file_data_open5 = open(create_path_to_file5, "r")

      e = json.load(file_data_open5)

      for i in e["data"]["pincodes"]:
        entityName = i["entityName"]
        count = i["metric"]["count"]
        amount = i["metric"]["amount"]
        columns5["Pincodes"].append(entityName)
        columns5["Transaction_count"].append(count)
        columns5["Transaction_amount"].append(amount)
        columns5["States"].append(state_tt)
        columns5["Years"].append(year_tt)
        import re
        quarter = re.search(r'\d+', file_tt).group()
        columns5["Quarter"].append(int(quarter))


top_transaction_list_of_indiadf = pd.DataFrame(columns5)


top_transaction_list_of_indiadf["States"] = top_transaction_list_of_indiadf["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_transaction_list_of_indiadf["States"] = top_transaction_list_of_indiadf["States"].str.replace("-"," ")
top_transaction_list_of_indiadf["States"] = top_transaction_list_of_indiadf["States"].str.title()
top_transaction_list_of_indiadf['States'] = top_transaction_list_of_indiadf['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



# TOP USER

top_user_list_of_india_path6 = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/top/user/country/india/state/"
top_user_list_of_india = os.listdir(top_user_list_of_india_path6)

columns6 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for state_tu in top_transaction_list_of_india:
  create_path_to_state6 = top_user_list_of_india_path6 + state_tu + "/"
  created_path_to_state6 = os.listdir(create_path_to_state6)

  for year_tu in created_path_to_state6:
    create_path_to_year6 = create_path_to_state6 + year_tu + "/"
    created_path_to_year6 = os.listdir(create_path_to_year6)

    for file_tu in created_path_to_year6:
      create_path_to_file6 = create_path_to_year6 + file_tu
      file_data_open6 = open(create_path_to_file6, "r")

      f = json.load(file_data_open6)


      for i in f["data"]["pincodes"]:
          name = i["name"]
          registeredusers = i["registeredUsers"]
          columns6["Pincodes"].append(name)
          columns6["RegisteredUser"].append(registeredusers)
          columns6["States"].append(state_tu)
          columns6["Years"].append(year_tu)
          columns6["Quarter"].append(int(file_tu.strip(".json")))


top_user_list_of_indiadf = pd.DataFrame(columns6)



top_user_list_of_indiadf["States"] = top_user_list_of_indiadf["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_user_list_of_indiadf["States"] = top_user_list_of_indiadf["States"].str.replace("-"," ")
top_user_list_of_indiadf["States"] = top_user_list_of_indiadf["States"].str.title()
top_user_list_of_indiadf['States'] = top_user_list_of_indiadf['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



# TOP INSURANCE

top_insurance_list_of_india_path5_6conti = "C:/Users/sabar/OneDrive/Desktop/phonePe Data/pulse/data/top/insurance/country/india/state/"
top_insurance_list_of_india = os.listdir(top_insurance_list_of_india_path5_6conti)

columns5_6conti = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state_ti in top_insurance_list_of_india:
  create_path_to_state5_6conti = top_insurance_list_of_india_path5_6conti + state_ti + "/"
  created_path_to_state5_6conti = os.listdir(create_path_to_state5_6conti)

  for year_ti in created_path_to_state5_6conti:
    create_path_to_year5_6conti = create_path_to_state5_6conti + year_ti + "/"
    created_path_to_year5_6conti = os.listdir(create_path_to_year5_6conti)

    for file_ti in created_path_to_year5_6conti:
      create_path_to_file5_6conti = create_path_to_year5_6conti + file_ti
      file_data_open5_6conti = open(create_path_to_file5_6conti, "r")

      ef_conti = json.load(file_data_open5_6conti)

      for i in ef_conti["data"]["pincodes"]:
        entityName = i["entityName"]
        count = i["metric"]["count"]
        amount = i["metric"]["amount"]
        columns5_6conti["Pincodes"].append(entityName)
        columns5_6conti["Transaction_count"].append(count)
        columns5_6conti["Transaction_amount"].append(amount)
        columns5_6conti["States"].append(state_ti)
        columns5_6conti["Years"].append(year_ti)
        columns5_6conti["Quarter"].append(int(file_ti.strip(".json")))


top_insurance_list_of_indiadf = pd.DataFrame(columns5_6conti)


top_insurance_list_of_indiadf["States"] = top_insurance_list_of_indiadf["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_insurance_list_of_indiadf["States"] = top_insurance_list_of_indiadf["States"].str.replace("-"," ")
top_insurance_list_of_indiadf["States"] = top_insurance_list_of_indiadf["States"].str.title()
top_insurance_list_of_indiadf['States'] = top_user_list_of_indiadf['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


#************************************************************************************************************************************

# sqlite connection
mydb = sqlite3.connect(database = "phonepe_data.db" )
cursor = mydb.cursor()

#aggregated transaction table
create_query1 = '''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Transaction_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''
cursor.execute(create_query1)
mydb.commit()

for index,row in aggregated_transaction_list_of_india_df.iterrows():
    insert_query1 = '''INSERT INTO aggregated_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                        values(?,?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Transaction_type"],
              row["Transaction_count"],
              row["Transaction_amount"]
              )
    cursor.execute(insert_query1,values)
    mydb.commit()


#aggregated user table
create_query2 = '''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                Brands varchar(50),
                                                                Transaction_count bigint,
                                                                Percentage float)'''
cursor.execute(create_query2)
mydb.commit()

for index,row in aggregated_user_list_of_india_df.iterrows():
    insert_query2 = '''INSERT INTO aggregated_user (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                                    values(?,?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Brand"],
              row["Transaction_count"],
              row["Percentage"])
    cursor.execute(insert_query2,values)
    mydb.commit()


# Aggregated insurance table
create_query3= '''CREATE TABLE if not exists aggregated_insurance (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Insurance_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''
cursor.execute(create_query3)
mydb.commit()

for index,row in aggregated_insurance_list_of_indiadf.iterrows():
    insert_query3 = '''INSERT INTO aggregated_insurance (States, Years, Quarter, Insurance_type, Transaction_count, Transaction_amount)
                                                        values(?,?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Insurance_type"],
              row["Insurance_count"],
              row["Insurance_amount"]
              )
    cursor.execute(insert_query3,values)
    mydb.commit()


#map_transaction_table
create_query4 = '''CREATE TABLE if not exists map_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                District varchar(50),
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''
cursor.execute(create_query4)
mydb.commit()

for index,row in map_transaction_list_of_india_df.iterrows():
            insert_query4 = '''
                INSERT INTO map_Transaction (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                VALUES (?, ?, ?, ?, ?, ?)

            '''
            values = (
                row['States'],
                row['Years'],
                row['Quarter'],
                row['District'],
                row['Transaction_count'],
                row['Transaction_amount']
            )
            cursor.execute(insert_query4,values)
            mydb.commit()


#map_user_table
create_query5 = '''CREATE TABLE if not exists map_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(50),
                                                        RegisteredUser bigint,
                                                        AppOpens bigint)'''
cursor.execute(create_query5)
mydb.commit()

for index,row in map_user_list_of_indiadf.iterrows():
    insert_query5 = '''INSERT INTO map_user (States, Years, Quarter, Districts, RegisteredUser, AppOpens)
                        values(?,?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Districts"],
              row["RegisteredUser"],
              row["AppOpens"])
    cursor.execute(insert_query5,values)
    mydb.commit()


#map_insurance_table
create_query6 = '''CREATE TABLE if not exists map_insurance (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                District varchar(50),
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''
cursor.execute(create_query6)
mydb.commit()

for index,row in map_insurance_list_of_indiadf.iterrows():
            insert_query6 = '''
                INSERT INTO map_insurance (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                VALUES (?, ?, ?, ?, ?, ?)

            '''
            values = (
                row['States'],
                row['Years'],
                row['Quarter'],
                row['Districts'],
                row['Transaction_count'],
                row['Transaction_amount']
            )
            cursor.execute(insert_query6,values)
            mydb.commit()


#top_transaction_table

create_query7 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
cursor.execute(create_query7)
mydb.commit()

for index,row in top_transaction_list_of_indiadf.iterrows():
    insert_query7 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(?,?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
    cursor.execute(insert_query7,values)
    mydb.commit()



#top_user_table
create_query8 = '''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                        )'''
cursor.execute(create_query8)
mydb.commit()

for index,row in top_user_list_of_indiadf.iterrows():
    insert_query8 = '''INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser)
                                            values(?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["RegisteredUser"])
    cursor.execute(insert_query8,values)
    mydb.commit()



#top_insurance_table
create_query9 = '''CREATE TABLE if not exists top_insurance (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                Pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
cursor.execute(create_query9)
mydb.commit()

for index,row in top_insurance_list_of_indiadf.iterrows():
    insert_query9 = '''INSERT INTO top_insurance (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(?,?,?,?,?,?)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
    cursor.execute(insert_query9,values)
    mydb.commit()



mydb.close()
