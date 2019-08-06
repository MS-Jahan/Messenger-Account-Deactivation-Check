# Messenger Account Deactivation Check
Real-time monitor when an Facebook Messenger account is deactivated or activated.

# Usage
* Make sure you have installed Python 3 in your machine. 
* Install <b>fbchat</b> module via pip3.
* Edit the <b>run.py</b> file with your email, password and the *user_id* of the person's facebook account you want to monitor. To check if the *user_id* is correct or usable, go to https://messenger.com/t/<user_id> and check if your desired conversation is shown.
* Now run the <b>run.py</b> script and it'll check if account is available (not deactivated) or not available (deactivated) on Facebook Messenger. To avoid account blocking or bot behaviour, this script will check for account existance in every 5 minutes which can be changed. Logs can be found in the reports.txt file.
