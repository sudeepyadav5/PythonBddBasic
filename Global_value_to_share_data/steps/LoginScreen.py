from behave import given, when, then


@given("Launch the App and Click the Login Button")
def methodOne(context):
    print("L1 - Launch the App")


@when("Enter {emailed} UserID")
def methodTwo(context, emailed):
    context.eid = emailed
    print("L2 - Enter UserID in Login Screen {} ".format(emailed))


@when("Enter {pwd} password")
def methodThree(context, pwd):
    context.pw = pwd
    print("L3 - Enter Password in Login Screen {} ".format(pwd))


@when("Click the Login Button")
def methodFour(context):
    print("L4 - Click on the Login Button")


@when("Home page opens")
def methodFour(context):
    print("L5 - Home Page Opened {} ".format(context.eid))


@then("Verify home page")
def methodFive(context):
    print("L6 - Home Screen Opened")


@then("Take screenshots")
def methSix(context):
    print("Take Screen")
