#   1. we don't need to "declare" spam_amount before assigning to it
#   2. we don't need to tell Python what type of value
#      spam_amount is going to refer to. In fact,
#      we can even go on to reassign spam_amount to refer to a different
#      sort of thing like a string or a boolean.
spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4
# The colon (:) at the end of the if line indicates that
# a new code block is starting. 
# Subsequent lines which are indented are part of that code block.
if spam_amount > 0:
    print("But I don't want ANY spam!")
# (The technical term for this is operator overloading.) 
# you can 
viking_song = "Spam " * spam_amount
print(viking_song)
#type: function tell us 
print(type(spam_amount))