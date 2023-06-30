from behave import given, when, then


@given("Launch the App and Click the Login Button")
def methodOne(context):
    print("L1 - Launch the App")


@when("Enter {emailed} UserID")
def methodTwo(context, emailed):
    print("L2 - Enter UserID in Login Screen {} ".format(emailed))


@when("Enter {pwd} password")
def methodThree(context, pwd):
    print("L3 - Enter Password in Login Screen {} ".format(pwd))


@then("Verify {Verify_Sc} Home screen")
def methFour(context, Verify_Sc):
    print("L4 - Screen {} ".format(Verify_Sc))
