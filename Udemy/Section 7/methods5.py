"""
Section 7: Practice Exercise with Solution ***Homework***

Tax in US based on states:
Create a method, which takes the state and gross income as the arguments and returns the net income
after deducting tax based on state.

Assume Fed Tax: 10%

State Tax values from
https://en.wikipedia.org/wiki/State_income_tax
Retrieved 2/28/19
"""


def state_tax(state, gross):
    """
    Calculate the net income after federal and state tax
    :param state:
    :param gross:
    :return:
    """

    states = {'AL': 0.05, 'AK': 0, 'AZ': 0.0454, 'AR': 0.069, 'CA': 0.15, 'CO': 0.0463,
              'CT': 0.0699, 'DE': 0.056, 'FL': 0, 'GA': 0, 'HI': 0, 'ID': 0, 'IL': 0,
              'IN': 0, 'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0,
              'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0, 'NH': 0,
              'NJ': 0, 'NM': 0, 'NY': .09, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0, 'OR': 0,
              'PA': 0, 'RI': 0, 'SC': 0, 'SD': 0, 'TN': 0, 'TX': 0, 'UT': 0, 'VT': 0,
              'VA': 0, 'WA': 0, 'WV': 0, 'WI': 0, 'WY': 0}

    # Fed Tax
    net = gross - (gross * .10)

    # State Tax
    if state in states:
        tax = states[state]
        net = net - (gross * tax)
        print("Your net income after Federal and State Tax deductions is: " + str(net))
    elif state not in states:
        print("State not found. Please contact your administrator. ")
    else:
        print("Your net income after Federal Tax deduction is: " + str(net))


# Test Code
# in_state = 'AL'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'AZ'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'AR'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'CA'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'CO'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'CT'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'DE'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'TX'
# income = 5000
# state_tax(in_state, income)
#
# in_state = 'ZZ'
# income = 5000
# state_tax(in_state, income)

print("California")
in_state = 'CA'
income = 100000
state_tax(in_state, income)

print("\nNew York")
in_state = 'NY'
income = 100000
state_tax(in_state, income)

print("\nNew Jersey")
in_state = 'NJ'
income = 100000
state_tax(in_state, income)

print("\nTexas")
in_state = 'TX'
income = 100000
state_tax(in_state, income)

