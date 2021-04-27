# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")
define r = Character("Receptionist")
define red = Character("BadBoy")
define boss = Character("Boss")
define yellow = Character("Muscle")
define mf = Character ("Male Friend")


# The game starts here.
label start:

    # Show a background.
    scene company entrance

    # This shows a character sprite.
    #show eileen happy

    # These display lines of dialogue.
    #After arriving at the company:
    p "(Finally arrived at XXX city. I really got lucky landing this job.)"

    p "(I heard the taxi leave as I was about to enter the new apartment, but god damn,
    these suitcases are HEAVY!! What a struggle.)"

    # GO UP THE APARTMENT
    # scene empty apartment
    scene company reception desk
    with hpunch

    p "(It looks the same as last time, still empty, but it’s pretty neat for a one bedroom apartment)"
    p "(I layed down the mattress for the night and ate a sandwich thinking about my first day at work tomorrow)"
    p "I really hope I don’t mess it up..."

    # NEXT DAY

    "DRIIIIIIM DRIIIIIIM"
    #SCREEN SHAKE

    #CHOICE
    p "WHERE AM I?"
    p "Ow,  my head"
    p "(I got up as soon as I heard the alarm ring, scared and confused of my whereabouts,
    but quickly remembered I just moved to a new city)"
    p "Why am I so dramatic? I hope i get used used to this place fast"

    p "(With that in mind, I went to the bathroom, took a shower and brushed my teeth)"
    p "(Today was going to be my first day at this publishing company. They were known for
    being old fashioned with their attire, so there wasn’t really much to choose from other than what
    colored suit i should wear)"
    p "Hmm...maybe I’ll wear..."

    #CHOICE
    p "Black"
    p "Grey"
    p "Pink"
    p "Blue"
    p "Orange"

    p "I’m happy with it, I think (insert color) was a great choice!"
    p "Now onto the company, which is...20 MINUTES AWAY? I’VE GOTTA RUN!!!"

    #LEAVE THE APARTMENT AND GO TO THE COMPANY
    #IN FRONT OF THE COMPANY

    p "(This must be it, XXX COMPANY. I just arrived but I’m already so tired. I need to perk up, gotta look professional)"
    "Here goes nothing…"

    #ENTER THE COMPANY

    p "(Wow, this place has a really nice atmosphere, and it looks very modern)"
    p "(I look around analyzing the place, looking a bit lost, until i notice the front desk lady coming up to me)"

    #RECEPTIONIST
    r "Hello, how can I help you?"

    #CHOICE
    p "Hi, I’m here for my first day of work, I’m XXX"
    p "Hello, you can help me by telling me where to go, you see, I’m new here."
    p "Hello, I’m a new worker here, I need my badge and need to know where to go. Make it quick please, I’m late."

    r "Indeed, I see your name on the list. Welcome to the company, here’s your badge."

    #YOU’VE RECEIVED A BADGE, CHECK IT IN YOUR INVENTORY/DESK

    r "Just go up to the 10th floor and enter Mr. XXX office."
    r "Have a good day."

    p "Thank you, you too."

    #USE THE ELEVATOR TO GO UP TO THE 10TH FLOOR

    p "(Ok, that wasn’t so bad)"
    "(So far so good, now let’s hope this elevator comes fast)"

    #IN THE ELEVATOR

    p "This is really nice, it has a lot of lights"
    "(I take a few deep breaths. The nerves came pilling in)"


    #SCREEN SHAKE
    p "(As soon as the elevator doors open a large open floor appears in front of me. Filled with fancy desks, small decorations and office workers, the atmosphere felt yet foreign to me.)"

    p "(Now let’s see...wheres Mr.XXX office)"
    p "(I spot a few offices to my right)"

    #MOVE TO THE OFFICES
    p "(Ok, I’m in front of the office, it’s now or never. I’m so nervous.)"

    #CHOICE
    p "(But...I don’t have the guts to enter. I’m just going to wait until they notice me)"
    p "(Knock on the door and wait)"
    p "Knock on the door and enter the office)"

    #ONOMATOPEIA
    p "(I knock on the door a bit nervous)"

    boss "Come in"

    p "(I open the door slowly and enter the office)"

    #ENTER THE OFFICE
    #MAKE HIM TALK FIRST
    p "Good morning, I’m- my name’s XXX. Pleasure to meet you. (Oh my god, did i just stutter…?)"
    p "Good morning, I’m XXX. PLEASURE TO MEET YOU!!! (Did my voice came out a bit loud?)"
    p "Goodmorning,I’mXXX.Pleasuretomeetyou!!! (I think I spoke too fast.)"

    #SHOW BOSS WRITING SOMETHING
    p "(He made a weird face and wrote something on his paper. I’m doomed, oh my god, someone save me)"
    p "(He made a weird face and wrote something on his paper. This is it, shit’s going down)"
    p "(He made a weird face and wrote something on his paper. That’s it, I better end my lease, I’m gonna get fired)"
    #SE CALHAR ISTO TÁ UM BOCADO EXAGERADO MAS PRONTO, A IDEIA TÁ LÁ

    boss "Good morning XXX, I’m XXX XXX, welcome to XXX company."

    p "Thank you."

    boss "Please take a seat. This is XXX, he will be starting work today as well, I hope both of you get along with the rest of the team and adapt well to the workplace."

    p "(Sitting besides me there was another young man)"

    boss "As both of you may know, XXX (our company) is in the middle of trying to close a special deal with a very famous writer, that will guarantee us a partnership with XXX company."

    p "(...)"

    boss "I believe you possess the skills we need to aid us in completing said deal, so I hope you don’t prove us wrong"

    p "(This just got really serious...I’m getting chills)"

    boss "With that said I’m going to show you around the office. Follow me."

    p "(...)"

    #Follow the BOSS around the office
    #ou deixar que ele nos guie automaticamente?

    #OUTSIDE OF THE OFFICE

    boss "As you just saw, the offices are in this corner. Because you are still starting, you will have to report everything to me at the end of the day, so get used to this place."

    p "(...)"

    boss "Here is the main working area. Please refrain from shouting and keep it professional"

    p "(...)"

    boss "This is your desk, feel free to personalize it, but don’t paint anything or use damaging tape"

    p "(...)"

    boss "Right here is the 'lounge'" #(aquela pequena cozinha onde eles almoçam e tal, ver melhor no ANTI P.T.). You can come here to take a break, drink coffee or eat lunch. We don’t have fixed times for lunch so you make your own schedule.

    p "(...)"

    boss "Lastly this is the conference room, where the meetings take place. Got everything down?"

    p "Yes, thank you."
    p "No, can you explain one more time, please?"

    #(...)

    boss "Good. Then you can choose what to start working on today."

    #CHOICE
    p "(Right...I remember they sent an email talking about the things they wanted to test me on.)"
    p "(I think it was)"
    #CHOICE
    p "Between handling files and handling data, right, Sir?"
    p "Between cleaning the place and helping you, right Sir?"
    p "Between handling reviews and data research, right Sir?"

    boss "Yes, that’s right. Then what do you choose?"

    #CHOICE
    p "Handling reviews, Sir."
    p "Data research, Sir."

    boss "Understood."

    #SHOW BOSS TEXTING
    p "(As he finished talking I saw him text someone on his phone)"

    #SHOW BOSS LOOKING UP THE PHONE
    p "One last thing, miss XXX. We use our phones a lot to make communication easier outside of the office, and we use Instacall. Make sure to follow the company page, it’s private."

    #CHOICE
    p "Can I use my personal account or do I need to create an office one?"
    p "(Don’t ask anything)"

    boss "I ask you to use your judgement when making that decision, but please, refer to common sense"

    #CHOICE
    p "Understood"
    p "Do you use your personal account, Sir…? Or you have a private one?"

    boss "Don’t ask about personal things, Miss XXX."

    p "Understood, I’m sorry Sir."
    p "(As he finished talking, a man appeared besides me.)"

    #HANDLING REVIEWS YELLOW

    p "Understood, I’m sorry Sir."
    p "(As he finished talking, a man appeared besides me.)"

    yellow "Good morning Sir, is this the new worker you told me about?"

    boss "Yes, I need you to teach her how we handle reviews and help her adapt. I’m counting on you."

    yellow "Understood"

    p "(Yellow looked at me smiling while the boss left. I’m sure he already has a lot of work to do as they’re short on personnel, so I’m thankful for the help)"

    #CHOICE
    p "A.(Thank him for helping you)"
    p "B. (Don’t say anything, it’s part of his job)"

    #IF A:
    p "Thank you for the help, I know you’re busy"

    #SHOW YELLOW SMILING
    #Sente-se agradecido
    yellow "Don’t mention it, we’re here to help. I’m XXX, by the way, you’re XXO, right?"

    p "Yes (It’s actually wrong but I don’t have the guts to tell him)"
    p "No, it’s actually XXX"

    yellow "Oh, then XXX wrote your name wrong."

    p "(Don’t ask anything)"
    p "XXX?"

    #Frustrated/Worried face
    yellow "One of our workers, she’s prone to these kinds of mistakes. We’ll probably have to go over your badge and other information."

    p "I see... (Maybe that’s why Mr.XXX (BOSS) wrote something on his paper earlier? What a relief, I was dramatizing over nothing. Although this seems like it’s going to be a hard thing to fix. He seems worried)"

    #CHOICE
    p "A. (Maybe I should try to change the subject)"
    p "B. (Maybe I should try to empathize with him)"

    #IF B
    p "Will you have to work overtime?"

    #Smiling
    yellow "Hopefully not. The boss will also help us, so it’s fine."

    #CHOICE
    p "A.(Offer your help)"
    p "B.(Don’t say anything, I’ll only delay them if I try to help)"

    #IF A
    p "You know, since it’s also my problem I’ll be glad to help in what I can."

    yellow "Thank you for thinking about us, but it’s really fine. We’re used to this kind of stuff."

    p "(With a smile like that there’s nothing more I can say. He looks super reassuring."

    #Não gosto desta conversa, é difícil tbh, porque a trama dele não começa logo no início...hm. Hei de escrever isto outra vez.

    #IF ALL A’S AND FINAL OF B
    p "Then, uhm, can we get started?"

    yellow "Yes, let’s."

    #DATA RESEARCH RED

    #CHOICE
    p "Understood, I’m sorry Sir."
    p "(As he finished talking, a man appeared besides me.)"

    red "Good morning, is this the new worker?"

    boss "Yes, I need you to teach her how we handle data research and help her adapt. I’m counting on you."

    red "Got it, boss."

    p "(Red looked at me while the boss left. I’m sure he already has a lot of work to do as they’re short on personnel, so I’m thankful for the help)"

    #CHOICE
    p "A.(Thank him for helping you)"
    p "B. (Don’t say anything, it’s part of his job)"

    #IF A:
    p "Thank you for the help, I know you’re busy"

    #SHOW RED SHRUGGING
    #Tanto lhe faz
    red "It’s just part of the job. You’re XXO, right?"

    #CHOICE
    p "A. Uhm, Yes (It’s actually wrong but I don’t have the guts to tell him)"
    p "B. No, I’m actually XXX"

    #IF B
    #Show him confused
    red "XXX? Not XXO? You sure?"

    p "Uh, yes"
    p "Uh, yes, I’m pretty sure I know my name"

    #Show him frustrated
    red "Then...what? Is the information wrong?"

    p "(I hear him mumbling to himself, he looks scary)"

    #Looks pissed.
    red "Hand me your badge."

    #CHOICE
    p "A. (Hand it over)"
    p "B. (Ask why)"

    #IF B
    p "Wait, why? (He asked it so bluntly it took me aback)"

    #Show him frustrated
    red "Just hand it over, I’m not gonna steal it. I just need to check your name."

    #IF A AND FINAL OF B
    p "Ok then.(Hand it over)"
    p "You could’ve asked more nicely... (Hand it over)"

    #(He looks frustrated at the badge.)
    red "(...)"

    p "(Wow, he totally ignored me)"
    p "(He checks his phone for a second)"

    #Looks pissed
    red "What a real mess...She got your name wrong. They should have fired that girl ages ago."

    #CHOICE
    p "A. Fire who?/Someone’s going to get fired?"
    p "B. Wait, what do you mean?"
    p "C. (Don’t ask anything)"

    #IF A
    red "That’s what you care about? It doesn’t matter, she won’t be here soon. You should be more worried about yourself "

    #CHOICE
    p "A.(Insist)"
    p "B.(Don’t insist)"

    #IF A
    p "Still though, I work here now, I have the right to know"

    red "You’re a real pain, don’t get cocky. Plus someone just wrote another name on your contract and insurance, are you not worried?"

    p "Well, yes, but it can be fixed, I’m sure it was just a mistake, why fire her?"

    #Looks pissed
    red "It can be fixed? It’s not that simple. Plus what do you even know? Don’t meddle into people businesses when you don’t know what you’re talking about"

    p "(Maybe I shouldn’t have insisted, but I was just curious. I don’t believe someone must be fired just over that.)"

    #IF B
    p "Wait, what do you mean?"

    red "Don’t you get it? Someone wrote all of your personal information wrong on the contract, your badge, insurance and what not."

    #CHOICE
    p "So what, it just needs to be fixed"
    p "What? That person should fix it"

    red "Indeed, Miss XXX, she should fix it but I’m sure she has other plans"
    #ou
    red "Indeed, Mr Obvious, she should fix it but I’m sure she has other plans"

    p "(I can feel his sarcasm everywhere. What does he mean by other plans by the way? I don’t want to be jeopardized.)"

    #CHOICE
    p "A.Well, that hasn’t got to do with me, so someone has got to fix it."
    p "B...Then who is going to fix it?"

    p "(I admit I was also dumb not to check my badge properly, but I even signed the contract. How is this possible?)"

    #IF B
    red "Probably our team as always"

    #CHOICE
    p "(As always?)"
    p "Will you work overtime?"

    red "Hopefully not"

    #CHOICE
    p "A.(Offer your help)"
    p "B.(Don’t say anything, I’ll only delay them if I try to help)"

    #IF A
    p "You know, since it’s also my problem I’ll be glad to help in what I can."

    #Sarcastic Smiling
    red "Thank you, miss XXX, but I’m sure we’ll do fine without you"

    p "(Well I tried, but 	he doesn’t seem so mad anymore, so it was for the best)"

    #IF C AND FINAL OF A AND B
    p "(I’m already stressed, what a rough start)"
    p "Ok then, then let’s just start working."






































    p "(looking around) Wow, this place is really fancy for a publishing company. But...I'm kind of lost."

    p "(As I was lost in thoughts someone appeared in front of me)"

    show receptionist 1

    r "Hello, how can i help you?"

    p "Hi, I'm here for my first day at the XXX section of the company"

    r "I see, you're name is XXXX, correct?"

    menu:
        "Y-yes! (It was actually missing a letter but I don't have the courage to tell her that right now...)":
            jump dontTell

        "Yes, that's me! But there's actually one letter missing, it's pronounced as XXYX":
            jump Tell

    label dontTell:

        r "Pleasure to meet you XXXX. Your boss will guide you through the company in a while.
        Just take the elevator to the 4th floor and wait for a bit. Have a good day."
        jump mainStory

    label Tell:

        r "Oh, I'm sorry for that. We'll make sure to fix this error. Nevertheless, you can take
        the elevator to the 4th floor and wait for a bit. Your boss will meet you in a second
        to guide you through the company"

        jump mainStory

    label mainStory:

    p "Thank you"

    scene elevator

    p "..."

    scene wrong floor 1

    p "(I wait for a bit standing up, looking at everyone focused on their work. It's
    been a hot minute and no signs of my boss. Maybe i should return to the reception?"

    p "(As I was starting to walk back to take the elevator, I see someone waving in my
    direction while approaching."

    menu:
        "(wave back)":
            jump Wave

        "What if it's not for me? (ignore)":
            jump dontWave

    label Wave:
        show male friend
        mf "Hello! Are you XXXX?"

        jump mainStory2

    label dontWave:
        show male friend
        mf "Hi there? You completely ignored me..."

        jump mainStory2

    label mainStory2:

    p"..."

    #This ends the game.
    return
