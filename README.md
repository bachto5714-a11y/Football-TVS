# Football Transfer Value Score (TVS)

A Python-based football transfer evaluation system designed to estimate a player's transfer value relative to their performance, age, club strength, and transfer cost.

## Features

- **Position-based evaluation:** Uses different performance statistics for attackers, midfielders, defenders, and goalkeepers.
- **Overall Rating (OVR):** Incorporates the player's overall rating into the score.
- **Age coefficient:** Adjusts the score according to the player's age.
- **Club coefficient:** Accounts for the strength of the league and club.
- **Superstar Multiplier:** Applies an additional coefficient to players with high OVR.
- **Budget validation:** Checks whether the transfer is affordable within the available budget.

## How It Works

The system calculates a Transfer Value Score (TVS) using player performance statistics, OVR, transfer cost, age, and club-related coefficients.

The result is used to classify a transfer into recommendation categories, ranging from highly recommended to not recommended.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Run the Python program:

```bash
python main.py
```

Replace `main.py` with the actual Python filename if it is different.

## Project Status

**Version:** 1.0 — Initial release

This is an experimental football scouting model. Its coefficients and recommendation thresholds are heuristic and have not yet been validated against a comprehensive real-world transfer dataset.

## Future Improvements

- Medical and injury risk assessment
- Position-specific scoring refinements
- Separate current ability and potential
- Squad tactical fit
- Automated player comparisons and test cases

## Disclaimer

TVS is an independent evaluation model for experimentation and learning. Its scores are not official market valuations or guarantees of transfer success.
