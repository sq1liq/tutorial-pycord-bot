import discord
from discord.ext import commands
import datetime
import asyncio


###
# notice that this code doesn't work with only this code you need the code from episode 5 and 6 to get the final result
###

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
        await channel4.send(embed = em, view = Ticketview)

