# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 


# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 



def main():
	"""Semi Automated ML App with Streamlit """

	activities = ["EDA","Plots"]	
	st.subheader("Economic Emulator")
	data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
	
	
	st.subheader("Please see the sample data to prepare your data")
	sample = "income_expenses.csv"
	df_sample = pd.read_csv(sample)
	st.dataframe(df_sample.head())

	#sampel_data={'Company':['A','B','C','D','E','F','G','H','I','J'],
    #         'Profit':[3,4.5,2,2.5,1.25,3,3.25,5,6,2.75]}
    #data = "income_expenses.csv"

	if data is not None:
		#df=pd.DataFrame(data=sampel_data)
		df = pd.read_csv(data)
		st.subheader("Actual Data")
		st.dataframe(df.head(12))


		all_columns_names = df.columns.tolist()

		select_month = ""
		select_year = ""

		select_month_year = st.selectbox("Choose Yearly data or monthly Data",["Year"])
		if select_month_year == "Month":
			select_month = st.selectbox("Choose Month",["Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sept","Oct","Nov","Dec"])
			select_year = st.selectbox("Choose Year",["2020","2021","2022"])
			#selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

		elif select_month_year == "Year":
			select_year = st.selectbox("Choose Year",[2020,2021,2022])
			#income = df[df['Income'].dt.year == select_year]
			income = df.loc[df['Year'] == select_year,['Month','Income','Expenses']]
			print("incom", income)
			st.dataframe(income.head(12))
			#selected_columns_names = ['Income','Expenses']
			#expenses = df[df['Expenses'].dt.year == select_year]
			#print("expenses", expenses)
		else:
			select_month = ""
			select_year = ""

		type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line"])
		#selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

		if st.button("Generate Plot"):
			#st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

			# Plot By Streamlit
			if type_of_plot == 'area':
				#cust_data = df[selected_columns_names]
				st.area_chart(income, x = "Month", y = ["Income"])

			elif type_of_plot == 'bar':
				#chart_data = pd.DataFrame(np.random.randn(20, 3),columns=selected_columns_names)
				#cust_data = df[selected_columns_names]
				st.bar_chart(income, x = "Month", y = ["Income"])

			elif type_of_plot == 'line':
				#cust_data = df[selected_columns_names]
				st.line_chart(income, x = "Month", y = ["Income"])

			# Custom Plot 
			#elif type_of_plot:
			#	cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
			#	st.write(cust_plot)
			#	st.pyplot()
    


if __name__ == '__main__':
	main()
