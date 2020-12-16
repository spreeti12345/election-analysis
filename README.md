# election-analysis
python

## Project Overview

A Colorado employee gave me the following tasks to complete an election audit of the recent local congression election 

1.Calculate total number of votes cast  
2.Breakdown of number of votes and percentage by County
3.Determine largest turnout votes by county  
4.Get a complete list of candidate votes   
5.Calculate the total votes each candidate received    
6.Calculate the percentage of votes each candidate won  
7.Determine the winner based on popular vote  

## Resources
-Data source= election_results.csv
-Python 3.7.6  Visual Code Studio version 1.52.0 (user setup)

## Summary

Total Votes: 369,711 were cast

County Votes:  
Jefferson: 10.5% (38,855)  
Denver: 82.8% (306,055)  
Arapahoe: 6.7% (24,801)  
 
Largest county Turnout : Denver   

The Candidates were  
Charles Casper Stockham  
Diana Degette  
Raymon Anthony Doane  

Charles Casper Stockham got 23.0% or 85,213 votes  
Diana DeGette got 73.8% or 272,892 votes  
Raymon Anthony Doane got only 3.1% or 11,606  

Clearly the Winner is Diana DeGette leading with 272,892 votes and a percentage of 73.8% of popular votes  

## Challenge Overview
https://github.com/spreeti12345/election-analysis 

## Election-Audit Summary
Using python the code can be modified and used to find wining voter turn out only instead of county name
If you modify line 116 to largest voter turnout and change " winning_county" to voter turnout

It can also be used for cleaning out the data and have information about 1 county or 1 candidate.
after .get(county_name) another code can be added to state.remove(candidate_name)  










