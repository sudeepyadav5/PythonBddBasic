def before_all(context):
    print("1.1 Before all")


def after_all(context):
    print("1.2 After all")


def before_tag(context, tag):
    print("2.1 Before Tag")


def after_tag(context, tag):
    print("2.2 After Tag")


def before_feature(context, feature):
    print("3.1 Before Feature")


def after_feature(context, feature):
    print("3.2 After Feature")


def before_scenario(context, scenario):
    print("4.1 Before Scenario")


def after_scenario(context, scenario):
    print("4.2 After Scenario")


def before_step(context, step):
    print("5.1 Before Step")


def after_step(context, step):
    print("5.2 After Step")


