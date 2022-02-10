# lyrics-visualiser
This repository contains a python app written with dash that visualises lyrics based on their section/line-based self-similiarity. 
The app is automatically deployed to heroku after each successful commit to the repository:
<a href="http://dashlyrics.herokuapp.com/">http://lyricsvis.herokuapp.com/</a>

It is inspired by https://github.com/colinmorris/SongSim. 
The self-similiarity is however computed based on the song structure (sections) using the jaccard-distance instead of matching single words.
Further the lyrics are loaded using the genius.com api giving it access to a huge lyrics-database.


# links:
<a href="https://github.com/JLiekenbrock/lyrics-visualiser">1: git</a>

<a href="https://github.com/JLiekenbrock/lyrics-visualiser/tree/main/UML" target="_blank">2: UML</a>

<a href="https://miro.com/app/board/uXjVOccEnLI=/?invite_link_id=553649028755" target="_blank">3: Event-Storming/DDD</a>

<a href="https://sonarcloud.io/summary/new_code?id=JLiekenbrock_lyrics-visualiser" target="_blank">4: Metrics</a>

<a href="https://github.com/JLiekenbrock/lyrics-visualiser/blob/main/clean_code.txt" target="_blank">5: Clean Code</a>

<a href="https://app.travis-ci.com/github/JLiekenbrock/lyrics-visualiser" target="_blank">6: Travis CI, runs tests and uploads Documentation generated with pdoc3 to Github Pages</a>

<a href="https://jliekenbrock.github.io/lyrics-visualiser/index.html" target="_blank">6: automated Documentation</a>

