# BallerMentality

[![Build](https://github.com/cryptopatrick/ballermentality/actions/workflows/ci.yml/badge.svg)](
https://github.com/cryptopatrick/ballermentality/actions)
[![License](https://img.shields.io/badge/license-Apache--2.0_OR_MIT-blue.svg)](
https://github.com/cryptopatrick/ballermentality)

<!--
[![Cargo](https://img.shields.io/crates/v/ballermentality.svg)](
https://crates.io/crates/ballermentality)
[![Documentation](https://docs.rs/ballermentality/badge.svg)](
https://docs.rs/ballermentality)
[![Chat](https://img.shields.io/matrix/cryptopatrick%3Amatrix.org)](
https://matrix.to/#/#cryptopatrick:matrix.org)
-->

<img src="https://raw.githubusercontent.com/cryptopatrick/ballermentality/master/assets/images/logo_basketball_transparent.png" alt="basketball" width="100px" style="float: left;" />

"Improve as a basketball player by overcoming self-doubt and nervousness. 
Get advice from sports psychologists on how to build confidence and becoming 
a mentally strong baller."

> Disclaimer: BallerMentality is a portfolio project that I'm [building in public](https://www.youtube.com/watch?v=dEJ1xQ_A2B4). It's __not__ a real service. If you need help with sports psychology related services, please consult outher sources.

BallerMentality is a toy full stack project that I'm building with the hopes of learning how to do web development with Rust.
In other words, it is not a real service.

## Core Functionality
The core service of BallerMentality is a web site where a user can: 
1. create an account
2. select to have the role basketball player or sports psychologist
3. interact with other members of the community
4. book a session with a counterpart (player and psychologist)
5. grade a session with stars based on how useful it was

## Technology
The backend will be written in Rust using Poem and GraphQL, with OpenAPI integration.
Persistence will be handled with a Dockerized Postgres database via SQLx.
The frontent will be written in TypeScript using the Solid JS framework.
Authentication will be provided via Google Auth.

## Example Use Case Scenario
The following scenario is written to get a sense of what functionlity that I'm 
hoping to provide in the the final version of the web application.

### "We lost the game because I missed two Free Throws"
Adam Bearing is devastated. Last night's loss, in the division 1, first round game of
the state champtionship tournament, has kept him awake all night.
With three seconds remaining in the fourth quarter, Adam had the chance to win the game
for his team, The Running Rebels - down by one against The City Sonics. 
Simple, just make one free throw to tie the game, make them both to win the game.
Instead, he missed them both, and they lost the game. *HE* lost them the game.

Unable to sleep, Adam's picks up his phone and surfs the web.
He spots an ad for BallerMentality "The hell is that?".
The website is simple and the message is straight "Helping basketball players
overcome anxiety and grow a baller mentality!"

#### Core Services
Without hesitation, Adam creates an account using his Google gmail.  
Once the account is created, he's presented with the following options:
1. `Edit` his profile
2. `Check` his calendar and notifications
3. `Book` a new session (with a sports psychologist in the community)
4. `Cancel` an previously booked session  
5. `Logout` of the web page

#### Edit
Adam decides to edit his profile. He's presented with a `form` which he fills out,
describing himself and confidence/anxiety-related things that are bothering him
on the court.
He's also asked to grade himself on a number of strengths and weaknesses, what type
of player he his, and what type of player he wants to become.

#### Check
Adamm clicks the calendar icon and he's presented with a monthly calendar.
Waisting no time, Adam decides to book a session with a sports psychologist.

#### Book
Clicking the `Book Session` button opens up a simpel form where Adam is asked to 
provide some details on what type of session he would like, and write a few words 
on the kind of challenge he's facing.
Adam writes that he's feeling depressed because he let his team down and that
he doesn't know who to talk to.
Adam selects a couple of dates and time slots that would be suitable for a session.
A few minutes later, Adam is notified by an icon in the top left corner, that two
sports psychologists have shown interest to book a session with him.
He looks at their profile and then confirms the invite from one of them.
The date and time of the session is added to his calendar.

#### Logout
Adam feels both relieved, having taken action to deal with his feelings, but also
a bit nervous about the booked session.
He logs out of the website, and realises that he's tired. 
He goes to sleep, feeling much better.
The alarm clock rings...  
"Shit! I gotta hurry, I got class in 20 minutes."


There will be a few more personas and use case scenarios in the [examples] directory.
[examples]: https://github.com/cryptopatrick/ballermentality/tree/master/examples


## Prompts Used
1. Initial prompt to create a rough outline of system and of parts to build:  
[🏗️](https://chatgpt.com/share/6803afd0-d6f8-800a-8b51-ca002991bc60)

---

## MSRV Policy

The Minimum Supported Rust Version (MSRV) of this crate is **1.85**. As a **tentative** policy, the MSRV will not advance past the [current Rust version provided by Debian Stable](https://packages.debian.org/stable/rust/rustc). At the time of writing, this version of Rust is *1.85*. However, the MSRV may be advanced further in the event of a major ecosystem shift or a security vulnerability.

## License

Licensed under either of

 * Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
