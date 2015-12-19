# slack-cat
Cat slack bot that lights up my Philips Hue LED when a cat pic is posted to #cats.

SlackCat has a very specific raison d'etre so she never feels like her days are futile or meaningless, even though all days are futile and meaningless.

             .__....._             _.....__,
                 .": o :':         ;': o :".
                 `. `-' .'.       .'. `-' .'   
                   `---'             `---'  

         _...----...      ...   ...      ...----..._
      .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
     '.-'   _.--"""'       `-._.-'       '"""--._   `-.`
     '  .-"'                  :                  `"-.  `
       '   `.              _.'"'._              .'   `
             `.       ,.-'"       "'-.,       .'
               `.                           .'
                 `-._                   _.-'
                     `"'--...___...--'"`


sudo pip install -r requirements.txt

### Slack integration
In slack: <your team>.slack.com/apps/manage > custom integrations > bots > add configuration. 
Add bot to your channel of choice. 

### Hue integration
Make sure Hue lights are connected and go to www.meethue.com/api/nupnp to find IP address of bridge on your network.

### Run app
Add IP and bot's slack token to rtmbot.conf.
Add list of lights you wish to alert.
Run python rtmbot.py
