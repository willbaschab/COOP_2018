# U08_EX15_ImageNegative.py
#
#  Author: Will Baschab
#  Course: Coding for OOP
# Section: A2
#    Date: 1 April 2019
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 08
#
# Program Description
#  This program allows the user to upload an image and
# edit it with a photo negative function. The image can be saved
# or remove after it is edited.
#
# Algorithm (pseudocode)
"""
*** Refer to main() function for algorithm ***
"""
from graphics import *


# ==================================================
#           Array/Object Creation Methods
# ==================================================


def create_new_win(title, width, height):
    window = GraphWin(title, width, height)  # make the window according to arguments
    window.setCoords(0.0, 0.0, 10.0, 10.0)  # set coords on a 10x10 grid
    return window  # return the window object to caller


def create_textbox(lx, ly, ux, uy, color, text):
    # l values are coords of the lower left point of rectangle
    # u values are coords of the upper right point of rectangle
    r = Rectangle(Point(lx, ly), Point(ux, uy))  # uses l and y values to make rectangle
    r.setFill(color)  # takes color argument
    t = Text(r.getCenter(), text)  # draws text in the center of textbox

    return [r, t]  # in order to call on it as one object instead of two, return rectangle and text in array


def create_entreebox(lower, upper, display_text):
    """
    This method generates an object (in the form of an array) for entering text into

    ALG:
    - define rectangle using the lower and upper arguments (lower left and upper right points) and fill rectangle gray

    - define a second rectangle (going inside the first) to hold the text using <lower> and .5 off of <upper> for it's
    lower left point, and <upper> for it's upper right point
    - so that text can be seen, fill this rectangle with white

    - create text object in center of second rectangle using display_text argument

    - create entree object in center of first rectangle with a 20 character max, with a white fill

    - return the first and second rectangle, the text, and the entree as an array to caller
    """
    r = Rectangle(lower, upper)
    r.setFill('gray')

    display_rect = Rectangle(Point(lower.getX(), upper.getY() - .5), upper)
    display_rect.setFill('white')

    t = Text(display_rect.getCenter(), display_text)

    e = Entry(r.getCenter(), 20)
    e.setFill('white')

    return [r, display_rect, t, e]


def create_buttons(starting_point, width, height, spacing, titles_list, starting_color_list):
    """
    This function combines text boxes into one large list of buttons to the caller
    """
    buttons = []  # list of buttons to be returned

    for i in range(len(titles_list)):  # each title represents a button, and so if there are 4 titles, 4 buttons
        buttons.append(
            create_textbox(starting_point.getX() + (spacing * i),  # lx will start off at starting point
                           # but is iterable with spacing
                           starting_point.getY(),  # the buttons all have same ly values
                           starting_point.getX() + width + (spacing * i),  # upper right x adds width too
                           starting_point.getY() + height,  # add the height to ly so it is now uy
                           starting_color_list[i],  # if in correct order, color and title will match up
                           titles_list[i]))  # if in correct order, title with match up with title list
    return buttons


# ==================================================
#                  Drawing Methods
# ==================================================


def draw_objs(win, obj_list):
    # this method allows multiple objects in the same list to be drawn
    for i in obj_list:  # the list represents a textbox object usually
        i.draw(win)


def undraw_objs(obj_list):
    # this method allows multiple objects in the same list to be undrawn
    for i in obj_list:  # the list represents a textbox object usually
        i.undraw()


def draw_buttons(win, obj_list):
    # this method allows a list of text boxes (a list of lists) to be drawn with one command
    for i in obj_list:
        draw_objs(win, i)  # new layer of abstraction is represented by the use of draw_buttons()


def draw_exitbox(win, lowerbound, upperbound):
    upperline = upperbound - .125  # upperline can be used as the upper right coordinate (the x shape is in middle)
    lowerline = lowerbound + .125  # lowerline can be used as the lower left coordinate (x is in middle

    # creation and drawing of the exit box shape using lower/upper bound twice bc it is a square
    exit_box = Rectangle(Point(lowerbound, lowerbound), Point(upperbound, upperbound))
    exit_box.setFill('red')  # rarely have I seen an exit box that isn't red
    exit_box.draw(win)

    # creation of an x shape using the upper/lower line described for coords above
    left_right_line = Line(Point(lowerline, lowerline), Point(upperline, upperline))
    right_left_line = Line(Point(lowerline, upperline), Point(upperline, lowerline))

    # colorizing of lines
    left_right_line.setFill("white")
    right_left_line.setFill("white")

    # fixed width of lines after seeing what they looked like (they need to be larger)
    left_right_line.setWidth(4)
    right_left_line.setWidth(4)

    # both lines are drawn after exit box so that they show up
    left_right_line.draw(win)
    right_left_line.draw(win)


def draw_menu(win, buttons):
    # Create a rectangle to serve as backdrop for for buttons
    menu_area = Rectangle(Point(0, 8), Point(10, 10))
    menu_area.setFill(color_rgb(211, 211, 211))
    menu_area.draw(win)

    draw_exitbox(win, 9.5, 10)  # draws exit box in upper right corner on top of menu
    draw_buttons(win, buttons)  # draws the buttons onto the menu area


# ==================================================
#                   Logic Methods
# ==================================================

def change_color(tbox, color):
    tbox[0].setFill(color)  # refers to the rectangle in a textbox array and changes the fill based on arguments


def negative(win, img):
    """
    This method handles the transformation of an image into a negative of itself and returns the
    new image back to caller

    ALG:
    - get the number of rows and columns from the width and height of the image
    - a chunk the size a tenth of the image will be represented by the widths (number of rows) integer divided by 10

    - for each row in in the range of rows and for each column in the range of columns
        - get the pixel rgb data of specific row and column
        - set the pixel of same row and column to have the rgb value of (255 - (r value),
                                                                         255 - (g value),
                                                                         255 - (b value))

        - (outside of column loop) check if the current row divides with no remainder into a tenth of the image width
            - if it does, redraw the image with new pixel values

    - return image object to caller
    """
    rows = img.getWidth()
    columns = img.getHeight()
    chunksize = rows // 10

    for row in range(rows):
        for column in range(columns):
            rgb = img.getPixel(row, column)
            img.setPixel(row, column, color_rgb(255 - rgb[0], 255 - rgb[1], 255 - rgb[2]))

        if row % chunksize == 0:
            img.undraw()
            img.draw(win)

    return img


def is_inbounds_rectangle(mouse, lower, upper):
    lx, ly = lower.getX(), lower.getY()  # lx and ly represent the lower left corner of rectangle
    ux, uy = upper.getX(), upper.getY()  # ux and uy represent the upper right corner of rectangle

    if lx < mouse.getX() < ux and ly < mouse.getY() < uy:  # check if mouse is in-between the x's and y's
        return True  # if the mouse clicked inside the area, than return true


def is_inbounds_button(mouse, button):
    # because a button stores it's rectangle in an array, a different method is need for accessing it
    lower = button[0].getP1()  # button[0] is the button's rectangle object
    upper = button[0].getP2()

    # this part is same as is_inbounds_rectangle()
    lx, ly = lower.getX(), lower.getY()
    ux, uy = upper.getX(), upper.getY()

    if lx < mouse.getX() < ux and ly < mouse.getY() < uy:
        return True


def check_option(mouse, button, photo_state, state):
    if is_inbounds_button(mouse, button) and photo_state % 2 == state:
        # photo_state represents whether or not a photo has been put on the canvas
        # this method allows for the result of the modulus (1, or 0) to be chosen, which is useful later
        return True
    else:
        return False


# ==================================================
#               Active State Methods
# ==================================================


def draw_upload_dialog(win, upload_state, buttons, upload_entreebox):
    """
    This method controls the drawing of the upload box, allowing the user to close the dialog box
    by toggling the state of the upload dialog box with each start

    buttons[0] is the upload photo text box
    """
    if upload_state % 2 == 0:  # the state starts on 1, so by clicking it will become 2 and be drawn
        change_color(buttons[0], 'gray')  # the gray means that the dialog box is active
        draw_objs(win, upload_entreebox)  # draws entree dialog
    else:
        change_color(buttons[0], 'white')  # having been clicked again, the text box becomes white
        undraw_objs(upload_entreebox)  # and the entree dialogue closes


def draw_save_dialog(win, save_state, buttons, save_entreebox):
    """
        This method controls the drawing of the save dialog box, allowing the user to close the dialog box
        by toggling the state of the save dialog box with each start

        buttons[3] is the save photo text box
        """
    if save_state % 2 == 0:  # the state starts on 1, so by clicking it will become 2 and be drawn
        change_color(buttons[3], 'gray')  # the gray means that the dialog box is active
        draw_objs(win, save_entreebox)  # draws entree dialog
    else:
        change_color(buttons[3], 'white')  # having been clicked again, the text box becomes white
        undraw_objs(save_entreebox)  # and the entree dialogue closes


def display_image(win, buttons, upload_entreebox):
    """
    This method draws the photo to the window and returns the photo as an object to the caller

    upload_entreebox[3] is the user entree field object provided by graphics.py
    """
    upload_entreebox[3].setText(upload_entreebox[3].getText())  # overcautious of making sure user input is read
    undraw_objs(upload_entreebox)  # remove the entree field after input is received
    photo = Image(Point(5, 4), upload_entreebox[3].getText())  # 5,4 is middle of area that is not menu
    # photo gets filename from user entree field
    photo.draw(win)
    for i in range(1, 4):  # now that there is a photo, the other 3 buttons are able to be interacted with
        change_color(buttons[i], 'white')  # this is indicated by them being white

    return photo  # returns the photo to the caller so that other methods can use it


def save_image(win, photo, button, save_entreebox, save_text):
    """
        This method handles the process of saving the image and changing buttons after save

        save_entreebox[3] is the user entree field object provided by graphics.py
    """
    save_entreebox[3].setText(save_entreebox[3].getText())  # overcautious of making sure user input is read
    undraw_objs(save_entreebox)  # remove the entree field after input is received
    photo.save(save_entreebox[3].getText())  # this saves the photo to local folder with whatever name was given
    change_color(button, 'white')  # returns the save button to white after it has finished

    # Replacement of text stating save progress
    save_text.undraw()
    save_text.setText("Image Saved! Viewable after exit.")
    save_text.setFill('green')
    save_text.draw(win)


# ==================================================
#                  Main Function
# ==================================================


def main():
    """
    ALG:
    - make a new window

    - declare large scale variables such as lists, states, and photo variable

    - create save text at 1.5, 8.25 with initial message 'Not saved' in red (the program has only started)

    - create entree dialog boxes in center of edit area for saving and uploading
    - create buttons using list of titles and colors inside the menu area

    - draw the menu and the initial save status message

    - In while True state:
        - set checking of any key and mouse click to variables (key and mouse)

        - if the mouse variable returns anything:
            - break out of loop (ending program) if it is in the bounds of exit box

            - if click was in upload box:
                - add one to the upload state
                - run upload dialog method

            - if click was in remove box:
                - undraw the photo
                - add one to photo_state (photo is no longer present)
                - add one to upoad_state (with no photo, ability to upload is not blocked)
                - set the negative_state to 0 (with last image removed, the next one will not have been negative yet)

                - change upload text box to white and other three to gray

                -reset save text to unsaved

            - if click was in save textbox:
                - add one to the save state
                - run save dialog method

            - if click was in negative box and the photo has not been color negatived yet:
                - turn all buttons grey while this one is active

                - set photo equal to negative() method (it returns the photo after editing it)

                - add one to the negative_state (so that image can't be color negatived twice)
                - change the remove and save buttons back to white

        - if the key variable returns 'return':
            - if the upload_state is toggled on (even) and the save_state is not on (odd):
                - photo object created from display_image() method
                - the photo is present, so the photo_state turns on to 1 (photo_state adds one to itself)
            - if saving the photo (save state should be even, thus on):
                - run method save_image()

    """
    # Window creation
    win = create_new_win('Image Editor', 1000, 1000)

    # Main Variables
    titles = ['Upload Photo', 'Remove Photo', 'Negative of Photo', 'Save Photo']
    colors = ['white', 'gray', 'gray', 'gray']
    # buttons[0] is upload box
    # buttons[1] is remove box
    # buttons[2] is negative box
    upload_state = 1
    negative_state = 0
    save_state = 1
    photo_state = 0
    photo = None  # if removed, python will complain that photo is used before assignment

    # Save Text
    save_text = Text(Point(1.5, 8.25), "Not Saved")
    save_text.setFill('red')

    # Buttons and Entree Boxes
    upload_entreebox = create_entreebox(Point(3, 4.25), Point(7, 5.75),
                                        "Enter Filename (.gif, .png, or .ppm) in entree field:")
    save_entreebox = create_entreebox(Point(3, 4.25), Point(7, 5.75),
                                      "Enter Filename to save by (same type as upload)\nin entree field:")
    buttons = create_buttons(Point(.5, 9.25), 1.75, .5, 2, titles, colors)

    # draws buttons and menu template
    draw_menu(win, buttons)
    save_text.draw(win)

    while True:
        key = win.checkKey()
        mouse = win.checkMouse()

        if mouse:
            if is_inbounds_rectangle(mouse, Point(9.5, 9.5), Point(10, 10)):  # if in exit box
                break

            elif check_option(mouse, buttons[0], photo_state, 0):  # if in upload text box (and no photo)
                upload_state += 1
                draw_upload_dialog(win, upload_state, buttons, upload_entreebox)

            elif check_option(mouse, buttons[1], photo_state, 1):  # if in remove text box (and there is photo)
                photo.undraw()
                photo_state += 1
                upload_state += 1
                negative_state = 0

                change_color(buttons[0], 'white')
                for i in range(1, 4):
                    change_color(buttons[i], 'gray')

                # After removing photo, save text resets to unsaved work of next photo
                save_text.undraw()
                save_text.setText("Not Saved")
                save_text.setFill('red')
                save_text.draw(win)

            elif check_option(mouse, buttons[3], photo_state, 1):  # if in save text box (and there is photo)
                save_state += 1
                draw_save_dialog(win, save_state, buttons, save_entreebox)

            elif check_option(mouse, buttons[2], photo_state, 1) and negative_state % 2 == 0:  # if in save text box
                # and the image has not been color negatived yet (to prevent it from happening again)
                for i in range(1, 4):
                    change_color(buttons[i], 'gray')

                photo = negative(win, photo)

                negative_state += 1
                change_color(buttons[1], 'white')
                change_color(buttons[3], 'white')

        if key == 'Return':
            if upload_state % 2 == 0 and save_state % 2 == 1:  # if the user presses enter
                # after writing filename to display photo (to make sure it is only upload, check save and upload state)
                photo = display_image(win, buttons, upload_entreebox)
                photo_state += 1

            if save_state % 2 == 0:  # if key is hit and the user meant to save,
                save_image(win, photo, buttons[3], save_entreebox, save_text)


if __name__ == '__main__':
    main()
