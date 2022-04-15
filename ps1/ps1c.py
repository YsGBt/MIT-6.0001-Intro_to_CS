#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 23:03:06 2022

@author: qishenpang
"""

annual_salary = int(input("Enter your annual salary: "))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04

possible = True
step = 0
left = 0
right = 10000
guess = 0
current_savings = 0

while current_savings > total_cost * portion_down_payment + 100 or current_savings < total_cost * portion_down_payment - 100:
    if guess == 10000:
        possible = False
        break
    step += 1
    if current_savings > total_cost * portion_down_payment + 100:
        right = guess
    else:
        left = guess
    guess = (left + right) / 2
    portion_saved = guess / 10000

    local_annual_salary = annual_salary
    local_monthly_salary = local_annual_salary / 12
    current_savings = 0
    for count in range(1, 37):
        current_savings = current_savings + current_savings * \
            r / 12 + local_monthly_salary * portion_saved
        if count % 6 == 0:
            local_annual_salary *= 1 + semi_annual_raise
            local_monthly_salary = local_annual_salary / 12

if possible:
    print("\nBest savings rate:", round(portion_saved, 4))
    print("\nStemps in bisection search:", step)
else:
    print("\nIt is not possible to pay the dwon payment in three years.")
