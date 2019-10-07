# mars_sos
Problem from HackerRank https://www.hackerrank.com/challenges/mars-exploration/problem

Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.
Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, _*s*_, determine how many letters of Sami's SOS have been changed by radiation.
For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message characters were changed in transit.

## Function Description
Complete the marsExploration function in the editor below. It should return an integer representing the number of letters changed during transmission.
marsExploration has the following parameter(s):<br>
s: the string as received on Earth

## Input Format
There is one line of input: a single string, *_s_*.
Note: As the original message is just SOS repeated *_n_* times, *_s_*'s length will be a multiple of *_3_*.

## Constraints
1 <= len(*_s_*) <= 99<br>
len(*_s_*) % 3 = 0<br>
*_s_* will contain only uppercase English letters, ascii[A-Z]

## Output Format
Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input: SOSSPSSQSSOR <br>
Sample Output: 3 SOSS _P_ SS _Q_ SSO _R_ 
