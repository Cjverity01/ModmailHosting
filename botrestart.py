import requests


url = "https://discord.com/api/v9/channels/1256887562706882641/messages"

payload = {
      "content" : "Modmail bot restarted!" 
}


headers = {
  "Authorization" : "MTA1MDQ5NDY2NzYxMzAxMjA0OQ.Gj-lwM.1JzZ7NcbefMP5cg9bS5bYAgU9liEtgfcDhHJG8"
}

res = requests.post(url, payload, headers=headers)
