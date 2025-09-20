# Customer Churn Prediction Dashboard

A machine learning web application that predicts customer churn risk and provides actionable retention strategies for telecom businesses.

## Business Problem

Customer acquisition costs 5-25 times more than retention. This project addresses the critical business challenge of identifying customers likely to leave before they actually churn, enabling proactive retention efforts that directly impact revenue.

## Key Business Insights

**High-Risk Customer Profile Analysis:**
- New customers (tenure < 12 months) show 40% churn probability vs. industry average of 15-25%
- Fiber optic customers churn at significantly higher rates despite premium pricing
- Month-to-month contracts correlate with 3x higher churn than two-year agreements
- Customers with monthly charges above $70 represent the highest risk segment

**Feature Importance Findings:**
1. **Total Charges (20% importance)** - Primary predictor indicating price sensitivity patterns
2. **Tenure (19% importance)** - Customer relationship length directly correlates with loyalty
3. **Monthly Charges (17% importance)** - Price point optimization opportunity identified
4. **Contract Type (7% importance)** - Two-year contracts reduce churn by 60%

**Actionable Retention Strategies:**
- Target fiber customers with value-demonstration campaigns
- Implement early engagement programs for customers under 6 months tenure
- Offer contract upgrade incentives with locked-in pricing
- Deploy price optimization for customers in the $60-80 monthly charge range

## Technical Implementation

**Model Performance:**
- Classification algorithm trained on comprehensive customer dataset
- 25 engineered features covering demographics, services, and billing patterns
- Real-time prediction capability through Streamlit interface

**Technology Stack:**
- Python 3.x with scikit-learn for model development
- Streamlit for production-ready web interface
- Pandas for data processing and feature engineering
- Joblib for model serialization and deployment

## Getting Started

### Installation
```bash
git clone https://github.com/shivan-kigenyi/Customer-churn-Prediction-Project.git
cd customer-churn-prediction
pip install -r requirements.txt
streamlit run churn_app.py
```

### Usage
1. Input customer data through the web interface
2. Receive instant churn probability and risk classification
3. Access personalized retention recommendations
4. Export results for customer success team follow-up

## Project Structure
```
├── churn_app.py                    # Main application
├── customer_churn_pipeline_v1.pkl  # Trained model
├── requirements.txt                # Dependencies
├── data/                          # Training dataset
├── notebooks/                     # Model development
└── images/                        # Documentation assets
```

## Business Impact Metrics

This solution enables businesses to:
- Reduce customer churn by identifying at-risk segments before they leave
- Increase customer lifetime value through targeted retention campaigns  
- Optimize pricing strategies based on churn probability patterns
- Implement data-driven customer success workflows

## Model Features

**Customer Demographics:** Gender, age group, family status, geographic factors
**Service Portfolio:** Phone services, internet type, streaming subscriptions, security features
**Financial Indicators:** Monthly charges, total charges, payment patterns, billing preferences
**Relationship Metrics:** Tenure, contract terms, service usage history

## Deployment Options

The application supports multiple deployment strategies:
- **Streamlit Cloud** for rapid prototyping and demonstration
- **Heroku** for scalable production deployment
- **AWS/GCP** for enterprise-grade implementations

## Future Development

Planned enhancements include batch processing capabilities, integration with CRM systems, automated A/B testing for retention strategies, and real-time model retraining pipelines.

## Key Takeaways for Business Stakeholders

This project demonstrates proficiency in end-to-end machine learning solution development, from business problem identification through model deployment. The focus on actionable insights and real-world application showcases ability to bridge technical capabilities with business value creation.

The retention strategies derived from model insights provide immediate implementation opportunities, while the scalable technical architecture supports enterprise deployment requirements.