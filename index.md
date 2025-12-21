# Professional Self-Assessment

Completing the Computer Science program and building this ePortfolio helped me clearly understand my strengths and how I want to move forward in the computer science field. Over time, I moved beyond simply making programs work and began focusing on writing software that is organized, readable, reliable, and easier to maintain. Working on the capstone and assembling this portfolio gave me the opportunity to reflect on how my technical skills and professional mindset have grown throughout the program.

Throughout my coursework, I gained experience collaborating and communicating in technical environments. Many assignments required explaining design decisions, documenting code, and responding to feedback from instructors. These experiences helped me learn how to clearly communicate technical ideas, whether the audience was technical or nontechnical. I also learned the value of clean documentation and readable code, especially when others need to understand or evaluate my work.

The program strengthened my understanding of data structures and algorithms by applying them in practical projects rather than treating them as purely theoretical topics. I worked extensively with loops, conditionals, collections, and structured logic to control program flow and manage state. This helped me improve my problem-solving skills and understand how algorithm design directly impacts program behavior, efficiency, and user experience.

Software engineering and database concepts were a major part of my development as well. I learned how to refactor code into reusable components, reduce duplication, and design programs that are easier to update and expand. I also gained experience working with structured data and understanding how databases support persistence and analysis. These skills helped me better understand how real-world software systems are designed and maintained.

Security became an increasingly important focus as I progressed through the program. I learned to think more carefully about user behavior and how unexpected input can cause crashes or incorrect program states. By applying input validation, safe defaults, and defensive programming techniques, I learned how to build programs that are more reliable and secure from the start.

The artifacts included in this ePortfolio demonstrate how these skills work together. The text-based adventure game featured here combines software design, algorithms, database integration, and secure coding in a single application. The code review and enhancement sections that follow explain how I evaluated the original program and applied targeted improvements based on best practices. Together, these artifacts reflect my readiness to enter the computer science field as a capable and thoughtful developer.

---

## Code Review

The code review video walks through the original version of my text-based adventure game and explains how the program works at a high level. In the video, I describe the game’s structure, how user commands are processed, and how the game state changes as the player moves through different rooms.

I also identify limitations in the original design, such as repeated logic, minimal input validation, and a lack of organization. The review explains why these issues matter and how they affect usability, reliability, and maintainability.

Finally, the video introduces the enhanced version of the game and explains the major improvements that were made. These include reorganizing the code into a class-based design, improving input handling, adding a shortest-path feature, and logging game results to a database. The code review provides context for the enhancements described in the sections below.

[Watch Code Review](https://youtu.be/k8O-w3O-wOE)

---

## Artifact Overview

The original artifact for this portfolio is a text-based adventure game developed earlier in the Computer Science program. The game is entirely text-driven and uses a command-based system where the player navigates through rooms, collects gemstones, and attempts to defeat the Shadow Thief to escape the castle.

The original version demonstrates fundamental programming concepts such as conditionals, loops, and basic control flow. Players can move between rooms, collect items, and reach different outcomes based on their choices. From a functionality standpoint, the game works and provides a complete interactive experience.

However, the original implementation reflected an earlier stage in my development as a programmer. Much of the logic was written in a linear and repetitive way, and the program assumed that users would always enter valid commands. This made the code harder to maintain and more likely to break when unexpected input was provided.

This original version serves as a clear baseline for the enhancements that follow. It provides context for the design, algorithmic, and database improvements made later and helps demonstrate my growth in applying software engineering and secure coding principles.

[Original Artifact](https://github.com/j-snhu/CS499/blob/main/TextBasedGame.py)

---

## Enhancements

---

### Enhancement One: Software Engineering and Design

The first enhancement focuses on improving the overall software design and structure of the game. In the original version, most of the logic was contained in a single flow, which made the code harder to read, debug, and extend.

In the enhanced version, the entire game was reorganized into a Game class, which centralizes game state such as the current room, inventory, move count, and available items. The code was broken into smaller, clearly named methods that handle specific responsibilities, such as displaying instructions, processing commands, moving the player, collecting items, and running the main game loop.

This design greatly improves readability and maintainability. By separating responsibilities and reducing repetition, the program is easier to understand and update. From a software engineering perspective, this enhancement demonstrates modular design, separation of concerns, and cleaner architecture that more closely reflects professional coding practices.

[Enhancement One Artifact](https://github.com/j-snhu/CS499/blob/main/EnhancementOne%20-%20TextBasedGame.py)
[Enhancement One Narrative](https://github.com/j-snhu/CS499/blob/main/CS%20499%20-%20Module%203%20Milestone%202%20-%20Sanchez.pdf)

---

### Enhancement Two: Algorithms and Data Structures

The second enhancement focuses on improving algorithms and data structures used to control game logic and navigation. In addition to improving input validation, a major enhancement was the addition of a shortest-path feature using a Breadth-First Search (BFS) algorithm.

The enhanced game includes a path command that allows the player to request the shortest route to any room. This feature uses a queue (deque), a visited set, and a previous-room mapping to calculate and display the optimal path. The algorithm also includes a rule that avoids the villain’s room unless the player specifically targets it, which improves gameplay flow.

These changes demonstrate applied algorithmic thinking and effective use of data structures such as sets, dictionaries, and queues. The enhanced logic improves reliability, reduces unnecessary branching, and provides helpful guidance to the player while maintaining predictable control flow.

[Enhancement Two Artifact](https://github.com/j-snhu/CS499/blob/main/EnhancementTwo%20-%20TextBasedGame.py)
[Enhancement Two Narrative](https://github.com/j-snhu/CS499/blob/main/CS%20499%20-%20Module%204%20Milestone%203%20-%20Sanchez.pdf)

---

### Enhancement Three: Databases

The third enhancement introduces a real database using SQLite to store game results. In the enhanced version, the game creates a database file and logs the outcome of each playthrough, including whether the player won, lost, or quit, how many gemstones were collected, how many moves were made, and a timestamp.

This database is automatically updated when the game ends, and the connection is safely closed even if an error occurs. By storing results in a database, the game supports persistence and enables future analysis, such as reviewing player performance or tracking multiple playthroughs.

This enhancement demonstrates practical database skills, including table creation, inserting records, and managing database connections. It shows how databases can be integrated into an application to support data persistence and long-term use, rather than relying only on in-memory data.

[Enhancement Three Artifact](https://github.com/j-snhu/CS499/blob/main/EnhancementThree%20-%20TextBasedGame.py)
[Enhancement Three Narrative](https://github.com/j-snhu/CS499/blob/main/CS%20499%20-%20Module%205%20Milestone%204%20-%20Sanchez.pdf)

---
