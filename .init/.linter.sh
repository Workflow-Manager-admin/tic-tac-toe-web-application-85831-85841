#!/bin/bash
cd /home/kavia/workspace/code-generation/tic-tac-toe-web-application-85831-85841/tic_tac_toe_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

