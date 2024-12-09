# FlyPrice: Analyzing and Forecasting Flight Fares

## 1. Title and Author
- **Project Title:** FlyPrice: Analyzing and Forecasting Flight Fares
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Sai Rahul Maddula
- **GitHub Repository:** [https://github.com/rahulmaddula3/UMBC-DATA606-Capstone]
- **LinkedIn Profile:** [https://www.linkedin.com/in/rahul-maddula-b6008117a/]
- **PowerPoint Presentation:** [https://github.com/rahulmaddula3/UMBC-DATA606-Capstone/blob/main/docs/Capstone_Presentation.pptx] 
- **YouTube Video:** [https://youtu.be/KeqXY0pg1Ho]

---

## 2. Background
- **What is FlyPrice?**  
  FlyPrice leverages machine learning to predict flight ticket prices, helping travelers book cost-effective flights and assisting businesses in understanding pricing trends. Using over 300,000 flight booking records, FlyPrice analyzes factors like airline, departure time, number of stops, and days left to forecast fares in USD. The goal is to make air travel more accessible and economical for users.

- **Why is it Important?**  
  Flight prices often fluctuate due to demand, seasonality, and timing, creating uncertainty for travelers. Predictive modeling enables:
  - **Travelers:** Helps users save money by optimizing booking decisions.
  - **Airlines and Businesses:** Offers insights into customer behavior and allows strategic adjustments to maximize revenue.

- **Research Questions:**
  1. How can historical flight booking data be used to predict ticket prices?  
  2. What are the most important factors influencing flight fares?  
  3. How does the combination of airline, departure time, and stops impact price variation?

---

## 3. Data
- **Data Sources:** EaseMyTrip dataset.
- **Data Size:** ~300,261 rows.
- **Data Shape:** Rows: 300,261 | Columns: [Number of Columns].
- **Time Period:** [Add Time Period].
- **What does each row represent?** Each row represents one flight booking option.

- **Data Dictionary:**

| Column Name       | Data Type | Definition                           | Potential Values                                |
|--------------------|-----------|---------------------------------------|------------------------------------------------|
| Airline           | Object    | Name of the airline                  | 'SpiceJet', 'AirAsia', 'Vistara', etc.         |
| Flight            | Object    | Unique flight number                 | Unique alphanumeric values                     |
| Source City       | Object    | Origin city of the flight            | 'Delhi', 'Mumbai', 'Bangalore', etc.           |
| Departure Time    | Object    | Time category for departure          | 'Morning', 'Evening', 'Night', etc.            |
| Stops             | Object    | Number of stops on the flight        | 'Zero', 'One', 'Two'                           |
| Arrival Time      | Object    | Time category for arrival            | 'Afternoon', 'Night', etc.                     |
| Destination City  | Object    | Destination city of the flight       | 'Delhi', 'Mumbai', 'Bangalore', etc.           |
| Class             | Object    | Ticket class                         | 'Economy', 'Business'                          |
| Duration          | Float     | Duration of the flight in hours      | Numeric values (e.g., 2.17, 49.83)             |
| Days Left         | Integer   | Days remaining until the flight      | Integer values (e.g., 1, 49)                   |
| Price             | Float     | Ticket price in USD                  | Numeric values (e.g., 13.1, 1458)              |

- **Features/Target:**
  - **Target:** `price`
  - **Features:** `airline`, `departure_time`, `stops`, `days_left`

---

## 4. Exploratory Data Analysis (EDA)

### 1. Distribution of Ticket Prices
The distribution of flight prices is heavily skewed to the right, with most ticket prices concentrated in lower ranges. This skewness indicates that the dataset primarily includes affordable flight fares, but there are also premium-priced tickets.

![/Users/rahulmaddula/Desktop/capstone docs/1](1.png)

---

### 2. Airline Distribution
The dataset contains flights operated by six airlines. Vistara dominates the market with 42.6% of the share, followed by Air India (27%) and Indigo (14.4%). Airlines like SpiceJet, AirAsia, and GO_FIRST have smaller market shares.

![Airline Distribution](2.png)

---

### 3. Class Distribution
The majority of the flights in the dataset are in the Economy class (68.85%), while Business class flights account for 31.15%.

![Class Distribution](3.png)

---

### 4. Stop Analysis
The average ticket price varies with the number of stops. Flights with one stop tend to be more expensive than direct flights or flights with two or more stops.

![Stop Analysis](4.png)

---

### 5. Airline Prices Based on Class
A comparison of ticket prices by airline and ticket class shows that Business class fares are significantly higher than Economy class fares, particularly for airlines like Air India and Vistara.

![Airline Prices Based on Class](5.png)

---

### 6. Economy Class Ticket Prices by Airline
The boxplot shows the distribution of Economy class ticket prices for each airline. Air India and Vistara offer higher-priced Economy tickets compared to budget carriers like AirAsia and SpiceJet.

![Economy Class Ticket Prices by Airline](6.png)

---

### 7. Business Class Ticket Prices by Airline
The boxplot shows the distribution of Business class ticket prices for Air India and Vistara. Business fares are substantially higher, reflecting the premium service provided.

![Business Class Ticket Prices by Airline](7.png)

---

### 8. Most Popular Airlines
This bar chart displays the number of flights per airline in the dataset. Vistara and Air India operate the highest number of flights.

![Most Popular Airlines](8.png)

---

### 9. Average Price by Days Left
As the number of days left until departure decreases, the average ticket price increases sharply, emphasizing the importance of early bookings for cost savings.

![Average Prices Depending on the Days Left](9.png)

---

### 10. Top 10 Most Expensive Flights Between Cities
This chart highlights the most expensive flight routes in the dataset. The routes between certain cities, such as Chennai and Mumbai, are among the costliest.

![Top 10 Most Expensive Flights Between Cities](10.png)

---

## 5. Model Training
- **Models Used:**
  - Random Forest Regressor
  - XGBoost
  - Linear Regression
- **Training Setup:**
  - Train/Test Split: 80/20
  - Libraries: scikit-learn, pandas, numpy
  - Environment: Jupyter Notebook and Streamlit
- **Performance Metrics:**
  - Mean Absolute Error (MAE)
  - Root Mean Square Error (RMSE)
  - R² Score

---

## 6. Application of the Trained Models
- **Web App Development:**
  - Tool: Streamlit
  - Features:
    - Input parameters (airline, departure time, stops, days left).
    - Display predicted price.
    - Show feature importance visualization.

---

## 7. Conclusion

- **Summary:**
  - The FlyPrice project successfully developed a machine learning-based predictive model to forecast flight fares with high accuracy.
  - The Gradient Boosting Regressor emerged as the best-performing model, achieving the highest R² score and lowest Mean Squared Error (MSE) among the tested models.
  - Key features like `airline`, `days_left`, and `number of stops` were identified as the most significant predictors of ticket prices.
  - The predictive model effectively captured complex relationships in the data, providing reliable fare estimates.

- **Real-World Application:**
  - A Streamlit web application was created to demonstrate the practical use of the model. The user-friendly interface allows travelers to input flight-related parameters (e.g., source, destination, class, days left) and receive predicted fares instantly.
  - This application makes fare predictions accessible to users, enabling cost-effective booking decisions and empowering businesses with actionable insights.

- **Limitations:**
  - **Data Coverage:** The dataset used in this study is limited to a specific region and may not capture global pricing trends or all possible flight routes.
  - **Real-Time Changes:** The model does not account for real-time fare fluctuations influenced by last-minute demand surges or promotional discounts.
  - **Feature Constraints:** Factors like weather, holiday seasons, and passenger demand—key contributors to airfare variations—were not included in the analysis.

- **Future Research and Improvements:**
  - **Incorporating External Data:** Adding real-time information on holidays, weather, and passenger demand can improve prediction accuracy by capturing seasonal and situational trends.
  - **Model Deployment:** Develop a fully integrated real-time fare prediction tool accessible via web and mobile platforms to provide dynamic pricing information to users.
  - **Broader Dataset:** Expanding the dataset to include flights from different regions, additional airlines, and longer time periods will make the model more robust and applicable on a global scale.
  - **Advanced Algorithms:** Exploring advanced algorithms such as neural networks or hybrid models could further enhance the predictive power and adaptability of the system.

- **Conclusion:**
  - FlyPrice has laid the groundwork for building an effective and scalable flight fare prediction system. By leveraging historical data and machine learning, the project not only provides travelers with valuable pricing insights but also opens avenues for further research and innovation in the travel and airline industries.
  - With future improvements, FlyPrice has the potential to become a powerful tool for real-time fare prediction, catering to a global audience and contributing to smarter decision-making in air travel.


---

## 8. References
- Dataset: [EaseMyTrip](#)
- Libraries: scikit-learn, Streamlit
- Visualization Tools: Plotly

