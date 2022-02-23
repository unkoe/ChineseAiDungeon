from utils.story_helper import initize,Story


if __name__ == '__main__':
    initize("./tmp_weight/")
    begin = f'''你在树林里冒险，指不定会从哪里蹦出来一些奇怪的东西，你握紧手上的手枪，希望这次冒险能够找到一些值钱的东西'''
    story = Story(begin)
    story.interactive()