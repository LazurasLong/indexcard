import random

from operator import attrgetter


class Character(object):
    POINTS_TO_DISTRIBUTE = 6
    HEART_POINT_MULTIPLIER = 5
    CRIT_POINT_MULTIPLIER = 4

    START_HEART = 20
    START_BAM = 1
    START_EVADE = 1
    START_CRIT = 4

    def __init__(self, name, heart, bam, evade, crit):
        self.name = name
        self._heart = heart  # for reset
        self.heart = heart
        self.bam = bam
        self.evade = evade
        self.crit = crit

    @classmethod
    def from_points(cls, name, into_heart=0, into_bam=0,
                    into_evade=0, into_crit=0):

        # need to total points coming in to make sure
        # it doesn't exceed the points to distrib constant
        heart = cls.START_HEART
        bam = cls.START_BAM
        evade = cls.START_EVADE
        crit = cls.START_CRIT

        if into_heart:
            heart += cls.HEART_POINT_MULTIPLIER * into_heart

        if into_bam:
            bam += into_bam

        if into_evade:
            evade += into_evade

        if into_crit:
            crit += cls.CRIT_POINT_MULTIPLIER * into_crit

        return Character(name, heart, bam, evade, crit)

    @classmethod
    def from_interactive(cls):

        while True:

            name = input("Enter a name:\n> ")

            if len(name) == 0:
                print("Must be at least one character long")

                continue

        # get heart, bam, evade, crit from input
        while True:

            # If we fail to retreive three valid integers a ValueError is raised
            try:
                answer = input(("Distribute %d points with heart/bam/evade/crit,"
                                "e.g., 5/0/1/0:\n> " % cls.POINTS_TO_DISTRIBUTE))

                # This can raise a value error (if i is not int-able)
                points = [int(i) for i in answer.split('/')]

                # this could raise a ValueError
                into_heart, into_bam, into_evade, into_crit = points

                if sum(points) != cls.POINTS_TO_DISTRIBUTE:

                    raise ValueError()

            except ValueError:
                print("Incorrect format or bad sum")

                continue

        return cls.from_points(name, into_heart, into_bam,
                               into_evade, into_crit)


class CharacterRecord(object):
    """Battle records for a character.

    Total misses includes when your attack is
    evaded.

    """

    def __init__(self, name):
        self.name = name

        self.total_crits = 0
        self.total_crit_damage = 0
        self.total_damage = 0
        self.total_misses = 0
        self.total_evades = 0
        self.wins = 0
        self.deaths = 0
        self.kills = 0


class BattleRecord(object):
    """Statistics/records for a battle.

    Belongs to a Battle object.

    ATTRIBUTES:
        CHARACTER_STATS: The stats of the characters
            involved with this battle record.

    """

    def __init__(self, battle):
        self.battle = battle
        self._character_records = {}

        # the non-character-specific battle stats
        self.average_turns_to_win = 0.0

        for character in battle.all_characters:
            self._character_records[character.name] = CharacterRecord(character.name)

    def __getitem__(self, character_name):

        return self._character_records[character_name]

    def __iter__(self):

        for character in self._character_records.values():

            yield character

    def print_records(self):
        character_records = self._character_records.values()

        for score in ("kills", "deaths", "total_crits", "total_crit_damage",
                      "total_damage", "total_misses", "wins"):

            character_records.sort(key=lambda c: getattr(c, score), reverse=True)

            print("%s:" % score)

            for character_record in character_records:
                print("  * %s: %d" % (character_record.name, getattr(character_record, score)))

            print()


class Battle(object):
    # could be [6]
    CRIT_ON = [6]
    EVADE_ON = [6]

    # could be 0
    MISS_ON = [1]

    CRITS_SKIP_EVADE = False

    def __init__(self, *characters):
        characters = list(characters)
        characters.sort(key=lambda c: c.evade, reverse=True)
        self.all_characters = characters
        self.alive_characters = characters[:]
        self.dead_characters = []
        self.records = BattleRecord(self)

    def reset(self):

        for character in self.all_characters:
            character.heart = character._heart

        self.alive_characters = self.all_characters[:]
        self.dead_characters = []

    def run(self):
        """Do the battle simulation!!!!!"""

        turns_it_took_to_win = 0

        while len(self.alive_characters) > 1:

            for character in self.alive_characters:
                character_record = self.records[character.name]
                roll = random.randint(1, 6)

                possible_targets = self.alive_characters[:]
                possible_targets.remove(character)
                target = random.choice(self.alive_characters)
                target_record = self.records[target.name]

                total_damage = character.bam

                # this remains False UNLESS it's set to True when critting
                # <if CRITS_SKIP_EVADE> is True
                skip_evade_roll = False

                if roll in self.CRIT_ON:
                    # need to increase player's crit record
                    # here...
                    total_damage += character.crit
                    skip_evade_roll = self.CRITS_SKIP_EVADE
                    # could be wrong as it could be evaded
                    character_record.total_crits += 1
                    character_record.total_crit_damage += total_damage

                elif roll in self.MISS_ON:
                    # record miss
                    character_record.total_misses += 1

                    continue

                # this will be false unless crit said otherwise
                target_evades_damage = False

                if not skip_evade_roll:

                    # anytime anyone rolls and it's in evade_on
                    # it's evaded, rather than rerolling for every evade
                    for evade_chance in xrange(target.evade):
                        target_evade_roll = random.randint(1, 6)

                        if target_evade_roll in self.EVADE_ON:
                            target_record.total_evades += 1
                            character_record.total_misses += 1

                            target_evades_damage = True

                            break

                    if target_evades_damage:

                        continue

                target.heart -= total_damage
                character_record.total_damage += total_damage

                if target.heart <= 0:
                    self.alive_characters.remove(target)
                    self.dead_characters.append(target)
                    character_record.kills += 1
                    target_record.deaths += 1
                    target.heart = target._heart

            turns_it_took_to_win += 1

        character_record.wins += 1

        turns_it_took_to_win = float(turns_it_took_to_win)
        battle.records.average_turns_to_win = float((battle.records.average_turns_to_win
                                                     + turns_it_took_to_win) / 2.0)
        battle.reset()


if __name__ == "__main__":
    barb = Character.from_points("barb", into_heart=3, into_bam=3)
    rogue = Character.from_points("rogue", into_evade=3, into_crit=3)
    pure_crit = Character.from_points("pure_crit", into_crit=6)
    pure_bam = Character.from_points("pure_bam", into_bam=6)
    pure_evade = Character.from_points("pure_evade", into_evade=6)
    pure_heart = Character.from_points("pure_heart", into_heart=6)
    battle = Battle(barb, rogue, pure_crit, pure_bam, pure_evade, pure_heart)

    while True:

        try:
            times = input("Run this battle how many times?\n> ")
            times = int(times)

            break

        except ValueError:

            continue

    for time in xrange(times):
        battle.run()

    # yield the stats
    battle.records.print_records()
    print(battle.records.average_turns_to_win)
