import random
print("Good morning ")
dog = True
like_count = 0  
roblox = 100000
cat = True
print("bon is funny")

while dog:
    print("I like roblox")

    user_input = input("Do you still like roblox? y/n ").lower()
    if user_input == "n" or user_input == "no":
        print(f"Okay, stopping now! You said you liked roblox {like_count} times.")
        dog = False  

    print("bon is funny")
    print("clutch!!")
    print("random chaos incoming...")
    like_count += 1

    # 🏆 Chaos Score Leaderboard Setup
    leaderboard_file = "leaderboard.txt"
    
    def save_score(score):
        try:
            with open(leaderboard_file, "a") as f:
                f.write(str(score) + "\n")
        except Exception as e:
            print("[ERROR] Could not save score:", e)
    
    def display_leaderboard():
        try:
            with open(leaderboard_file, "r") as f:
                scores = [int(line.strip()) for line in f.readlines()]
            scores.sort(reverse=True)
            print("\n🔥 Top Chaos Scores 🔥")
            for i, s in enumerate(scores[:5], 1):
                print(f"{i}. {s}")
        except FileNotFoundError:
            print("No leaderboard found yet. Be the first chaotic hero!")


    roblox_change = random.randint(-1000, 1000)
    roblox += roblox_change
    print("Roblox fluctuation:", roblox_change, "| New roblox value:", roblox)
    
    if random.randint(1, 10) == 5:
        print("Bonus event: You discovered hidden extra points for persistence!")
    roblox += 500
        print("Your roblox balance increased to", roblox)

    chaos_multiplier = like_count * roblox_change
    chaos_level = chaos_multiplier + roblox_change
    if chaos_level > 5000:
        print("🚨 CHAOS OVERLOAD DETECTED! Initiating slow-motion mode...")
    elif chaos_level < 0:
        print("💤 Negative chaos... did we break the matrix?")
    else:
        print("Chaos status: Stable... for now.")

    cat_event = random.choice(["nap", "hack_system", "vanish", "meow_loop"])
    if cat_event == "hack_system":
        print("🐱 Cat is hacking the mainframe!")
        roblox -= 42  
    elif cat_event == "meow_loop":
        print("Cat is stuck in an infinite meow loop. Send help.")

    debug_mode = random.choice([True, False])
    if debug_mode:
        print("[DEBUG MODE ENABLED] Diagnostic data streaming...")

    random_value = random.randint(1, 100)
    if random_value % 2 == 0:
        print("Even chaos level detected:", random_value)
    else:
        print("Odd chaos level detected:", random_value)
    chaos_multiplier = like_count * random_value
    print("Chaos multiplier is:", chaos_multiplier)

    print("Quantum hamsters are powering the mainframe...")
    print("like_count is now", like_count)
    print("snakes everywhere")
    print("launching into orbit")

    print("Warning: unknown variable detected")
    print("System malfunction in progress")
    print("Turning off lights... maybe")
    print("Rebooting imagination module")
    print("Error: too much fun")
    print("Spinning in circles...")
    print("Inserting random numbers:", like_count * 7)

    print("Calculating probability of cheese invasion")
    print("Deploying emergency rubber duck unit")
    
    print("Activating stealth mode")
    print("Unexpected dance break")
    print("Check inventory: empty")
    print("Simulation of chaos continues")
    print("Power fluctuating")
    print("Debugging nothing at all")
    print("This line is definitely random")

    print("Downloading emotional support algorithms...")

    print("Turning into a ninja...")
    print("Sushi lunch break")
    print("Ninjato disappeared?")
    print("Chaotic simulation rambles onward")
    print("Energy diminishing")
    print("Falling asleep...")
    print("Dreaming")

    print("Calculating imaginary numbers")
    print("Launching invisible rockets")
    print("Reading thoughts of the dog")
    print("Time is just a concept")
    print("Aliens are probably laughing")
    print("Rewriting the rules")
    print("Confusion level: maximum")

    print("Reality glitch detected in sector 42")
    print("Backup unicorns have been notified")

    # 🎲 Random Event Generator
    event_chance = random.randint(1, 100)
    if event_chance > 95:
        event = random.choice(["alien_invasion", "meme_storm", "time_distortion"])
        if event == "alien_invasion":
            print("👽 Aliens just stole your roblox points!")
            roblox_loss = random.randint(100, 500)
            roblox -= roblox_loss
            print(f"Lost {roblox_loss} roblox, new total: {roblox}")
        elif event == "meme_storm":
            memes_generated = random.randint(1, 10)
            like_count += memes_generated
            print(f"A wild meme storm! Gained {memes_generated} like_count, total now {like_count}")
        elif event == "time_distortion":
            print("⏳ Time distortion! Chaos levels fluctuate wildly...")
            chaos_level += random.randint(-5000, 5000)
            print(f"New chaos_level: {chaos_level}")

    print("Summoning invisible sandwiches")
    print("Running in reverse")
    print("Error: coffee not found")
    print("Unlocking secret achievements")
    print("Gravity is optional")
    print("Computing random nonsense")
    print("Spaghetti code detected")

    print("Teleporting to the fridge")
    print("Counting invisible beans")
    print("Dancing with shadows")
    print("Activating hyperdrive")
    print("Measuring nothingness")
    print("Random beep sounds")
    print("Generating chaos numbers")

    print("Summoning digital spaghetti monsters")          
    print("Reversing gravity for dramatic effect")         
    print("Initiating spontaneous combustion of boredom")  
    print("Reversing gravity for dramatic effect")         
    print("Initiating spontaneous combustion of boredom")  
    print("Invading the kitchen with invisible forks")     
    print("Time-traveling with a rubber chicken")          
    print("Summoning a council of sarcastic pigeons")      

    print("Uploading dreams to the cloud")
    print("Charging emotional batteries")
    print("Compiling laughter.exe")
    print("Decrypting banana protocols")
    print("Rendering pixelated universes")
    print("Synchronizing with parallel timelines")
    print("Executing undefined behavior")

    print("Inventing new colors...")
    print("Detecting paradox in progress...")
    print("Creating recursive nonsense loops")
    print("Befriending the nearest toaster")
    print("Initializing potato AI")
    print("Debugging existential dread...")
    print("Rendering cat in 4D")
    print("Error: too much caffeine detected")
    print("Unlocking secret debug menu")
    print("Reality buffer overflow!")
    print("Trying to count to infinity... please wait...")
    print("Launching interdimensional memes")
    print("Initiating intergalactic pizza delivery sequence...")

    while cat:
        print("flag false")
        print("cat is plotting something...")
        print("error 404: mouse not found")
        break

if roblox == 100000:
    print("power on")
    print("do not unplug the mainframe!")
else:
    print("Time travel unavailable. Please reboot your DeLorean.")

aliens_present = random.choice([True, False])
if aliens_present:
    print("Alien contact established 👽")
    alien_language = "".join(random.choices("ΔΞΩ§†µ", k=8))
    print("Alien message received:", alien_language)
    print("Attempting universal translator...")
    translation_success = random.choice([True, False])
    if translation_success:
        print("Translation: 'Send more memes.'")
    else:
        print("Translation failed. Initiating interpretive dance.")
else:
    print("No aliens... just raccoons in space suits.")

print("Caffeine levels critical: deploying espresso drones...")

quest = input("A mysterious portal appears. Do you enter it? y/n ").lower()
if quest in ['y', 'yes']:
    realm = random.choice(["Waffle Dimension", "Upside Down Library", "Haunted Codebase", "Infinite Loop Valley", "Quantum Playground"])
    print(f"You've entered the {realm}!")
    challenge_rating = random.randint(1, 100)
    print("Challenge rating:", challenge_rating)
    if challenge_rating > 50:
        print("It's dangerous! You need backup.")
    else:
        print("You handle it like a pro—epic win!")
    print("Collecting loot... found: a glowing rubber duck!")
    print("Portal guardian whispers: 'Beware the semicolons.'")
else:
    print("You wisely walk away. The portal sighs in disappointment.")
    print("You feel an odd sense of peace... and mild confusion.")

meme_quality = random.randint(0, 10)
print("Meme quality score:", meme_quality)
if meme_quality < 3:
    print("Too stale. Try again.")
elif meme_quality < 7:
    print("Mediocre meme. Slight chuckle achieved.")
else:
    print("Legendary meme! You broke the simulation.")
print("Uploading meme to cloud storage of destiny...")
print("Analyzing meme quantum frequency... success!")

print("Rebooting imagination kernel v2.0...")

# 📊 Player Stats Tracker
player_stats = {
    "total_memes_uploaded": meme_quality,
    "total_chaos_level": chaos_level,
    "portals_entered": 1 if quest in ['y', 'yes'] else 0
}

print("\n📝 Player Stats Summary:")
for stat, value in player_stats.items():
    print(f"{stat.replace('_', ' ').title()}: {value}")

print("Launching Pet Rock Simulator...")
pet_rock_mood = random.choice(["bored", "happy", "angry", "sleeping", "philosophical", "vibing"])
print(f"Your pet rock is currently: {pet_rock_mood}")
if pet_rock_mood == "happy":
    print("It rolls around joyfully.")
elif pet_rock_mood == "bored":
    print("It stares blankly into the void.")
elif pet_rock_mood == "angry":
    print("It does nothing... but aggressively.")
elif pet_rock_mood == "philosophical":
    print("It contemplates the meaning of pebbles.")
elif pet_rock_mood == "vibing":
    print("It bops its nonexistent head to lo-fi beats.")
else:
    print("It snores gently. You tuck it in.")

print("Reality now bending...")
print("Frogs with jetpacks incoming")
print("Downloading more bananas...")
print("Error 008: Too much awesome")
print("Initializing endless loop of fun")

# NEW: 🪨 Pet Rock Adventure Expansion
print("\nLaunching Pet Rock Adventure DLC...")
adventure_outcome = random.choice(["treasure", "storm", "portal", "dance_party"])
if adventure_outcome == "treasure":
    print("Your rock discovers a golden pebble of wisdom!")
elif adventure_outcome == "storm":
    print("A pebble storm begins! Your rock bravely endures it.")
elif adventure_outcome == "portal":
    print("The rock rolls into a glowing portal and disappears...")
    print("...only to return with sunglasses and a mysterious aura.")
else:
    print("Your rock starts an intergalactic dance party with nearby boulders!")

rock_energy = random.randint(1, 100)
print("Rock energy level:", rock_energy)
if rock_energy > 80:
    print("Your rock ascends to pebble nirvana.")
else:
    print("Your rock decides to nap again.")

# 🎉 FINAL MESSAGES
print("\n🎉 FINAL MESSAGE:")
print("Congratulations, traveler! You have reached the end of the randomness.")
print("Or maybe... the randomness has reached YOU.")
print("Either way, the universe winks approvingly. ✨")
print("Rebooting your sense of normalcy in 3... 2... 1...")
print("Wait... did someone forget to feed the quantum hamsters?")
print("System alert: your imagination just leveled up to tier ∞.")
print("Synchronizing dreams with alternate universe servers...")
print("A mysterious narrator whispers: 'You weren’t supposed to see this ending.'")

# 🆕 EXPANDED FINAL CHAOS MESSAGES
print("Glitch detected: reality patching itself in the background...")
print("Someone just rolled a 20 on the chaos check.")
print("Uploading your consciousness to the meme cloud...")
print("Duck.exe has stopped responding.")
print("ERROR 505: Humor overflow detected.")
print("Deploying emergency giggle containment field.")
print("Rebooting universal sense of purpose... please hold.")
print("Quantum hamster wheel overheating—sending backup gerbils.")
print("The simulation applauds your commitment to nonsense.")
print("New achievement unlocked: 'Master of Random.'")
print("Parallel universe agrees: 10/10 would simulate again.")
print("Time paradox resolved by turning it off and on again.")
print("A cosmic cat just sat on the keyboard. Everything makes sense now.")
print("You’ve reached enlightenment... or maybe just lunchtime.")
print("The mainframe whispers: 'Don’t take reality too seriously.'")
print("Random number generator achieved sentience and wants a raise.")
print("Congratulations! You’ve officially broken the fourth wall.")
print("A portal opens... it’s filled with spaghetti and hope.")
print("You find a note: 'The true chaos was the friends we made along the way.'")
print("Simulation shutting down... rebooting in dream mode.")
print("Unicorns confirmed stable. Bananas normalized.")
print("The void stares back—and gives you a thumbs-up 👍.")
print("Achievement unlocked: Survived the nonsense loop.")
print("Recompiling giggle algorithms...")
print("AI narrator signing off. Please feed the raccoons responsibly.")
print("Quantum pigeons salute you as the credits roll.")
print("Final message received: 'Keep being weird.'")
print("End of transmission. ✨")
print("Error 9001: Fun levels over 9000! System cannot handle the joy.")
print("A wormhole opens, delivering a pizza you didn’t order but totally deserve.")
print("Time traveler appears: ‘Don’t worry, you did everything correctly—mostly.’")
print("The cosmic hamster union demands better snacks.")
print("A parallel dimension just liked your code.")
print("Plot twist: you were the AI all along.")
print("Final reboot initiated... just kidding. The fun never ends.")
print("Deploying anti-seriousness shield v3.14...")
time_portal = random.choice(["open", "closed", "stuck halfway"])
print(f"Temporal stability: {random.randint(0, 100)}% — portal is {time_portal}.")
if time_portal == "stuck halfway":
    print("Warning: Half your snacks are now in another timeline!")

# NEW CODE

# 🌌 Multiverse Expansion Mode
multiverse_chance = random.randint(1, 100)
if multiverse_chance > 80:
    universe_effect = random.choice(["reverse_gravity", "loop_messages", "invert_chaos"])
    print("\n🪐 Multiverse Expansion Activated!")
    if universe_effect == "reverse_gravity":
        print("Gravity is inverted! All objects float upwards. Chaos is off the charts!")
    elif universe_effect == "loop_messages":
        print("Time echoes! Previous messages start repeating randomly...")
        repeat_count = random.randint(2, 5)
        for i in range(repeat_count):
            print(f"[Time Echo {i+1}] 'Randomness continues...'")
    elif universe_effect == "invert_chaos":
        chaos_level = -chaos_level
        print(f"Chaos levels inverted! New chaos_level: {chaos_level}")

print(Lebron, Lebron, Lebron James)
if input==yes
   print(you are my sunshine lebron)


revert_normal = random.randint(1, 100)
if revert_normal < 40:
    revert = random.choice(["wormhole", "tesseract"])
    print("\n 🌎 Going back to our universe ... ")
    if revert == "blackhole":
        print("You have been sucked into a wormhole and dropped back into our current galaxy!")
    elif revert == "tesseract":
        print("You find yourself in a weird place with multiple ways to go ... but each one is not in the present timeline! Where shall you go ...")
        elif revert == "tesseract":
    print("You find yourself in a weird place with multiple ways to go ... but each one is not in the present timeline! Where shall you go ...")
    
    paths = ["The Neon Forest", "The Library of Forgotten Code", "The Upside-Down Café", "The Hallway of Infinite Doors", "The Glitch Dimension"]
    chosen_path = random.choice(paths)
    print(f"You step cautiously into {chosen_path}...")

    print("Time flickers like a faulty lightbulb.")
    print("Your footsteps echo in multiple realities at once.")
    print("Reality itself seems to take a coffee break...")

    event = random.choice(["meet_future_self", "find_time_duck", "loop_in_time", "discover_secret_exit"])
    if event == "meet_future_self":
        print("👁 You meet your future self! They hand you a note that says, 'Don’t trust the raccoons.'")
    elif event == "find_time_duck":
        print("🦆 A Time Duck waddles by and quacks in binary. You gain +42 wisdom.")
    elif event == "loop_in_time":
        print("⏳ You realize you’re in a time loop... again. You wave at your past self. Awkward.")
    elif event == "discover_secret_exit":
        print("🚪 You find a glowing exit labeled ‘Back to Mild Reality’. You take it without hesitation.")

    print("A mysterious voice whispers: 'The tesseract bends to those who laugh at paradoxes.'")
    print("You feel space folding around you like origami... and suddenly—")
    print("💫 You’re back! Everything feels... almost normal. But your socks are now quantum entangled.")
elif revert == "tesseract":
    print("You find yourself in a weird place with multiple ways to go ... but each one is not in the present timeline! Where shall you go ...")
    
    paths = ["The Neon Forest", "The Library of Forgotten Code", "The Upside-Down Café", "The Hallway of Infinite Doors", "The Glitch Dimension"]
    chosen_path = random.choice(paths)
    print(f"You step cautiously into {chosen_path}...")

    print("Time flickers like a faulty lightbulb.")
    print("Your footsteps echo in multiple realities at once.")
    print("Reality itself seems to take a coffee break...")

    event = random.choice(["meet_future_self", "find_time_duck", "loop_in_time", "discover_secret_exit"])
    if event == "meet_future_self":
        print("👁 You meet your future self! They hand you a note that says, 'Don’t trust the raccoons.'")
    elif event == "find_time_duck":
        print("🦆 A Time Duck waddles by and quacks in binary. You gain +42 wisdom.")
    elif event == "loop_in_time":
        print("⏳ You realize you’re in a time loop... again. You wave at your past self. Awkward.")
    elif event == "discover_secret_exit":
        print("🚪 You find a glowing exit labeled ‘Back to Mild Reality’. You take it without hesitation.")

    print("A mysterious voice whispers: 'The tesseract bends to those who laugh at paradoxes.'")
    print("You feel space folding around you like origami... and suddenly—")
    print("💫 You’re back! Everything feels... almost normal. But your socks are now quantum entangled.")

    # 🌀 15 NEW LINES OF CHAOTIC ADVENTURE 🌀
    print("The walls of reality ripple like water, showing fragments of infinite memes.")
    print("You hear faint elevator music — but it’s being played by cosmic jellyfish.")
    print("A door labeled '404: Reality Not Found' appears and disappears.")
    print("A floating sign reads: 'Welcome
    print("A soft 'pop' echoes as reality reinflates itself like a cosmic balloon.")
    print("You open your eyes to find that gravity is now optional — again.")
    print("A nearby wormhole offers you tea. You politely accept, even though it screams in Morse code.")
    print("The tea tastes like nostalgia and static electricity.")
    print("A voice from nowhere asks, 'Have you tried turning the universe off and on again?'")
    print("You nod. The voice sighs in relief and gives you +10 existential XP.")
    print("Suddenly, confetti rains down — but each piece contains a tiny dimension.")
    print("One confetti piece opens a portal showing your pet rock breakdancing in another timeline.")
    print("The cosmic narrator sneezes, and time skips ahead three sentences.")
    print("Your reflection waves at you — but it's holding a banana phone.")
    print("A floating UI prompt appears: [Achievement Unlocked: Temporal Tourist 🕓]")
    print("Somewhere, a robot penguin starts singing ‘Never Gonna Give You Up’ in binary.")
    print("The tesseract hums like a sleepy computer fan. You realize it's powered by pure imagination.")
    print("You feel the ground dissolve into glowing pixels beneath your feet.")
    print("Then, with a cheerful ‘boop!’, the entire scene resets — as if nothing ever happened.")

    print("A faint jazz soundtrack starts playing from somewhere beyond comprehension.")
    print("You check your inventory: 1 rubber chicken, 2 paradoxes, and infinite curiosity.")
    print("A loading bar appears in midair: 'Reassembling Continuity... 87%'")
    print("A cosmic intern appears and hands you a clipboard. 'Please sign for your timeline delivery.'")
    print("You sign it, but your signature turns into a small galaxy that immediately spins away.")
    print("A quantum pigeon lands nearby, cooing the secrets of the multiverse.")
    print("You take notes, but the pen writes in hieroglyphic emojis.")
    print("Reality blinks again — the sky is now made entirely of snack advertisements.")
    print("A friendly glitch offers to guide you through the nearest plot hole.")
    print("You follow it, only to emerge inside a 1990s screensaver of flying toasters.")
    print("One toaster salutes you and promotes you to 'Deputy of Dimensional Affairs.'")
    print("You receive an email from yourself titled: 'Do Not Open This Until Yesterday.'")
    print("Curiosity wins. You open it. The subject line reads: 'Too late.'")
    print("Thunder claps dramatically — but only inside your left ear.")
    print("Suddenly, you realize the entire Tesseract may have just been a really vivid loading screen.")
print("A floating progress bar appears: 'Installing Updates to Causality... 3% complete.'")
print("You try to cancel, but free will has already been deprecated in this version.")
print("The sky flickers through several genres — noir, cyberpunk, then unexpectedly romantic comedy.")
print("Rain starts to fall, but every drop politely introduces itself before landing.")
print("A neon sign materializes midair: 'Welcome Back, Deputy. Reality Missed You (sort of).'")
print("The cosmic intern reappears, now holding a mug labeled 'Multiverse Management Trainee.'")
print("'Sign here again,' they say, handing you a pen that hums with untapped prophecy.")
print("Your signature draws itself this time, spelling out your name in Morse code and regret.")
print("A door appears, labeled 'Do Not Enter Unless You Already Have.'")
print("You step through anyway, because curiosity has tenure.")
print("Inside, you find an infinite hallway of loading screens arguing about continuity.")
print("A holographic receptionist greets you: 'Please hold, your existence is important to us.'")
print("Elevator music plays, but it’s suspiciously aware of your emotional state.")
print("A mirror on the wall reflects your data instead of your face.")
print("Lines of code scroll across your reflection, commenting on your life choices.")
print("One of the comments reads: '# TODO: Figure out the meaning of all this.'"
