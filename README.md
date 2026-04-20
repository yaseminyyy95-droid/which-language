# mini-timer

## Version Summary

### V0
- `init` and `start` were the only working commands.
- Other commands returned a placeholder message.
- Data storage was minimal.

### V1
- `start` and `stop` now work as a real timer flow.
- Completed sessions are written to a persistent log file.
- `log` and `stats` provide session history and summary output.
- The SPEC was clarified with a single-active-session rule and an exact timestamp format.

### V2 (New)
- Added a `status` command to check the elapsed time of a running session without stopping it.
- Added a `cancel` command to abort a session without saving it to the persistent log.
- Enhanced the `stats` command to calculate and display the longest session recorded.

## V2 Tasks
1. Implement `status` command to show real-time progress.
2. Implement `cancel` command to safely discard an unwanted timer.
3. Improve `stats` command with a "Longest session" metric.

## Notes
- Project data is stored in `.minitimer/`.
- The CLI entry point is now `solution_v2.py`.