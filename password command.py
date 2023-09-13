@client.slash_command(name="passwordcommand", description="command with a preset password pass is ", guild_ids=[testingServerID,])
async def passwordcommand(inter : Interaction, password:str):
  passwordcode = "Ur password here"
  if password == passwordcode:
    await inter.response.send_message("Nice you got the password!")
  if password != passwordcode:
    await inter.response.send_message("Thats not the right password!")
