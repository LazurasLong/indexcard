# IndexCard RPG

Tabletop RPG rules that fit on a single 5x3 inch index card.

5-20 minute playtime.

Materials required:

  * paper
  * writing utensil
  * six-sided die.

**Lily Lemmer**: Concept and mother. Testing, LaTeX, source,
software engineer.

**Catlin Thomas**: Editor, testing, quality assurance,
software engineer.

# Core Ruleset

Start with: 20 `HEARTS`, 1 `BAM`, 1 `EVADE`, 4 `CRIT`, and 6 points
to distribute; point adds 4 to `CRIT` and 5 to `HEARTS`.

  1. Player with highest EVADE rolls first

    * Roll 6: +`CRIT` `BAM` bonus
    * Roll 1: miss, skip to step 4

  2. Defender rolls for every point in `EVADE`; if
     roll 6, skip step 3
  3. Defender loses `HEARTS` equal to attacker's
     `BAM` plus possible bonuses
  4. Start at step #1, but rotate players
     in order of `EVADE`

Creating supplemental rulesets:

  * Fits on index card (5x3 inches)
  * List required supplements on top, e.g.,
    `REQUIRED: Fruit`

# Fruit

Must announce which fruit you'll consume before rolling. You
may attack after eating a fruit.

Characters start with one fruit:

  * CHERRY: restore `ROLL` `HEART`, if roll
    1 restore full health
  * COCONUT: +ROLL BAM bonus
  * BANANA: Attack becomes unevadeable
  * GRAPES: Next `ROLL` of is 6
  * ORANGE: Deal `ROLL` x2 damage

# Tag Teams

  * Each player creates two characters, instead of one
  * Switching characters takes a turn
  * When a character dies, its tag team takes its place,
    same round

# Path Cards

`REQUIRES: Usable Items`

Characters now have `TALK` stat which starts at 1. Path cards
have a scenario and options which trigger `EVENTS`.

Options may have `REQUIREMENTS`:

  * `USE`: Must have item. Remove item.
  * `stat x`: `stat` + `roll` must be at least `x`

Option may trigger `EVENTS`:

  * `TALK`: Choose an option from dialog on back of path card. Some
    options have a `stat x` check, i.e., `TALK x`, failing disables
    the item.
  * `GET`: All players get item
  * `OPEN`: Get item #ROLL from chest on back of path card
  * `BATTLE`: Battle monster on back of path card
  * `NEXTCARD`: select new path card

# Shoutouts

If you notice any of the conditions being met, exclaim
"shoutout!" and name the condition satisfied (and reap
your reward!):

  * You roll two-of-a-kind when evading. Recover matched
    number in `HEART`.
  * You guessed your roll correctly before an attack. The
    defending player must roll their turn with one finger.
  * You guessed your roll correctly before using an item. You
    do not dispose the item after this use.
  * Everyone's HP is the same. Everyone else takes `ROLL` damage.
