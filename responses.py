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
