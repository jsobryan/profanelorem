import random

part_a = [
'dingle̵',
'dangle',
'dongus',
'scrangle',
'flank',
'crungus',
'slarpo',
'floogle',
'ass',
'butt',
'weiner',
'dong',
'chong',
'schlong',
'bong',
'hurdle',
'gurdle',
'slorble',
'flongus',
'hungus',
'nip',
'hongo',
'slagon',
'flurple',
'plonk',
'chango',
'wango',
'wang',
'dingo',
'bastard',

]
verbs = [
    'slap',
    'plop',
    'scrop',
    'slop',
    'stank',
    'flag',
    'fart',
    'shit',
    'dick',
    'suck',
    'fuck',
    'rankle',
    'stingle',
    'floom',
    'slarp',
    'flunk',
    'floople',
    'shank',
    'clank',
    'sloorp',
    'scroon',
    'flange',
    'weedle',
    'screedle',
    'flangle',
    'hurble',
    'durble',
    'shorp',
    'flallop',
    'hurbleburb',
    'scrunch',
    'winghurb'
]

adjectives_a = [
    'ass',
    'shit',
    'fuck',
    'dingle',
    'shit',
    'grundle',
    'butt',
    'dong',
    'turd',
    'diarrhea',
    'stank',
    'aeolus',
'ahole',
'anal',
'anus',
'areola',
'areole',
'arian',
'aryan',
'ass',
'assbang',
'ass hole',
'assholes',
'assmaster',
'assmunch',
'asswipe',
'asswipes',
'azazel',
'azz',
'babe',
'babes',
'ballsack',
'bang',
'banger',
'barf',
'bastard',
'bastards',
'bawdy',
'beaner',
'beardedclam',
'beastiality',
'beatch',
'beater',
'beaver',
'beer',
'beeyotch',
'beotch',
'biatch',
'bigtits',
'big tits',
'bimbo',
'bitch',
'bitched',
'bitches',
'bitchy',
'blow job',
'blow',
'blowjob',
'blowjobs',
'bod',
'bodily',
'boink',
'bollock',
'bollocks',
'bollok',
'corpse',
'bone',
'boned',
'boner',
'boners',
'bong',
'boob',
'boobies',
'boobs',
'booby',
'booger',
'bookie',
'bootee',
'bootie',
'booty',
'booze',
'boozer',
'boozy',
'bosom',
'bosomy',
'bowel',
'bowels',
'bra',
'brassiere',
'breast',
'breasts',
'bugger',
'bukkake',
'bullshit',
'bull shit',
'bullshits',
'bullshitted',
'bullturds',
'bung',
'busty',
'butt',
'butt fuck',
'buttfuck',
'buttfucker',
'buttfucker',
'buttplug',
'c.o.c.k.',
'c.u.n.t',
'caca',
'cahone',
'cameltoe',
'carpetmuncher',
'cawk',
'cervix',
'chinc',
'chincs',
'chink',
'chink',
'chode',
'chodes',
'climax',
'clit',
'clitoris',
'clitorus',
'clits',
'clitty',
'cocain',
'cocaine',
'cock',
'coital',
'commie',
'condom',
'coon',
'coons',
'crabs',
'crack',
'cracker',
'crap',
'crappy',
'cum',
'cummin',
'cumming',
'cumshot',
'cumshots',
'cumslut',
'cumstain',
'cunilingus',
'cunnilingus',
'cunny',
'cunt',
'cunts',
'dago',
'dagos',
'dammit',
'damn',
'dick',
'diddle',
'dike',
'dildo',
'dildos',
'diligaf',
'dillweed',
'dimwit',
'dingle',
'dipship',
'doggie-style',
'doggy-style',
'dong',
'doofus',
'doosh',
'dopey',
'douche',
'douchebag',
'douchebags',
'douchey',
'drunk',
'dumass',
'dumbass',
'dumbasses',
'dummy',
'dyke',
'dykes',
'ejaculate',
'enlargement',
'erect',
'erection',
'erotic',
'essohbee',
'extacy',
'extasy',
'fannybandit',
'fart',
'fartknocker',
'fat',
'felch',
'felcher',
'felching',
'fellate',
'fellatio',
'feltch',
'feltcher',
'fisted',
'fisting',
'fisty',
'floozy',
'foad',
'fondle',
'foobar',
'foreskin',
'freex',
'frigg',
'frigga',
'fuk',
'fvck',
'fxck',
'gae',
'gai',
'ganja',
'gay',
'gays',
'gey',
'gfy',
'ghay',
'ghey',
'gigolo',
'glans',
'goatse',
'goldenshower',
'gonad',
'gonads',
'gook',
'gringo',
'gspot',
'g-spot',
'gtfo',
'guido',
'handjob',
'hardon',
'hebe',
'heeb',
'hell',
'hemp',
'heroin',
'herp',
'herpes',
'herpy',
'hitler',
'hiv',
'hobag',
'homey',
'homo',
'homoey',
'honky',
'hooch',
'hookah',
'hooker',
'hoor',
'hootch',
'hooter',
'hooters',
'horny',
'hump',
'humped',
'humping',
'hussy',
'hymen',
'inbred',
'incest',
'injun',
'jackass',
'jack',
'jackoff',
'jap',
'japs',
'jerk',
'jerked',
'jerkoff',
'jism',
'jiz',
'jizm',
'jizz',
'jizzed',
'junkie',
'junky',
'kike',
'kikes',
'kill',
'kinky',
'klan',
'knobend',
'kooch',
'kooches',
'kootch',
'kraut',
'labia',
'lech',
'leper',
'lesbians',
'lesbo',
'lesbos',
'lez',
'lezbian',
'lezbians',
'lezbo',
'lezbos',
'lezzie',
'lezzies',
'lezzy',
'lmao',
'lmfao',
'loin',
'loins',
'lube',
'lusty',
'mams',
'massa',
'maxi',
'menses',
'menstruate',
'menstruation',
'meth',
'm-fucking',
'mofo',
'molest',
'moolie',
'moron',
'nad',
'nads',
'naked',
'napalm',
'nappy',
'nazi',
'nimrod',
'ninny',
'nipple',
'nooky',
'nympho',
'opiate',
'opium',
'oral',
'orally',
'organ',
'orgasm',
'orgy',
'ovary',
'ovum',
'paddy',
'paki',
'pantie',
'panties',
'panty',
'pastie',
'pasty',
'pcp',
'pecker',
'pee',
'peepee',
'penetrate',
'penetration',
'penial',
'penile',
'penis',
'perversion',
'peyote',
'phalli',
'phallic',
'phuck',
'pillowbiter',
'pimp',
'pinko',
'piss',
'pissed',
'pissoff',
'piss-off',
'pms',
'polack',
'pollock',
'poon',
'poontang',
'porn',
'porno',
'pornography',
'pot',
'potty',
'prick',
'prig',
'prostitute',
'prude',
'pube',
'pubic',
'pubis',
'punkass',
'punky',
'puss',
'pussies',
'pussy',
'puto',
'queaf',
'queef',
'queef',
'queer',
'queero',
'queers',
'quicky',
'quim',
'racy',
'raunch',
'rectal',
'rectum',
'rectus',
'reefer',
'reetard',
'reich',
'retard',
'retarded',
'revue',
'rimjob',
'rum',
'rump',
'rumprammer',
'ruski',
's.o.b.',
'sadism',
'sadist',
'scag',
'scantily',
'schizo',
'schlong',
'screw',
'screwed',
'scrog',
'scrot',
'scrote',
'scrotum',
'scrud',
'scum',
'seaman',
'seamen',
'seduce',
'semen',
'sex',
'sexual',
'shiz',
'sissy',
'skag',
'skank',
'slave',
'sleaze',
'sleazy',
'slut',
'sluts',
'smegma',
'smut',
'smutty',
'snatch',
'sniper',
'snuff',
'sodom',
'souse',
'soused',
'sperm',
'spooge',
'spunk',
'steamy',
'stfu',
'stiffy',
'stoned',
'strip',
'stroke',
'stupid',
'suck',
'sucked',
'sucking',
'sumofabiatch',
'tampon',
'tard',
'tawdry',
'teabag',
'teat',
'terd',
'teste',
'testee',
'testes',
'testicle',
'testis',
'thrust',
'thug',
'tinkle',
'toke',
'toots',
'tramp',
'trashy',
'tubgirl',
'turd',
'tush',
'twat',
'twats',
'ugly',
'undies',
'unwed',
'urinal',
'urine',
'uterus',
'uzi',
'vag',
'vagina',
'valium',
'viagra',
'virgin',
'vixen',
'vodka',
'vomit',
'voyeur',
'vulgar',
'vulva',
'wad',
'wang',
'wank',
'wanker',
'wazoo',
'wedgie',
'weed',
'weenie',
'weewee',
'weiner',
'weirdo',
'whitey',
'whiz',
'whore',
'womb',
'woody',
'wop',
'yeasty',
'diarrhea',
'gimp',
'midget'
]

adjectives_b = [
    'tard',
    'waffle',
    'butter',
    'batter',
    'blaster',
    'chowder',
    'flake',
    'nugget',
    'berry',
    'stain',
    'muncher',
    'shaver',
    'wit',
    'licker',
    'humper',
    'chunder',
    'face',
    'goblin',
    'wallop',
    'flapper',
    'slapper',
    'biter',
    'breath',
    '-for-brains',
    'wiper',
    'head',
    'eater',
    'chomper',
    'dumper',
    'hole',
    'bag',
    'dipper',
    'face',
    'flipper',
    'head',
    'heads',
    'ish',
    '-ish',
    'ripper',
    'pincher',
    'robber',
    'worshipper',
    'pleaser',
    'sipper',
    'weed',
    'whipper',
    'zipper',
    'bang',
    'hole',
    'holes',
    'master',
    'munch',
    'wipe',
    'wipes',
    'plunger',
    'lover',
    'muffin',
    'gremlin',
    'meister',
    'stuffer',
    'burglar',
    'singer',
    'taster',
    'gobbler',
    'captain',
    'lord',
    'commander'
]

part_b = [
    'hibbo',
    'sclibbo',
    'flibble',
    'dibble',
    'blongo',
    'scrandle',
    'lapso',
    'flabble',
    'dibbledeedoo',
    'blerp',
    'blep',
    'can',
    'higgle',
    'scriggle',
    'flappo',
    'sloorp',
    'tingle',
    'blang',
    'blooosh',
    'florks',
    'crango',
    'stango',
    'wango',
    'tango',
    'flibbledy',
    'slappo',
    'woooosh',
    'nononono',
    'grappo',
    'mork',
    'pork',
    'orkbork',
    'stork',
    'gibble',
    'barble',
    'flibble',
    'flobble'
]

realwords = ['adversary', 'aplomb', 'apprehensive', 'aptitude', 'attentive', 'banish', 'barricade', 'bluff', 'brackish', 'brandish', 'circumference', 'commotion', 'concoction', 'conspicuous', 'contortion', 'counter', 'cunning', 'debris', 'defiance', 'deft', 'destination', 'diminish', 'disdain', 'dismal', 'dispel', 'eavesdrop', 'egregious', 'ember', 'emerge', 'engross', 'exasperation', 'exhilarate', 'falter', 'foresight', 'fragrance', 'furtive', 'grueling', 'gusto', 'habitation', 'hasten', 'headway', 'ignite', 'illuminate', 'impending', 'imperious', 'jabber', 'jargon', 'jostle', 'jut', 'kindle', 'knoll', 'luminous', 'malleable', 'materialize', 'meander', 'meticulous', 'misgiving', 'momentum', 'monotonous', 'multitude', 'muster', 'narrate', 'obscure', 'ominous', 'outlandish', 'persistent', 'pertinent', 'plenteous', 'potential', 'precipice', 'pristine', 'quell', 'recluse', 'recuperate', 'replenish', 'repugnant', 'restitution', 'sabotage', 'scarcity', 'scurry', 'serenity', 'sociable', 'somber', 'specimen', 'stamina', 'subside', 'swagger', 'swarm', 'tactic', 'terse', 'translucent', 'uncanny', 'unsightly', 'versatile', 'vigilant', 'vulnerable', 'waft', 'waver', 'weather', 'zeal' 'ad hominem', 'alliteration', 'anaphora', 'anastrophe', 'antithesis', 'apostrophe', 'apposition', 'archaism', 'assonance', 'asyndeton', 'bathos', 'cacophony', 'chiasmus', 'colloquialism', 'dialectic', 'discourse', 'epigraph', 'epithet', 'eponym', 'eristic', 'euphemism', 'euphony', 'hyperbole', 'hypothesis', 'invective', 'irony', 'jargon', 'litotes', 'maxim', 'metaphor', 'metonymy', 'non sequitur', 'onomatopoeia', 'oxymoron', 'paradox', 'parallelism', 'parenthesis', 'parody', 'personification', 'pleonasm', 'rebuttal', 'repetition', 'simile', 'syllogism', 'synecdoche', 'tautology', 'thesis', 'trope', 'understatement', 'zeugma', 'industrialization', 'urbanization', 'tenement', 'muckraker', 'union', 'strike', 'monopoly', 'militarism', 'nationalism', 'neutrality', 'alliance', 'propaganda', 'pandemic', 'prohibition', 'suffrage', 'speculation', 'stock', 'depression', 'employment', 'foreclosure', 'bumble', 'gruel', 'beverage', 'energy', 'admirable', 'employee', 'cargo', 'adult', 'enlarge', 'collide', 'depend', 'blizzard', 'debate', 'adolescent', 'candidate', 'ballet', 'enormous', 'dazzle', 'advisor', 'yearling', 'beseech', 'besiege', 'bias', 'bleak', 'bliss', 'bluff', 'boisterous', 'solemn', 'absurd', 'abuse', 'champion', 'emergency', 'banquet', 'batch', 'admiral', 'embrace', 'flimsy', 'colt', 'bargain', 'idyllic', 'makeshift', 'ordeal', 'wake', 'camp', 'scab', 'scamper', 'scan', 'scar', 'skill', 'skillet', 'skit', 'smart', 'sting', 'incarcerate', 'misdemeanor', 'criminal', 'felony', 'prosecutor', 'liability', 'legislate', 'overview', 'civil', 'preponderance', 'defendant', 'initiate', 'prosecution', 'plaintiff', 'statute', 'element', 'regulate', 'theft', 'responsible', 'legislator', 'federal', 'furthermore', 'define', 'illegal', 'impact', 'violation', 'procedure', 'resolve', 'established', 'constitute', 'persuade', 'code', 'establish', 'jury', 'dispute', 'structure', 'contrast', 'conviction', 'accident', 'absence', 'organization', 'victim', 'yield', 'consist', 'title', 'murder', 'extend', 'consequence', 'operation', 'evidence', 'government', 'Congress', 'property', 'court', 'evolutionary', 'fertility', 'subliminal', 'savanna', 'cue', 'caveat', 'infidelity', 'undercurrent', 'fascinate', 'adhesion', 'symmetrical', 'mechanism', 'subtly', 'mammal', 'symmetry', 'ostensibly', 'adultery', 'subtle', 'presumably', 'fidelity', 'substantial', 'subsequent', 'linger', 'concealed', 'consciousness', 'phantom', 'flee', 'dowdy', 'fugitive', 'heckle', 'docile', 'sapling', 'mock', 'standoffish', 'illusion', 'stalk', 'conspicuous', 'bluff', 'discard', 'affectionate', 'accumulate', 'vivid', 'outcome', 'snub', 'elegant', 'protest', 'embrace', 'meek', 'object', 'candor', 'harass', 'luminous', 'proclamation', 'thrash', 'sonorous', 'innuendo', 'jut', 'petty', 'tone', 'restrain', 'outlandish', 'hue', 'protrude', 'tranquil', 'mishap', 'guzzle', 'bizarre', 'gorge', 'prod', 'grave', 'vexation', 'garnish', 'placid', 'menace', 'exodus', 'pneumonia', 'sustainability', 'respiratory', 'pathogen', 'antibiotic', 'contaminate', 'devastate', 'iteration', 'infrastructure', 'particle', 'patent', 'organelle', 'vacuole', 'cytoplasm', 'mitochondrion', 'cell', 'flagellum', 'membrane', 'protein', 'enzyme', 'plasma', 'matrix', 'photosynthesis', 'nucleus', 'wavelength', 'glucose', 'centrifuge', 'pore', 'doublet', 'algae', 'convoluted', 'chlorophyll', 'primary', 'digest', 'specimen', 'convert', 'nuclear', 'hormone', 'gene', 'reproductive', 'muscle', 'secretion', 'biologist', 'genetic', 'bacteria', 'enzyme', 'molecule', 'catalyst', 'inhibitor', 'reaction', 'biological', 'synthesis', 'cell', 'chemical', 'organelle', 'mitochondrion', 'centrifuge', 'enzyme', 'cell', 'chlorophyll', 'membrane', 'pestle', 'module', 'nucleus', 'technique', 'homogeneous', 'predominate', 'analyze', 'biological', 'component', 'specific', 'harvest', 'neuroscience', 'exclusion', 'mitochondrion', 'centrifuge', 'optimal', 'enzyme', 'cell', 'chlorophyll', 'membrane', 'pestle', 'differential', 'nucleus', 'contamination', 'homogeneous', 'predominate', 'biological', 'dendrite', 'proliferation', 'inhibit', 'domain', 'horrify', 'anthology', 'literary', 'retrospect', 'nostalgia', 'symbiosis', 'pattern', 'connection', 'link', 'sequence', 'anchor', 'lasso', 'capture', 'seize', 'grip', 'seize', 'stronghold', 'lasso', 'capture', 'seize', 'grip', 'seize', 'stronghold', 'store', 'customer', 'contest', 'cashier', 'plastic', 'invidious', 'alias', 'antithesis', 'bilk', 'bombastic', 'cacophony', 'cadence', 'defunct', 'delineate', 'emaciated', 'encore', 'fickle', 'fidelity', 'grandiose', 'gratuitous', 'haughty', 'hedonist', 'idiosyncratic', 'immerse', 'knell', 'lithe', 'acumen', 'adamant', 'anonymous', 'antiseptic', 'audible', 'benign', 'bequeath', 'calamity', 'calibrate', 'callous', 'comprehensive', 'deface', 'defamatory', 'eloquent', 'encumber', 'fabricate', 'figurative', 'flabbergasted', 'hiatus', 'hierarchy', 'altruistic', 'assent', 'benefactor', 'chivalrous', 'clemency', 'dearth', 'diffident', 'discrepancy', 'embark', 'indomitable', 'pungent', 'temerity', 'truculent', 'unfeigned', 'sincere', 'virulent', 'stagnate', 'trepidation', 'verbose', 'wallow', 'zenith', 'comport', 'behave', 'gait', 'score', 'ignoramus', 'reverence', 'euphoria', 'unequivocal', 'don', 'eccentric', 'keenly', 'keen', 'impotence', 'preamble', 'tenacity', 'antagonist', 'protagonist', 'epilogue', 'legacy', 'lore', 'environment', 'interview', 'plot', 'etymology', 'alibi', 'evidence', 'inference', 'investigator', 'mystery', 'red herring', 'sleuth', 'suspect', 'victim', 'witness', 'idiom', 'imagery', 'meter', 'metaphor', 'simile', 'alliteration', 'onomatopoeia', 'memoir', 'personification', 'realism', 'engage', 'insanity', 'accuse', 'agree', 'assume', 'presume', 'respond', 'monumental', 'traumatize', 'therapist', 'differential', 'clinician', 'client', 'vulnerability', 'vulnerable', 'counseling', 'counselor', 'imbalance', 'undercurrent', 'unilateral', 'syndrome', 'inherent', 'intern', 'proctor', 'omnipotence', 'ethics', 'power', 'inclusive', 'depressed', 'ignore', 'coercion', 'unified', 'relevant', 'dominating', 'ethic', 'assumption', 'unify', 'faulty', 'enhance', 'impaired', 'management', 'fraught', 'depress', 'graduate', 'relationship', 'abuse', 'powerful', 'exclusively', 'license', 'successful', 'exploit', 'injustice', 'dependent', 'prominent', 'influence', 'perceived', 'professional', 'culture', 'reflection', 'exception', 'discussion', 'universal', 'distress', 'evident', 'tend', 'setting', 'anxious', 'benefit', 'functionality', 'grid', 'incremental', 'severance', 'integrate', 'update', 'distribution', 'customer', 'deliver', 'automate', 'scope', 'implementation', 'automation', 'workforce', 'deployment', 'operational', 'envisage', 'proactive', 'investment', 'mitigation', 'incorporate', 'forecast', 'system', 'integrated', 'benefit', 'feedback', 'release', 'include', 'data', 'datum', 'appendix', 'replacement', 'upgrade', 'underpin', 'productivity', 'risk', 'process', 'option', 'impact', 'regulatory', 'implemented', 'schedule', 'reduction', 'solution', 'increase', 'delivery', 'contingency', 'savings', 'ensure', 'methodology', 'require', 'sap', 'additional', 'operate', 'management', 'improvement', 'capability', 'expenditure', 'sustainable', 'facilitate', 'incorporated', 'improve', 'deploy', 'implement', 'reduce', 'summary', 'compliance', 'assumption', 'enhance', 'design', 'transformation', 'asset', 'control', 'incentive', 'allocation', 'replace', 'sanction', 'procurement', 'infrastructure', 'mitigate', 'validation', 'arbitrage', 'seamless', 'office', 'mobile', 'meter', 'achieve', 'executive', 'analysis', 'associate', 'support', 'align', 'efficiency', 'strategy', 'integration', 'emergency', 'core', 'approve', 'financial', 'input', 'leverage', 'multiple', 'estimate', 'objective', 'database', 'disruption', 'identify', 'requirement', 'necessitate', 'information', 'productive', 'enhanced', 'submission', 'current', 'impacted', 'model', 'restructure', 'national', 'employee', 'phase', 'overrun', 'breed', 'coincidental', 'framework', 'exist', 'archive', 'level', 'component', 'project', 'manual', 'complete', 'staff', 'approval', 'manage', 'scenario', 'enable', 'capture', 'constraint', 'interface', 'displacement', 'continue', 'device', 'tactical', 'performance', 'anticipate', 'contractor', 'plan', 'repository', 'sanctioned', 'compare', 'repair', 'remaining', 'value', 'adversely', 'vendor', 'hurdle', 'bulk', 'consequential', 'delegation', 'eliminate', 'provider', 'graph', 'board', 'efficiently', 'suite', 'steer', 'total', 'robust', 'tool', 'operative', 'resource', 'engagement', 'environmental', 'automated', 'sponsor', 'user', 'anticipated', 'describe', 'disparate', 'application', 'governance', 'contact', 'base', 'alignment', 'subsequently', 'test', 'processed', 'comprise', 'aggregate', 'propose', 'stewardship', 'recommend', 'server', 'funding', 'primarily', 'provide', 'migrate', 'communications', 'annual', 'turnover', 'closure', 'undertake', 'future', 'currently', 'complexity', 'issue', 'dispatch', 'configuration', 'through', 'result', 'calculate', 'maintenance', 'enquiry', 'focus', 'relative', 'consistent', 'minimum', 'diagram', 'remain', 'coupled', 'interaction', 'attributable', 'documented', 'plus', 'significant', 'invest', 'readiness', 'relationship', 'acceleration', 'incorporation', 'retirement', 'workshop', 'initial', 'delegate', 'table', 'approximately', 'maintain', 'smart', 'consequent', 'efficient', 'delay', 'accurate', 'prone', 'exceed', 'critical', 'service', 'blueprint', 'assume', 'avoidance', 'communication', 'adjustment', 'introduction', 'completion', 'expertise', 'bespoke', 'senior', 'effective', 'depreciation', 'availability', 'inadequate', 'available', 'transform', 'pertinent', 'access', 'director', 'comprehensive', 'drive', 'assets', 'retrieve', 'embedded', 'predominantly', 'accountable', 'hub', 'agency', 'need', 'define', 'embed', 'execute', 'complex', 'limit', 'defining', 'address', 'initiate', 'compatible', 'factor', 'delight', 'manager', 'remit', 'committee', 'obligation', 'autumn', 'intensive', 'network', 'failure', 'job', 'addition', 'satisfaction', 'uncertainty', 'recommendation', 'adherence', 'recurring', 'expected', 'initially', 'previous', 'location', 'develop', 'procedure', 'consequently', 'reflect', 'complaint', 'assess', 'execution', 'bespeak', 'accordance', 'investigation', 'quality', 'allowance', 'industrial', 'balance', 'budget', 'criterion', 'margin', 'negative', 'prior', 'enabling', 'likely', 'range', 'flow', 'articulate', 'frustration', 'review', 'potentially', 'possible', 'decision', 'environment', 'dependent', 'appropriate', 'technology', 'nominal', 'alternative', 'successfully', 'timely', 'submit', 'discharge', 'consistency', 'basis', 'obsolete', 'flexible', 'inform', 'specific', 'retain', 'software', 'distribute', 'proportion', 'progress', 'grade', 'approach', 'operation', 'portal', 'relate', 'score', 'reward', 'consumer', 'consistently', 'inconsistent', 'peak', 'indicate', 'warehouse', 'implication', 'train', 'positive', 'negotiate', 'priority', 'exclude', 'unit', 'element', 'track', 'transfer', 'couple', 'standard', 'final', 'creation', 'adjusted', 'prepare', 'legacy', 'deem', 'major', 'perspective', 'script', 'explore', 'link', 'recur', 'payment', 'engineer', 'defer', 'conjunction', 'authority', 'dictate', 'respectively', 'create', 'effectively', 'function', 'elements', 'profile', 'construction', 'document', 'extend', 'consequence', 'expanded', 'demonstrate', 'specialist', 'projected', 'consultation', 'essential', 'acceptable', 'balanced', 'consider', 'quotation', 'overall', 'initiative', 'cycle', 'scheduled', 'strategic', 'opportunity', 'accuracy', 'combine', 'incident', 'ability', 'considered', 'creative', 'illustrate', 'trend', 'compensation', 'calculation', 'restriction', 'discretion', 'tailor', 'secure', 'acceptance', 'preference', 'precise', 'excessive', 'excellence', 'extension', 'values', 'technique', 'register', 'contract', 'guide', 'connection', 'description', 'modify', 'continuous', 'communicate', 'removal', 'procure', 'product', 'equipped', 'electricity', 'successful', 'architecture', 'intelligence', 'section', 'period', 'fund', 'adjust', 'central', 'directly', 'representative', 'technical', 'involve', 'subject', 'engage', 'potential', 'equip', 'request', 'sustained', 'regime', 'gap', 'inflation', 'particularly', 'force', 'remainder', 'introduce', 'calculated', 'confidence', 'seek', 'arise', 'expensive', 'avoid', 'apply', 'selection', 'penalty', 'compromise', 'cynical', 'enfeeble', 'actuate', 'disbursement', 'attachment', 'nation', 'government']

punctuation = [
    '?',
    '.',
    '!'
]

def sentence():
    swear = f'{random.choice(adjectives_a)}{random.choice(adjectives_b)}'
    sentence = f'{random.choice(part_a)} {random.choice(part_b)} {swear} {random.choice(realwords)}{random.choice(punctuation)}'
    new_sentence = []
    for i in sentence.split():
	    new_sentence.append(i)
    random.shuffle(new_sentence)
    shuffled = (' '.join(new_sentence))
    print(shuffled, end = " ")

def swears():
    swear = f'{random.choice(adjectives_a)}{random.choice(adjectives_b)}'
    print(swear)

choice = input('press 1 for sentences or 2 for just swears ')
if choice == '1':
    x = int(input('lorem sentences: '))
    for i in range(x):
        sentence()
    print('\n')
elif choice == '2':
    x = int(input('number of swears: '))
    for i in range(x):
        swears()
else:
    print('not a valid choice')
