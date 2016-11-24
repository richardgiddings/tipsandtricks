# README #

An application designed to store commands useful for development against sections.

A Section has a title.
A Tip has a title, a place to put notes and a link to the Section it belongs to.
A Trick has a command and a link to the Tip it belongs to.

**Develop branch**

Re-implemented using React and react-router for the front-end. New Django requirements are in the requirements text file for this branch.

In addition to the packages installed from package.json I also installed browserify and uglify-js globally using npm (npm install -g browserify uglify-js').