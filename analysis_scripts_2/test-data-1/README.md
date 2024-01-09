# Raw test response data, output by `PsychoPy`

This directory contains raw test response data for all 16 participants (14 with 3 sessions, 2 with 2 sessions). 

Data is organized by unique participant ID.

Survey data is stored in `post_test_responses.csv` and mappings between participant IDs, session numbers, and TMS conditions (which were randomized during data collection) are stored in `logistics.csv`.

Participant `00001` has a corrupted copy of their first session test data, with most rows missing values. Make sure that the `[...]block_1.csv` file corresponding to the corrupted copy is renamed to `[...]block_1-corrupted.csv` before running the data management script, so that the correct copy is used.

For each participant and session, data is stored in multiple file formats. We only read data from the files titled `[...]block_1.csv`.

