import logging as log
import discord
import os, re
import clap_converter


class ClapBot(discord.Client):
    async def on_ready(self):
        log.info('ClapBot started with username {0.name} and id {0.id}'.format(self.user))

    async def on_message(self, message):
        if len(message.mentions) > 0 and self.user in message.mentions and message.content.startswith("> "):
            messages = list(
                filter(lambda msg: msg.author != self.user, await message.channel.history(limit=6).flatten()))

            pattern = re.compile(r'> (.+)\n')
            message_to_clapify = pattern.match(messages[2].content).group(1)
            await message.channel.send(clap_converter.clapify(message_to_clapify))


client = ClapBot()
client.run(os.getenv('CLAPIFY_KEY'))
