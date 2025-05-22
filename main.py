import pandas as pd
import streamlit as st

file1 = st.file_uploader("Input Excel file", type=["xlsx"])
file2 = st.file_uploader("Source Excel file", type=["xlsx"])

if file1 and file2:
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    st.write("Input file preview:")
    st.dataframe(df1)
    st.write("Source file preview:")
    st.dataframe(df2)

    # Compare dataframes
    comparison_result = pd.concat([df1, df2, df2]).drop_duplicates(keep=False)

    st.write("Differences:")
    st.dataframe(comparison_result)

    # Download result
    if not comparison_result.empty:
        output_filename = "excel_differences.xlsx"
        comparison_result.to_excel(output_filename, index=False)

        with open(output_filename, "rb") as f:
            st.download_button("Download Differences Excel", f, file_name=output_filename)

