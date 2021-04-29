init:
    transform arrowSize:
        zoom 0.5


screen gotoApartmentArrow():
    imagebutton:
        xalign 0.35
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Apartment")
        at arrowSize

screen gotoOusideApartment():
    imagebutton:
        xalign 0.115
        yalign 0.3
        idle "arrow_left.png"
        hover "arrow_hover_left.png"
        action Jump("OutsideApartment")
        at arrowSize

screen gotoCompany():
    imagebutton:
        xalign 0.95
        yalign 0.4
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Company")
        at arrowSize

screen gotoFrontDesk():
    imagebutton:
        xalign 0.85
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("FrontDesk")
        at arrowSize

screen gotoElevator():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Elevator")
        at arrowSize

screen gotoOpenArea():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("OpenArea")
        at arrowSize

screen gotoOfficesOutside():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("OfficesDoor")
        at arrowSize

screen gotoOfficesOutside2():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("explanation")
        at arrowSize

screen gotoOffice():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Office")
        at arrowSize

screen multiple():
    imagebutton:
        xalign 0.35
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Apartment")
        at arrowSize
    imagebutton:
        xalign 0.95
        yalign 0.4
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Company")
        at arrowSize

screen multiple2():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrow_left.png"
        hover "arrow_hover_left.png"
        action Jump("OutsideApartment")
        at arrowSize
    imagebutton:
        xalign 0.85
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("FrontDesk")
        at arrowSize

screen multiple3():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrow_left.png"
        hover "arrow_hover_left.png"
        action Jump("Company")
        at arrowSize
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrow.png"
        hover "arrow_hover.png"
        action Jump("Elevator")
        at arrowSize
