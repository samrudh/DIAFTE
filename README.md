
# DIAFTE
This repository contains winning solution for DBS codeshield hackathon for machine learning track for reducing false positive rate for SWIFT transaction.

Hackerearth Link: https://www.hackerearth.com/challenges/hackathon/fraudathon/

### Problem Statement Overview
Every day there are lot of transactions happening in bank generally using swift message format, already there are systems which scan these transactions and then declare those as suspicious. After that team sitting in bank needs to verify manually these transactions wheather it is valid or not. If not then those transactions will be blocked.
Due to digitilization, every day amount of transactions are increasing so is the suspicious/fradulent transactions. Now your job is to device a system that can act in real time to detect fradulent transactions, at the same time keeping false positive rate very low.

### Solution Approach
Our hack tells a real life solution for real life data given by business! We emphasized on running a model in real-time than exploring offline time-consuming models.

Key things we prototyped and envisioned: 
1. Kafka based streaming to simulate Swift Msg scenario in real time 
2. Feature engineering with minimum complexity to generate key features 
3. Models with EDA derived features ensuring real-time constraints 
4. Visualization of swift messages by geo tags.

Contributers:
1. Aditya Kumar
2. Samrudha Kelkar
3. Sridhar
4. Venkat Sai kiran
5. Yasar Arafat
