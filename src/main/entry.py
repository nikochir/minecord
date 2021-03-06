#init#
import os.path
import sys
sys.path.append(os.path.dirname(__file__))
#includes
import config
##discord
import discord
from discord import utils
#work#
class Client(discord.Client):
    async def on_ready(self):
        print("logged as {0}!".format(self.user))
    async def on_message(self, mesg):
        print("mesg from {0.author}: {0.content}".format(mesg))
    async def on_raw_reaction_add(self, data):
        chan = self.get_channel(data.channel_id)
        mesg = await chan.fetch_message(data.message_id)
        user = utils.get(mesg.guild, id=payload.user_id)
        try:
            emoj = str(data.emoji)
            role = utils.get(mesg.guild.roles, id = config.ROLE_ALL[emoj])
            role = mesg.guild.roles.get_role(id)
            if (len([itr for itr in user.roles if itr.id not in config.ROLE_EXC]) <= config.ROLE_NUM):
                await user.add_roles(role)
                print("user {0.display_name} has been granted with the role {1.name}".format(user, role))
            else:
                print("user {0.display_name} cannot be granted with the role {1.name}".format(user, role))
        except KeyError as exc:
            print("the role is not found!")
        except Exception as exc:
            print("something is going wrong!")
#quit#
client = Client()
client.run(config.BOTA_TOKEN)
#endf#