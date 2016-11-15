# README #

An application originally designed to store commands useful for development against sections.

A Section has a title.
A Tip has a title, a place to put notes and a link to the Section it belongs to.
A Trick has a command and a link to the Tip it belongs to.

**Main branch**

Currently requires:

- A (Postgres) database to store the Sections, Tips and Tricks.

The application can be seen at:

http://sub4.giddingsr.webfactional.com/tips/

**Develop branch**

Re-implemented using React and react-router for the front-end. New Django requirements are in the requirements text file for this branch.