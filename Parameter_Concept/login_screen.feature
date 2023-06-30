# This is a feature file

  Feature: Fill the Contact Form

    Scenario: User Login Credentials

      Given Launch the App and Click the Login Button
      When Enter "sudeepyadav@gmail.com" UserID
      When Enter '12345678' password
      When Click the Login Button
      And Home page opens
      Then Verify home page
      Then Take screenshots