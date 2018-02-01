# count frequency of words in Star Wars opening text (excluding words 'the' and 'has')
# text from starwars.wikia.com/wiki/Opening_crawl


def addeptext(eptext):
    '''append to list of strings the opening crawl text of each Stars Wars episode'''

    eptext.append('''Episode I
    THE PHANTOM MENACE
    Turmoil has engulfed the
    Galactic Republic. The taxation
    of trade routes to outlying star
    systems is in dispute.
    
    Hoping to resolve the matter
    with a blockade of deadly
    battleships, the greedy Trade
    Federation has stopped all
    shipping to the small planet
    of Naboo.
    
    While the Congress of the
    Republic endlessly debates
    this alarming chain of events,
    the Supreme Chancellor has
    secretly dispatched two Jedi
    Knights, the guardians of
    peace and justice in the
    galaxy, to settle the conflict....''')

    eptext.append('''Episode II
    ATTACK OF THE CLONES
    There is unrest in the Galactic
    Senate. Several thousand solar
    systems have declared their
    intentions to leave the Republic.
    
    This separatist movement,
    under the leadership of the
    mysterious Count Dooku, has
    made it difficult for the limited
    number of Jedi Knights to maintain
    peace and order in the galaxy.
    
    Senator Amidala, the former
    Queen of Naboo, is returning
    to the Galactic Senate to vote
    on the critical issue of creating
    an ARMY OF THE REPUBLIC
    to assist the overwhelmed
    Jedi....''')

    eptext.append('''Episode III
    REVENGE OF THE SITH
    War! The Republic is crumbling
    under attacks by the ruthless
    Sith Lord, Count Dooku.
    There are heroes on both sides.
    Evil is everywhere.
    
    In a stunning move, the
    fiendish droid leader, General
    Grievous, has swept into the
    Republic capital and kidnapped
    Chancellor Palpatine, leader of
    the Galactic Senate.
    
    As the Separatist Droid Army
    attempts to flee the besieged
    capital with their valuable
    hostage, two Jedi Knights lead a
    desperate mission to rescue the
    captive Chancellor....''')

    eptext.append('''Episode IV
    A NEW HOPE
    It is a period of civil war.
    Rebel spaceships, striking
    from a hidden base, have won
    their first victory against
    the evil Galactic Empire.
    
    During the battle, Rebel
    spies managed to steal secret
    plans to the Empire's
    ultimate weapon, the DEATH
    STAR, an armored space
    station with enough power to
    destroy an entire planet.
    
    Pursued by the Empire's
    sinister agents, Princess
    Leia races home aboard her
    starship, custodian of the
    stolen plans that can save
    her people and restore
    freedom to the galaxy.....''')

    eptext.append('''Episode V
    THE EMPIRE STRIKES BACK
    It is a dark time for the
    Rebellion. Although the Death
    Star has been destroyed,
    Imperial troops have driven the
    Rebel forces from their hidden
    base and pursued them across
    the galaxy.
    
    Evading the dreaded Imperial
    Starfleet, a group of freedom
    fighters led by Luke Skywalker
    has established a new secret
    base on the remote ice world
    of Hoth.
    
    The evil lord Darth Vader,
    obsessed with finding young
    Skywalker, has dispatched
    thousands of remote probes into
    the far reaches of space....''')

    eptext.append('''Episode VI
    RETURN OF THE JEDI
    Luke Skywalker has returned to
    his home planet of Tatooine in
    an attempt to rescue his
    friend Han Solo from the
    clutches of the vile gangster
    Jabba the Hutt.
    
    Little does Luke know that the
    GALACTIC EMPIRE has secretly
    begun construction on a new
    armored space station even
    more powerful than the first
    dreaded Death Star.
    
    When completed, this ultimate
    weapon will spell certain doom
    for the small band of rebels
    struggling to restore freedom
    to the galaxy...''')

    eptext.append('''Episode VII
    THE FORCE AWAKENS
    Luke Skywalker has vanished.
    In his absence, the sinister
    FIRST ORDER has risen from
    the ashes of the Empire
    and will not rest until
    Skywalker, the last Jedi,
    has been destroyed.
    
    With the support of the
    REPUBLIC, General Leia Organa
    leads a brave RESISTANCE.
    She is desperate to find her
    brother Luke and gain his
    help in restoring peace
    and justice to the galaxy.
    
    Leia has sent her most daring
    pilot on a secret mission
    to Jakku, where an old ally
    has discovered a clue to
    Luke's whereabouts....''')

    eptext.append('''Episode VIII
    THE LAST JEDI
    The FIRST ORDER reigns.
    Having decimated the peaceful
    Republic, Supreme Leader Snoke
    now deploys the merciless
    legions to seize military
    control of the galaxy.
    
    Only General Leia Organa's
    band of RESISTANCE fighters
    stand against the rising
    tyranny, certain that Jedi
    Master Luke Skywalker will
    return and restore a spark of
    hope to the fight.
    
    But the Resistance has been
    exposed. As the First Order
    speeds toward the rebel base,
    the brave heroes mount a
    desperate escape....''')


def countwords(epcount, eptext, EXCLUDEWORDS):
    '''generate frequency table in dictionary of occurrences of words in supplied list of strings'''
    import string
    for episode in eptext:
        for word in episode.split():
            cleanword = word.translate(str.maketrans('','',string.punctuation)).lower()
            if cleanword not in EXCLUDEWORDS: epcount[cleanword] += 1


def outputcount(epcount, EXCLUDEWORDS):
    '''Output frequency table dictionary of word occurrences ordered by value then key'''


    print('\n\n')
    print("Star Wars films - opening 'crawl' text frequency count.")
    if EXCLUDEWORDS:
        print(f'\t(excluding the words: {", ".join(EXCLUDEWORDS)})\n')
    print(f'{"word":<15} {"count":>4}')
    for word, count in sorted(epcount.items(), key=lambda x: (-x[1],x[0])):
        print(f'{word:<15} {count:>4d}')

'''
    main code
'''
def main():

    from collections import defaultdict as dd

    eptext = []
    epcount = dd(int)
    EXCLUDEWORDS = frozenset({'the','of', 'to', 'has', 'a'})

    addeptext(eptext)
    countwords(epcount, eptext, EXCLUDEWORDS)
    outputcount(epcount, EXCLUDEWORDS)


if __name__ == "__main__":
    main()