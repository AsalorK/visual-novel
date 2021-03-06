# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#115610")
define r = Character("Receptionist", color="#e38e66")
define red = Character("BadBoy", color="#a30000")
define boss = Character("Boss", color="#15044f")
define yellow = Character("Muscle", color="#d1c000")
define mf = Character ("Male Friend")
define gui.text_size = 28
define gui.textbox_height = 200
#https://www.youtube.com/c/HypnagogiXGaming/abouts
#HypnagogiX Gaming -> senhor dos tutoriais
#por agora fazer só um screen de cada vez. Ou seja, nada de multiple screens
#NADA DE MULTIPLE SCREENS

#o que eu quero:
#dar assign de um botao a uma localização sem ter que enviar por labels ou mandar para outros screens.
#será que posso criar mais labels com variáveis, e assim que passar uma parte chama-las em vez de chamar as primeiras? assim posso criar novos booleans,
# em vez de utilizar os mesmos ou ter de criar ints? idk...acho que posso continuar a utilizar estes tho. Tenho de experimentar quq

# The game starts here.
label start:
    call Variables from _call_Variables

    jump Apartment

label Variables:

    $ firstStart = True
    $ firstTimeApartment = True
    $ firstTimeCompany = True
    $ firstTimeFrontDesk = True
    $ firstTimeElevator = True
    $ firstTimeOpenArea = True
    $ firstTimeOfficesDoor = True
    $ firstTimeOffice = True
    $ firstTimeHandlingReviews = True
    $ firstTimeHandlingReviews = True

label OutsideApartment:

    scene outside appartment

if firstStart == True:

    p "Finally arrived at my new place. I really got lucky landing an apartment near the company."

    p "(I heard the taxi leave as I was about to open the door.)"

    $ firstStart = False

    # GO UP THE APARTMENT
    # scene empty apartment
    show screen gotoApartmentArrow
    $ renpy.pause(hard=True)

else:
    show screen Apartment_Company1
    hide screen OutsideApartment_FrontDesk1
    hide screen gotoOusideApartment
    $ renpy.pause(hard=True)

label Apartment:

    hide screen gotoApartmentArrow
    #hide screen Apartment_Company1
    scene empty room night

if firstTimeApartment == True:

    p "Oh my god, finally...I thought I was going to die, the suitcases are so heavy!!"
    p "(The place looks the same as last time, still empty, but it’s pretty neat for a one bedroom apartment)"
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
            call same from _call_same

        "Ow,  my head":
            call same from _call_same_1

    $ firstTimeApartment = False

    show screen gotoOusideApartment
    hide screen Apartment_Company1
    hide screen OutsideApartment_FrontDesk1
    $ renpy.pause(hard=True)

else:
    show screen gotoOusideApartment
    scene empty room w mattress
    hide screen Apartment_Company1
    hide screen OutsideApartment_FrontDesk1
    $ renpy.pause(hard=True)

label same:
    p "(I got up as soon as I heard the alarm ring, scared and confused of my whereabouts,
    but quickly remembered I just moved to a new place)"
    p "Why am I so dramatic? I hope i get used used to this house pretty fast"

    p "(I went to the bathroom, took a shower and brushed my teeth, thinking about my day)"
    p "(Today was going to be my first day at this publishing company. They were known for
    being old fashioned with their attire, so there wasn’t really much to choose from other than what
    colored suit i should wear)"
    p "Hmm...maybe I’ll wear..."

    #CHOICE
    menu:

        "Black":
            jump black
        "Grey":
            jump grey
        "Pink":
            jump pink
        "Blue":
            jump blue
        "Orange":
            jump orange

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
    return

label Company:
    hide screen Apartment_Company1
    hide screen Company_Elevator1
    hide screen gotoCompany
    scene
    scene company entrance

if firstTimeCompany == True:

    p "(This must be it, XX PUBLISHING COMPANY.)"
    p "(I just arrived but I’m already so tired from all the running. I need to perk up, gotta look professional)"
    p "Here goes nothing…"

    $ firstTimeCompany = False

    show screen OutsideApartment_FrontDesk1
    #show screen gotoFrontDesk
    $ renpy.pause(hard=True)

else:
    hide screen FrontDesk_OpenArea1
    hide screen Apartment_Company1
    show screen OutsideApartment_FrontDesk1
    $ renpy.pause(hard=True)



label FrontDesk:
    scene company reception desk
    hide screen OutsideApartment_FrontDesk1
    hide screen gotoFrontDesk

if firstTimeFrontDesk == True:

    p "(It looks even more spacious from the inside, and the decorations are very modern looking)"
    p "(I keep looking around looking a bit lost, until i notice the front desk lady coming up to me)"

    #RECEPTIONIST
    show receptionist 1
    r "Hello, how can I help you?"

    #CHOICE
    menu:
        "Hi, I’m here for my first day of work, I’m XXX":
            call nice from _call_nice
        "Hello, I’m a new worker here, I need my badge and need to know where to go.
        Make it quick please, I’m late.":
            call mean from _call_mean

    $ firstTimeFrontDesk = False

    #USE THE ELEVATOR TO GO UP TO THE 10TH FLOOR
    show screen Company_Elevator1
    #show screen gotoElevator
    $ renpy.pause(hard=True)

else:
    hide screen Elevator_Offices1
    hide screen FrontDesk_OpenArea1
    show screen Company_Elevator1
    #show screen gotoElevator
    $ renpy.pause(hard=True)

label nice:

    r "Hello, pleasure to meet you. You said your name was XXX?"
    p "(I see her frowning a bit) Yes, that's correct."
    r "Can you confirm your security ID number?"
    p "Yes, sure. It's ----------"
    r "That's correct. Then welcome to the companys, here’s your badge. Don't wear it right away, please."
    p "Thank you. (I receive my badge and briefly look at it before putting it away)"
    #YOU’VE RECEIVED A BADGE, CHECK IT IN YOUR INVENTORY/DESK
    r "Just go up to the 10th floor and enter Mr. Kim's office, have a good day."
    p "Thank you, you too."

    hide receptionist 1

    p "(Ok, that wasn’t so bad)"
    p "(So far so good, now onto the elevator)"
    return

label mean:
    r "... OK so what's your name?"
    p "My name's XXX"
    r "Can you confirm your security ID number?"
    p "Uh, Sure... It's ----------"
    r "Ok, it matches. Take your badge but don't wear it right away please."
    p "(I receive my badge and briefly look at it before putting it away)"
    #YOU’VE RECEIVED A BADGE, CHECK IT IN YOUR INVENTORY/DESK
    r "Just go up to the 10th floor and enter Mr. Kim's office."
    p "Ok, thank you."

    hide receptionist 1

    p "(I don't have time to lose)"
    p "(Gotta find the elevator!)"
    return

label Elevator:

    #IN THE ELEVATOR
    scene
    hide screen Company_Elevator1
    hide screen gotoElevator
    scene elevator

if firstTimeElevator == True:
    #p "This is really nice, it has a lot of lights"
    p "(I take a few deep breaths as the nerves come pilling in)"

    #SCREEN SHAKE
    with hpunch
    with vpunch

    p "(As soon as the elevator doors open a large open floor appears in front of me."

    $ firstTimeElevator = False
    show screen FrontDesk_OpenArea1
    $ renpy.pause(hard=True)

else:
    hide screen Elevator_Offices1
    show screen FrontDesk_OpenArea1
    $ renpy.pause(hard=True)

label OpenArea:
    hide screen FrontDesk_OpenArea1
    scene open area2
if firstTimeOpenArea == True:

    p "(Filled with fancy desks, small decorations and office workers, the atmosphere feels very foreign to me.)"
    p "Now let’s see...where's Mr.Kim's office?"
    p "(I spot a few offices to my right)"

    $ firstTimeOpenArea = False
    show screen Elevator_Offices1
    $ renpy.pause(hard=True)

else:
    #MOVE TO THE OFFICES
    hide screen OpenArea_Office1
    show screen Elevator_Offices1
    $ renpy.pause(hard=True)

label OfficesDoor:
    hide screen Elevator_Offices1
    hide screen gotoOfficesOutside
    scene office door

if firstTimeOfficesDoor == True:

    p "(Ok, I’m here, it’s now or never. I’m so nervous.)"
    #CHOICE
    menu:
        #"(But...I don’t have the guts to enter. I’m just going to wait until someone notices me)":
            #call knockAndWait
        "(Knock on the door and wait)":
            call knockAndWait from _call_knockAndWait
        "Knock on the door and enter the office)":
            call knockAndEnter from _call_knockAndEnter

    $ firstTimeOfficesDoor = False
    show screen OpenArea_Office1
    $ renpy.pause(hard=True)
else:
    show screen OpenArea_Office1
    hide screen gotoOfficesOutside2
    $ renpy.pause(hard=True)

label knockAndEnter:
    p "(I knock on the door and enter the office right away)"

    jump Office

label knockAndWait:
    #ONOMATOPEIA
    p "(I knock on the door a bit nervous)"

    boss "Come in"
    return


label Office:
    hide screen OpenArea_Office1
    scene
    scene office
    show boss

if firstTimeOffice == True:

    #MAKE HIM TALK FIRST
    menu:
        "Good morning, I’m- my name’s XXX. Pleasure to meet you. (Oh my god, did i just stutter…?)":
            call continue1 from _call_continue1
        "Good morning, I’m XXX. PLEASURE TO MEET YOU!!! (Did my voice came out a bit loud?)":
            call continue1 from _call_continue1_1
        "Goodmorning,I’mXXX.Pleasuretomeetyou!!! (I think I spoke too fast.)":
            call continue1 from _call_continue1_2

    $ firstTimeOffice = False
    hide boss
    show screen gotoOfficesOutside
    $ renpy.pause(hard=True)

else:
    hide boss
    show screen gotoOfficesOutside2
    $ renpy.pause(hard=True)

label continue1:
    #SHOW BOSS WRITING SOMETHING
    p "(He made a weird face and wrote something on his paper. I’m doomed, oh my god, someone save me)"
    #p "(He made a weird face and wrote something on his paper. This is it, shit’s going down)"
    #p "(He made a weird face and wrote something on his paper. That’s it, I better end my lease, I’m gonna get fired)"
    #SE CALHAR ISTO TÁ UM BOCADO EXAGERADO MAS PRONTO, A IDEIA TÁ LÁ

    boss "Good morning XXX, I’m Mr.Kim, welcome to our company."

    p "Thank you."

    boss "Please take a seat."

    p "(I sit down on one of the chairs.)"

    boss "As you may know, our company is in the middle of trying to close a
    special deal with a very famous writer, that will guarantee us a partnership with a movie director."

    p "(...)"

    boss "I believe you possess the skills we need to aid us in completing said deal,
    so I hope you don’t prove us wrong."

    p "(Maybe I should have just applied as an editor, this seems harder than i thought.)"

    p "I'll do my best, sir."

    boss "I'm glad."

    boss "Follow me. I’m going to show you around the office."

    #p "(...)"
    return


    #Follow the BOSS around the office
    #ou deixar que ele nos guie automaticamente?


    #por agora e,e vamos deixar que ele nos guie automaticamente, só pra despachar esta parte
    #OUTSIDE OF THE OFFICE

label explanation:
    hide screen gotoOfficesOutside
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
            call continue2 from _call_continue2
        "No, can you explain one more time, please?":
            jump explanation

    # (...)
label continue2:
    boss "Good. Then you can choose what to start working on today."

    #CHOICE
    p "(Right...I remember they sent an email talking about the things they wanted to test me on.)"
    p "(I think it was)"
    #CHOICE
    menu:
        "It was between handling files and handling data, right, Sir?":
            call wrongChoice from _call_wrongChoice
        "It was between cleaning the place and helping you, right Sir?":
            call wrongChoice from _call_wrongChoice_1
        "It was between handling reviews and data research, right Sir?":
            call rightChoice from _call_rightChoice

label wrongChoice:

    p "(He's making a weird face, oh no)"

    boss "I hope pay more attention to the emails we send you from now on."

    p "Yes, I'm sorry... (Can't believe I'm already messing up)"

    boss "I'll ignore this mistake. Between handing reviews and doing data research, what do you prefer?"

    jump choice

label rightChoice:
    boss "Yes, that’s right. Then what do you choose?"

    jump choice

label choice:

    menu:
        "Handling reviews, Sir.":
            jump handlingReviews #yellow
        "Data research, Sir.":
            jump dataResearch #red

label handlingReviews:
    #YELLOW
    scene
    scene open area2

if firstTimeHandlingReviews == True:

    show boss
    boss "Understood."

    #SHOW BOSS TEXTING
    p "(As he finished talking I saw him text someone on his phone)"

    #SHOW BOSS LOOKING UP THE PHONE
    p "One last thing, miss XXX. We use our phones a lot to make communication easier outside of the office,
    and we use Instacall. Make sure to follow the company page, it’s private."

    menu:
        "Can I use my personal account or do I need to create an office one?":
            call personalAccount from _call_personalAccount
        "(Don’t ask anything)":
            call yellow from _call_yellow

    $ firstTimeHandlingReviews = False
    hide yellow
    show screen Elevator_Offices1
    $ renpy.pause(hard=True)
else:
    show screen Elevator_Offices1
    $ renpy.pause(hard=True)

label personalAccount:
    boss "I ask you to use your judgement when making that decision, but please, refer to common sense"

    menu:
        "Understood":
            jump yellow
        "Do you use your personal account, Sir…? Or you have a private one?":
            jump personalAccount2

label personalAccount2:

    boss "Don’t ask about personal things, Miss XXX."

    p "Understood, I’m sorry Sir."
    jump yellow

label yellow:

    p "(As he finished talking, a man appeared besides me.)"

    hide boss
    show yellow plus boss

    #HANDLING REVIEWS YELLOW

    yellow "Good morning Sir, is this the new worker you told me about?"

    boss "Yes, I need you to teach her how we handle reviews and help her adapt. I’m counting on you."

    yellow "Okay."

    p "(He looked at me smiling while the boss left. I’m sure he already has a lot of work to
    do as they’re short on personnel, so I’m thankful for the help)"

    show yellow

    #CHOICE
    menu:
        "A.(Thank him for helping you)":
            jump thanks
        "B. (Don’t say anything, it’s part of his job)":
            jump nothing

    #IF A:
label thanks:
    p "Thank you for the help, I know you’re busy"

    #SHOW YELLOW SMILING
    #Sente-se agradecido
    yellow "Don’t mention it, we’re here to help. I’m XXX, by the way, you’re XXO, right?"
    jump name

label nothing:
    yellow "Hello, I'm XXX, you're XXO, right?"

    jump name

label name:
    #menu:
        #"Yes (It’s actually wrong but I don’t have the guts to tell him)":
            #jump rigthname
    p "No, it’s actually XXX"

    jump wrongName

label wrongName:
    yellow "Oh, then Melanie wrote your name wrong."

    #menu:
        #"(Don’t ask anything)":
            #jump finishconversation
    p "Melanie?"

    jump XXX

label XXX:
    #Flustered/Worried face
    yellow "A colleague, she’s prone to these kinds of mistakes. We’ll probably have to
    go over your badge and other information."

    p "I see... (That sounds complicated)"

    menu:
        "A. (Maybe I should try to change the subject)":
            jump finishconversation
        "B. (Maybe I should try to empathize with him)":
            jump empathize

    #IF B
label empathize:
    p "Will you have to work overtime?"

    #Smiling
    yellow "Hopefully not. The boss will also help us, so it’s fine."

    menu:
        "A.(Offer your help)":
            jump offerHelp
        "B.(Don’t say anything, I’ll only delay them if I try to help)":
            jump finishconversation

    #IF A
label offerHelp:
    p "You know, since it’s also my problem I’ll be glad to help in what I can."

    yellow "Thank you for thinking about us, but it’s really fine. We’re used to this kind of stuff."

    p "(With a smile like that there’s nothing more I can say. He looks super reassuring."

    #Não gosto desta conversa, é difícil tbh, porque a trama dele não começa logo no início...hm.
    #Hei de escrever isto outra vez.
label finishconversation:
    #IF ALL A’S AND FINAL OF B
    p "Then, uhm, can we get started?"

    yellow "Yes, let’s."

    "DEMO IS OVER"
    return


label dataResearch:
    #RED
    scene
    scene open area2
    show boss
if firstTimeHandlingReviews == True:

    boss "Understood."

    #SHOW BOSS TEXTING
    p "(As he finished talking I saw him text someone on his phone)"

    #SHOW BOSS LOOKING UP THE PHONE
    p "One last thing, miss XXX. We use our phones a lot to make communication easier outside of the office,
    and we use Instacall. Make sure to follow the company page, it’s private."

    menu:
        "Can I use my personal account or do I need to create an office one?":
            call personalAccount3 from _call_personalAccount3
        "(Don’t ask anything)":
            call red from _call_red

    $ firstTimeHandlingReviews = False
    hide red
    show screen Elevator_Offices1
    $ renpy.pause(hard=True)
else:
    show screen Elevator_Offices1
    $ renpy.pause(hard=True)

label personalAccount3:
    boss "I ask you to use your judgement when making that decision, but please, refer to common sense"

    menu:
        "Understood":
            jump red
        "Do you use your personal account, Sir…? Or you have a private one?":
            jump personalAccount4

label personalAccount4:

    boss "Don’t ask about personal things, Miss XXX."

    p "Understood, I’m sorry Sir."

    jump red

label red:
    p "(As he finished talking, a man appeared besides me.)"
    hide boss
    show red plus boss

    red "Good morning, is this the new worker?"

    boss "Yes, I need you to teach her how we handle data research and help her adapt. I’m counting on you."

    red "Got it, boss."

    p "(He looked at me while the boss left. I’m sure he already has a lot of work to do as
    they’re short on personnel, so I’m thankful for the help)"

    show red

    #CHOICE
    menu:
        "A.(Thank him for helping you)":
            jump thanks2
        "B. (Don’t say anything)":
            jump nothing2

    #IF A:

label nothing2:

    red "Your name's XXO, right?"
    jump name2

label thanks2:
    p "Thank you for the help, I know you’re busy"

    #SHOW RED SHRUGGING
    #Tanto lhe faz
    red "It’s just part of the job. You’re XXO, right?"
    jump name2

label name2:
    #menu:
        #"A. Uhm, Yes (It’s actually wrong but I don’t have the guts to tell him)":
        #    jump wrongName2
    p "No, I’m actually XXX."
    jump wrongName2

    #IF B
label wrongName2:
    #Show him confused
    red "XXX? Not XXO? You sure?"

    menu:
        "Uh, yes":
            jump yes
        "Uh, yes, I’m pretty sure I know my name":
            jump yes

label yes:
    #Show him frustrated
    red "Then...what? Is the information wrong?"

    p "(I hear him mumbling to himself, he looks scary)"

    #Looks pissed.
    red "Hand me your badge."

    menu:
        "A. (Hand it over)":
            jump handBadge
        "B. (Ask why)":
            jump why

    #IF B
label why:
    p "Wait, why? (He asked it so bluntly it took me aback)"

    #Show him frustrated
    red "Just hand it over, I’m not gonna steal it. I just need to check your name."

    #IF A AND FINAL OF B
    menu:
        "Ok then.(Hand it over)":
            jump handBadge
        "You could’ve asked more nicely... (Hand it over)":
            jump handBadgeMad

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
        "A. Fire who?":
            jump fireWho
        "B. Wait, what do you mean?":
            jump waitWhat
        "C. (Don’t ask anything)":
            jump dontAsk

    #IF A
label fireWho:
    #red "That’s what you care about? It doesn’t matter, she won’t be here soon.
    #You should be more worried about yourself"
    red "It doesn't matter."

    menu:
        "A.(Insist)":
            jump insist
        "B.(Don’t insist)":
            jump dontInsist
    #IF A
label insist:
    p "Still though, I work here now, I have the right to know"

    red "You’re a real pain, don’t get cocky. It's not important who did it. Someone just wrote another name on your
    contract and insurance, are you not worried?"

    p "Well, yes, but it can be fixed, I’m sure it was just a mistake, why fire her?"

    #Looks pissed
    red "It can be fixed? It’s not that simple. Plus what do you even know? Don’t meddle
    into people businesses when you don’t know what you’re talking about"

    p "(Maybe I shouldn’t have insisted, but I was just curious. I don’t believe someone must
    be fired just over that.)"
    jump stress

    #IF B
label dontInsist:
    p "Then what is happening?"
    jump redExplains

label waitWhat:
    p "Wait, what do you mean?"
    jump redExplains

label redExplains:
    red "Don’t you get it? Someone wrote all of your personal information wrong on the contract,
    your badge, insurance and what not."

    #menu:
        #"So what, it just needs to be fixed":
            #jump worried
    p "What? That person should fix it!!"
    jump worried

label worried:
    red "Indeed, Mr Obvious, she should fix it but I’m sure she has other plans."

    p "(I can feel his sarcasm everywhere. What does he mean by other plans by the way?
    I don’t want to be jeopardized.)"

    #menu:
        #"A.Well, that hasn’t got to do with me, she has got to fix it.":
            #jump whoWillFix
    p"...Then who is going to fix it?"
    jump whoWillFix
    #"(I admit I was also dumb not to check my badge properly, but I even signed the contract.
    #How is this possible?)"
label whoWillFix:
    #IF B
    #p "(I admit I was also dumb not to check my badge properly, but I even signed the contract.
    #How is this possible?)"
    red "Probably our team as always."

    #CHOICE
    p "(As always?)"
    p "Will you work overtime?"

    red "Hopefully not"

    #CHOICE
    menu:
        "A.(Offer your help)":
            jump offerHelp2
        "B.(Don’t say anything, I’ll only delay them if I try to help)":
            jump stress

label offerHelp2:
    #IF A
    p "You know, since it’s also my problem I’ll be glad to help in what I can."

    #Sarcastic Smiling
    red "Thank you, miss XXX, but I’m sure we’ll do fine without you"

    p "(Well I tried, but 	he doesn’t seem so mad anymore, so it was for the best)"
    jump dontAsk

label stress:
    #IF C AND FINAL OF A AND B
    p "(Whatever though, I’m already stressed, what a rough start)"
    jump dontAsk

label dontAsk:
    p "Ok then, then let’s just start working."
    #This ends the game.
    "DEMO IS OVER"
    return
