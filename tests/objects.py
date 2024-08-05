from balethon.conditions import private, text
from balethon.dispatcher import Chain
from balethon.event_handlers import MessageHandler

chain = Chain(__name__, private & text)
@chain.on_message(~private & text)
def kos():
    pass
@chain.on_initialize()
def mos():
    pass
@chain.on_callback_query(private)
def chos():
    pass


chain2 = Chain("2", text)
@chain2.on_command()
def ok():
    pass

chain.add(chain2)
chain.include(chain2)

def main():
    # eh = MessageHandler(lambda kos: kos)
    # print(eh)

    print(chain)


if __name__ == "__main__":
    main()
