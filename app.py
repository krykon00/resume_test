"""Main app file"""
import streamlit as st

from src import utils

st.set_page_config(
  page_title="Gawel Design",
  page_icon=":art:",
  layout="wide",
  initial_sidebar_state="collapsed"
)

langs: dict = utils.get_langs_names()

# --- side bar ---
with st.sidebar:
    lang = st.selectbox(label="Language", options=langs.keys(), index=0)
    content = utils.read_json(langs[lang])
    
    st.markdown("""---""")
    
    with st.container() as links:
        for name, url in  content["links"].items():
            st.markdown(f"[{name}]({url})")

    
with st.container() as header: # Header with profile pic and basic informations 
    photo_column, basic_info_column = st.columns(2)
    with photo_column:
        st.image('src/assets/rafal.png', width=300)
    with basic_info_column:
        st.title(content["title"])
        st.caption(content["short_info"])
        st.caption(f'{content["contact"]["email"]} | {content["contact"]["tel"]}')
        st.button(label=content["csv_button_label"])

with st.container() as main_body:
    tabs_list = list(content["tabs"].keys())
    tab_skills, tab_video, tab_img = st.tabs(tabs_list)
    with tab_skills:
        tab_content = content["tabs"][tabs_list[0]]
        st.header(tab_content["header"])
        for name, elements  in tab_content["elements"].items():
            st.markdown(f"### {name}")
            for elem_name, elem_content in elements.items():
                st.markdown(f"__{elem_name}:__ {elem_content}")
    with tab_video:
        tab_content = content["tabs"][tabs_list[1]]
        n_of_videos = len(tab_content)
        names = list(tab_content.keys())
        links = list(tab_content.values())
        for i in range(0, int(n_of_videos/3)+1):
            with st.container():
                columns = st.columns(3)
                for column in columns:
                    with column:
                        try:
                            st.header(names.pop())
                            st.video(links.pop())
                        except IndexError:
                            pass # If number of videos is uneven


