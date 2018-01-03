#!usr/bin/env python
#coding=utf-8

from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def is_going_to_stateBuf1(self, update):
        text = update.message.text
        return (text == '吃早餐囉') or (text == '吃晚餐囉')
    def is_going_to_stateBuf2(self, update):
        text = update.message.text
        return text == '怎麼玩'
    def is_going_to_state1(self, update):
        text = update.message.text
        return text == '吃午餐囉'
    def is_going_to_state2(self, update):
        text = update.message.text
        return text == '獨角獸'
    def is_going_to_state3(self, update):
        text = update.message.text
        return text == '蜂鳥'
    def is_going_to_state4(self, update):
        text = update.message.text
        return text == '把她當作午餐'
    def is_going_to_state5(self, update):
        text = update.message.text
        return text == '騎著她尋找食物'
    def is_going_to_state6(self, update):
        text = update.message.text
        return text == '跟他走'
    def is_going_to_state7(self, update):
        text = update.message.text
        return text == '繼續尋找午餐'
    def is_going_to_state8(self, update):
        text = update.message.text
        return text == '黑皇后'
    def is_going_to_state9(self, update):
        text = update.message.text
        return text == '精靈帕金森的家'
    def is_going_to_state10(self, update):
        text = update.message.text
        return text == '拿著金斧頭的河女神'
    def is_going_to_state11(self, update):
        text = update.message.text
        return text == '拿著你的彈弓的河男神'
    def is_going_to_state12(self, update):
        text = update.message.text
        return text == '美人魚'

    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == 'restart'

    def on_enter_stateBuf1(self, update):
        update.message.reply_text("沒得吃[restart]")

    def on_enter_stateBuf2(self, update):
        update.message.reply_text("[restart] 記得在restart後打入「吃午餐囉」，才可以順利地知道今天該吃什麼喔!")
        
    def on_enter_user(self, update):
        update.message.reply_text("restart")

    def on_exit_user(self, update):
        pass
#黑人問號
    def on_enter_state1(self, update):
        update.message.reply_photo(photo='https://i.imgur.com/YOtU7Pe.jpg')
        update.message.reply_text("你是個森林獵人，走在魔法森林裡，尋找美味的午餐，這時，樹叢裡發出奇怪的聲響，你遇到的是[獨角獸]還是[蜂鳥]呢？")

    def on_enter_state2(self, update):
        update.message.reply_text("獨角獸是個非常迷人的生物，白色的毛皮，溫潤的角，身為獵人的你，會[把她當作午餐]還是[騎著她尋找食物]？")

    def on_enter_state3(self, update):
        update.message.reply_text("蜂鳥看到你，唱起了一首歌，美麗的森林不再，青翠的綠樹消失，邪惡的力量在世界擴散，勇敢的獵人呀，你是否願意跟著我，拯救失衡的世界。心中很受觸動的你，會選擇[跟他走]還是[繼續尋找午餐]？")

    def on_enter_state4(self, update):
        update.message.reply_text("選擇把獨角獸吃掉的你，屬於A型人，堅決果斷，做事不猶豫，不易受到誘惑，敢把奇幻動物中的佼佼者獨角獸吃掉，代表你不迷信，有很大的可能，是個宅宅。建議你今天的午餐吃紅酒燉牛肉配西瓜汁，兩個分別吃起來都很美味，一起就不知道了。[restart]")

    def on_enter_state5(self, update):
        update.message.reply_text("騎在獨角獸的背上，你感受到一種輕盈的感覺，不知不覺就睡著了……等你清醒之後，發現自己來到一個美麗的水晶皇宮，這是[黑皇后]還是[精靈帕金森的家]呢？")

    def on_enter_state6(self, update):
        update.message.reply_text("選擇成為超級英雄的你，是B型人，憨厚老實，但內心又存著熱血，像這種人，肯定是宅宅，建議你午餐去吃泡麵，回到現實社會吧。[restart]")

    def on_enter_state7(self, update):
        update.message.reply_text("走著走著，你來到湖邊，耳邊又傳來一陣悅耳的歌聲，她是[拿著金斧頭的河女神]還是[拿著你的彈弓的河男神]或是[美人魚]呢？")

    def on_enter_state8(self, update):
        update.message.reply_text("選擇黑皇后的你，最後跟黑皇后共進了美味的午餐，屬於C型人。溫柔體貼，風流成性是你的代名詞，每天跟不同妹子帥哥吃飯，並且是大家的精神支柱，建議你今天的午餐跟往常一樣，去找最正的女朋友一起吃大豆豆吧。[restart]")

    def on_enter_state9(self, update):
        update.message.reply_text("會選擇這麼不靠譜的精靈帕金森的你，是個浪漫可愛，總是活在自己幻想的少女，屬於D型人。像你這麼可愛，肯定是男孩紙，午餐就吃珍奶配豬排吧，或是你再忍一下，晚餐去吃鳳凰來～[restart]")

    def on_enter_state10(self, update):
        update.message.reply_text("選擇金斧頭而不是自己的彈弓，你是一個會審視自己，努力向上的人，是傳說中的E型人。身為E型人的你，每天忙著工作、寫作業、打扣，才不會吃午餐呢。[restart] ")

    def on_enter_state11(self, update):
        update.message.reply_text("選擇男神的你，忠實的面對自己的慾望，是所謂的F型人，你在別人的眼中，總是神祕、有才華，但實際上你是個很愛喵喵的人，每天都一定要吸貓。今天你的午餐就吃咖哩飯吧，香濃濃的味道，你的貓也好喜歡。[restart] ")

    def on_enter_state12(self, update):
        update.message.reply_text("美人魚真的很美，你與她過著幸福快樂的日子。在美人面前沒辦法的你，是G型人，你喜歡跟你的朋友聚在一起看正妹帥哥，只要是美的東西你都喜歡，既然這樣，午餐就找助教吃吧，每個助教都花容月貌的<3快去邀助教吃目白！[restart]")


    def on_exit_stateBuf1(self, update):
        print('Leaving state buf1')
    def on_exit_stateBuf2(self, update):
        print('Leaving state buf2')
    def on_exit_state0(self, update):
        print('Leaving state0')
    def on_exit_state1(self, update):
        print('Leaving state1')
    def on_exit_state2(self, update):
        print('Leaving state2')
    def on_exit_state3(self, update):
        print('Leaving state3')
    def on_exit_state4(self, update):
        print('Leaving state4')
    def on_exit_state5(self, update):
        print('Leaving state5')
    def on_exit_state6(self, update):
        print('Leaving state6')
    def on_exit_state7(self, update):
        print('Leaving state7')
    def on_exit_state8(self, update):
        print('Leaving state8')
    def on_exit_state9(self, update):
        print('Leaving state9')
    def on_exit_state10(self, update):
        print('Leaving state10')
    def on_exit_state11(self, update):
        print('Leaving state11')
    def on_exit_state12(self, update):
        print('Leaving state12')
