import discord
from discord.ext import commands
import datetime
import asyncio
from discord.ui.item import Item

class Yesno2(discord.ui.View): #make the same for the second view
    def __init__(self):
        super().__init__(timeout=None)

    
    @discord.ui.button(
        label = "Yes",
        style = discord.ButtonStyle.green,
        emoji = "✅",
        custom_id = "yes"
    )
    async def yes(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.message.delete()

        em = discord.Embed(
            title = "Ticket System",
            description = f"Ticketlöschung wurde von {interaction.user.mention} am {datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y um %H:%M:%S')} aktiviert. Ticket wird in 5 sekunden gelöscht.",
            color = discord.Color.red()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        await interaction.channel.send(embed=em)
        await asyncio.sleep(5)
        await interaction.channel.delete()

    
    @discord.ui.button(
        label = "No",
        style = discord.ButtonStyle.red,
        emoji = "❌",
        custom_id = "no"
    )
    async def no(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.message.delete()

        em = discord.Embed(
            title = "Ticket System",
            description = "Ticketlöschung wurde nicht aktiviert.",
            color = discord.Color.orange()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        await interaction.channel.send(embed=em)

class Yesno1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label = "Yes",
        style = discord.ButtonStyle.green,
        emoji = "✅",
        custom_id = "yes"
    )
    async def yes(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.message.delete()

        em = discord.Embed(
            title = "Ticket System",
            description = f"Ticket wurde von {interaction.user.mention} am {datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y um %H:%M:%S')} geschlossen.",
            color = discord.Color.red()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        await interaction.channel.send(embed=em)

    
    @discord.ui.button(
        label = "No",
        style = discord.ButtonStyle.red,
        emoji = "❌",
        custom_id = "no"
    )
    async def no(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.message.delete()

        em = discord.Embed(
            title = "Ticket System",
            description = "Ticket wurde nicht geschlossen.",
            color = discord.Color.orange()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        await interaction.channel.send(embed=em)

class ComponentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) #that's important for the persitent view.
    
    @discord.ui.button(
        label = "Close the Ticket",
        style = discord.ButtonStyle.red,
        emoji = "🔒",
        custom_id = "ticket_close" #that's important for the persitent view too.
    ) #now we make a call back function for the first buttton
    async def ticket_close(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        em = discord.Embed(
            title = "Ticket System",
            description = "Möchtest du das Ticket wirklich schließen?",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        msg = await interaction.channel.send(embed=em, view = Yesno1())
        

        


    @discord.ui.button(
        label = "Delete the Ticket",
        style = discord.ButtonStyle.grey,
        emoji = "🗑️",
        custom_id = "ticket_delete" #all buttons must have a custom_id if you want to have the persitent views.
    )#now we meke the same by this button
    async def ticket_delete(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        em = discord.Embed(
            title = "Ticket System",
            description = "Möchtest du das Ticket wirklich löschen?",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        msg = await interaction.channel.send(embed=em, view = Yesno2())
        

class Ticketview(discord.ui.View):
    def __init__(self, ticketmsg, createttext, name, role1, role2, role3, channel3):
        super().__init__(timeout=None) # we make this for later
        self.ticketmsg = ticketmsg
        self.createttext = createttext
        self.name = name
        self.role1 = role1
        self.role2 = role2
        self.role3 = role3
        self.channel3 = channel3
        # now you have tthe arguments in the class
        
    @discord.ui.button(
        label = "Ticket öffen",
        style = discord.ButtonStyle.green,
        emoji= "📨", # to get this emoji widget press windows + .
        custom_id="ticket_open"
    )
    async def ticket_open(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()

        info = await interaction.followup.send("🔧 Ticket wird geöffnet. dies kann ein paar sekunden dauern.", ephemeral=True)

        
        for i in interaction.guild.categories:
            if i.name == "Tickets":
                cate = i
                break
        else:
            cate = await interaction.guild.create_category(name="Tickets")

        channel = await interaction.guild.create_text_channel(
            name = f"{self.name}",
            category = cate,
            topic = f"Ticket für {interaction.user.name} | Ticket erstellt am {datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y um %H:%M:%S')}",
        )

        role1 = interaction.guild.get_role(int(self.role1))
        role2 = interaction.guild.get_role(int(self.role2)) # this is for gettting the roles
        role3 = interaction.guild.get_role(int(self.role3))

        if role1 is None or role2 is None or role3 is None:
            await interaction.followup.send("🔧 Ticket konnte nicht geöffnet werden. bitte kontaktieren sie einen Administrator", ephemeral=True)
            return
        

        #now we set the permissions
        await channel.set_permissions(
            role1, 
            view_channel=True,
            read_messages=True,
            send_messages=True, 
            attach_files=True, 
            embed_links=True, 
            read_message_history=True
        )

        await channel.set_permissions(
            role2,
            view_channel=True,
            read_messages=True,
            send_messages=True,
            attach_files=True,
            embed_links=True,
            read_message_history=True
        )

        await channel.set_permissions(
            role3,
            view_channel=True,
            read_messages=True,
            send_messages=True,
            attach_files=True,
            embed_links=True,
            read_message_history=True
        )

        await channel.set_permissions(
            interaction.guild.default_role,
            view_channel=False,
            read_messages=False,
            send_messages=False,
            attach_files=False,
            embed_links=False,
            read_message_history=False
        )

        await info.edit(content="🔧 Ticket wurde geöffnet.")


        #now we want to ping the roles before the message in the ticket channel pops up.
        em = discord.Embed(
            title = f"Ticket for `{interaction.user.name}`",
            description = f"{self.createttext}",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = interaction.guild.icon.url)
        await channel.send(content=f"{interaction.user.mention} | {role1.mention} | {role2.mention} | {role3.mention}", embed = em, view = ComponentView())








class ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup_ticket(self, ctx: commands.Context):

        em = discord.Embed(
            title = "Ticket System",
            description = "Bitte sende mit den Text der Nachicht die du in den ticket channel senden möchtest.",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await ctx.send(embed = em)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            msg = await self.bot.wait_for("message", check = check, timeout = 60)
            msg1 = msg.content
            ticketmsg = msg1
        except asyncio.TimeoutError:
            em = discord.Embed(
                title = "Ticket System",
                description = "Du hast zu lange gebraucht um zu antworten.",
                color = discord.Color.red()
            )
            em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
            await ctx.send(embed = em)
            return
        
        em = discord.Embed(
            title = "Ticket System",
            description = "Bitte sende mit den Text der Nachicht die du in den ticket channel senden möchtest.",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await ctx.send(embed = em)

        try:
            msg = await self.bot.wait_for("message", check = check, timeout = 60)
            msg2 = msg.content
            createttext = msg2

        except asyncio.TimeoutError:
            em = discord.Embed(
                title = "Ticket System",
                description = "Du hast zu lange gebraucht um zu antworten.",
                color = discord.Color.red()
            )
            em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
            await ctx.send(embed = em)
            return
        
        em = discord.Embed(
            title = "Ticket System",
            description = "Bitte sende mir den namen für dein tickets.",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await ctx.send(embed = em)

        try:
            msg = await self.bot.wait_for("message", check = check, timeout = 60)
            name = msg.content

        except asyncio.TimeoutError:
            em = discord.Embed(
                title = "Ticket System",
                description = "Du hast zu lange gebraucht um zu antworten.",
                color = discord.Color.red()
            )
            em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
            await ctx.send(embed = em)
            return
        

        em = discord.Embed(
            title = "Ticket System",
            description = "Bitte sende mir 3 Rollen ids die zugriff auf das Ticket haben sollen.",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await ctx.send(embed = em)

        try:
            msg = await self.bot.wait_for("message", check = check, timeout = 60)
            role1 = msg.content
            await msg.add_reaction("👍")

            msg3 = await self.bot.wait_for("message", check = check, timeout = 60)
            role2 = msg3.content
            await msg3.add_reaction("👍")

            msg4 = await self.bot.wait_for("message", check = check, timeout = 60)
            role3 = msg4.content
            await msg4.add_reaction("👍")

        except asyncio.TimeoutError:
            em = discord.Embed(
                title = "Ticket System",
                description = "Du hast zu lange gebraucht um zu antworten.",
                color = discord.Color.red()
            )
            em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
            await ctx.send(embed = em)
            return
        
        em = discord.Embed(
            title = "Ticket System",
            description = "Bitte ping den channel wo das ticket system erstellt werden soll.",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await ctx.send(embed = em)

        try:
            msg = await self.bot.wait_for("message", check = check, timeout = 60)
            channel = msg.content
            channel1 = channel.replace("<#", "")
            channel2 = channel1.replace(">", "")
            channel3 = int(channel2)
        
        except asyncio.TimeoutError:
            em = discord.Embed(
                title = "Ticket System",
                description = "Du hast zu lange gebraucht um zu antworten.",
                color = discord.Color.red()
            )
            em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
            await ctx.send(embed = em)
            return
        

        
        em = discord.Embed(
            title = "Ticket System",
            description = "Erfolgreich ein Ticket System erstellt.",
            color = discord.Color.green()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await ctx.send(embed = em)

        channel4 = await self.bot.fetch_channel(channel3)

        if channel4 is None:
            em = discord.Embed(
                title = "Ticket System",
                description = "Der Channel wurde nicht gefunden.",
                color = discord.Color.red()
            )
            em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
            await ctx.send(embed = em)
            return
        
        em = discord.Embed(
            title = "Ticket System",
            description = f"{msg1}",
            color = discord.Color.blue()
        )
        em.set_footer(text = "Ticket System", icon_url = ctx.guild.icon.url)
        await channel4.send(embed = em, view = Ticketview(ticketmsg, createttext, name, role1, role2, role3, channel3)) # now you must be pastte the copyed arguments in the brackets
        #to get this widget press windows + v



def setup(bot):
    bot.add_cog(ticket(bot))
