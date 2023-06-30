# This is a feature file

  Feature: Fill the Contact Form

    Scenario: Student Login Credentials

      Given Launch the App and Click the Login Button
      When Enter "sudeepyadav@gmail.com" UserID
      When Enter "S1234" password
      Then Verify Home screen


    Scenario: Teacher Login Credentials

      Given Launch the App and Click the Login Button
      When Enter "sudeepteacher@gmail.com" UserID
      When Enter "T1234" password
      Then Verify Home screen