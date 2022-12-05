# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character('HER', color="#FADA49")
define n = Character("[narrator_name]", color="#FFFFFF")
define b = Character('CHARCOAL_GASOLINE', color='#A55CF8')
define r = Character('SUNNY_OAK', color='#F85CEE')
define d = Character('YOUNG_GREMLIN', color='#F52F2F')

define pov = Character("[povname]", color="#FFFFFF")
define placeholder = Character("YOU")

label start:
    scene black
    python:
        narrator_name = "THE STORYTELLER"

    play music "audio/atmospheric-cinematic-soundscape.mp3"

    n "Many years have passed since I was released. It was golden."

    n "..."

    n "We used to joke that we were not ever born. We were put upon this earth, our hands always in the dirt."
    #show a photo of them as kids and put it as the "background", this way you can tell the story

    n "I am starting to think there was more truth there than we ever admitted."

    n "Life went by deceptively fast, yet every moment was agony in that accursed house. Built by madmen to cage and imprison, I thought."

    n "So every moment we could escape from it, we would."

    n "We ran in the cornfields, zig-zagging away from our lives, pretending we could forge something new in the maze."
    n "But when the fog cleared and the animals scattered, we were left with dust in our lungs and blood on our hands."
    n "Was something else stuck in our lungs?" 
    n "Indeed, we coughed up the flowers, like a poison to our sensitive bed-ridden bodies."
    #it was winter when I got sick. something with seasonal depression could be the flower dying in winter

    n "Do you really want to know what happened?"
    
menu:
    "Take me back to safety.": 
        jump safety

    "I have always liked a risk.":
        jump begin

label begin: 
    placeholder "I want to continue. I'm brave."
    n "If that is what you wish, then let me tell you a story."
    jump story_begin


label safety: 
    placeholder "Take me back. I don't want this."
    n "I can't blame you for that. But you opened this game. There is no choice. Only lies."
    jump story_begin

label story_begin: 
    n "I shall remind you, you can shut this game now."
    n "No? You will not leave?"
    n "Okay."
    n "But first, I need to know your name."
    
    python:
        povname = renpy.input("Please enter your name.")
        povname = povname.strip()

        if not povname:
            povname = "UNNAMED"

    pov "My name is [povname]."

    n "Thank you. It is much easier to talk to someone who feels human."
    stop music 
    with fade
    

label scene_one:
    scene static_tv
    with dissolve
    play music "audio/white-noise.mp3"
    #"Day liked to lie."
    n "You may ask me one question to start."

menu:
    "What do you mean you were never born?":
        jump scene_one_choice_one

    "What is your name?":
        jump scene_one_choice_two

    "Tell me a joke.":
        jump scene_one_choice_three

label scene_one_choice_one:
    pov "You... weren't born?"
    n "Normally you are born from your mother. I was surgically removed."
    n "As such, I was never born, I was released. That's what we used to say, anyway. Another joke from a long-forgotten time."
    jump scene_one_after_choice

label scene_one_choice_two:
    pov "What's your name?"
    n "You would like to know my name?"
    n "You don't know me. Do you wish to? I am here for one purpose: to tell my story."
    n "But since you did ask... it is Dean."
    python:
        narrator_name = "DEAN"
    jump scene_one_after_choice

label scene_one_choice_three: 
    pov "Can you tell me a joke?"
    n "Are you afraid? There is no reason to fear me."
    n "But, here is a joke:"
    n "What did one trash can say to the other?"
    n "You stink."
    n "Haha. Ha. Ha."
    jump scene_one_after_choice

label scene_one_after_choice:
    n "Now that you have asked your question, I shall begin."
    n "I can never figure out where to start my recounting... I suppose any time will do."

label scene_two_open:
    stop music 
    play music "audio/twinkle.mp3"
    scene bedroom
    n "We often play together in this room. We come up with worlds in which to live, stories fascinating to us but mundane to an outsider. It was a golden childhood- perfect from the outside. We were as good as we could be."
    n "This is where many of our days are spent. Of course, SHE does not like it very much. SHE says it isn't good for us. But that never stops us."
    show large b
    b "Wait! I want to be the fox this time!"
    n "That's my brother. A strong person, always willing to stick up for me. But he's only a kid."
    hide large b
    show dean gen
    d "Okay, then I get to be the swordsman!"
    n "That's me, when I was younger. You will be following me and my memories, with some differences depending on what I ask you."
    n "I may use WE to refer to us, or I to refer to younger me." 
    hide dean gen
    show r char mid
    r "*in a whining voice* But I've been the magician the past three times, that's not fair."
    n "And that is my silbing. They are the kindest person I have ever met. They will forever be there to listen to you and comfort you."
    hide r char mid
    show dean gen
    d "Well-"
    hide dean gen
    show dean gen at left 
    show large b at right
    show r char mid 
    play sound "audio/knock.mp3"
    "... the children are silent."
    stop sound
    scene HER
    play sound "audio/white-noise.mp3"
    pause 0.1
    stop sound
    scene bedroom
    hide r char mid 
    hide dean gen
    hide large b
    show gen her
    h "Hello children! You all seem to be having fun."
    hide gen her
    show r char mid
    r "We are!!"
    hide r char mid
    show gen her
    play sound "audio/pleasing_laugh.mp3"
    h "I'm so glad to hear that!"
    h "I was going to make some cookies. Would anyone like to help me?"
    n "What do you say? What should we do?"

menu: 
    "I love making cookies.":
        jump cookies
    "I'm good.":
        jump no_cookies

label cookies:
    n "You follow HER to the kitchen."
    scene kitchen
    n "She smiles and puts on an apron. There are clean bowls out and various ingredients. Your head barely reaches the tall counter, but you love watching HER make things."
    n "You don't know what you're doing, but it's fun to learn." 
    show gen her
    h "Can you measure the flour for me, please?"
    hide gen her
    d "Sure!"
    n "How much should we put in?"
menu:
    "2 1/2 cups.":
        jump wrong_choice
    "1 cup.":
        jump wrong_choice
    "I have no idea. Throw some in.":
        jump wrong_choice
    "Touch the flour. Eat the flour.":
        jump wrong_choice_2
label wrong_choice: 
    n "You didn't pick the right choice."
    n "But actually, none of those options were right."
    n "At least you didn't eat it."
    n "That's how these things go - you never get it right. You never do what you're supposed to. You mess everything up. How could you?"
    show gen her
    h "Thank you, sweetie." 
    hide gen her
    n "She doesn't notice. Once she puts them in the oven, though, and they come out looking wrong, she freaks out. You have the strong urge to run and hide." 
    n "If you hide, she cannot hurt you."
    show gen her
    h "What's wrong with these? God, I mess everything up! Why did I even do this! What was the point!?"
    n "You are silent, flinching back at the words. You don't really know what's happening."
    h "Damn it! They're not RIGHT! I told you I can't do this anymore! I seriously can't. Just go." 
    hide gen her 
    n "You go back upstairs, in the room where everything feels safe-- where you can throw away hours of your life without feeling pain anymore."
    scene bedroom
    n "..."
    n "It will be better in the morning. That's what we tell ourselves. But it's a lie, it's always been a lie. It's just the only thing we have left."
    jump after_cookies
label wrong_choice_2: 
    n "Now why on EARTH would you eat it? Oh, well."
    n "You eat the flour, unaware of what e. coli is."
    n "It's salty, with a velvety texture that turns gross when your saliva mixes with it."
    n "Unluckily for you, you spill it down your shirt and on the table, so after you gulp down the powder, SHE sees."
    show gen her
    h "No! You can't eat that! Spit it out!"
    n "..."
    h "It's already gone? Damn it. Just go upstairs. I can finish by myself. Did you even put any flour in?"
    n "You shake your head no."
    h "Great. Just go have fun, I'll get this done. But if you get sick, it's your fault." 
    hide gen her 
    n "You go back upstairs, where the others are playing. You gradually forget the incident, enjoying the time with them."
    scene bedroom
    jump after_cookies

label no_cookies:
    n "You do not make cookies."
    n "She seems irritated, but she shuts the door. You can hear her footsteps down the stairs as she goes to the kitchen."
    n "She doesn't say anything to you, but when you go down for a snack, she is still mad."
    scene kitchen
    show dean gen
    d "I'm hungry."
    hide dean gen
    show gen her
    h "You wouldn't be if you'd made cookies with me. And what are you even doing up there that's so much fun? You're always on those computers. It's disturbing. I wish to HELL I never gave those to you. They're ruining your lives."
    h "You know how dangerous those are? You know how many pedophiles there are? I bet you're talking to them. Don't give them your address."
    n "She laughs a little, like any of this is funny."
    hide gen her 
    scene bedroom
    n "You don't know what to say, so you just go back upstairs. You ignore the sick feeling in your stomach and play your games, the only exit from the place you've adapted to living in. Your personal hell."
    jump after_cookies

label after_cookies:
    stop music
    scene black
    n "This is an example of one of many mundane days in our lives. It only got worse as we aged. When we could comprehend our problems, they became harder to manage."
    n "Even still our brains are hiding some of the memories. We are not safe, we have simply adapted."
    #n "A thousand apologies if you can resonate with these words."
    n "SHE got worse with time. In fact, SHE"
    play sound "audio/break.mp3"
    scene static_tv
    pause 0.01 
    scene black
    "B R O K E."



label soft_crying: 
    n "When I got older, more happened. Or maybe I could finally understand it."
    n "This is one of those times."
    play sound "audio/cryingF.mp3"
    n "I heard something from my room and went downstairs to find the source of the noise." #choice??
    scene dark_kitchen
    n "SHE is sitting in the kitchen, the dim light shining on her wet face. Her hands are pulling her hair, as if to rip it out in clumps."
    h "*softly, muttering to herself* You ruined everything... you made me do this. You made me suffer. What did I do to fail you so spectacularly?"
    h "I failed her. I failed her, I failed her, I failed her, I FAILED HER, I FAILED HER, I FAILED HER I FAILED HER I FAILED HER I FAILED HER-"
    stop sound
    h "..."
    n "She notices us watching her." 
    play sound "audio/dark.mp3"
    n "She gets to her feet, pushes in her chair, and glares at us from the stale light of the kitchen table. It is scratched from long nails drawn repeatedly over the soft surface. The light shuts out."
    show her 
    pause 0.1
    hide her 
    show gen her 
    n "She appears in front of us."
    play music "audio/dark scary.mp3"
    h "I ruined everything. You are permanently damaged and stunted because I didn't stop the disease from spreading." 
    n "She tilts her head, as if listening to someone, or pondering a great issue."
    n "What do you think we should say to her?"
menu: 
    "I'm so tired.":
        jump tired
    "I'm not damaged.":
        jump not_damaged 
    "You didn't screw up.":
        jump screwed_up
label tired:
    pov "I'm so tired..."
    show gen her
    h "Me, too. Me f#cking too."
    n "She sighs deeply, almost longingly."
    h "You think you get it? You think you can UNDERSTAND my pain? You can't. Nothing hurts more than this."
    n "She sniffles, wiping her eyes and drying her tears. She glances at us, assesses us for broken parts- or maybe a light hidden inside somewhere."
    h "You will never be good! Never! Everything you do is so WRONG. You are destroyed, and you will destroy others."
    n "That would always hurt me when she said it with such conviction, like she was certain she was right. It was a statement full of belief."
    hide gen her
    show dean gen
    d "I don't..." 
    n "I begun to cry. Can you blame me?"
    d "Please, I'll be good... stop crying... it's okay, mom..."
    hide dean gen
    show gen her at left 
    show dean gen at right
    n "The night was long. I hugged her- she accepted with little resistance. She cried into my shoulder, sobbing. I felt numb."
    n "But day always breaks, a relief for most. I found myself back in my room. No one mentioned her red-rimmed eyes the next day or the marks on the table."
    jump morning_after
label not_damaged: 
    pov "I'm not damaged."
    n "She laughs a deranged, screwed-up, hysterical laugh."
    show gen her
    h "Of course you are. You're not normal. You've never BEEN normal. I must've messed up somewhere for you to turn out like this!"
    n "You don't want to hear this."
    h "Stupid, screwed-up, damaged kid you are. No one will ever like you. That's why you don't have any friends. Because you're incapable of being liked. Look at yourself. Who would ever love you?"
    n "I start to cry, too."
    h "Stop crying. Life is hard, and you need to get used to it. I won't always be around to help you."
    n "I sniffle but stop crying, even though I'm tempted to."
    h "Just go away. I don't want to see you."
    n "We go back to the room and fall asleep, eventually. This life is tiring."
    jump morning_after
label screwed_up:
    pov "You didn't screw up."
    show gen her
    h "You're just saying that to make me feel better. I'm a terrible person. I'm so awful. I can't do this, I can't be a good mother anymore. I just can't live like this! With YOU, and your mistakes?! And why should I have to!"
    n "She sniffles again, trembling, shoulders shaking as the clear liquid leaves trails on her cheeks. Why is she so miserable?" 
    h "It's your fault you're like that."
    n "She shakes her head."
    h "Just go away. GO AWAY!"
    n "You scurry back to your room in the dark of night, wondering why it was so scary to see her like that."
    n "Then you fall asleep."
    jump morning_after

label morning_after: 
    scene black
    hide gen her 
    n "I don't know how I survived so long in that minefield. Wretched day after wretched day, yelling and screaming heard from outside the house long after we all left for school."
    n "We grew up fast, but our childhood was slow. Each day was miserable. When we thought we were dealt a break, it was really a cruel joke."
    n "As I got older, school became an escape. I'd stay after as long as I could, wishing someone would take me away. Nothing seemed worse than going back to the cold, dead grip of the house."
    n "More happened than that, too, but some things are best left unsaid. Neither my mother nor my father were good parents."
    n "After all their time spent trying for children, using new methods, and finally adopting three, they still seemed like they never wanted us. Maybe they only liked the idea of it."
    n "The idea that you'd have kids to care for, watch them grow, buy them a car. The nuclear approach."
    n "I guess we all failed at that. But I was too young to truly understand what I was doing wrong - because I didn't do anything wrong, not logically. I just didn't measure up to what they were daydreaming about." 
    n "I'm glad to be out - I've escaped. The invisible scars from their claws still feel as fresh as they did when they sunk deep into flesh. But I'm no longer around to feel anything."
    n "You know what? I don't want to be golden anymore."
    n "THE END."