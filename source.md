# IndexCard RPG

Tabletop RPG rules that fit on a single 5x3 inch index card.

Materials required:

  * paper
  * writing utensil
  * six-sided die.

Please offer elegant summaries of these rules!

Lillian Lemmer, Catlin T

## Core Ruleset

Character starts with 5 HEARTS, 1 BAM, 1 EVADE, and 8 points
to distribute; each point into HEARTS adds five HEARTS.

  1. Player with highest EVADE rolls first

    * Roll 6: +2 BAM bonus, skip step 2
    * Roll 5: +1 BAM bonus, skip step 2
    * Roll 1: miss

  2. Defender rolls up to their EVADE times,
     if roll 6 skip step 3
  3. Defender loses HEARTS equal to attacker's
     BAM plus possible bonuses
  4. Start at step #1, but rotate players
     in order of EVADE

Rules for creating supplement cards:

  * Fits on index card (5x3 inches)
  * 8 point Inconsolata Regular font
  * List required supplements on top, e.g.,
    `REQUIRED: Usable Items, Crazy Crits`

## Supplement Card: Usable Items

Must announce which item used before rolling.

Characters start with one item:

  * CANDY: restore `ROLL * 2` `HEARTS`; do not attack
  * SODA: +ROLL BAM bonus; unevadable attack

Untested:

  * TOKEN: acts as a roll of 6; can attack
  * MOLOTOV: Damage is 2x roll; unevadable
  * THROWING STARS: Roll thrice, the total is unevadable damage.

## Supplement Card: Crazy Crits

  * New stat: `crit`, starts at 2
  * Each point invested in `crit` adds two
  * Rolling 6 or 5: the total BAM bonus is `crit` value

## Supplement Card: Novel

`REQUIRES: Usable Items`

A novel is a series of cards which have a scenario and options. Write the story, where each option may have `REQUIREMENTS` and `EVENTS`.

Option `REQUIREMENTS`:
  * `USE x`: Item `x` is required for this option.
  * `CHECK stat x FAIL y`: Option requires `stat` + `roll` to at least be `x`, else `FAIL` event `y`. Example: use for conversation, `"You're looking pretty!" CHECK HEARTS 20 FAIL BATTLE`

Option `EVENTS`:
  * `OPEN`: Get item #ROLL from the chest on the back of this path card
  * `BATTLE`: Battle monster on the back of this path card
  * `NEXTCARD`: select random path card from this novel

Preface non-required things which require a supplement with `SUPPLEMENT supplement card name`.

Use die roll to determine who the monster attacks.
  
### Example Novel

#### Path Card: Sleeping Ugly (Front)

You are in a room with a slumbering troll, a locked door, and a treasure chest.

To get to the chest, you must either tip-toe around the troll or fight it.

- Sneak around Troll and `OPEN` the chest (`CHECK evade 14 FAIL BATTLE`)
- `BATTLE` the Troll and `OPEN` the chest
- Go to door and `USE key` (`NEXTCARD`)

#### Path Card: Sleeping Ugly (Back)

Troll
  - H: 16 (48)
  - B: 14
  - E: 1
  - `SUPPLEMENT crazy crits` C: 4 (8)
Drops: Key

Treasure Chest
  1. KEY
  2. TOKEN
  3. MOLOTOV
  4. THROWING STARS
  5. CANDY
  6. SODA

#### Path Card: Monk Up Your Mind (Front)

You come across a meditating monk sitting in front of two doors.

  - "Philosophical banter here" CHECK STAT HEARTS 17 FAIL GAME OVER
  - BATTLE MONK
  - LEFT DOOR
  - RIGHT DOOR

#### Path Card: Monk Up Your Mind (Back)

MONK
  - H: 20
  - B: 5
  - E: 24
  - C: 12
