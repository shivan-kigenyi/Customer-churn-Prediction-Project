# SIMPLIFIED STARTING POINT
import streamlit as st
import pandas as pd
import joblib
import os

# Page config
st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊")

# Load model
@st.cache_resource
def load_model():
    try:
        # Try to load from parent directory first
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pkl_files = [f for f in os.listdir(parent_dir) if f.endswith('.pkl')]
        if pkl_files:
            model_path = os.path.join(parent_dir, pkl_files[0])
            model = joblib.load(model_path)
            st.success(f"✅ Model loaded: {pkl_files[0]}")
            return model
        else:
            # Try current directory
            model = joblib.load('customer_churn_pipeline_v1.pkl')
            st.success("✅ Model loaded successfully!")
            return model
    except Exception as e:
        st.error(f"❌ Model not found: {e}")
        st.error("Please make sure the .pkl file is in the correct folder.")
        return None

# Simple input form
st.title("🔮 Customer Churn Predictor")
st.markdown("Enter customer information to predict churn risk")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Info")
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.checkbox("Senior Citizen (65+)")
    partner = st.checkbox("Has Partner")
    dependents = st.checkbox("Has Dependents")
    tenure = st.slider("Tenure (months)", 0, 72, 24)

with col2:
    st.subheader("Services & Billing")
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    paperless_billing = st.checkbox("Paperless Billing")
    monthly_charges = st.slider("Monthly Charges ($)", 18.0, 120.0, 65.0)
    total_charges = st.number_input("Total Charges ($)", 18.0, 8500.0, float(tenure * monthly_charges))

# Additional services
st.subheader("Additional Services")
col3, col4 = st.columns(2)

with col3:
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with col4:
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])

col5, col6 = st.columns(2)
with col5:
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])

with col6:
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

# Prediction button
if st.button("🔮 Predict Churn Risk", type="primary"):
    model = load_model()
    if model:
        try:
            # Create input data matching your model's exact features
            # Based on the feature list you provided earlier
            input_data = pd.DataFrame({
                'gender': [1 if gender == 'Female' else 0],  # 0=Male, 1=Female
                'SeniorCitizen': [1 if senior_citizen else 0],
                'Partner': [1 if partner else 0],
                'Dependents': [1 if dependents else 0],
                'tenure': [tenure],
                'PhoneService': [1 if phone_service == 'Yes' else 0],
                'PaperlessBilling': [1 if paperless_billing else 0],
                'MonthlyCharges': [monthly_charges],
                'TotalCharges': [total_charges],
                'MultipleLines_No phone service': [1 if multiple_lines == 'No phone service' else 0],
                'MultipleLines_Yes': [1 if multiple_lines == 'Yes' else 0],
                'OnlineSecurity_No internet service': [1 if online_security == 'No internet service' else 0],
                'OnlineSecurity_Yes': [1 if online_security == 'Yes' else 0],
                'InternetService_Fiber optic': [1 if internet_service == 'Fiber optic' else 0],
                'InternetService_No': [1 if internet_service == 'No' else 0],
                'OnlineBackup_No internet service': [1 if online_backup == 'No internet service' else 0],
                'OnlineBackup_Yes': [1 if online_backup == 'Yes' else 0],
                'TechSupport_No internet service': [1 if tech_support == 'No internet service' else 0],
                'TechSupport_Yes': [1 if tech_support == 'Yes' else 0],
                'StreamingTV_No internet service': [1 if streaming_tv == 'No internet service' else 0],
                'StreamingTV_Yes': [1 if streaming_tv == 'Yes' else 0],
                'StreamingMovies_No internet service': [1 if streaming_movies == 'No internet service' else 0],
                'StreamingMovies_Yes': [1 if streaming_movies == 'Yes' else 0],
                'Contract_One year': [1 if contract == 'One year' else 0],
                'Contract_Two year': [1 if contract == 'Two year' else 0]
            })
            
            # Debug: Show the input data shape and columns
            st.write(f"Input data shape: {input_data.shape}")
            with st.expander("Debug: Input Data"):
                st.write(input_data)
            
            # Make prediction
            prediction_proba = model.predict_proba(input_data)[0][1]
            churn_percent = prediction_proba * 100
            
            # Display results
            st.subheader(f"📊 Churn Risk: {churn_percent:.1f}%")
            
            # Risk level indicator
            if churn_percent > 70:
                st.error('🚨 HIGH RISK - Immediate action required!')
                risk_level = "HIGH"
            elif churn_percent > 40:
                st.warning('⚠️ MEDIUM RISK - Monitor closely')
                risk_level = "MEDIUM"
            else:
                st.success('✅ LOW RISK - Routine follow-up')
                risk_level = "LOW"
            
            # Simple recommendations
            st.subheader("💡 Recommendations")
            
            if risk_level == "HIGH":
                st.write("🎯 **Immediate Actions:**")
                st.write("• Contact customer within 24 hours")
                st.write("• Offer retention discount or upgrade")
                st.write("• Schedule personal consultation")
                
            elif risk_level == "MEDIUM":
                st.write("🎯 **Proactive Measures:**")
                st.write("• Send personalized retention offer")
                st.write("• Monitor usage patterns closely")
                st.write("• Follow up in 2 weeks")
                
            else:
                st.write("🎯 **Standard Care:**")
                st.write("• Include in loyalty program")
                st.write("• Continue regular engagement")
                st.write("• Re-evaluate in 3 months")
            
            # Show key factors
            st.subheader("🔍 Key Risk Factors")
            risk_factors = []
            
            if contract == "Month-to-month":
                risk_factors.append("Month-to-month contract (higher risk)")
            if tenure < 12:
                risk_factors.append("New customer (< 12 months)")
            if monthly_charges > 80:
                risk_factors.append("High monthly charges")
            if internet_service == "Fiber optic" and tech_support == "No":
                risk_factors.append("Fiber optic without tech support")
            
            if risk_factors:
                for factor in risk_factors:
                    st.write(f"• {factor}")
            else:
                st.write("• No major risk factors identified")
                
        except Exception as e:
            st.error(f"❌ Prediction error: {e}")
            st.write("This might be due to a feature mismatch. Let's debug:")
            
            # Show model info for debugging
            if hasattr(model, 'feature_names_in_'):
                st.write("Model expects these features:")
                st.write(list(model.feature_names_in_))
            
            st.write("We provided these features:")
            st.write(list(input_data.columns))