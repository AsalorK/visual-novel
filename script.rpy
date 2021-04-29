# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#000000")
define r = Character("Receptionist", color="#e38e66")
define red = Character("BadBoy", color="#a30000")
define boss = Character("Boss", color="#15044f")
define yellow = Character("Muscle", color="#d1c000")
define mf = Character ("Male Friend")

#por agora fazer só um screen de cada vez. Ou seja, nada de multiple screens
#NADA DE MULTIPLE SCREENS

#o que eu quero:
#dar assign de um botao a uma localização sem ter que enviar por labels ou mandar para outros screens.

# The game starts here.
label start:

    # Show a background.
    scene outside appartment

    # This shows a character sprite.
    #show eileen happy

    # These display lines of dialogue.
    #After arriving at the company:
    p "(Finally arrived at XXX city. I really got lucky landing this job.)"

    p "(I heard the taxi leave as I was about to enter the new apartment, but god damn,
    these suitcases are HEAVY!! What a struggle.)"

    # GO UP THE APARTMENT
    # scene empty apartment
    show screen gotoApartmentArrow
    $ renpy.pause(hard=True)

label Apartment:

    hide screen gotoApartmentArrow
    #hide screen multiple
    scene empty room night


    p "(It looks the same as last time, still empty, but it’s pretty neat for a one bedroom apartment)"
    p "(I layed down the mattress for the night and ate a sandwich thinking about my first day at work tomorrow)"

    scene empty room w mattress night

    p "I really hope I don’t mess it up..."

    # NEXT DAY
    scene empty room w mattress
    define fade = Fade(0.5, 1.0, 0.5)
    with fade
    with hpunch
    with hpunch

    "DRIIIIIIM DRIIIIIIM"

    menu:

        "WHERE AM I?":
            call same

        "Ow,  my head":
            call same

label same:
    p "(I got up as soon as I heard the alarm ring, scared and confused of my whereabouts,
    but quickly remembered I just moved to a new city)"
    p "Why am I so dramatic? I hope i get used used to this place fast"

    p "(With that in mind, I went to the bathroom, took a shower and brushed my teeth)"
    p "(Today was going to be my first day at this publishing company. They were known for
    being old fashioned with their attire, so there wasn’t really much to choose from other than what
    colored suit i should wear)"
    p "Hmm...maybe I’ll wear..."

    #CHOICE
    menu:

        "Black":
            call black
        "Grey":
            call grey
        "Pink":
            call pink
        "Blue":
            call blue
        "Orange":
            call orange

label black:
    p "I’m happy with it, I think black was a great choice!"
    jump continue
label grey:
    p "I’m happy with it, I think grey was a great choice!"
    jump continue
label pink:
    p "I’m happy with it, I think pink was a great choice!"
    jump continue
label blue:
    p "I’m happy with it, I think blue was a great choice!"
    jump continue
label orange:
    p "I’m happy with it, I think orange was a great choice!"
    jump continue

label continue:

    p "Now onto the company, which is...20 MINUTES AWAY? I’VE GOTTA RUN!!!"

    #LEAVE THE APARTMENT AND GO TO THE COMPANY
    #IN FRONT OF THE COMPANY
    show screen gotoOusideApartment
    $ renpy.pause(hard=True)

label OutsideApartment:
    #hide screen multiple2
    hide screen gotoOusideApartment
    scene outside appartment
    #show screen multiple
    show screen gotoCompany
    $ renpy.pause(hard=True)

label Company:
    #hide screen multiple
    #hide screen multiple3
    hide screen gotoCompany
    scene
    scene company entrance

    p "(This must be it, XXX COMPANY. I just arrived but I’m already so tired.
    I need to perk up, gotta look professional)"
    p "Here goes nothing…"

    #ENTER THE COMPANY
    #show screen multiple2
    show screen gotoFrontDesk
    $ renpy.pause(hard=True)

label FrontDesk:
    scene company reception desk
    #hide screen multiple2
    hide screen gotoFrontDesk

    p "(Wow, this place has a really nice atmosphere, and it looks very modern)"
    p "(I look around analyzing the place, looking a bit lost, until i notice the front desk lady coming up to me)"

    #RECEPTIONIST
    show receptionist 1
    r "Hello, how can I help you?"

    #CHOICE
    menu:
        "Hi, I’m here for my first day of work, I’m XXX":
            call nice
        "Hello, you can help me by telling me where to go, you see, I’m new here.":
            call nice
        "Hello, I’m a new worker here, I need my badge and need to know where to go.
        Make it quick please, I’m late.":
            call nice

label nice:

    "Indeed, I see your name on the list. Welcome to the company, here’s your badge."

    #YOU’VE RECEIVED A BADGE, CHECK IT IN YOUR INVENTORY/DESK

    r "Just go up to the 10th floor and enter Mr. XXX office."
    r "Have a good day."

    p "Thank you, you too."

    hide receptionist 1

    p "(Ok, that wasn’t so bad)"
    "(So far so good, now onto the elevator)"
    #USE THE ELEVATOR TO GO UP TO THE 10TH FLOOR
    #show screen multiple3
    show screen gotoElevator
    $ renpy.pause(hard=True)

label Elevator:

    #IN THE ELEVATOR
    scene
    hide screen gotoElevator
    scene elevator

    #p "This is really nice, it has a lot of lights"
    p "(I take a few deep breaths. The nerves came pilling in)"


    #SCREEN SHAKE
    with hpunch
    with vpunch

    p "(As soon as the elevator doors open a large open floor appears in front of me."

    show screen gotoOpenArea
    $ renpy.pause(hard=True)

label OpenArea:
    hide screen gotoOpenArea
    scene open area2
    p "Filled with fancy desks, small decorations and office workers, the atmosphere feels very foreign to me.)"

    p "(Now let’s see...wheres Mr.XXX office)"
    p "(I spot a few offices to my right)"

    #MOVE TO THE OFFICES
    show screen gotoOfficesOutside
    $ renpy.pause(hard=True)

label OfficesDoor:
    hide screen gotoOfficesOutside
    scene office door
    #scene office
    p "(Ok, I’m in front of the office, it’s now or never. I’m so nervous.)"

    #CHOICE
    menu:
        "(But...I don’t have the guts to enter. I’m just going to wait until they notice me)":
            call knockAndWait
        "(Knock on the door and wait)":
            call knockAndWait
        "Knock on the door and enter the office)":
            call knockAndWait

label knockAndWait:
    #ONOMATOPEIA
    p "(I knock on the door a bit nervous)"

    boss "Come in"

    p "(I open the door slowly and enter the office)"

    show screen gotoOffice
    $ renpy.pause(hard=True)

label Office:
    hide screen gotoOffice
    scene
    scene office
    show boss

    #ENTER THE OFFICE
    #MAKE HIM TALK FIRST
    menu:
        "Good morning, I’m- my name’s XXX. Pleasure to meet you. (Oh my god, did i just stutter…?)":
            call continue1
        "Good morning, I’m XXX. PLEASURE TO MEET YOU!!! (Did my voice came out a bit loud?)":
            call continue1
        "Goodmorning,I’mXXX.Pleasuretomeetyou!!! (I think I spoke too fast.)":
            call continue1

label continue1:
    #SHOW BOSS WRITING SOMETHING
    p "(He made a weird face and wrote something on his paper. I’m doomed, oh my god, someone save me)"
    #p "(He made a weird face and wrote something on his paper. This is it, shit’s going down)"
    #p "(He made a weird face and wrote something on his paper. That’s it, I better end my lease, I’m gonna get fired)"
    #SE CALHAR ISTO TÁ UM BOCADO EXAGERADO MAS PRONTO, A IDEIA TÁ LÁ

    boss "Good morning XXX, I’m XXX XXX, welcome to XXX company."

    p "Thank you."

    boss "Please take a seat. This is XXX, he will be starting work today as well,
    I hope both of you get along with the rest of the team and adapt well to the workplace."

    p "(Sitting besides me there was another young man)"

    boss "As both of you may know, XXX (our company) is in the middle of trying to close a
    special deal with a very famous writer, that will guarantee us a partnership with XXX company."

    p "(...)"

    boss "I believe you possess the skills we need to aid us in completing said deal,
    so I hope you don’t prove us wrong"

    p "(This just got really serious...I’m getting chills)"

    boss "With that said I’m going to show you around the office. Follow me."

    p "(...)"

    hide boss

    show screen gotoOfficesOutside2
    $ renpy.pause(hard=True)

    #Follow the BOSS around the office
    #ou deixar que ele nos guie automaticamente?
    #por agora e,e vamos deixar que ele nos guie automaticamente, só pra despachar esta parte
    #OUTSIDE OF THE OFFICE
label explanation:
    hide screen gotoOfficesOutside2
    scene
    scene office door

    show boss
    boss "As you just saw, the offices are in this corner. Because you are still starting,
    you will have to report everything to me at the end of the day, so get used to this place."

    p "(...)"

    scene open area2
    show boss
    boss "Here is the main working area. Please refrain from shouting and keep it professional"

    p "(...)"

    scene personal desk
    show boss
    boss "This is your desk, feel free to personalize it, but don’t paint anything or use damaging tape"

    p "(...)"

    scene breakroom
    show boss
    boss "Right here is the breakroom. You can come here to take a break, drink coffee or eat lunch.
    We don’t have fixed times for lunch so you make your own schedule."
 #(aquela pequena cozinha onde eles almoçam e tal, ver melhor no ANTI P.T.).
    p "(...)"

    scene conference room
    show boss
    boss "Lastly this is the conference room, where the meetings take place."

    scene open area2
    show boss
    boss "Got everything down?"

    menu:
        "Yes, thank you.":
            call continue2
        "No, can you explain one more time, please?":
            jump explanation

    #(...)
label continue2:
    boss "Good. Then you can choose what to start working on today."

    #CHOICE
    p "(Right...I remember they sent an email talking about the things they wanted to test me on.)"
    p "(I think it was)"
    #CHOICE
    menu:
        "It was between handling files and handling data, right, Sir?":
            call rightChoice
        "It was between cleaning the place and helping you, right Sir?":
            call rightChoice
        "It was betewwn handling reviews and data research, right Sir?":
            call rightChoice

label rightChoice:
    boss "Yes, that’s right. Then what do you choose?"

    menu:
        "Handling reviews, Sir.":
            call handlingReviews #yellow
        "Data research, Sir.":
            call dataResearch #red

label handlingReviews:
    #YELLOW
    boss "Understood."

    #SHOW BOSS TEXTING
    p "(As he finished talking I saw him text someone on his phone)"

    #SHOW BOSS LOOKING UP THE PHONE
    p "One last thing, miss XXX. We use our phones a lot to make communication easier outside of the office,
    and we use Instacall. Make sure to follow the company page, it’s private."

    menu:
        "Can I use my personal account or do I need to create an office one?":
            call personalAccount
        "(Don’t ask anything)":
            call personalAccount

label personalAccount:
    boss "I ask you to use your judgement when making that decision, but please, refer to common sense"

    menu:
        "Understood":
            call personalAccount2
        "Do you use your personal account, Sir…? Or you have a private one?":
            call personalAccount2

label personalAccount2:

    boss "Don’t ask about personal things, Miss XXX."

    p "Understood, I’m sorry Sir."
    p "(As he finished talking, a man appeared besides me.)"
    hide boss
    show yellow plus boss

    #HANDLING REVIEWS YELLOW

    yellow "Good morning Sir, is this the new worker you told me about?"

    boss "Yes, I need you to teach her how we handle reviews and help her adapt. I’m counting on you."

    yellow "Understood"

    p "(Yellow looked at me smiling while the boss left. I’m sure he already has a lot of work to
    do as they’re short on personnel, so I’m thankful for the help)"

    show yellow

    #CHOICE
    menu:
        "A.(Thank him for helping you)":
            call thanks
        "B. (Don’t say anything, it’s part of his job)":
            call thanks

    #IF A:
label thanks:
    p "Thank you for the help, I know you’re busy"

    #SHOW YELLOW SMILING
    #Sente-se agradecido
    yellow "Don’t mention it, we’re here to help. I’m XXX, by the way, you’re XXO, right?"

    menu:
        "Yes (It’s actually wrong but I don’t have the guts to tell him)":
            call wrongName
        "No, it’s actually XXX":
            call wrongName

label wrongName:
    yellow "Oh, then XXX wrote your name wrong."

    menu:
        "(Don’t ask anything)":
            call XXX
        "XXX?":
            call XXX

label XXX:
    #Flustered/Worried face
    yellow "One of our workers, she’s prone to these kinds of mistakes. We’ll probably have to
    go over your badge and other information."

    p "I see... (Maybe that’s why Mr.XXX (BOSS) wrote something on his paper earlier? What a
    relief, I was dramatizing over nothing. Although this seems like it’s going to be a hard thing to fix.
    He seems worried)"

    menu:
        "A. (Maybe I should try to change the subject)":
            call empathize
        "B. (Maybe I should try to empathize with him)":
            call empathize

    #IF B
label empathize:
    p "Will you have to work overtime?"

    #Smiling
    yellow "Hopefully not. The boss will also help us, so it’s fine."

    menu:
        "A.(Offer your help)":
            call offerHelp
        "B.(Don’t say anything, I’ll only delay them if I try to help)":
            call offerHelp

    #IF A
label offerHelp:
    p "You know, since it’s also my problem I’ll be glad to help in what I can."

    yellow "Thank you for thinking about us, but it’s really fine. We’re used to this kind of stuff."

    p "(With a smile like that there’s nothing more I can say. He looks super reassuring."

    #Não gosto desta conversa, é difícil tbh, porque a trama dele não começa logo no início...hm.
    #Hei de escrever isto outra vez.

    #IF ALL A’S AND FINAL OF B
    p "Then, uhm, can we get started?"

    yellow "Yes, let’s."

label dataResearch:
    #RED
    boss "Understood."

    #SHOW BOSS TEXTING
    p "(As he finished talking I saw him text someone on his phone)"

    #SHOW BOSS LOOKING UP THE PHONE
    p "One last thing, miss XXX. We use our phones a lot to make communication easier outside of the office,
    and we use Instacall. Make sure to follow the company page, it’s private."

    menu:
        "Can I use my personal account or do I need to create an office one?":
            call personalAccount3
        "(Don’t ask anything)":
            call personalAccount3

label personalAccount3:
    boss "I ask you to use your judgement when making that decision, but please, refer to common sense"

    menu:
        "Understood":
            call personalAccount4
        "Do you use your personal account, Sir…? Or you have a private one?":
            call personalAccount4

label personalAccount4:

    boss "Don’t ask about personal things, Miss XXX."

    p "Understood, I’m sorry Sir."
    p "(As he finished talking, a man appeared besides me.)"
    hide boss
    show red plus boss

    red "Good morning, is this the new worker?"

    boss "Yes, I need you to teach her how we handle data research and help her adapt. I’m counting on you."

    red "Got it, boss."

    p "(Red looked at me while the boss left. I’m sure he already has a lot of work to do as
    they’re short on personnel, so I’m thankful for the help)"

    show red

    #CHOICE
    menu:
        "A.(Thank him for helping you)":
            call thanks2
        "B. (Don’t say anything, it’s part of his job)":
            call thanks2

    #IF A:
label thanks2:
    p "Thank you for the help, I know you’re busy"

    #SHOW RED SHRUGGING
    #Tanto lhe faz
    red "It’s just part of the job. You’re XXO, right?"

    menu:
        "A. Uhm, Yes (It’s actually wrong but I don’t have the guts to tell him)":
            call wrongName2
        "B. No, I’m actually XXX":
            call wrongName2

    #IF B
label wrongName2:
    #Show him confused
    red "XXX? Not XXO? You sure?"

    menu:
        "Uh, yes":
            call yes
        "Uh, yes, I’m pretty sure I know my name":
            call yes

label yes:
    #Show him frustrated
    red "Then...what? Is the information wrong?"

    p "(I hear him mumbling to himself, he looks scary)"

    #Looks pissed.
    red "Hand me your badge."

    menu:
        "A. (Hand it over)":
            call handBadge
        "B. (Ask why)":
            call why

    #IF B
label why:
    p "Wait, why? (He asked it so bluntly it took me aback)"

    #Show him frustrated
    red "Just hand it over, I’m not gonna steal it. I just need to check your name."

    #IF A AND FINAL OF B
    menu:
        "Ok then.(Hand it over)":
            call handBadge
        "You could’ve asked more nicely... (Hand it over)":
            call handBadgeMad

label handBadge:
    red "(...)"

    p "(He checks his phone for a second)"

    #Looks pissed
    red "What a real mess...She got your name wrong. They should have fired that girl ages ago."

    jump common

label handBadgeMad:
    #(He looks frustrated at the badge.)
    red "(...)"

    p "(Wow, he totally ignored me)"
    p "(He checks his phone for a second)"

    #Looks pissed
    red "What a real mess...She got your name wrong. They should have fired that girl ages ago."

label common:
    menu:
        "A. Fire who?/Someone’s going to get fired?":
            call fireWho
        "B. Wait, what do you mean?":
            call waitWhat
        "C. (Don’t ask anything)":
            call dontAsk

    #IF A
label fireWho:
    red "That’s what you care about? It doesn’t matter, she won’t be here soon.
    You should be more worried about yourself"

    menu:
        "A.(Insist)":
            call insist
        "B.(Don’t insist)"

    #IF A
label insist:
    p "Still though, I work here now, I have the right to know"

    red "You’re a real pain, don’t get cocky. Plus someone just wrote another name on your
    contract and insurance, are you not worried?"

    p "Well, yes, but it can be fixed, I’m sure it was just a mistake, why fire her?"

    #Looks pissed
    red "It can be fixed? It’s not that simple. Plus what do you even know? Don’t meddle
    into people businesses when you don’t know what you’re talking about"

    p "(Maybe I shouldn’t have insisted, but I was just curious. I don’t believe someone must
    be fired just over that.)"

    #IF B
label waitWhat:
    p "Wait, what do you mean?"

    red "Don’t you get it? Someone wrote all of your personal information wrong on the contract,
    your badge, insurance and what not."

    menu:
        "So what, it just needs to be fixed":
            call worried
        "What? That person should fix it":
            call worried

label worried:
    red "Indeed, Mr Obvious, she should fix it but I’m sure she has other plans"

    p "(I can feel his sarcasm everywhere. What does he mean by other plans by the way?
    I don’t want to be jeopardized.)"

    menu:
        "A.Well, that hasn’t got to do with me, she has got to fix it."
        "B...Then who is going to fix it?"
        "(I admit I was also dumb not to check my badge properly, but I even signed the contract.
        How is this possible?)":
            call whoWillFix

label whoWillFix:
    #IF B
    red "Probably our team as always"

    #CHOICE
    p "(As always?)"
    p "Will you work overtime?"

    red "Hopefully not"

    #CHOICE
    menu:
        "A.(Offer your help)":
            call offerHelp2
        "B.(Don’t say anything, I’ll only delay them if I try to help)":
            call offerHelp2

label offerHelp2:
    #IF A
    p "You know, since it’s also my problem I’ll be glad to help in what I can."

    #Sarcastic Smiling
    red "Thank you, miss XXX, but I’m sure we’ll do fine without you"

    p "(Well I tried, but 	he doesn’t seem so mad anymore, so it was for the best)"

    #IF C AND FINAL OF A AND B
    p "(I’m already stressed, what a rough start)"

label dontAsk:
    p "Ok then, then let’s just start working."


    #This ends the game.
    return
