'''
A handy little piece of code that sniffs your Microsoft Teams logs.txt for the latest status update and returns it as:
"Available" = Available
"Busy" = Busy
"BRB" = Be Right Back
"DND" = Do Not Disturb
"Presenting" = Presenting
"IAM" = In A Meeting
"Offline" = Offline

It takes one argument, a string with the path to the teams AppData folder. It looks something like:
C:/Users/XXXXXXX/AppData/Roaming/Microsoft/Teams

This code is issued under the free-for-all to use principle.
However if you work for a large company that plan to use it, you should hit me up and pay something. Come-on..

Also if you use it for any project, please like it on github or something. Always fun to know it was used!

Casper Christiansen
casper.nils.christiansen@gmail.com
'''


def get_teams_status(teams_path):
    f = open(teams_path + "/logs.txt", "r")
    for x in reversed(list(f)):
        if "available" in x or "Available" in x:
            f.close()
            return "Available"
        elif "busy" in x or "Busy" in x:
            f.close()
            return "Busy"
        elif "Away" in x or "away" in x:
            f.close()
            return "Away"
        elif "BeRightBack" in x:
            f.close()
            return "BRB"
        elif "DoNotDisturb" in x:
            f.close()
            return "DND"
        elif "Presenting" in x or "presenting" in x:
            f.close()
            return "Presenting"
        elif "InAMeeting" in x:
            f.close()
            return "IAM"
        elif "Offline" in x or "offline" in x:
            f.close()
            return "Offline"
