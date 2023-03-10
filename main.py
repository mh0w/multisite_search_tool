# -*- coding: utf-8 -*-
"""
Multisite search tool.

Created: January 2023

@author: Matthew Hawkes

"""

import streamlit as st
from bokeh.models.widgets import Div
from st_keyup import st_keyup
from extra_sites_list import create_extra_sites_list


def config_streamlit_page():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="Multisite search",
        page_icon="🦆",  # critical feature
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={"Get Help": None, "Report a bug": None, "About": None},
    )


def create_page():
    """Create the Streamlit page."""
    st.sidebar.write(
        "Select the sites you want to search:<br>",
        unsafe_allow_html=True,  # enables markup language e.g. <b>text</b>
    )

    default_sites_list = {
        "Private Gists": "https://gist.github.com/search?q=SEARCH_TEXT_HERE+user:mh0w",
        "Public Gists": "https://gist.github.com/search?q=SEARCH_TEXT_HERE",
        "Google": "https://google.com/search?q=SEARCH_TEXT_HERE",
        "Best Practice": "https://best-practice-and-impact.github.io/qa-of-code-guidance/search.html?q=SEARCH_TEXT_HERE",
        "StackOverflow": "https://stackoverflow.com/search?q=SEARCH_TEXT_HERE",
        "Stack Google": "https://google.com/search?q=Stack+SEARCH_TEXT_HERE",
        "ONS website": "https://www.ons.gov.uk/search?q=SEARCH_TEXT_HERE",
        "Yammer": "https://web.yammer.com/main/search/threads?search=SEARCH_TEXT_HERE",
    }

    extra_sites_list = create_extra_sites_list()

    sites_list = {**default_sites_list, **extra_sites_list}

    sites_list = dict(sorted(sites_list.items()))

    checkboxes = {}

    for site in sites_list.keys():
        checkboxes[f"{site}"] = st.sidebar.checkbox(
            f"{site}",
            value=False,
        )

    st.sidebar.write("")

    st.markdown(
        (
            """<h1 style="text-align: center;">Multisite search</h1>"""
        ),
        unsafe_allow_html=True,  # enables markdown like <p>text</p>
    )

    search_string = st_keyup(
        label="Enter your search text below",
        label_visibility="visible",
        placeholder="Enter your search text here. E.g., python merge pandas dataframes",
    )
    st.write(f"""Click 'Search' to search for: {search_string}""")

    def search(site):
        js = f"window.open('{site}')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    if st.button("Search"):
        for key, value in sites_list.items():
            if checkboxes[f"{key}"] is True:
                value = value.replace("SEARCH_TEXT_HERE", f"{search_string}")
                search(f"{value}")

    st.write()

    st.sidebar.write("[GitHub Repo](https://github.com/mh0w/multisite_search_tool)")


config_streamlit_page()
create_page()
