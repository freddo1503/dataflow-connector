# Dataflow Connector

This project demonstrates how to build a data integration solution that writes
data from Kafka topics into Postgres
tables. It covers real-time data processing concepts, including configurable
mappings and basic data transformations.

## Learning Objectives

* Understand how to map Kafka topics to relational database tables.
* Gain hands-on experience in handling real-time data workflows.
* Learn to apply basic data transformations during data integration.

## Key Concepts

* **Configurable Mappings**:  
Define flexible relationships between Kafka topics and Postgres tables.

* **Data Transformations**:
Modify data on-the-fly, such as converting types or adding static fields.

* **Real-Time Data Integration**:  
Explore the challenges of integrating streaming data into databases.

## Getting Started

1. Clone the repository

```bash
git clone <repository-url>  
cd dataflow-connector 
```

2. Install dependencies

```bash
just install
```

3. Run the application

```bash
just start
```
