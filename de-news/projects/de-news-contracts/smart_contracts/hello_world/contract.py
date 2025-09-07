from algopy import ARC4Contract, String
from algopy.arc4 import abimethod


class HelloWorld(ARC4Contract):
    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello, " + name


class PublishNews(ARC4Contract):
    @abimethod()
    def publish(self, title: String, content: String) -> String:
        return "Published news article: " + title + "\n" + content
