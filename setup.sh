#!/bin/bash
# export DATABASE_URL="postgres://ujldzdumwmqgmo:462b05e6c2d3828cd40994886ffd528ec9398fa0dcea28ca2e10fd00332a86f2@ec2-52-204-157-26.compute-1.amazonaws.com:5432/d8k1e0r5m2jnd7"
export EXCITED="true"
export DATABASE_URL="postgresql://postgres:admin@localhost:5433/capston"
export AUTH0_DOMAIN="dev-dh8lpj82.us.auth0.com"
export ALGORITHMS='['RS256']'
export API_AUDIENCE='http://localhost:5000/'
echo "setup.sh script executed successfully!"
