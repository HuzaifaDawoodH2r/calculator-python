import streamlit as st # type:ignore #ignore

import streamlit as st  # type: ignore

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation:")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter your first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter your second number", value=0.0)

    operations = st.selectbox('Choose operation', 
                              ['Addition (+)', 'Subtraction (-)', 'Multiplication (*)', 'Division (/)'])

    if st.button('Calculate'):
        try:
            if operations == 'Addition (+)':
                result = num1 + num2
                symbol = '+'
            elif operations == 'Subtraction (-)':
                result = num1 - num2
                symbol = '-'
            elif operations == 'Multiplication (*)':
                result = num1 * num2
                symbol = '*'
            elif operations == 'Division (/)':
                if num2 == 0:
                    st.error("Division by zero is not allowed.")
                    return
                result = num1 / num2
                symbol = '/'
            else:
                st.error("Unknown operation selected.")
                return

            st.success(f"{num1} {symbol} {num2} = {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

