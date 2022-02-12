# lyrics-visualiser
This repository contains a python app written with dash that visualises lyrics based on their section/line-based self-similiarity. 
The app is automatically deployed to heroku after each successful commit to the repository:
<a href="http://dashlyrics.herokuapp.com/">http://lyricsvis.herokuapp.com/</a>

It is inspired by https://github.com/colinmorris/SongSim. 
The self-similiarity is however computed based on the song structure (sections) using the jaccard-distance instead of matching single words.
Further the lyrics are loaded using the genius.com api giving it access to a huge lyrics-database.

## Report:

The automated documentation will guide you through project in terms of the assignment:

<a href="https://jliekenbrock.github.io/lyrics-visualiser" target="_blank">Documentation</a>