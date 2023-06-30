# This is a feature file

  Feature: Fill the Login Form

    Scenario: User Login Credentials

      Given Launch the App and Click the Login Button
      When Enter UserID
      When Enter password
      When Click the Login Button
      And Home page opens
      Then Verify home page
      Then Take screenshots