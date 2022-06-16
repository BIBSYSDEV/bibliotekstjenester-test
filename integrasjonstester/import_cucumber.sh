export CLIENT_ID="7CC7DB5B1CC2485DB9F58D2ACE9D17C6"
export CLIENT_SECRET="351297fa46ef518116b1b9939ff5f806ee09cb682c7caa03d99176d17b77d9e1"
export AUTH_BODY="{\"client_id\": \"$CLIENT_ID\", \"client_secret\": \"$CLIENT_SECRET\"}"
export BEARER_TOKEN=$(curl -H "Content-Type:application/json" -X POST --data "$AUTH_BODY" https://xray.cloud.getxray.app/api/v2/authenticate | tr -d '"')
curl -H "Content-Type:application/json" -X GET -H "Authorization:Bearer $BEARER_TOKEN"  "https://xray.cloud.getxray.app/api/v2/export/cucumber?keys=SMILE-1623" > cucumber.zip
unzip cucumber.zip -d cypress/e2e
rm cucumber.zip