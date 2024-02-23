import discord
import asyncio
import subprocess
from discord.ext import commands
from config import owners

def is_owner():
    async def predicate(ctx):
        return ctx.author.id in owners
    return commands.check(predicate)

class Owners (commands.Cog) :
    def __init__ (self, bot):
        self.bot = bot
        self.normal_color = 0x00fa6c
        self.error_color = 0xff4a4a

    @commands.command (name = 'load', aliases = ['로드'])
    @is_owner()
    async def load (self, ctx, module) :
        try :
            self.bot.load_extension(module)
            embed = discord.Embed (
                title = '로드 성공!',
                description = f'모둘 : {module}',
                color = self.normal_color
            )
        except Exception as error :
            embed = discord.Embed (
                title = '로드 실패!',
                description = '에러 : {}'.format(error),
                color = self.error_color
            )
        await ctx.send (embed = embed)

    @commands.command (name = 'reload', aliases = ['리로드'])
    @is_owner()
    async def loadre (self, ctx, module) :
        try :
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
            embed = discord.Embed (
                title = '리로드 성공!',
                description = f'모둘 : {module}',
                color = self.normal_color
            )
        except Exception as error :
            embed = discord.Embed (
                title = '리로드 실패!',
                description = '에러 : {}'.format(error),
                color = self.error_color
            )
        await ctx.send (embed = embed)

    @commands.command (name = 'unload', aliases = ['언로드'])
    @is_owner()
    async def unload (self, ctx, module) :
        try :
            self.bot.unload_extension(module)
            embed = discord.Embed (
                title = '언로드 성공!',
                description = f'모둘 : {module}',
                color = self.normal_color
            )
        except Exception as error :
            embed = discord.Embed (
                title = '언로드 실패!',
                description = '에러 : {}'.format(error),
                color = self.error_color
            )
        await ctx.send (embed = embed)
        
    @commands.command ()
    @is_owner()
    async def shell (self, ctx, *cmd) :
        try :
            cmd = " ".join(cmd[:])
            res = subprocess.check_output(cmd, shell=True, encoding='utf-8')
            embed=discord.Embed(title="**Command Sent!**", description=f"Input : **{cmd}**", color=self.normal_color)
            embed.add_field(name="Output", value=f"```{res}```")
            await ctx.send(embed=embed)
        except (discord.errors.HTTPException) :
            await ctx.send ('글자수가 많아 일반 텍스트로 전송합니다.')
            cmd = " ".join(cmd[:])
            res = subprocess.check_output(cmd, shell=True, encoding='utf-8')
            await ctx.send("```" + res + "```")
        except (subprocess.CalledProcessError) :
            embed=discord.Embed(title="**Command Error!**", description="명령어 처리 도중 오류 발생!",color=self.error_color)
            await ctx.send(embed=embed)
            
def setup (bot) :
    bot.add_cog(Owners(bot))
