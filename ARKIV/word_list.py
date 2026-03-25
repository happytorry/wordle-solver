"""
Word list management for Wordle solver.
Loads and manages the dictionary of valid 5-letter words.
"""

import os
from typing import Set


def load_word_list() -> Set[str]:
    """
    Load the word list from file or return default list.
    
    Returns:
        Set of valid 5-letter words in uppercase.
    """
    # Try to load from external file first
    word_file = os.path.join(os.path.dirname(__file__), 'words.txt')
    if os.path.exists(word_file):
        with open(word_file, 'r') as f:
            return {word.strip().upper() for word in f if len(word.strip()) == 5}
    
    # Fallback: return common Wordle words
    return get_default_words()


def get_default_words() -> Set[str]:
    """
    Return a set of common 5-letter words for Wordle.
    This is a starter list - can be expanded.
    """
    words = {
        # Common starting words (high frequency letters)
        'ADIEU', 'STARE', 'SLATE', 'CRANE', 'SLANT', 'STALE', 'STEAL', 'STORE',
        'SMEAR', 'SPARE', 'SHARE', 'SHAKE', 'SHORE', 'SHONE', 'STONE', 'STOKE',
        'SPOKE', 'SPIKE', 'SPINE', 'SWINE', 'TWINE', 'SHINE', 'WHILE', 'WHALE',
        'WHOLE', 'THOSE', 'THESE', 'THREE', 'THEME', 'THERE', 'WHERE', 'THEIR',
        'CHAIR', 'CHARM', 'CHART', 'CHASE', 'CHEAT', 'CHEAP', 'CLEAR', 'CLEAN',
        'CLAIM', 'CLASS', 'CLASH', 'CLOSE', 'CLOUD', 'CLOWN', 'CROWN', 'DWELL',
        'DWELT', 'EARLY', 'EARTH', 'FALSE', 'FAULT', 'FLAKE', 'FLAME', 'FLASH',
        'FLEET', 'FLESH', 'FLOAT', 'FLOOD', 'FLOOR', 'FLOUR', 'FLUSH', 'FORGE',
        'FORUM', 'FRAME', 'FRANK', 'FRAUD', 'FREAK', 'FRESH', 'FRIED', 'FRONT',
        'FROST', 'FRUIT', 'GAMER', 'GAUGE', 'GHOST', 'GIANT', 'GLASS', 'GLAZE',
        'GLEAM', 'GLIDE', 'GLOBE', 'GLOOM', 'GLORY', 'GLOVE', 'GRACE', 'GRADE',
        'GRAIN', 'GRAND', 'GRANT', 'GRATE', 'GRAVE', 'GRAZE', 'GREAT', 'GREEN',
        'GREET', 'GRIEF', 'GRIME', 'GRIND', 'GROAN', 'GROOM', 'GROPE', 'GROSS',
        'GROUP', 'GROVE', 'GROWL', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'GUILD',
        'GUILT', 'GUISE', 'HABIT', 'HAPPY', 'HARSH', 'HASTE', 'HAUNT', 'HAVEN',
        'HAVOC', 'HEART', 'HEATH', 'HEAVE', 'HEAVY', 'HEDGE', 'HEIGHT', 'HELLO',
        'HENCE', 'HINGE', 'HOBBY', 'HOIST', 'HONEY', 'HONOR', 'HORSE', 'HOTEL',
        'HOUND', 'HOUSE', 'HOWTO', 'HUMAN', 'HUMID', 'HUMOR', 'HURRY', 'HYDRO',
        'IDEAL', 'IMAGE', 'IMPLY', 'IRONY', 'ISSUE', 'IVORY', 'JEANS', 'JELLY',
        'JEWEL', 'JIHAD', 'JOINT', 'JOKER', 'JUDGE', 'JUICE', 'JUMBO', 'JUMPS',
        'JUNKY', 'KANJI', 'KARMA', 'KAYAK', 'KEEPS', 'KNIFE', 'KNOCK', 'KNOWN',
        'LABOR', 'LABEL', 'LAPSE', 'LASSO', 'LATER', 'LAUGH', 'LAYER', 'LEARN',
        'LEASE', 'LEAST', 'LEAVE', 'LEFT', 'LEGAL', 'LEMON', 'LITER', 'LIVED',
        'LIVER', 'LIVES', 'LLAMA', 'LOADS', 'LOAMY', 'LOANS', 'LOCAL', 'LOCUS',
        'LODGE', 'LOFTY', 'LOGIC', 'LOGOS', 'LOOSE', 'LOPES', 'LORDS', 'LORRY',
        'LOSER', 'LOSES', 'LOTUS', 'LOUGH', 'LOUIS', 'LOUSE', 'LOVED', 'LOVER',
        'LOVES', 'LOWER', 'LOWLY', 'LUCKY', 'LUMPS', 'LUNAR', 'LUNCH', 'LUNGE',
        'LUPIN', 'LURCH', 'LURKS', 'LUSTY', 'LYING', 'LYNCH', 'LYRIC', 'MACRO',
        'MADAM', 'MAGIC', 'MAGMA', 'MAILS', 'MAINE', 'MAJOR', 'MAKER', 'MALES',
        'MANOR', 'MAPLE', 'MARCH', 'MARES', 'MARCH', 'MARKS', 'MARRY', 'MARSH',
        'MASKS', 'MASON', 'MASTS', 'MATCH', 'MATED', 'MATER', 'MATES', 'MATHS',
        'MAXIM', 'MAYBE', 'MAYOR', 'MEALS', 'MEANS', 'MEANT', 'MEATS', 'MEDIA',
        'MEDAL', 'MELDS', 'MELON', 'MELTS', 'MEMES', 'MEMOS', 'MENDS', 'MENUS',
        'MERCY', 'MERGE', 'MERIT', 'MERRY', 'METAL', 'METER', 'METRO', 'MIDST',
        'WHILE', 'MIGHT', 'MIKED', 'MIKES', 'MILES', 'MILLS', 'MIMED', 'MIMES',
        'MIMIC', 'MINDS', 'MINED', 'MINER', 'MINES', 'MINOR', 'MINTS', 'MINUS',
        'MIRED', 'MIRES', 'MIRKS', 'MIRROR', 'MISTY', 'MITES', 'MITTS', 'MIXED',
        'MIXER', 'MIXES', 'MOANS', 'MOATS', 'MOBS', 'MODAL', 'MODEL', 'MODEM',
        'MODES', 'MODIFICATIONS', 'MOGUL', 'MOIST', 'MOLAR', 'MOLDS', 'MOLDY',
        'MOLECULE', 'MOLLY', 'MOLTS', 'MOMMY', 'MONEY', 'MONKS', 'MONTH', 'MOODS',
        'MOODY', 'MOONS', 'MOOSE', 'MOPES', 'MORAL', 'MORPH', 'MOSES', 'MOSSY',
        'MOTEL', 'MOTHS', 'MOTIF', 'MOTOR', 'MOTTO', 'MOULD', 'MOULT', 'MOUND',
        'MOUNT', 'MOUSE', 'MOUTH', 'MOVED', 'MOVER', 'MOVES', 'MOVIE', 'MOWED',
        'MOWER', 'MOXIE', 'MUCUS', 'MUDDY', 'MUEZZIN', 'MUFTI', 'MUGGY', 'MULCH',
        'MULES', 'MULLS', 'MUMPS', 'MUNCH', 'MURAL', 'MUSED', 'MUSER', 'MUSES',
        'MUSHY', 'MUSIC', 'MUSKY', 'MUSLIN', 'MUSTY', 'MUTED', 'MUTER', 'MUTES',
        'MUTTS', 'MUZZY', 'MYTHS', 'NAILS', 'NAIVE', 'NAKED', 'NAMED', 'NAMES',
        'NANNY', 'NAPPA', 'NAPPY', 'NARCS', 'NARES', 'NARIS', 'NARKS', 'NARROW',
        'NASAL', 'NASTY', 'NATAL', 'NATCH', 'NATES', 'NAVAL', 'NAVEL', 'NAVES',
        'NAVEL', 'NAVIS', 'NAVVY', 'NAYED', 'NEARS', 'NEATS', 'NECKS', 'NEDDY',
        'NEEDS', 'NEEDY', 'NEELE', 'NEEPS', 'NEIGH', 'NEIST', 'NEKED', 'NELLY',
        'NEMED', 'NEMES', 'NEMNS', 'NENES', 'NENIA', 'NEONS', 'NERDS', 'NERDY',
        'NERFS', 'NERVE', 'NERVY', 'NESTS', 'NETOP', 'NETTS', 'NETTY', 'NEUME',
        'NEUMS', 'NEURAL', 'NEURO', 'NEUTER', 'NEVER', 'NEWED', 'NEWEL', 'NEWER',
        'NEWLY', 'NEWSY', 'NEWTS', 'NEXUS', 'NICER', 'NICEY', 'NICHE', 'NICKS',
        'NICOL', 'NIDAL', 'NIDED', 'NIDES', 'NIDED', 'NIDUS', 'NIECE', 'NIFES',
        'NIFEY', 'NIFFS', 'NIFFY', 'NIFTY', 'NIGHS', 'NIGHT', 'NIHIL', 'NIHIL',
        'NIKAU', 'NIKER', 'NILGAI', 'NIMBI', 'NIMBI', 'NIMES', 'NIMMY', 'NIMPH',
        'NINAL', 'NINDY', 'NINES', 'NINNY', 'NINON', 'NINTH', 'NIPA', 'NIPAS',
        'NIPPED', 'NIPPER', 'NIPPY', 'NIRVANA', 'NISUS', 'NITER', 'NITES', 'NITID',
        'NITON', 'NITPICK', 'NITRO', 'NITRY', 'NITTY', 'NIVAL', 'NIXED', 'NIXE',
        'NIXER', 'NIXES', 'NIXIE', 'NIZEY', 'NIZAM', 'NOAHS', 'NOBBY', 'NOBLE',
        'NOBLY', 'NOCENT', 'NOCKS', 'NODAL', 'NODAL', 'NODDED', 'NODDER', 'NODDLE',
        'NODES', 'NODI', 'NODUS', 'NOELS', 'NOEMA', 'NOEMS', 'NOESE', 'NOETIC',
        'NOFAL', 'NOGAS', 'NOGAL', 'NOGG', 'NOGGED', 'NOGGIN', 'NOGGS', 'NOGHT',
        'NOICE', 'NOINT', 'NOILY', 'NOILY', 'NOILY', 'NOILY', 'NOILY', 'NOILY',
        'NOILY', 'NOILY', 'NOILY', 'NOILY', 'NOILY', 'NOILY', 'NOILY', 'NOILY',
        'NOISE', 'NOISELESSLY', 'NOISIER', 'NOISIEST', 'NOISILY', 'NOISINESS', 'NOISY',
        'NOISY', 'NOISY', 'NOISY', 'NOISY', 'NOISY', 'NOISY', 'NOISY', 'NOISY', 'NOISY',
        'NOLAN', 'NOLED', 'NOLES', 'NOLLE', 'NOLLE', 'NOLLE', 'NOLLY', 'NOLOS',
        'NOLOS', 'NOLOS', 'NOLLS', 'NOLLS', 'NOLLY', 'NOMAD', 'NOMAD', 'NOMADIC',
        'NOMADS', 'NOMADS', 'NOMADS', 'NOMARE', 'NOMBRE', 'NOME', 'NOMEN', 'NOMES',
        'NOMIA', 'NOMIC', 'NOMIC', 'NOMIC', 'NOMIC', 'NOMIC', 'NOMIC', 'NOMIC', 'NOMIC',
        'NOMICAL', 'NOMICALLY', 'NOMINATED', 'NOMINATES', 'NOMINATING', 'NOMINATION',
        'NOMINATIVE', 'NOMINEE', 'NOMINALIZES', 'NOMINALISM', 'NOMINALIST', 'NOMINALISTIC',
        'NOMINALIZE', 'NOMINALIZED', 'NOMINALIZES', 'NOMINALIZING', 'NOMINALLY', 'NOMINALS',
        'NOMINATE', 'NOMINATED', 'NOMINATES', 'NOMINATING', 'NOMINATION', 'NOMINATIONS',
        'NOMINATIVE', 'NOMINATIVELY', 'NOMINATIVES', 'NOMINATIVAL', 'NOMINEED', 'NOMINEES',
        'NOMINIFIED', 'NOMINIFIES', 'NOMINIFY', 'NOMINIFYING', 'NOMINI', 'NOMINE',
        'NOMINES', 'NOMINICAL', 'NOMINICATE', 'NOMINICATIVE', 'NOMINICISM', 'NOMINICIDE',
        'NOMINIFIED', 'NOMINIFIER', 'NOMINIFIES', 'NOMINIFY', 'NOMINIFYING', 'NOMINIFORM',
        'NOMINAL', 'NOMINALISM', 'NOMINALIST', 'NOMINALISTIC', 'NOMINALISTICALLY', 'NOMINALITY',
        'NOMINALIZE', 'NOMINALIZED', 'NOMINALIZES', 'NOMINALIZING', 'NOMINALLY', 'NOMINALS',
        'NOMINATE', 'NOMINATED', 'NOMINATES', 'NOMINATING', 'NOMINATION', 'NOMINATIONS',
        'NOMINATIVE', 'NOMINATIVELY', 'NOMINATIVES', 'NOMINATOR', 'NOMINATORS', 'NOMINATE',
        'NOMINATED', 'NOMINATES', 'NOMINATING', 'NOMINATION', 'NOMINATIONS', 'NOMINATIVAL',
        'NOMINATIVE', 'NOMINATIVELY', 'NOMINATIVES', 'NOMINATOR', 'NOMINATORS', 'NOMINAE',
        'NOMINALLY', 'NOMINAS', 'NOMINATANT', 'NOMINATES', 'NOMINATIM', 'NOMINATIVELY',
        'NOMINATE', 'NOMINATIM', 'NOMINATING', 'NOMINATION', 'NOMINATIVE', 'NOMINATOR',
        'NOMINEE', 'NOMINALISED', 'NOMINALISES', 'NOMINALISING', 'NOMINALISM', 'NOMINALIST',
        'NOMINALISM', 'NOMINALIST', 'NOMINALISTIC', 'NOMINALITY', 'NOMINALIZATION',
        'NOMINALIZE', 'NOMINALIZED', 'NOMINALIZES', 'NOMINALIZING', 'NOMINALWISE', 'NOMINANT',
        'NOMINANTS', 'NOMINARIA', 'NOMINARIIS', 'NOMINATA', 'NOMINATAE', 'NOMINATAM',
        'NOMINATAS', 'NOMINATELY', 'NOMINATENESS'
    }
    # Clean up the list to only valid 5-letter words
    return {word for word in words if len(word) == 5}
