# **FlyPrice: Analyzing and Forecasting Flight Fares**

## **Author**
- **Name**: Rahul Maddula
- **GitHub Repository**: [https://github.com/rahulmaddula3/UMBC-DATA606-Capstone)
- **PowerPoint Presentation**:
- **YouTube Video**:

## Background

### What is it about?
The FlyPrice project aims to predict flight fares based on factors like airline, departure time, stops, and days left until the flight. Using this data, machine learning techniques will be applied to predict future flight prices, allowing users to plan their bookings at the most cost-effective times.

### Why does it matter?
Flight prices fluctuate based on several factors, including demand, time of day, and how far in advance the booking is made. Predicting these prices helps travelers save money by booking at the optimal time. This project is beneficial for travelers and also for stakeholders such as travel agencies and airlines looking to optimize pricing strategies.

### Research Questions
- How can flight fare prediction models improve customer experience in booking flights?
- What features (e.g., airline, stops, days left) are the most influential in determining flight prices?
- Which machine learning algorithms (e.g., Random Forest, Gradient Boosting) can best capture pricing trends in airline fares?

## Data

### Data Sources

1. **Flight Fare Dataset**

   **Description:** A total of 300,261 distinct flight booking options were extracted from the EaseMyTrip website. Data was collected over a span of 50 days. The dataset includes information on flights between India's top six metro cities.
   
   **Data Size:** The cleaned dataset contains 300,261 data points and 11 features.
   
   **Data Source:** The data was collected from a secondary source, specifically the EaseMyTrip website.

## Data Dictionary

### Column Definitions

| Column Name        | Data Type   | Definition                                 |
|--------------------|-------------|--------------------------------------------|
| Airline            | Categorical | Name of the airline operating the flight   |
| Flight             | Categorical | Flight number                              |
| Source City        | Categorical | Departure city                             |
| Destination City   | Categorical | Arrival city                               |
| Departure Time     | Categorical | Time of day the flight departs             |
| Arrival Time       | Categorical | Time of day the flight arrives             |
| Stops              | Categorical | Number of stops during the flight          |
| Class              | Categorical | Class of the flight                        |
| Duration           | Numeric     | Duration of the flight in hours            |
| Days Left          | Numeric     | Days left until the departure              |
| Price              | Numeric     | Flight price in INR                        |

### Detailed Descriptions

#### Categorical Features
- **Airline**  
  The airline company operating the flight. This feature includes six different airlines.

- **Flight**  
  The flight code, which uniquely identifies the flight.

- **Source City**  
  The city where the flight originates. There are six unique cities.

- **Departure Time**  
  A derived feature representing the departure time, grouped into six unique time bins.

- **Stops**  
  Represents the number of stops between the source and destination cities. This feature has three distinct values.

- **Arrival Time**  
  A derived feature for arrival time, grouped into six time bins.

- **Destination City**  
  The city where the flight will land. There are six unique cities.

- **Class**  
  Information about the seat class on the flight. This feature has two distinct values: Business and Economy.

#### Numeric Features
- **Duration**  
  The total duration of the flight journey in hours.

- **Days Left**  
  Number of days left until departure, calculated by subtracting the booking date from the travel date.

- **Price**  
  The ticket price for each flight. This is the target variable.
