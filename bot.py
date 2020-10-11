import logging as log
import discord
import os
import clap_converter


class ClapBot(discord.Client):
    async def on_ready(self):
        log.info('ClapBot started with username {0.name} and id {0.id}'.format(self.user))

    async def on_message(self, message):
        if len(message.mentions) > 0 and message.mentions[0].id == self.user.id:
            await message.channel.send(clap_converter.clapify(message.content))


client = ClapBot()
client.run(os.getenv('DISCORD_KEY'))
