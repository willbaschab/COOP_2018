# U08_EX17_ImageManipulation.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Apr 2019
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 8
#
# Problem Description
#   Write a program that provides a vertical menu on right side of window for image manipulation algorithms.
#   The menu should include Load Image, Save Image, and Quit buttons at the top. Image manipulation algorithm
#   buttons should be displayed below, separated from the top buttons by a separator line. A vertical separator
#   line should divide the menu from image space. The program should accept mouse clicks for the buttons. When
#   image manipulation algorithm buttons are clicked, their fill color should toggle. Clicking again will
#   untoggle and reverse the effect. The user should also be allowed to press Ctrl/Command O to Load Image,
#   Ctrl/Command S to Save Image, and the Esc key to quit. The image should be displayed centered in the image
#   space. The image may need to be scaled if it is too big for the image space. The GraphWin should be 800
#   pixels in height and 1000 pixels in width (200 pixels are reserved for menu space).
#
# Program Description
#   Adds a menu to code for exercises 14 and 15.
#   Buttons: Load Image, Save Image, Quit, Grayscale, Negative, user defined buttons
#   Esc can be pressed to quit.
#
# Algorithm (pseudocode)
#   global variables: button objects, button constant values (e.g. LOADIMAGE = 0), image height and width, win
#   create GraphWin
#
#   main:
#       call drawMenu()
#       enter into event loop, looking for mouse clicks and key presses
#           key press: call handleKeys()
#           mouse clicks: call handleClicks()
#
#   drawMenu:
#       at top of program, define global variables for button locations (they get set here)
#       set standard height, width, and separation space for buttons
#       draw three buttons at top, a separator line, and at least five buttons below
#       set global button object variables as you go
#       set button fill color to light gray
#       draw button text for each button (bottom three will be blank)
#       draw a vertical separator line between menu and image space
#
#   handleKeys:
#       O  -> loadImage()
#       S  -> saveImage()
#
#   handleClicks:
#       call buttonClicked()
#       take action based on return value (see global constants)
#       0           -> do nothing
#       LOADIMAGE   -> loadImage()
#       SAVEIMAGE   -> saveImage()
#       Quit        -> quit
#       GRAYSCALE   -> toggle fill; grayscale()
#       NEGATIVE    -> toggle fill; negative()
#       Other Effects toggle fill and call appropriate user-defined functions
#
#   buttonClicked:
#       test to see if pt is on a button; return appropriate global constant (or zero)
#           if ptX is within x coords AND ptY is within y coords for this button return global var for button
#           otherwise, return 0
#
#   loadImage:
#       get the image file using askopenfilename from tkinter.filedialog
#       if no selection, return
#       open the file
#       get width and height of image and store to global variables
#       display image
#
#   saveImage:
#       save image using asksavefilename from tkinter.filedialog
#       if canceled, return
#       save the file
#
#   grayscale:
#       if already grayscale
#           revert to original pixels
#       otherwise
#           save state
#           convert pixels to grayscale
#               using image width and height, get pixel rgb values and set to grayscale
#       display image
#
#   negative:
#       convert pixels to color negative
#           using image width and height, get pixel rgb values and set to color negative
#       display image
#
#   other effects:
#       if effect already applied
#           revert to original pixels
#       otherwise
#           save state
#           convert pixels to effect
#               using image width and height, get pixel rgb values and set to effect
#       display image


from graphics import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

#   global variables: button objects, button constant values (e.g. LOADIMAGE = 0), image height and width, win
buttonLoad = Rectangle(Point(0,0), Point(1,1)); LOADIMAGE = 1; buttonLoadActive = 0
buttonSave = Rectangle(Point(0,0), Point(1,1)); SAVEIMAGE = 2; buttonSaveActive = 0
buttonQuit = Rectangle(Point(0,0), Point(1,1)); QUIT = 3; buttonQuitActive = 0
buttonGray = Rectangle(Point(0,0), Point(1,1)); GRAYSCALE = 4; buttonGrayActive = 0; isNewEffect = False
buttonNeg = Rectangle(Point(0,0), Point(1,1)); NEGATIVE = 5; buttonNegActive = 0; isNegative = False
buttonOther1 = Rectangle(Point(0,0), Point(1,1)); OTHER1 = 6; buttonOther1Active = 0; isOther1 = False
buttonOther2 = Rectangle(Point(0,0), Point(1,1)); OTHER2 = 7; buttonOther2Active = 0; isOther2 = False
buttonOther3 = Rectangle(Point(0,0), Point(1,1)); OTHER3 = 8; buttonOther3Active = 0; isOther3 = False
buttonIdleFill = '#cccccc'; buttonActiveFill = '#999999'

# create GraphWin
win = GraphWin('Image Manipulation', 1000, 800)
midX = (win.getWidth() - 200) / 2; midY = win.getHeight() / 2
buttonHeight = 30; buttonWidth = 180; buttonSep = 10; menuLeft = win.getWidth() - 200
img = Image(Point(midX, midY), 800, 800); imgHeight = 0; imgWidth = 0
imgOrig = img

# main:
def main():
    # call drawMenu()
    drawMenu()

    # enter into event loop, looking for mouse clicks and key presses
    while True:
        # key press: call handleKeys()
        key = win.checkKey()
        if key == "Escape":  # loop exit
            break

        if key:
            handleKeys(key)

        # mouse clicks: call handleClicks()
        pt = win.checkMouse()
        if pt:
            if not handleClicks(pt):
                break

    win.close()

#   drawMenu:
def drawMenu():
    # at top of program, define global variables for button locations (they get set here)
    global buttonLoad, buttonSave, buttonQuit, buttonGray, buttonNeg

    # set standard height, width, and separation space for buttons
    # these are global variables

    # draw three buttons at top, a separator line, and at least five buttons below
    # set global button object variables as you go
    # set button fill color to light gray
    # draw button text for each button (bottom three will be blank)
    # draw a vertical separator line between menu and image space
    Line(Point(menuLeft, 0), Point(menuLeft, win.getHeight())).draw(win)

    # Load Image button
    topLeft = Point(menuLeft + buttonSep, buttonSep)
    botRight = Point(menuLeft + buttonSep + buttonWidth, buttonSep + buttonHeight)
    buttonLoad = Rectangle(topLeft, botRight)
    buttonLoad.setFill(color=buttonIdleFill)
    buttonLoad.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Load Image').draw(win)

    # Save Image button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonSave = Rectangle(topLeft, botRight)
    buttonSave.setFill(color=buttonIdleFill)
    buttonSave.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Save Image').draw(win)

    # Quit button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonQuit = Rectangle(topLeft, botRight)
    buttonQuit.setFill(color=buttonIdleFill)
    buttonQuit.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Quit').draw(win)

    # Horizontal separator line
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonSep)
    Line(Point(topLeft.getX() - buttonSep, topLeft.getY()),
         Point(botRight.getX() + buttonSep ,botRight.getY())).draw(win)

    # Grayscale button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonGray = Rectangle(topLeft, botRight)
    buttonGray.setFill(color=buttonIdleFill)
    buttonGray.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'New Effect').draw(win)

    # Negative button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonNeg = Rectangle(topLeft, botRight)
    buttonNeg.setFill(color=buttonIdleFill)
    buttonNeg.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Negative').draw(win)

    # Other Effect 1 button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonOther1 = Rectangle(topLeft, botRight)
    buttonOther1.setFill(color=buttonIdleFill)
    buttonOther1.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Other Effect 1').draw(win)

    # Other Effect 2 button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonOther2 = Rectangle(topLeft, botRight)
    buttonOther2.setFill(color=buttonIdleFill)
    buttonOther2.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Other Effect 2').draw(win)

    # Other Effect 3 button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonOther3 = Rectangle(topLeft, botRight)
    buttonOther3.setFill(color=buttonIdleFill)
    buttonOther3.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Other Effect 3').draw(win)

#   handleKeys:
def handleKeys(key):
    """
    Handles keys pressed to execute menu options (except ESC)
    :param key: str -> key that was pressed
    :return: None
    """
    # O  -> loadImage()
    if key == "o" or key == "O":
        loadImage()

    # S  -> saveImage()
    if key == "s" or key == "S":
        saveImage()

#   handleClicks:
def handleClicks(pt):
    """
    Handles valid mouse clicks, executing button actions
    :param pt: Point -> location of mouse click as a Point object
    :return: int -> 0 if Quit button clicked; otherwise 1
    """
    global buttonLoadActive, buttonSaveActive, buttonQuitActive, buttonGrayActive, \
        buttonNegActive, buttonOther1Active, buttonOther2Active, buttonOther3Active
    # call buttonClicked()
    clickResult = buttonClicked(pt)
    # take action based on return value (see global constants)
    # 0           -> do nothing
    # LOADIMAGE   -> loadImage()
    # SAVEIMAGE   -> saveImage()
    # Quit        -> quit
    # GRAYSCALE   -> toggle fill; grayscale()
    # NEGATIVE    -> toggle fill; negative()
    # Other Effects toggle fill and call appropriate user-defined functions
    if clickResult == LOADIMAGE:
        buttonLoadActive = buttonFillToggle(buttonLoad, buttonLoadActive)
        loadImage()
        buttonLoadActive = buttonFillToggle(buttonLoad, buttonLoadActive)
    if clickResult == SAVEIMAGE:
        buttonSaveActive = buttonFillToggle(buttonSave, buttonSaveActive)
        saveImage()
        buttonSaveActive = buttonFillToggle(buttonSave, buttonSaveActive)
    if clickResult == QUIT:
        buttonQuitActive = buttonFillToggle(buttonQuit, buttonQuitActive)
        return 0
    if clickResult == GRAYSCALE:
        buttonGrayActive = buttonFillToggle(buttonGray, buttonGrayActive)
        NewEffect()
    if clickResult == NEGATIVE:
        buttonNegActive = buttonFillToggle(buttonNeg, buttonNegActive)
        negative()
    return 1

#   buttonClicked:
def buttonClicked(pt):
    """
    Checks to see if a button was clicked
    :param pt: Point -> location of mouse click as a Point object
    :return: int -> global constant matching button clicked; zero if none
    """
    # test to see if pt is on a button; return appropriate global constant (or zero)
    #     if ptX is within x coords AND ptY is within y coords for this button return global var for button
    #     otherwise, return 0
    buttonLoadCenter = buttonLoad.getCenter()
    buttonSaveCenter = buttonSave.getCenter()
    buttonQuitCenter = buttonQuit.getCenter()
    buttonGrayCenter = buttonGray.getCenter()
    buttonNegCenter = buttonNeg.getCenter()
    buttonOther1Center = buttonOther1.getCenter()
    buttonOther2Center = buttonOther2.getCenter()
    buttonOther3Center = buttonOther3.getCenter()

    retVal = 0

    if buttonLoadCenter.getX() - buttonWidth / 2 < pt.getX() < buttonLoadCenter.getX() + buttonWidth / 2 and \
        buttonLoadCenter.getY() - buttonHeight / 2 < pt.getY() < buttonLoadCenter.getY() + buttonHeight / 2:
        retVal =  LOADIMAGE

    elif buttonSaveCenter.getX() - buttonWidth / 2 < pt.getX() < buttonSaveCenter.getX() + buttonWidth / 2 and \
        buttonSaveCenter.getY() - buttonHeight / 2 < pt.getY() < buttonSaveCenter.getY() + buttonHeight / 2:
        retVal = SAVEIMAGE

    elif buttonQuitCenter.getX() - buttonWidth / 2 < pt.getX() < buttonQuitCenter.getX() + buttonWidth / 2 and \
        buttonQuitCenter.getY() - buttonHeight / 2 < pt.getY() < buttonQuitCenter.getY() + buttonHeight / 2:
        retVal = QUIT

    elif buttonGrayCenter.getX() - buttonWidth / 2 < pt.getX() < buttonGrayCenter.getX() + buttonWidth / 2 and \
        buttonGrayCenter.getY() - buttonHeight / 2 < pt.getY() < buttonGrayCenter.getY() + buttonHeight / 2:
        retVal = GRAYSCALE

    elif buttonNegCenter.getX() - buttonWidth / 2 < pt.getX() < buttonNegCenter.getX() + buttonWidth / 2 and \
        buttonNegCenter.getY() - buttonHeight / 2 < pt.getY() < buttonNegCenter.getY() + buttonHeight / 2:
        retVal = NEGATIVE

    elif buttonOther1Center.getX() - buttonWidth / 2 < pt.getX() < buttonOther1Center.getX() + buttonWidth / 2 and \
        buttonOther1Center.getY() - buttonHeight / 2 < pt.getY() < buttonOther1Center.getY() + buttonHeight / 2:
        retVal = OTHER1

    elif buttonOther2Center.getX() - buttonWidth / 2 < pt.getX() < buttonOther2Center.getX() + buttonWidth / 2 and \
        buttonOther2Center.getY() - buttonHeight / 2 < pt.getY() < buttonOther2Center.getY() + buttonHeight / 2:
        retVal = OTHER2
    elif buttonOther3Center.getX() - buttonWidth / 2 < pt.getX() < buttonOther3Center.getX() + buttonWidth / 2 and \
        buttonOther3Center.getY() - buttonHeight / 2 < pt.getY() < buttonOther3Center.getY() + buttonHeight / 2:
        retVal = OTHER3

    win.checkMouse()
    return retVal

def buttonFillToggle(button, buttonFillActive):
    """
    Toggles button fill color when clicked
    :param button: Rectangle -> button as a Rectangle object
    :param buttonFillActive: boolean -> current state of button
    :return: boolean -> toggled state for button
    """
    if buttonFillActive:
        button.setFill(color=buttonIdleFill)
        return False
    button.setFill(color=buttonActiveFill)
    return True

#   loadImage:
def loadImage():
    """
    Loads a user-specified image file from disk
    :return: None
    """
    global img, imgHeight, imgWidth, imgOrig
    img.undraw()

    # get the image file using askopenfilename from tkinter.filedialog
    imgFile = askopenfilename(filetypes=(("GIF files", "*.gif"), ("All files", "*.*")))

    # if no selection, return
    if not imgFile:
        return

    # open the file
    img = Image(Point(midX, midY), imgFile)
    imgOrig = img.clone()

    # get width and height of image and store to global variables
    imgWidth = img.getWidth(); imgHeight = img.getHeight()

    # display color image
    img.draw(win)

#   saveImage:
def saveImage():
    """
    Saves the image to disk with user-specified path
    :return: None
    """
    global img
    # save image using asksavefilename from tkinter.filedialog
    imgNew = asksaveasfilename()

    # if canceled, return
    # save the file
    if imgNew:
        img.save(imgNew)

#   New Effecg:
def NewEffect():
    """
    Converts image to new effect (or back to previous state if already new effect)
    :return: None
    """
    global img, imgOrig, isNewEffect
    # if already n
    if isNewEffect:
        # revert to original pixels
        img = imgOrig.clone()
        isNewEffect = False

    # otherwise
    else:
        # save state
        imgOrig = img.clone()

        # convert pixels to new effect
        #     using image width and height, get pixel rgb values and set to new effect
        for i in range(imgWidth):
            for j in range(imgHeight):
                rgb = img.getPixel(i, j)
                new_effect_1 = color_rgb(rgb[2]//2, rgb[1]//2, rgb[0]//2)
                img.setPixel(i, j, new_effect_1)
        isNewEffect = True

    # display new effect image
    img.undraw()
    img.draw(win)

#   negative:
def negative():
    """
    Converts image to color-negative
    :return: None
    """
    global img
    # convert pixels to color negative
    #     using image width and height, get pixel rgb values and set to color negative
    for i in range(imgWidth):
        for j in range(imgHeight):
            rgb = img.getPixel(i, j)
            negR = 255 - rgb[0]; negG = 255 - rgb[1]; negB = 255 - rgb[2]
            img.setPixel(i, j, color_rgb(negR, negG, negB))


    # display color negative image
    img.undraw()
    img.draw(win)



if __name__ == '__main__':
    main()