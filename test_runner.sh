#!/usr/bin/env bash

PYTEST_CMD="pytest --alluredir=results --reruns 5 ./tests/"
ALLURE_CMD="allure serve results"

echo "Running tests..."
$PYTEST_CMD

echo "Generating report..."
$ALLURE_CMD