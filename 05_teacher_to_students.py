import easygui
import math


def main():
    school = easygui.enterbox("Enter the name of the school", "School name")
    max_children = easygui.integerbox("Enter the maximum number of children "
                                      "allowed per class.\n"
                                      "Must be between 10 and 30", "Max class "
                                                                   "size",
                                      lowerbound=10, upperbound=30)
    children_in_school = easygui.integerbox("Enter total number of children "
                                            "enrolled.\n"
                                            "Must be between 10 and 1400",
                                            "Total children in school",
                                            lowerbound=10, upperbound=1400)

    classes = math.ceil(children_in_school / max_children)

    teachers = easygui.integerbox(
        f"Enter the number of teachers at {school}.\n"
        f"Must be between 1 and 120", "Actual # of "
                                      "teachers",
        lowerbound=1, upperbound=120)

    if teachers == classes:
        easygui.msgbox(f"You have the correct number of teachers.\n\n"
                       f"You have {teachers} teachers.")
    elif teachers > classes:
        easygui.msgbox(f"You have too many teachers.\n\n"
                       f"You could do without {teachers - classes} current "
                       f"teacher/s.\n\n"
                       f"This way you will have {classes} teachers")
    elif teachers < classes:
        easygui.msgbox(f"You do not have enough teachers.\n\n"
                       f"You should have {classes - teachers} more teachers.\n\n"
                       f"This way you will have {classes} teachers")

    if easygui.ynbox("Do you want to perform another calculation"):
        main()
    else:
        easygui.msgbox("Goodbye")


main()
