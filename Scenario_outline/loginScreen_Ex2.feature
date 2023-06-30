  Feature: Fill the Contact Form

    Scenario Outline: Users Login Credentials

      Given Launch the App and Click the Login Button
      When Enter <emailed> UserID
      When Enter <pwd> password
      Then Verify Home  screen

      Examples:
        | emailed                | pwd|
        | sudeep@gmail.com       | 1234|
        | sudeepyadav@gmail.com  | 123456|