from sellgate import sellgate

print(sellgate().create_checkout({
  "price": '10',
  "crypto": [
    {
      "network": "ETH",
      "coin": "ETH",
      "address": "0xB1DA646D1cD015d205a99198e809724D5C78109d"
    }
  ]
}))

print(sellgate().create_address({
  "crypto": 
    {
      "network": "ETH",
      "coin": "ETH",
      "address": "0xB1DA646D1cD015d205a99198e809724D5C78109d"
    },
  "webhook": "https://webhook.site/1234567890"
}))