import pymongo
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
client = pymongo.MongoClient("mongodb+srv://Raja:Shravanib30@serverlessinstance0.5atee.mongodb.net/?retryWrites=true&w=majority")
db = client["UserRegistrations"]
col = db["UserDatabase"]
List = []
names = []
for x in col.find():
    del x["Password"]
    name = x["Name"]
    names.append(name)
    List.append(x)
df = pd.DataFrame(List).from_records(List)
print(df)
st.set_page_config(layout='wide',page_title="Test LMS: Code to Change Jr.",page_icon="images/favicon.png",initial_sidebar_state="expanded")
st.markdown("<h2 style='text-align: center; color: #ffffff;background-color:#0ea2bd;border-radius:5px;'>C2C Jr : Admin Panel</h2>", unsafe_allow_html=True)
with st.sidebar:
    menu = option_menu("Admin menu",['Scoreboard', "User portal"],menu_icon="person-bounding-box"
                       ,icons=["clipboard-data", "person-check-fill"], default_index=1,
                       styles={"nav-link-selected": {"background-color": "#0ea2bd"}})
if menu == "User portal":
    st.markdown("<h1 style = 'text-align:center;  color:#0ea2bd;'>User Details</h1>",unsafe_allow_html=True)
    name = st.sidebar.selectbox("Select the names",names)
    details = col.find_one({"Name":name})
    cols = st.columns([1,2,6,1])
    cols[1].markdown("<h3 style = 'color:#0ea2bd;'>Name</h3>",unsafe_allow_html=True)
    cols[2].markdown("<h3>"+details["Name"]+"</h3>",unsafe_allow_html=True)
    cols[1].markdown("<h3 style = 'color:#0ea2bd;'>Email</h3>", unsafe_allow_html=True)
    cols[2].markdown("<h3>" + details["Email"] + "</h3>", unsafe_allow_html=True)
    cols[1].markdown("<h3 style = 'color:#0ea2bd;'>Courses</h3>", unsafe_allow_html=True)
    cols[2].markdown("<h3>" + ', '.join(details["Courses"]) + "</h3>", unsafe_allow_html=True)
    cols[1].markdown("<h3 style = 'color:#0ea2bd;'>Status</h3>", unsafe_allow_html=True)
    cols[2].markdown("<h3>" + details["Approval"] + "</h3>", unsafe_allow_html=True)
    if cols[1].checkbox("Approve"):
        col.find_one_and_update({"Name":name},{"$set":{"Approval":"Approved"}},upsert=True)
        st.markdown("")
        st.success("User is approved to access the portal.")
    st.markdown("<h1 style = 'text-align:center;  color:#0ea2bd;'>Update the scores</h1>", unsafe_allow_html=True)
    cols_score = st.columns([1,1,1,1])
    score_type = cols_score[1].selectbox("Select the score type",["Animations Reward","Animations Rating","AI Reward","AI Rating"])
    if score_type=="Animations Reward":
        score = cols_score[2].number_input("Enter the Reward")
        if cols_score[1].checkbox("update"):
            col.find_one_and_update({"Name": name}, {"$set": {"AnimationXp": details["AnimationXp"]+score}}, upsert=True)
            st.success("Score updated successfully")
    if score_type=="Animations Rating":
        score = cols_score[2].number_input("Enter the Rating")
        if cols_score[1].checkbox("update"):
            col.find_one_and_update({"Name": name}, {"$set": {"AnimationR": details["AnimationR"]+score}}, upsert=True)
            st.success("Score updated successfully")
    if score_type=="AI Reward":
        score = cols_score[2].number_input("Enter the Reward",key="AI")
        if cols_score[1].checkbox("update"):
            col.find_one_and_update({"Name": name}, {"$set": {"AIXP": details["AIXP"]+score}}, upsert=True)
            st.success("Score updated successfully")
    if score_type=="AI Rating":
        score = cols_score[2].number_input("Enter the Rating",key="AI")
        if cols_score[1].checkbox("update"):
            col.find_one_and_update({"Name": name}, {"$set": {"AIR": details["AIR"]+score}}, upsert=True)
            st.success("Score updated successfully")
if menu == "Scoreboard":
    st.markdown("<h1></h1>",unsafe_allow_html=True)
    df_1 = df.drop(["_id","Contact","Email","Courses","Avatar","Appreciation"],axis=1)
    df2=df_1.set_index("Name")
    st.table(df2.style.format({"AnimationXp":"{:.0f}✨","AnimationR":"{:.0f}💫","AIXP":"{:.0f}✨","AIR":"{:.0f}💫"}))
    with st.expander("Abbreviations"):
        st.markdown("")
        st.markdown("1.AnimationXp - Rewards in Animation")
        st.markdown("2.AnimationR - Rating in Animation")
        st.markdown("3.AIXP - Rewards in AI")
        st.markdown("4.AIR - Rating in AI")











