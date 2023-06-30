#this is a Feature file

@regression
Feature: Fill the Contact Form

  @Login @regression
  Scenario: User Login Credentials

    Given Launch the App and Clicked on Login Button
    When Enter UserID
    When Enter Password
    Then Verify Home Screen


