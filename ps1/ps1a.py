#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:09:24 2022

@author: YsGBt
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

monthly_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0
r = 0.04

count = 0
while current_savings < total_cost * portion_down_payment:
    current_savings = current_savings + current_savings * r / 12 + monthly_salary * portion_saved
    count += 1

print("\nNumber of months:", count)
