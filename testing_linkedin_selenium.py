import selenium_linked_in
import text_information

session = int(input('enter the session : '))
values_for_tracking = int(input("enter 0 for start, 1 for end, 2 for daily : "))
start_end = ['start','end','daily']

text = text_information.text()
text.call_methods(start_end[values_for_tracking],session)



linkedin = selenium_linked_in.linked_in()
if values_for_tracking == 0 :
    start_text = text.start_post_message
    start = linkedin.call_allvariables(start_text,'start.png')
elif values_for_tracking == 1 :
    end_text = text.end_post_message
    end = linkedin.call_allvariables(end_text,'start.png')
elif values_for_tracking == 2 :
    daily_text = text.daily_post_message
    daily = linkedin.call_allvariables(daily_text,'start.png')
else:
    print('error enter 0 for start, 1 for end, 2 for daily :  ')

