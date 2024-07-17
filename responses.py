import random
from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered[0] == '!':
        tokens = lowered[1:].split(" ")
        print(tokens)
        if tokens[0] == "roll":
            r_final = roll_dice(0,99)
            crit_result = ""
            skill_result = ""
            roll_result = f"You rolled a {r_final}"
            if len(tokens) > 1:
                if tokens[1] == "dis":
                    r_other = roll_dice(0,99)
                    roll_result = f"Roll 1: {r_final} \nRoll 2: {r_other} \nYou Rolled: {max(r_final, r_other)}"
                    r_final = max(r_final, r_other)
                elif tokens[1] == "adv":
                    r_other = roll_dice(0, 99)
                    roll_result = f"Roll 1: {r_final} \nRoll 2: {r_other} \nYou Rolled: {min(r_final, r_other)}"
                    r_final = max(r_final, r_other)
                elif int(tokens[1][0:]) < 100:
                    skill_result = skill_check(r_final, int(tokens[1][0:]))
                if len(tokens) == 3:
                    if int(tokens[2][0:]) < 100:
                        skill_result = skill_check(r_final, int(tokens[2][0:]))
            if r_final == 0 or r_final % 11 == 0:
                crit_result = "Critical! "
            return '```' + crit_result + roll_result + '...' + '\n' + skill_result + '```'
        if tokens[0] == "panic":
            if len(tokens) == 3:
                panic = roll_dice(2,20)

                return ('```' + f"Panic Roll: {panic}" + '\n' + f"Current Stress: {int(tokens[1])}" + '\n' +
                        f"Resolve: {int(tokens[2])}" + '\n' + roll_panic((panic + int(tokens[1]) - int(tokens[2])),
                        int(tokens[1])) + '```')

        if tokens[0] == "help":
            return 'help not implemented'
        if tokens[0] == "stress":
            stress_roll = roll_dice(2, 20)
            stress_result = ""
            if len(tokens) == 3:
                if tokens[1].isdigit():
                    stress_result = check_stress(stress_roll, int(tokens[1]), int(tokens[2]))
            return "```" + f"You rolled {stress_roll}\n" + "\n" + stress_result + "```"
        if tokens[0] == "scum":
            scum_roll = roll_dice(1,10)
            scum_name = ""
            scum_description = ""
            scum_notes = ""
            scum_motivations = crew_motiv()
            if scum_roll == 1:
                scum_name = "Whiskey Tango Ronin"
                scum_description = ("Domestic Violence, outstanding warrants, Fealty To One’s Lord, Honorable Combat, "
                                    "only obeys master, refuses stealthy solutions.")
                scum_notes = ("Loadout:\n Katana, Hagakure. Demand for One Year’s Pay from Their New Master "
                              "(non-negotiable, paid in spring).")
            elif scum_roll == 2:
                scum_name = "The Witness"
                scum_description = (" Exceedingly polite, courteous and dressed in crisp and clean clothing. Will "
                                    "explain their religion and  witness to you at any point you may be susceptible to"
                                    " conversion—we all know there are no atheists in foxholes—will happily torture"
                                    " and/or murder those who disparage their god.")
                scum_notes = ("Loadout:\n Religious Text, Immaculate Clothes, Pamphlets about Their Religion, "
                              "Missionary Zeal.")
            elif scum_roll == 3:
                scum_name = "The Sex Bot (Android)"
                scum_description = ("Some genius thought the logic chip on an Android attuned to game theory and human "
                                    "sexuality would be an unbeatable prostitute—their rote behavior and uncanny valley"
                                    " state were a turn off. Because of this they are hypersexual at all times, "
                                    "inappropriately frank about your appearance, "
                                    "lack any scientific knowledge and cannot handle weapons.")
                scum_notes = "Loadout:\n Lube, amyl nitrates, many sex manuals, tear away clothes, shady sunglasses."
            elif scum_roll == 4:
                scum_name = "The Wretch"
                scum_description = ("Self-pitying, ratfucked, miserable and talkative; they lack any awareness of how "
                                    "depressing they are and how much they stress everyone out.")
                scum_notes = ("Mechanical:\n Stress gains are doubled when the Wretch is around (they blurt out the "
                              "worst possible outcome and denigrate all solutions).")
            elif scum_roll == 5:
                scum_name = "The Preening Pseudo-Intellectual"
                scum_description = ("You have met their kind on every habitable planet, you will most likely encounter"
                                    " them in hell. This ignoramus seamlessly integrates a complete lack of self"
                                    " awareness and tact with a total paucity of knowledge. This results in tantrums,"
                                    " evasions, compulsive lying and attempts to micromanage others.")
                scum_notes = ("Mechanical:\n Intellect Saves have Disadvantage when the Preening Pseudo-Intellectual "
                              "is around (they argue in bad faith, making it difficult to accomplish anything).")
            elif scum_roll == 6:
                scum_name = "The Dude"
                scum_description = ("Lackadaisical, lax, indifferent, just wants to minimize work and half "
                                    "asses any task.")
                scum_notes = "Loadout:\n Tattered bathrobe, poorly maintained gear, drugs to cope with working."
            elif scum_roll == 7:
                scum_name = "The Rich Kid"
                scum_description = ("Feels stifled by the upper echelons of society and wishes for the authentic "
                                    "experiences of the poor. Is in a contest to be the “most poor,” performing as "
                                    "an isolated rich child would assume; wishes for the crew to go without luxuries "
                                    "or reserves; prides themself on using only scavenged, poorly maintained gear.")
                scum_notes = (" Mechanical:\n Their family will not financially help vagabonds; they will put out a"
                              " bounty on every member of the crew should their unwanted child die, simply to keep up "
                              "appearances.")
            elif scum_roll == 8:
                scum_name = "The Hitchhiker"
                scum_description = ("Only in it for the free ride, the Hitchhiker will abandon your crew as soon as it "
                                    "is most convenient for them, possibly making off with whatever isn’t tied down.")
                scum_notes = "Loadout:\n Towel, eReader, electronic toolkit."
            elif scum_roll == 9:
                scum_name = "The Moon Child"
                scum_description = ("Blessedly ignorant, into crystal healing, against medicine, wants to vibe with "
                                    "you, does not comprehend hygiene. Will replace your gear with “natural” solutions"
                                    ".")
                scum_notes = ("Loadout:\n Interesting twigs and rocks, some sort of fruit jerky, a book on non-violent"
                              " communication to be angrily foisted on your crew.")
            elif scum_roll == 10:
                scum_name = "The Sole Survivor"
                scum_description = ("Grizzled, seemingly immortal, a crew member of ill omen. They are the last to"
                                    " survive because they will cut down, abandon or sell out their companions to "
                                    "take the full share of the loot and minimize risk. Tells gruesome, stressful "
                                    "stories about the passing of previous compatriots distorted to minimize their "
                                    "responsibility.")
                scum_notes = ("Mechanical:\n During combat, when determining turn order, randomly give one member "
                              "of the crew Disadvantage on their Speed Checks for the entire Combat. The "
                              "Sole Survivor, however, always acts with those who succeeded.")
            return ("```" + "\n" + "Alias:" + "\n" + scum_name + "\n" + "Description: \n" + scum_description + "\n" +
                    scum_notes + "\n" + "Motivations:" + "\n" + scum_motivations + "```")
        if tokens[0] == "motiv":
            return "```" + "\n" + "Motivation:" + "\n" + crew_motiv() + "```"

def crew_motiv() -> str:
    sector_roll = roll_dice(0,99)
    motiv_roll = roll_dice(1,10)

    if sector_roll in range(0, 49):
        if motiv_roll == 1:
            return "Need to pay off a Crime Syndicate"
        if motiv_roll == 2:
            return "Need to pay off a Repossession agent"
        if motiv_roll == 3:
            return "Need to pay off advance from another Captain"
        if motiv_roll == 4:
            return "Need to pay off a Separatist Militia"
        if motiv_roll == 5:
            return "Need to pay off their Unpaid Taxes"
        if motiv_roll == 6:
            return "Need to pay off jumped Bail/Court fine"
        if motiv_roll == 7:
            return "Need to pay off a Pawn Shop"
        if motiv_roll == 8:
            return "Need to pay off a Brothel"
        if motiv_roll == 9:
            return "Need to pay off a Loan Shark / Payday Loan"
        if motiv_roll == 10:
            return "Need to pay off losing everything to a Ponzi Scheme"
    elif sector_roll in range(50, 80):
        if motiv_roll == 1:
            return "They are hunting down a former partner"
        if motiv_roll == 2:
            return "They are hunting down a bounty hunter"
        if motiv_roll == 3:
            return "They are hunting down a petty official"
        if motiv_roll == 4:
            return "They are hunting down a mining magnate"
        if motiv_roll == 5:
            return "They are hunting down a military commander"
        if motiv_roll == 6:
            return "They are hunting down a parent"
        if motiv_roll == 7:
            return "They are hunting down a loan shark"
        if motiv_roll == 8:
            return "They are hunting down a snitch"
        if motiv_roll == 9:
            return "They are hunting down their sibling"
        if motiv_roll == 10:
            return "They are hunting down an opulently wealthy Scion"
    elif sector_roll in range(81, 99):
        if motiv_roll == 1:
            return "They are secretly part of a cult (Aberrant, Secretive)"
        if motiv_roll == 2:
            return "They are secretly a spy (Corporate, Rival Crew, Government)"
        if motiv_roll == 3:
            return "They are secretly a Smuggler (Extremely Illegal Goods)"
        if motiv_roll == 4:
            return "They are secretly a Saboteur/Wrecker (Opportunistic)"
        if motiv_roll == 5:
            return "They are undercover Secret Police (Investigating Party)"
        if motiv_roll == 6:
            return "They are secretly Infected (Seeks to Spread)"
        if motiv_roll == 7:
            return ("They are secretly a Recruiter (Evaluating Ship on Behalf of Criminal Syndicate, "
                    "Corporate Concern, Cult, etc.)")
        if motiv_roll == 8:
            return "They are secretly a Con Artist"
        if motiv_roll == 9:
            return "They are secretly a Serial Killer hiding from the law"
        if motiv_roll == 10:
            return "They are secretly a Bounty Hunter looking for you"

def roll_dice(a: int,
              b: int) -> int:
    random.seed(random.SystemRandom().random())
    return randint(a,b)


def skill_check(dice: int,
                target: int) -> str:
    result = ""
    if dice < target:
        result = result + "Success!"
    if dice > target:
        result = result + "Failure!"
    return result


def check_stress(stress_roll: int,
                 current_stress: int,
                 resolve: int) -> str:
    if stress_roll > current_stress:
        return f"...You rolled over your current stress. Your current stress is now {current_stress - 1}."

    else:
        panic = roll_dice(2,20)
        return ("...You rolled under or equal to your current stress! Now rolling on panic table..." + '\n' +
                f"Panic result is: {panic} + {current_stress} - {resolve} = {panic + current_stress - resolve}" + '\n' +
                roll_panic((panic + current_stress - resolve), current_stress))


def roll_panic(stress_roll: int,
               current_stress: int) -> str:
    if stress_roll < 2:
        return f"Resolve has prevented a panic attack!"
    if stress_roll in range(2,3):
        return f"Laser Focus: Advantage on all rolls for the next {roll_dice(1,10)} hours."
    elif stress_roll in range(4,5):
        return f"Major Adrenaline Rush: Advantage on all rolls for the next {roll_dice(3,30)} minutes."
    elif stress_roll in range(6,7):
        return f"Minor Adrenaline Rush: Advantage on all rolls for the next {roll_dice(1,10)} minutes."
    elif stress_roll in range(8,9):
        return "Anxious: Gain 1 stress."
    elif stress_roll in range(10,11):
        return "Nervous Twitch: Gaint 2 stress. The nearest crew member gains 1 stress."
    elif stress_roll in range(12, 13):
        return (f"Cowardice: Gain 1 Stress. For the next {roll_dice(1,10)} hours you must make a Fear Save to "
                f"engage in combat or else flee.")
    elif stress_roll in range (14,15):
        return (f"Hallucinations: For the next [REDACTED] hours (determined secretly), you have trouble distinguishing "
                f"between fantasy and reality.")
    elif stress_roll in range (16, 17):
        return ("Crippling Fear: Gain a new permanent phobia. Whenever you encounter this phobia make a Fear Save at "
                "Disadvantage, or gain 1d10 stress.")
    elif stress_roll in range (18, 19):
        return f"Overwhelmed: Gain {roll_dice(1,10)} stress."
    elif stress_roll in range (20, 21):
        return (f"Rattled: Let out a blood-curdling scream. Disadvantage on all rolls for {roll_dice(2,20)} "
                f"minutes.")
    elif stress_roll == 22:
        return (f"Paranoid: For the next {roll_dice(1,10)} days, whenever a character joins your group (even if "
                f"they only stayed for a short period of time), make a Fear Save or gain 1 stress.")
    elif stress_roll == 23:
        return (f"Death Drive: For the next {roll_dice(1,10) * current_stress} days, whenever you encounter a "
                f"stranger or a known enemy, you must make a Sanity Save or else immediately attack them.")
    elif stress_roll == 24:
        return f"Catatonic: Become unresponsive and unmoving for {roll_dice(1,10) * 10} minutes."
    elif stress_roll == 25:
        return (f"Broken: For the next {roll_dice(1,10) * 10} days, make a Panic Check whenever a nearby crew "
                f"member fails a save.")
    elif stress_roll == 26:
        return (f"Psychotic: Immediately attack the closest crew member until you do at least {roll_dice(2,20)} "
                f"damage. If there is no crew member nearby, attack and destroy {roll_dice(1, 10)} pieces of nearby "
                f"equipment.")
    elif stress_roll == 27:
        return f"Compounding problems. Roll twice on this table."
    elif stress_roll == 28:
        return f"Descent into Madness: Gain 2 new phobias. Your stress cannot be relieved below 5."
    elif stress_roll == 29:
        return (f"Psychological Collapse. You become permanently, irreparably insane. Your character is now player by"
                f" the Warden.")
    else:
        return "Heart Attack. Instant Death."
