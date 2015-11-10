#def calculate_tip(total_bill):
 #   return total_bill*0.15

#print "%.0f" % calculate_tip(42.50)


#def calculate_tip2(total_bill, tip_percent):
 #   return total_bill*tip_percent

#print "%.7f" % calculate_tip2(42.50, 0.5)

def tips_with_friends(total_bill, tip_percent, num_friends):
    tip = (total_bill*tip_percent)/num_friends
    total = total_bill/num_friends
    amount = tip + total
    return amount

print "Each person should pay $" "%.2f" % tips_with_friends(42.50, 0.2, 2)
