# Election_Analysis

## Overview of Election Audit

The Colorado Board of Elections asked for an election audit of a recent local congressional election.
The tasks given were:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Get a complete list of the counties where the election took place.
7. Calculate the total number of votes cast in each county.
8. Calculate the percentage of votes cast in each county.
9. Determine the county with the largest vote turnout.

### Resources
- Data source: election_results.csv
- Software: Python 3.10, Visual Studio Code 1.72.1

## Election Audit Results

The analysis of the election show that:
- There were 369,711 votes cast in the election.

### County Results
- The counties where the election took place were:
  - Arapahoe
  - Denver
  - Jefferson
- The vote count per county was:
  - 6.7% of the vote and 24,801 number of votes were cast in Arapahoe.
  - 82.8% of the vote and 306,055 number of votes were cast in Denver.
  - 10.5% of the vote and 38,855 number of votes were cast in Jefferson.
- The county with the largest vote turnout was:
  - Denver, where 82.8% of the vote and 306,055 number of votes were cast.

### Candidate Results
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Election Audit Summary

As the Election Audit Results show, the script used for this analysis is efficient.
The principal strength is that this script performs the audit for any number of candidates and/or counties.
Furthermore, this script's scope can be adapted to suit deeper analyses with simple modifications.
Examples of it may be:
- Analysis of vote per candidate and county.
- Analysis of vote by time of cast*.
- Analysis of vote by voters' age*.
*In these cases, input data must contain specific information, in order for these analyses to be feasible.

In conclusion, it's been satisfying performing this audit and we'll be glad to assist on future elections/projects.
