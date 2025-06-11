import streamlit as st

st.title(" 💪 BMI Calculator")

weight = st.number_input("Enter your weight in kg.")
height_inch = st.number_input("Enter your height in inches.")

# Convert height from inches to meters
height_m = height_inch * 0.0254           #  1 inch = 0.0254 meters

# Avoid division by zero
if height_m > 0:
    bmi = weight / (height_m ** 2)
else:
    bmi = 0

if st.button("Calculate BMI"):
    st.success(f'Your BMI is: {bmi:.2f}')

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.info("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")