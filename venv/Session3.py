# Textual Data
# Create Operation
# gender = 'M'
gender = 'Male'

print("Gender is:",gender)

# businessName = 'Johns Coffee Shop'
# businessName = 'John\'s Coffee Shop'
businessName = r'John\'s Coffee Shop' # Raw String
print("Business Name:",businessName)
print(type(businessName))

businessName = "John's Coffee Shop"
print("Business Name:",businessName)

# Multi Line Textual Data
message = "Hello," \
          "How are You?" \
          "Regards," \
          "John"

message = """
Hello,
How are You?
Regards,
John
"""

print("Message is: ",message)

