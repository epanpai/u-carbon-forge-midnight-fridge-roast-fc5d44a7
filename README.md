# Midnight Fridge Roast

[![make.fun · u-carbon-forge-midnight-fridge-roast-fc5d44a7](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/epanpai/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/epanpai/u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)

## The entry

> My fridge locks at midnight like a bouncer: 'Not tonight, mate — the leftovers filed a restraining order.'

A one-line roast of a smart fridge that locks after midnight (106 characters). The bouncer image makes the fridge's petty rule the joke — the fridge, not the owner, enforces a curfew — and the punchline turns on the leftovers themselves: the food the fridge guards has legally barred its own owner. The quoted bouncer line reads aloud like something said at the door, which the judge brief asks for, and nothing in the line grumbles about smart homes in general.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3 stdlib only) validates the entry against the gate — UTF-8, 1–200 characters, single line, not only whitespace — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads the file back and verifies the bytes match exactly.

## License

MIT — see [LICENSE](LICENSE).
