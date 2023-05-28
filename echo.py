# echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

# def echo(text,repeat=3):
#     echoed=""
#     for i in range(repeat,0,-1):
#         echoed+=f"{text[-i:]}\n"
#     return f"{echoed.lower()}."

# if __name__=="__main__":
#     tex=input("Shoutout: ")
#     print(echo(tex))
