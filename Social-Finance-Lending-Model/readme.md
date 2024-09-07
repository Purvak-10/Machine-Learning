# Social Finance Lending

This project is designed to help the bank decide which customers are mostly to accept a personal loan, taking into account different attributes like age, income, experience, family size, mortgage, education, securities account, credit card usage patterns, and online banking.

## Insights with the help of different Plotting
### HeatMap
![image](https://github.com/user-attachments/assets/86381afe-78bc-4813-9ab3-11ed477f3ebd)

Observation from heatmap:
- Income and experience are correlated with each other
- Income and ann_cv are correlated with each other
- Personal loan has correlation with income, ann_cv, mortgage, and education
- Mortgage has moderate correlation with income
- Income influences ann_cv, personal loan, cd account, and Mortgage

### Graphs
![image](https://github.com/user-attachments/assets/d989d090-8a69-430e-8cc5-58fa7abb0e4f)

![image](https://github.com/user-attachments/assets/bfc70e64-4e2b-42fc-a127-8863bec354cb)

From above last two plots, we observed that:
- Income more than 100K are more likely to get loan
- If ann_cv more than 30 are more likely to get loan

![image](https://github.com/user-attachments/assets/fbd709ec-4198-49d9-ae5c-154b36fca28b)

![image](https://github.com/user-attachments/assets/c26d8ab3-993b-4190-91e4-ce3d4f176440)

![image](https://github.com/user-attachments/assets/a9383a9d-1ce1-4a23-91fd-2b57039c6002)

![image](https://github.com/user-attachments/assets/0f9c0ac2-9f80-4cae-be76-6411df7ef801)

## Algorithms Used
- Logistic Regression
- K Neighbors Classifier
- Decision Tree
- Random Forest
- Voting Classifier
  
## Finally
In the end, we found Voting Classifier is the best algorithm with accurecy score = 97.97 and with f1_score = 98 %
