#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:52:27 2022

@author: qishenpang
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

monthly_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0
r = 0.04

count = 0
while current_savings < total_cost * portion_down_payment:
    current_savings = current_savings + current_savings * r / 12 + monthly_salary * portion_saved
    count += 1
    if count % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12

print("\nNumber of months:", count)