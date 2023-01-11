from csv_creater import CSV
from readfile import Read
import validation
import PySimpleGUI as sg
import os


# from pathlib import Path

# selects default theme for window
def theme():
    new_theme = {'BACKGROUND': sg.COLOR_SYSTEM_DEFAULT,
                 'TEXT': sg.COLOR_SYSTEM_DEFAULT,
                 'INPUT': sg.COLOR_SYSTEM_DEFAULT,
                 'TEXT_INPUT': sg.COLOR_SYSTEM_DEFAULT,
                 'SCROLL': sg.COLOR_SYSTEM_DEFAULT,
                 'BUTTON': sg.COLOR_SYSTEM_DEFAULT,
                 'PROGRESS': sg.COLOR_SYSTEM_DEFAULT,
                 'BORDER': 2, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 }
    return new_theme


# Theme function is initialized
sg.theme_add_new("mytheme", theme())
sg.theme('mytheme')

# Window layout

layout = [[sg.Push(),
           sg.Text("Convert Text file into Excel File", font='_ 11 bold', text_color='Darkgreen', auto_size_text=True,
                   relief=sg.RELIEF_RAISED, grab=True, border_width=2), sg.Push()],
          [sg.Text("Enter the Text file name: ")],
          [sg.Input(key='-INPUT-', do_not_clear=True), sg.Push(),
           sg.FileBrowse(target='-INPUT-', button_color='white on green', tooltip='select a file',
                         file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))),
           sg.Button("Read", key='-READ-', use_ttk_buttons=True, mouseover_colors='white on green',
                     tooltip='Read the file')],
          [sg.Push(), sg.Text("Select Log type", relief=sg.RELIEF_SUNKEN, border_width=3, background_color='grey88'),
           sg.Radio('Cloud', 'Group 1', enable_events=True, k='-R1-'),
           sg.Radio('MGO', 'Group 1', enable_events=True, k='-R2-'),
           sg.Radio('OBSFAILA', 'Group 1', enable_events=True, k='-R3-'),
           sg.Push()],
          [sg.Text("Enter the Excel file name:"),
           sg.Input(key='-OUTPUT-', do_not_clear=True, size=(23, 1), default_text='.xlsx'), sg.Push(),
           sg.Button("Submit", size=(13, 1), key='-SUBMIT-', mouseover_colors='white on green', use_ttk_buttons=True,
                     bind_return_key=True,
                     tooltip="Press Enter to get the Excel file")],
          [sg.Button("Exit", size=(10, 1), use_ttk_buttons=True, mouseover_colors='Red on grey70')]]

window = sg.Window("Log File Extractor", layout, keep_on_top=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-READ-':
        if 'mlog.txt':
            try:  # Deletes the old "mlog.txt" file if exists 
                os.unlink('mlog.txt')
            except:
                pass
            validation_result = validation.validate(values)
            if validation_result["is_valid"]:
                # if Path(values['-INPUT-']).is_file():
                #     try:
                # Read operation is impelemented if input is valid
                file_read = Read(input_text=values['-INPUT-'], output_text='mlog.txt')
                if values['-R1-']:
                    sg.popup_quick_message('Reading Text file Please Wait!', background_color='brown',
                                           text_color='white', keep_on_top=True, auto_close_duration=2,
                                           location=(860, 620), modal=True)
                    try:
                        modify_file = file_read.Modify_cloud()
                    except IndexError:
                        sg.Popup("It looks some fields are" + '\n' " different from others", keep_on_top=True,
                                 icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                elif values['-R2-']:
                    sg.popup_quick_message('Reading Text file Please Wait!', background_color='brown',
                                           text_color='white', keep_on_top=True, auto_close_duration=2,
                                           location=(860, 620), modal=True)

                    try:
                        modify_file = file_read.Modify_MGO()
                    except IndexError:
                        sg.Popup("It looks some fields are" + '\n' "different from others", keep_on_top=True,
                                 icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                elif values['-R3-']:
                    sg.popup_quick_message('Reading Text file Please Wait!', background_color='brown',
                                           text_color='white', keep_on_top=True, auto_close_duration=2,
                                           location=(860, 620), modal=True)

                    try:
                        modify_file = file_read.Modify_OBSFAILA()
                    except IndexError:
                        sg.Popup("It looks some fields are" + '\n' "different from others", keep_on_top=True,
                                 icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                else:
                    sg.Popup("Log type not selected!", keep_on_top=True,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
            # except Exception as e:
            #     sg.Popup("File Error", e, keep_on_top=True)
            else:
                error_message = validation.generate_error_message(validation_result["values_invalid"])
                sg.popup(error_message, icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING, keep_on_top=True)
    elif event == '-SUBMIT-':
        validation_result = validation.validate1(values)
        if validation_result["is_valid"]:
            # CSV creation is started if input is valid
            csv_create = CSV(output_text='mlog.txt', output_csv=values['-OUTPUT-'])
            if values['-R1-']:
                try:
                    csv_create.conversion_cloud()
                    os.unlink('mlog.txt')
                    sg.Popup(f"The File '{values['-OUTPUT-']}' has been created", title=':)', auto_close=True,
                             auto_close_duration=2,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, keep_on_top=True)
                    # After CSV creation input and Radio buttons are cleared
                    window['-INPUT-'].update(' ')
                    window['-OUTPUT-'].update('.xlsx')
                    window['-R1-'].update(False)
                    window['-R2-'].update(False)
                except:
                    sg.Popup("It looks Incorrect" + '\n' " Log Type selected", keep_on_top=True,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL)
            elif values['-R2-']:
                try:
                    csv_create.conversion_MGO()
                    os.unlink('mlog.txt')
                    sg.Popup(f"The File '{values['-OUTPUT-']}' has been created", title=':)', auto_close=True,
                             auto_close_duration=2,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, keep_on_top=True)
                    window['-INPUT-'].update(' ')
                    window['-OUTPUT-'].update('.xlsx')
                    window['-R1-'].update(False)
                    window['-R2-'].update(False)
                    window['-R3-'].update(False)
                except:
                    sg.Popup("It looks Incorrect" + '\n' " Log Type selected", keep_on_top=True,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL)
            elif values['-R3-']:
                try:
                    csv_create.conversion_OBSFAILA()
                    os.unlink('mlog.txt')
                    sg.Popup(f"The File '{values['-OUTPUT-']}' has been created", title=':)', auto_close=True,
                             auto_close_duration=2,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, keep_on_top=True)
                    window['-INPUT-'].update(' ')
                    window['-OUTPUT-'].update('.xlsx')
                    window['-R1-'].update(False)
                    window['-R2-'].update(False)
                    window['-R3-'].update(False)
                except:
                    sg.Popup("It looks Incorrect" + '\n' " Log Type selected", keep_on_top=True,
                             icon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL)
        else:  # Error message is generated if input is invalid
            error_message = validation.generate_error_message(validation_result["values_invalid"])
            sg.popup(error_message, icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING, keep_on_top=True)
window.close()
