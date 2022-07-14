import discord
from discord.ext import commands
from discord import Embed

intents = discord.Intents.default()

intents.guilds = True

bot = commands.Bot(command_prefix = "?", intents = intents)
wordlist = ['RUG','BAD','SHIT','LOST','WASTE','NUDES','SCAM','SUCKS','FUCK','DICK','ASS','SUCK','EATS','DUMB','RETARD','STUPID','HUNGRY']


class Fud(discord.ui.View):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.value = None
   
    @discord.ui.button(label='False Alarm!', style=discord.ButtonStyle.green)
    async def FalseAlarm(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="False Alarm", description= "Alright, Nothing Happened", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)       
        
        
        self.value = "FalseAlarm"
        
             
          
    @discord.ui.button(label='Delete', style=discord.ButtonStyle.red)
    async def Delete(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="Deleted", description= "Anti-FUD", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)
        #await self.message.channel.send(self.message.id)
        await self.message.delete()
              
        self.value = "Deleted"
          
    @discord.ui.button(label='Ban', style=discord.ButtonStyle.blurple)
    async def Ban(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        
        embed = discord.Embed(title="Banned", description= "nice", color=discord.Color.dark_grey())
        await (interaction.followup).send(embed=embed, ephemeral=False)       
        await self.message.author.ban(reason = "FUD")
        
        self.value = "Banned"
        await 
        


@bot.event
async def on_message(message):
    
    
    if any(word in message.content.upper() for word in wordlist):
       
        mention = []
        for role in message.author.roles:
            if role.name != "@everyone":
                mention.append(role.mention)

        b = ", ".join(mention)

        channel = bot.get_channel(949715986167234570)
        embed = discord.Embed(title=message.author, description= "**Message sent**: " + message.content, color=discord.Color.dark_grey())
        
        embed.add_field(name="Roles:", value=b)
        view = Fud(message)
        #message1 = Buttons(message.id)
        await print(embed.id)
        await channel.send(embed=embed, view=view)
      

bot.run("TOKEN")