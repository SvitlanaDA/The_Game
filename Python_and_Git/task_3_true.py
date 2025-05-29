is_logged_in = True
has_permission = False
print ("AND  ", (is_logged_in and has_permission))
print ("OR  ", (is_logged_in or has_permission))
print ("NOT  ", (not has_permission))
print ("")
print ("& = AND  ", (is_logged_in & has_permission))
print ("| = OR  ", (is_logged_in | has_permission))
print ("!=  = NOT  ", (is_logged_in != has_permission))