# The Heroes {#part:heroes}

# The Heroes quests: preliminary report {#heroes-pdd status=ready}

The “Heroes” team is a special task force with the responsibility to make sure that “everything works” and create a smooth experience for the rest of the teams, in terms of developing own projects, integration with other teams and documentation. Apart from that, each of the heroes will also have their own individual quest...

## Motto

Motto: E PLURIBUS UNUM <br/>(From many, unity)


## Overview

### Responsibility

The system architect is ultimately responsible:

* The logical architecture

    * Decomposition in modules
    * Who knows what
    * Who says what to whom

* Definition of performance metrics
* Definition of contracts (bounds on metrics)

### Philosophy

* Look over Duckie teams and remind them of the greater goals of Duckietown.
* Improve Duckietown by using a higher dimensional view.

### Quests

The system architect project can be split into two quests:

1. Ensure that the development of the system goes smoothly (wooden spoon)
2. Develop a framework/tool to formally describe (and later optimize) the system (bronze, silver and gold)

The two quests and their respective descriptions will be explained separately in this document.

## Quest 1

With many teams working on many different parts of the system, chaos is inevitable (without divine intervention). Quest 1 is to minimise the chaos by acting as system-level wactchdog; spotting and addressing interface, contract and dependency issues between the teams.

## Quest 1, Part 1: Mission and scope

### Mission statement

Ensure that the development and integration of the projects into the system goes smoothly and that the resulting system makes sense, and is useful for future duckierations (duckie + generations).

### Project scope

#### What is in scope

* Documentation regarding system architecture (including ownership of functional diagram of system)
* Assisting in contract negotiation
* Giving advice to teams regarding functional layout and interfaces

#### What is out of scope

* Lower level architecture such as message formats, coding conventions etc (see Software Architect project)
* Documentation framework itself (see Knowledge Czarina project)

#### Stakeholders

* The Duckietown masters
* All other project teams that are part of the system

## Quest 1, Part 2: Definition of the problem

### Problem statement

Ensure that all teams know what their goal is and how it fits into the bigger picture.

### Assumptions

The current system makes at least kind-of sense. The current system will be used as a base, onto which improvements or functionality will be added by the projects.

### Approach

* Become one with the goals of Duckietown
    * In order to make Duckietown a better place, one has to keep in mind what “better” means in Duckie terms.
* Be familiar with the current system architecture and track changes
    * This can include having to update the functional diagram, for instance.
    * This also means identifying which teams affect which modules in the diagram
* Keep in close contact with teams
    * All teams will designate a contact person who can contact me whenever they change their project boundaries or have doubts/ need advice on their project’s boundaries/negotiating with other
    * The meetings of some of the other teams will be attended(especially early meetings). Some teams’ meetings have been prioritized since many parts of the system are dependant on their work, namely:
        * Anti-instagram
        * Controllers
        * Navigators
        * Explicit coordination
* Offer nudges in a different direction if needed
* Acting as middleman/helper to facilitate negotiation of contracts between groups
* Monitor status of projects to find possible problems

### Functionality-resources trade-offs

#### Functionality provided

* System integration of project modules

#### Resources required / dependencies / costs

* Biggest resource: Time
* Finding out how to maximise usefulness while being efficient with time

#### Performance measurement

* Approval of Duckietown masters
* Number of miscommunications about contracts between teams (measured in what-the-ducks per second)
* How many things didn’t go wrong
    * Some jobs are of the type where no one notices you until something doesn’t work. You should be the silent angel fixing all the problems that no one even noticed existed.

## Quest 1, Part 3: Preliminary design

### Preliminary plan of deliverables
* Functional diagram of the system
    * The system functional diagram will be the main tool to visualise the system decomposition, and show the relationships between the different teams.
* Documentation of system architecture

## Quest 1, Part 4: Project planning

### First steps for next phase

* Familiarisation with existing system architecture
* Going to group meetings
* Identifying potential problems

#### Relevant Duckietown resources to investigate

* The functional diagram of the system
* Other teams' preliminary design reports

### Risk analysis

** Challenges:**

* Maintaining the balance between project level scope and Duckietown level scope. For instance, teams are focused on completing their project, and might forget the greater vision of Duckietown. This might mean having to convince teams to do slightly more work, for it to be more useful to Duckietown. After all, what’s the point of doing a project if it does not contribute to Duckietown?

* Balancing priorities of quest 1 and 2. Quest 1 is crucial, and takes priority over quest 2. Therefore it will be challenging to find time (main resource) to work on quest 2.

## Quest 2

Where there is a system, there is a want (nay, need) for optimisation. Describing a system’s performance and resource requirements in a quantifiable way is a critical part of being able to benchmark modules and optimise the system.

The different levels of quest 2 are defined as follows:

* **Bronze standard:**
    * Define a formal, qualitative language to describe constraints/requirements between modules.

* **Silver standard:**
    * Each module has table of performance. A tool is developed that can give a qualitative answer to the question: With given configuration x, is the cost/requirements possible with available resources? f(x) smaller equal to Rmax?

* **Gold standard:**
    * Optimization of the system is possible to find the best implementation (most functionality and performance), given the available resources. Given f(x) and Rmax, find the/an optimal configuration x.

## Quest 2, Part 1: Mission and scope

### Mission statement

Formalise the description of the system characteristics, so that eventually the system performance can be optimised for some given resources.

#### Stakeholders

* The Duckietown masters, for they have started me on this quest.
* The future users of Duckietowns, as the Duckietown experience can be optimised per user, given their available resources.

## Quest 2, Part 2: Definition of the problem

### Problem statement

* Find a way to describe all the module requirements, specifications, etc in a formal, quantifiable language.
* Find a way to calculate the requirements and specifications of a whole system or subsystem, based on the requirements and specifications of the individual modules of the system.
* Find a way to calculate the optimal system configuration, based on the desired requirements and specifications of the system.

### Approach

* Research on the topic of formal description of a system
* Find/develop a suitable language to describe module characteristics
* Require groups to compile a description of their respective modules’ characteristics
* Find/develop functions to do mathematics on the language description of modules

### Functionality-resources trade-offs

#### Functionality provided

* Being able to quantifiably describe the system
* Being able to compare and benchmark different implementations of parts of the system

#### Resources required / dependencies / costs

* Time is the main resource that needs to be divided between tasks.
* The current system's characteristics will need to be measured/evaluated somehow to create a database of all the modules' specifications.

#### Performance measurement

* How effectively is the system described, and can the tool provide the answers we seek.
* Which level of funcitonality was provided? (bronze, silver, gold)

## Quest 2, Part 3: Preliminary design

### Preliminary plan of deliverables

* Documentation on the result of the project
* A description of the current system’s characteristics (bronze)
* A program/tool that can give a qualitative answer (yes/no) to the question: Are these resources sufficient for this system configuration? (silver)
* A program/tool that will give an optimised system configuration, based on the given available resources (gold)

## Quest 2, Part 4: Project planning

### First steps for next phase

* Look into yaml description of modules
* Research into existing methods of system description
* Graph based databases?
* Perhaps graph theory can be useful later if the (suspiciously graph-looking) system can be described suitably.

#### Data collection

* Module descriptions can be collected from the respective groups (by asking nicely)

#### Relevant Duckietown resources to investigate

* `devel-heroes-formal-description` branch on Software repository
* How the current system’s characteristics are defined
* What are the dependencies/interfaces between modules
* Which projects affect which modules
* Which values/parameters are needed

### Risk analysis

* Quest 1 takes priority over quest 2, since it is more crucial to the functioning of the system. This means that quest 2 may suffer if quest 1 takes more time than expected.
* Quest 2 has a research/experimental aspect, which makes it both interesting and challenging.
* There is a chance that it might not be solved, as it is not a trivial problem.
