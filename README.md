# N0-L3

Hi, and welcome to N0-L Bot! 

This is a hobby project of mine intended to assist me during my [Twitch.tv streams](https://www.twitch.tv/NoelleDay) and get me back in the habit of coding and using the GitHub workflow.

This is the third (technically fourth, N0L-Bot had a brief stint as a Discord bot once upon a time) iteration of the bot.
We are rebuilding the bot from the ground up in Python 3.11 (from 3.7) using Twitch.IO 2.5.0 (from 1.1.0), so there's probably going to be a few changes.


Current Functionality and Goals
- [X] Responds to basic commands with text response
- [X] Does not infinite loop on herself
- [X] Case insensitive commands (Tentatively checked)
- [X] Bot now checks an external file for command validation, separate from .env this time! Method will change in the future in order to accomodate the next two boxes.
- [ ] Ability to adjust command output without editing source code and redeploying
- [ ] Ability to add commands without editing source code and redeploying
- [ ] Uptime check
- [ ] Subscription/Donation Alerts
- [ ] HTML object creation and control
- [ ] Random chat function
