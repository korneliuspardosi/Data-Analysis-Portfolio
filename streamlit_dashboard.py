import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dashboard Title
st.title("E-commerce Analysis Dashboard")

# Load dataset
orders_merge_df = pd.read_csv("orders_merge_data.csv")

# Display the dataset in the app
st.write("Orders Dataset:")
st.dataframe(orders_merge_df)

# Use 'order_purchase_timestamp' for date filtering if available
if 'order_purchase_timestamp' in orders_merge_df.columns:
    orders_merge_df['order_purchase_timestamp'] = pd.to_datetime(orders_merge_df['order_purchase_timestamp'])
    
    # Sidebar date filter
    st.sidebar.header("Filter Options")
    start_date = st.sidebar.date_input("Start Date", orders_merge_df['order_purchase_timestamp'].min())
    end_date = st.sidebar.date_input("End Date", orders_merge_df['order_purchase_timestamp'].max())

    # Filter data
    filtered_df = orders_merge_df[
        (orders_merge_df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
        (orders_merge_df['order_purchase_timestamp'] <= pd.to_datetime(end_date))
    ]
    
    # Display filtered data
    st.write("Filtered Dataset:")
    st.dataframe(filtered_df)
else:
    st.error("No suitable date column found in the dataset.")

# Visualization 1: Total Payment Value by Payment Installments
payment_value_by_installments = filtered_df.groupby('payment_installments').agg(
    total_payment_value=('payment_value', 'sum')
).reset_index()

st.write("Visualization 1: Total Payment Value by Payment Installments")
fig1, ax1 = plt.subplots()
sns.barplot(
    x='payment_installments', 
    y='total_payment_value', 
    data=payment_value_by_installments, 
    color='skyblue', 
    ax=ax1
)
ax1.plot(
    payment_value_by_installments['payment_installments'], 
    payment_value_by_installments['total_payment_value'], 
    color='orange', 
    marker='o'
)
ax1.set_title("Total Payment Value by Payment Installments")
ax1.set_xlabel("Payment Installments")
ax1.set_ylabel("Total Payment Value")
st.pyplot(fig1)

# Visualization 2: Order Count by Payment Installments
order_count_by_installments = filtered_df.groupby('payment_installments').agg(
    order_count=('order_id', 'count')
).reset_index()

st.write("Visualization 2: Order Count by Payment Installments")
fig2, ax2 = plt.subplots()
sns.barplot(
    x='payment_installments', 
    y='order_count', 
    data=order_count_by_installments, 
    color='lightgreen', 
    ax=ax2
)
ax2.plot(
    order_count_by_installments['payment_installments'], 
    order_count_by_installments['order_count'], 
    color='red', 
    marker='o'
)
ax2.set_title("Order Count by Payment Installments")
ax2.set_xlabel("Payment Installments")
ax2.set_ylabel("Order Count")
st.pyplot(fig2)
