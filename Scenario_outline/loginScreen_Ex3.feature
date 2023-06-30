  Feature: Fill the Contact Form

    Scenario Outline: Users Login Credentials

      Given Launch the App and Click the Login Button
      When Enter <emailed> UserID
      When Enter <pwd> password
      Then Verify <Verify_Sc> Home screen

      Examples:
        | emailed                | pwd   | Verify_Sc  |
        | sudeep1@gmail.com       | 1234  | S1         |
        | sudeep2@gmail.com  | 12345| S2         |
      | sudeep3@gmail.com  | 123456| S3         |
      | sudeep4@gmail.com  | 1234567| S4         |