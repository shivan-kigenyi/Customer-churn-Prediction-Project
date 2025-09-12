# THE CUSTOMER CHURN PREDICTION PROJECT 
The Goal of this project is to build a classification model that predicts whether a customer will churn ('Yes' or 'no') based on their demographic and service usage information.

### Insights.
A new customer has 40% probability of churning

Interpretation.
- Its not a guarentee, but a risk Score: The model isn't saying this customer will definately leave, rather it's saying that based on the patterns it learned from the thousands of past customers who did churn, this customer shares many of those same characteristics and thats why they are at high-risk

- This is above average risk. Most telecome companies see 15-25% annual churn rates. While there is no need for urgent panic, this definately warrents intervention. 

### Why might this customer be at higher risk

![Feature Importance](images/Feature_importance.png)

1. Total Charges(with 0.20 importance). 
This is our most predictive factor. It is noticibly visible that customers with certain patterns are much more likely to churn
This could indicate price sensitivity or billing issues

2. Tenure(with 0.19 importance). 
Customer relationship length is critical- Likely newer customers churn more this implys that early churn risk is highest.

3. MonthlyCharges(0.17 importance)
Monthly spend level strongly predicts churn. This suggests the need for price point optimization opportunities.

4. ContractType-Two year(0.07 importance)
Contract length matters. Two-year contracts likely reduce churn compared to the month-to-month. The Actionable wayforward here is to push longer contracts for at-risk customers.


### Model's prediction for a single new customer
- InternetService_Fibre Optic = 0.1: Our model learns that Customers with Fibre Optic internet have a much higher churn rate. 
This could be due to higher prices, competition from other fibre providers or higher expectations that are not met.

- Tenure = 5.0: Newer customers are most likely to leave.

- MonthlyCharges = 70: A monthly charges of $70 is likely above average and is contributing to churn risk.

### Retension strategies
1. Address the main risk, which is Fibre internet.
Address the Main Risk: They are on Fiber. "Hi [Customer], we see you're on our premium Fiber plan. We want to ensure you're getting the best value..."

Lock Them In: The biggest lever is the contract. "We'd like to offer you a 10% discount locked in for 12 months if you switch to a one-year contract today. This would reduce your monthly bill from $70 to $63 and guarantee your rate."

Increase Engagement: They don't have add-ons. "As a thank you, we can also give you free access to our Streaming TV service for 3 months so you can experience the full value of your package."