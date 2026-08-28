rice = 10
milk = 5
fruit = 20
num_of_baskets = 5
family_members = 4

basket_cost_per_person = (10+5+20)*num_of_baskets/family_members

grocery_items = int(input("Total num. of grocery items."))
people = int(input("Enter the number of family members."))
if grocery_items % people == 0:
    print()

recorded_avg = 65
inc_weekly_cost = 50
cor_weekly_cost = 80
num_of_weeks = 4

recorded_total = recorded_avg*num_of_weeks
corrected_total = (recorded_total - inc_weekly_cost + cor_weekly_cost)
corrected_avg = corrected_total/num_of_weeks

grocery_costs_avgA = 70
grocery_costs_avgB = 75
grocery_costs_avgC = 80

if corrected_avg < grocery_costs_avgA and corrected_avg<grocery_costs_avgB and corrected_avg<grocery_costs_avgC:
    print("Your corrected grocery average is lower than all three store averages.")
 
elif (
    corrected_avg > grocery_costs_avgA
    and corrected_avg > grocery_costs_avgB
    and corrected_avg > grocery_costs_avgC
):
    print(
        "Your corrected grocery average is higher "
        "than all three store averages."
    )
 
else:
    print(
        "Your corrected grocery average is between "
        "the three store averages."
    )




