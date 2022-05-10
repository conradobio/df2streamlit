import streamlit as st
import pandas as pd


class Module:
    name = "Module"
    key = "module"
    instances = []
    submit_buttons = []

    def __init__(self):
        df = pd.read_csv("example.csv")
        df = df[['sentence', 'label', 'suggested_label']]
        df.columns = ['sentence.text_input.2', 'label.selectbox.1', 'suggested_label.checkbox.1']
        st.table(df.head(2))
        self.df2form(df.head(10))

    def build(self, key_index=None):
        if not key_index:
            key_index = len(self.instances)
        self.create_form(key_index)
        self.instances.append(self.name)

    def build_many(self, n):
        for i in range(n):
            self.build(i)

    def is_selectbox(self, key):
        return key.split(".")[1] == "selectbox"

    def is_text_input(self, key):
        return key.split(".")[1] == "text_input"

    def is_multiselect(self, key):
        return key.split(".")[1] == "multiselect"

    def is_checkbox(self, key):
        return key.split(".")[1] == "checkbox"

    def is_radio(self, key):
        return key.split(".")[1] == "radio"

    def is_button(self, key):
        return key.split(".")[1] == "button"

    def is_text(self, key):
        return key.split(".")[1] == "text"

    def df2form(self, df, submit_name='save'):
        """
        Component pattern: name.type.size
        "sentence.text_input.2"
        "class.selectbox.1"
        """
        for i, row in df.iterrows():
            form_key = f"{self.name}_form_{i}"
            with st.form(form_key):
                cols = st.columns([int(col.split(".")[-1]) for col in df.columns])
                for df_col, st_col in zip(df.columns, cols):

                    if self.is_selectbox(df_col):
                        st_col.selectbox(df_col.split(".")[0], row[df_col], key=f"{self.key}_{i}")

                    if self.is_multiselect(df_col):
                        st_col.multiselect(df_col.split(".")[0], row[df_col], key=f"{self.key}_{i}")

                    if self.is_text_input(df_col):
                        st_col.text_input(df_col.split(".")[0], row[df_col], key=f"{row[df_col]}_{i}")

                    if self.is_checkbox(df_col):
                        st_col.checkbox(row[df_col], key=f"{self.key}_{i}")

                    # if self.is_radio(df_col):
                    #     st_col.radio(key=f"{self.key}_{i}")

                    if self.is_button(df_col):
                        self.add_submit_button(row[df_col], i, st_col)

                    if self.is_text(df_col):
                        st_col.write(row[df_col])

                self.add_submit_button(submit_name, form_key, cols[0])


    def add_submit_button(self, label, form_key, col):
        button_key = f"FormSubmitter:{form_key}-{label}"
        if button_key not in st.session_state:
            col.form_submit_button(label)
            self.submit_buttons.append(button_key)


if __name__ == "__main__":
    Module()