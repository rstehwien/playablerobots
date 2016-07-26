# playablerobots
http://steamcommunity.com/sharedfiles/filedetails/?id=728268465

https://github.com/gtosh4/playablerobots

## Credit
* *Delincious* - [Original mod](http://steamcommunity.com/sharedfiles/filedetails/?id=681553348)
* *Cookiemonster364* - Fix for [trait copying issue](http://steamcommunity.com/workshop/filedetails/discussion/681553348/351660338704537339/)

## Notifications
<b>Do not run this AND the original mod. They have the same stuff except this one has a few fixes.</b>

<b>To enable synthetic playstyle, select the trait in species creation instead of as a window on game start (as in the original)</b>

<i>Should</i> be save-game compatible with the original - my current game was started on the original mod. Make sure you back up your save before just in case though.

## Installing from source
1. "Download as zip"
2. Extract to a new folder called `playablerobots` your local mods directory (eg on Windows `%USERPROFILE%\Documents\Paradox Interactive\Stellaris\mod\playablerobots`)
3. Copy `descriptor.mod` to the `mod` parent folder and rename to `playablerobots.mod`

## Fixes
* *Cookiemonster364's* fix for trait copying
* Fix habitibility bonus progression (was 10% -> 5% -> 7.5% -> 10%) to (10% -> 50% -> 75% -> 100%)
* Fix initial pops not being the same race as new pops (fix for xenophobic ethic and repugnant trait)
* Add support for [Awakening](http://steamcommunity.com/sharedfiles/filedetails/?id=719876273) traits
* Improve the game start tile modification a bit. Was: replace farms and power plant lvl 1 with power plant lvl 2. Now: replace farms with power plant lvl 1 & replace base tile food with energy.
* Select synthetic playstyle by selecting the trait in species creation instead of as a window on game start.
* Update election_term_years from 5 to 10 to match changes made to other elected governments in 1.2.1
* Require android trait for the new government types.
* Add opposite traits for the Breeder traits and when you reach level 3 upgrade (100% habitability bonus) you are refunded you adaptive traits since you no longer need them.
* Fixed bug where 'ai1' portrait couldn't build pops.

## FAQ
### My pop's happiness is capped, help!
The synthetics get a slight boost to habitability (increases with tech) but are otherwise still subject to habitability happiness caps.

### I just started and can't build any pops!
Make sure you selected the `Synthetic` trait when creating your species.

### Some of my traits aren't copying!
Due to limitations on the mod API, the trait support has to be hand-managed so only a few are supported.

The following traits are currently supported:
* Vanilla traits
* [Extended traits](https://steamcommunity.com/sharedfiles/filedetails/?id=681816257)
* [Awakening](http://steamcommunity.com/sharedfiles/filedetails/?id=719876273)
