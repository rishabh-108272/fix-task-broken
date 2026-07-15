#!/bin/bash

# Ensure output directory exists
mkdir -p /logs/verifier

# Run pytest and generate CTRF report
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
pytest_exit_code=$?

# Write reward based on exit code
if [ $pytest_exit_code -eq 0 ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi

exit $pytest_exit_code
