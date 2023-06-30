from behave import given, when, then


@given("Launch the App and Clicked on Login Button")
def methodOne(context):
    print("L1 - Launch the App")


@when("Enter UserID")
def methodTwo(context):
    print("L2 - Enter UserID in Login Screen")


@when("Enter Password")
def methodThree(context):
    print("L3 - Enter Password in Login Screen")


@then("Verify Home Screen")
def methodFour(context):
    print("Home Screen Opened")
