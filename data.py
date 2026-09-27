"""
Self-contained movie dataset for the Movie Universe Graph Explorer.

Each entry has: title, genre, overview (short plot summary used for
the recommender), and cast (list of actor names used to build the graph).

This dataset is hand-curated to be small but well-connected, so that
BFS path-finding between actors produces interesting, non-trivial results.
No external download or API key is required to run this project.
"""

MOVIES = [
    {
        "title": "Inception",
        "genre": "Sci-Fi Thriller",
        "overview": "A skilled thief who steals secrets through dream-sharing technology is given a chance to have his criminal history erased by planting an idea into a target's subconscious.",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Tom Hardy", "Cillian Murphy"],
    },
    {
        "title": "The Dark Knight",
        "genre": "Action Crime",
        "overview": "Batman raises the stakes in his war on crime, facing a criminal mastermind known as the Joker who wants to plunge Gotham into anarchy.",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Cillian Murphy", "Gary Oldman"],
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi Drama",
        "overview": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival as Earth becomes uninhabitable.",
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine", "Cillian Murphy"],
    },
    {
        "title": "The Revenant",
        "genre": "Adventure Drama",
        "overview": "A frontiersman on a fur trading expedition fights for survival after being mauled by a bear and left for dead by members of his own hunting team.",
        "cast": ["Leonardo DiCaprio", "Tom Hardy", "Will Poulter", "Domhnall Gleeson"],
    },
    {
        "title": "Dunkirk",
        "genre": "War Drama",
        "overview": "Allied soldiers are evacuated during a fierce battle in World War II amid chaos and danger on the beaches of Dunkirk.",
        "cast": ["Fionn Whitehead", "Tom Hardy", "Cillian Murphy", "Mark Rylance"],
    },
    {
        "title": "The Wolf of Wall Street",
        "genre": "Biography Comedy",
        "overview": "Based on the true story of Jordan Belfort, from his rise to a wealthy stockbroker to his fall involving crime and corruption on Wall Street.",
        "cast": ["Leonardo DiCaprio", "Jonah Hill", "Margot Robbie", "Matthew McConaughey"],
    },
    {
        "title": "Once Upon a Time in Hollywood",
        "genre": "Comedy Drama",
        "overview": "A faded television actor and his stunt double strive to achieve fame and success in the film industry during the final years of Hollywood's golden age.",
        "cast": ["Leonardo DiCaprio", "Brad Pitt", "Margot Robbie", "Emile Hirsch"],
    },
    {
        "title": "Fight Club",
        "genre": "Drama",
        "overview": "An insomniac office worker and a soap maker form an underground fight club that evolves into much more.",
        "cast": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"],
    },
    {
        "title": "Se7en",
        "genre": "Crime Thriller",
        "overview": "Two detectives hunt a serial killer who uses the seven deadly sins as his motives.",
        "cast": ["Brad Pitt", "Morgan Freeman", "Gwyneth Paltrow", "Kevin Spacey"],
    },
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
    },
    {
        "title": "Batman Begins",
        "genre": "Action Crime",
        "overview": "After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.",
        "cast": ["Christian Bale", "Michael Caine", "Liam Neeson", "Morgan Freeman"],
    },
    {
        "title": "The Prestige",
        "genre": "Mystery Drama",
        "overview": "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.",
        "cast": ["Christian Bale", "Hugh Jackman", "Scarlett Johansson", "Michael Caine"],
    },
    {
        "title": "Les Miserables",
        "genre": "Musical Drama",
        "overview": "In 19th-century France, an ex-convict pursued by a persistent policeman agrees to care for a factory worker's daughter.",
        "cast": ["Hugh Jackman", "Russell Crowe", "Anne Hathaway", "Amanda Seyfried"],
    },
    {
        "title": "Gladiator",
        "genre": "Action Drama",
        "overview": "A former Roman general sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "cast": ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"],
    },
    {
        "title": "Joker",
        "genre": "Crime Drama",
        "overview": "A mentally troubled stand-up comedian embarks on a downward spiral that leads to the creation of an iconic villain.",
        "cast": ["Joaquin Phoenix", "Robert De Niro", "Zazie Beetz"],
    },
    {
        "title": "Taxi Driver",
        "genre": "Crime Drama",
        "overview": "A mentally unstable veteran works as a nighttime taxi driver in New York City, where the perceived decadence and sleaze fuels his urge for violent action.",
        "cast": ["Robert De Niro", "Jodie Foster", "Cybill Shepherd"],
    },
    {
        "title": "The Departed",
        "genre": "Crime Thriller",
        "overview": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
        "cast": ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson", "Mark Wahlberg"],
    },
    {
        "title": "Good Will Hunting",
        "genre": "Drama",
        "overview": "A janitor at MIT with a gift for mathematics must confront his personal demons with the help of a psychologist after getting in trouble with the law.",
        "cast": ["Matt Damon", "Robin Williams", "Ben Affleck", "Minnie Driver"],
    },
    {
        "title": "The Bourne Identity",
        "genre": "Action Thriller",
        "overview": "A man is picked up by a fishing boat, suffering from amnesia, before racing to elude assassins and attempting to regain his memory.",
        "cast": ["Matt Damon", "Franka Potente", "Chris Cooper"],
    },
    {
        "title": "Argo",
        "genre": "Thriller Drama",
        "overview": "Acting under the cover of a Hollywood producer scouting a location for a science fiction film, a CIA agent launches a dangerous operation to rescue six Americans in Tehran.",
        "cast": ["Ben Affleck", "Bryan Cranston", "John Goodman"],
    },
    {
        "title": "Pulp Fiction",
        "genre": "Crime Drama",
        "overview": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis"],
    },
    {
        "title": "Django Unchained",
        "genre": "Western Drama",
        "overview": "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
        "cast": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio", "Samuel L. Jackson"],
    },
    {
        "title": "Kill Bill",
        "genre": "Action Crime",
        "overview": "After awakening from a four-year coma, a former assassin wreaks vengeance on the team of assassins who betrayed her.",
        "cast": ["Uma Thurman", "David Carradine", "Daryl Hannah", "Lucy Liu"],
    },
    {
        "title": "Die Hard",
        "genre": "Action Thriller",
        "overview": "An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at a Los Angeles skyscraper.",
        "cast": ["Bruce Willis", "Alan Rickman", "Bonnie Bedelia"],
    },
    {
        "title": "The Sixth Sense",
        "genre": "Mystery Thriller",
        "overview": "A boy who communicates with spirits seeks the help of a disheartened child psychologist.",
        "cast": ["Bruce Willis", "Toni Collette", "Haley Joel Osment"],
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action Sci-Fi",
        "overview": "After a devastating snap, the remaining Avengers assemble to reverse the damage and restore balance to the universe.",
        "cast": ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo"],
    },
    {
        "title": "Iron Man",
        "genre": "Action Sci-Fi",
        "overview": "A billionaire industrialist and genius inventor builds a powered exoskeleton and becomes a superhero after being held captive.",
        "cast": ["Robert Downey Jr.", "Gwyneth Paltrow", "Jeff Bridges"],
    },
    {
        "title": "Sherlock Holmes",
        "genre": "Action Mystery",
        "overview": "Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England.",
        "cast": ["Robert Downey Jr.", "Jude Law", "Rachel McAdams"],
    },
    {
        "title": "Captain America: The First Avenger",
        "genre": "Action Sci-Fi",
        "overview": "A rejected military soldier transforms into Captain America after taking a dose of a Super-Soldier serum, but he is soon enlisted to stop a Nazi force.",
        "cast": ["Chris Evans", "Hayley Atwell", "Sebastian Stan", "Tommy Lee Jones"],
    },
    {
        "title": "Knives Out",
        "genre": "Mystery Comedy",
        "overview": "A detective investigates the death of a patriarch of an eccentric, combative family after he is found dead at his estate.",
        "cast": ["Daniel Craig", "Chris Evans", "Ana de Armas", "Jamie Lee Curtis"],
    },
    {
        "title": "Skyfall",
        "genre": "Action Thriller",
        "overview": "Bond's loyalty to M is tested as her past comes back to haunt her, threatening MI6 itself.",
        "cast": ["Daniel Craig", "Judi Dench", "Javier Bardem"],
    },
    {
        "title": "No Time to Die",
        "genre": "Action Thriller",
        "overview": "James Bond has left active service, but his peace is short-lived when an old friend recruits him to help rescue a kidnapped scientist.",
        "cast": ["Daniel Craig", "Rami Malek", "Lea Seydoux", "Ana de Armas"],
    },
    {
        "title": "Bohemian Rhapsody",
        "genre": "Biography Drama",
        "overview": "A chronicle of the years leading up to Queen's legendary appearance at the 1985 Live Aid concert, centered on lead singer Freddie Mercury.",
        "cast": ["Rami Malek", "Lucy Boynton", "Gwilym Lee"],
    },
    {
        "title": "Blade Runner 2049",
        "genre": "Sci-Fi Drama",
        "overview": "A young blade runner unearths a long-buried secret that leads him to track down former blade runner Rick Deckard, who has been missing for years.",
        "cast": ["Ryan Gosling", "Harrison Ford", "Ana de Armas", "Jared Leto"],
    },
    {
        "title": "La La Land",
        "genre": "Musical Romance",
        "overview": "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.",
        "cast": ["Ryan Gosling", "Emma Stone", "John Legend"],
    },
    {
        "title": "Star Wars: The Force Awakens",
        "genre": "Sci-Fi Adventure",
        "overview": "As a new threat rises, old and new heroes come together to battle the forces of the dark side and restore balance to the galaxy.",
        "cast": ["Daisy Ridley", "Harrison Ford", "Adam Driver", "Oscar Isaac"],
    },
    {
        "title": "Indiana Jones and the Last Crusade",
        "genre": "Adventure",
        "overview": "In 1938, archaeologist Indiana Jones sets out to find his father, who has been kidnapped while pursuing the Holy Grail.",
        "cast": ["Harrison Ford", "Sean Connery", "Alison Doody"],
    },
    {
        "title": "Ex Machina",
        "genre": "Sci-Fi Drama",
        "overview": "A young programmer is selected to evaluate the human qualities of a breakthrough humanoid AI, but ends up questioning the true intentions of its creator.",
        "cast": ["Domhnall Gleeson", "Alicia Vikander", "Oscar Isaac"],
    },
    {
        "title": "A Star Is Born",
        "genre": "Musical Drama",
        "overview": "A musician helps a struggling artist find fame as age and alcoholism send his own career into a downward spiral.",
        "cast": ["Bradley Cooper", "Lady Gaga", "Sam Elliott"],
    },
    {
        "title": "Silver Linings Playbook",
        "genre": "Comedy Drama",
        "overview": "After a stint in a mental institution, a former teacher tries to rebuild his life and reconnect with his estranged wife.",
        "cast": ["Bradley Cooper", "Jennifer Lawrence", "Robert De Niro"],
    },
    {
        "title": "The Hunger Games",
        "genre": "Sci-Fi Adventure",
        "overview": "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death.",
        "cast": ["Jennifer Lawrence", "Josh Hutcherson", "Liam Hemsworth", "Woody Harrelson"],
    },
    {
        "title": "X-Men: Days of Future Past",
        "genre": "Action Sci-Fi",
        "overview": "The X-Men send Wolverine to the past to change a major historical event that could result in the extinction of mutants.",
        "cast": ["Hugh Jackman", "James McAvoy", "Michael Fassbender", "Jennifer Lawrence"],
    },
    {
        "title": "Atonement",
        "genre": "Romance Drama",
        "overview": "Fates diverge as a young girl's misunderstanding of what she witnesses leads to a devastating lie that ruins the lives of two young lovers.",
        "cast": ["James McAvoy", "Keira Knightley", "Saoirse Ronan"],
    },
    {
        "title": "Pride & Prejudice",
        "genre": "Romance Drama",
        "overview": "Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy, but Mr. Darcy repeatedly gets in the way of true love.",
        "cast": ["Keira Knightley", "Matthew Macfadyen", "Rosamund Pike"],
    },
]
