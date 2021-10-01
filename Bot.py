import discord
from datetime import date
import random
from discord.ext import commands
import code_chef
import Problem
import time
client = discord.Client()
iam = 'K-Bot#xxxx'
@client.event
async def on_ready():
    print("I am UP")
    await client.change_presence(activity=discord.Game(name="^help"))
    channel = client.get_channel(....)
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = discord.Embed(title='Welcome Jedi',
                       description='Welcome {}, tell us your name and your club in #welcome and #homenum-revelio'.format(member.mention))
            await channel.send(embed=embed)
@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = discord.Embed(title='So Long Warrior',
                       description='Its okay,Take your time.Life is Hard for INTERNET EXPLOER users... {}'.format(member.mention))
            await channel.send(embed=embed)
    print(f'{member} has left the test server')

@client.event
async def on_voice_state_update(member, before, after):
        for channel in member.guild.channels:
            if str(channel) == "logs":
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                today = date.today()
                if(discord.VoiceState.mute == True):
                    embed = discord.Embed(title ="",
                                              description = '{} muted {}```\nTime: {}\nDate: {}```'.format(member.mention,member.voice.channel.name,current_time,today),
                                              color=discord.Color.red())
                    await channel.send(embed = embed)
                else:
                    try:
                        embed = discord.Embed(title ="",
                                                  description = '{} joined {}```\nTime: {}\nDate: {}```'.format(member.mention,member.voice.channel.name,current_time,today),
                                                  color=discord.Color.green())
                        await channel.send(embed = embed)
                    except:
                        embed = discord.Embed(title = "",
                                              description = '{} Left the voice channel```Time: {}\nDate: {}```'.format(member.mention,current_time,today),
                                              color=discord.Color.red())
                        await channel.send(embed = embed)

@client.event
async def on_message(message):
    if message.content == "^help":
        embed = discord.Embed(title = "Bot Commands:",
                              description = "```^Hello - To know about me\n^TotalUsers - To get the number of users in this server\n^Ping - To check my latency\n^codechef - To see the ongoing contests on codechef\n^problem -This comand followed by a Difficulty level (easy,medium,hard) gives you a random cp qusetion to solve\n^Hackathons - To Know about the current Hackathons \n^WannaKnow - This command followed by a QUESTION you will enter a random luck based game where I answer your QUESTION.```",
                              color=discord.Color.blue())
        await message.channel.send(embed = embed)
    elif message.content == "^Hello" and str(message.author)!=iam:
        await message.channel.send("Hi, I am K-Bot I am currently under development and hopefully will be developed soon")
    elif message.content == "^Ping" and str(message.author)!=iam:
        await message.channel.send(f'Pong!{round(client.latency*1000)} ms')
    elif "^WannaKnow " in message.content and str(message.author)!= iam:
        question = message.content[11:]
        responses = ["It is certain.",        "It is decidedly so.",        "Without a doubt.",        "Yes - definitely.",        "You may rely on it.",        "As I see it, yes.",        "Most likely.",        "Outlook good.",        "Yes.",        "Signs point to yes.",        "Reply hazy, try again.",        "Ask again later.",        "Better not tell you now.",    "Cannot predict now.",        "Concentrate and ask again.",        "Don't count on it.",        "My reply is no.",        "My sources say no.",        "Outlook not so good.","Very doubtful."]
        await message.channel.send(f'Question: {question}\n Answer:{random.choice(responses)}')
    elif message.content == "^codechef" and str(message.author)!= iam:
        list_table = code_chef.start()
        await message.channel.send(f"Hey {message.author.mention} I am Glad you asked about it\nHere are the on going contests on codechef:  ")
        for i in list_table:
            await message.channel.send(f"```Code: {i[0]}\nName: {i[1]}\nStart: {i[2]}\nEnd: {i[3]}```")
    elif message.content =="^Hackathons":
        await message.channel.send(f"This Commands work is under Process")
    elif "^problem" in message.content and str(message.author)!=iam:
        dif = message.content[9:]
        ans = Problem.letsgive(dif)
        await message.channel.send(f"Well, if droids could think, there’d be none of us here, would there?\nNow Jedi {message.author.mention} Its Your Turn to think and solve this {ans[2].capitalize()} CP Problem...\nHope you will conquer the problem soon!!!")
        embed = discord.Embed(title = ans[1],
                              description = f"```Platform: {ans[0].capitalize()}\nCode/Name: {ans[1]}\nDifficulty: {ans[2].capitalize()}```\nLink: {ans[3]}",
                              color=discord.Color.purple())
        await message.channel.send(embed = embed)
    elif client.user.mention in message.content :
        await message.channel.send("Hey Jedi {} I am K-Bot here to serve you\nPlease enter your query in the text channel #help and our support team Yodas will respond you as soon as possible...\nSince you mentioned me!!!\nHave A Nice Day".format(message.author.mention))

client.run('')
