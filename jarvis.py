import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

app_id= #enter your API key here
client = wolframalpha.Client(app_id)

sg.theme('LightTeal')	                    # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Jarvis', layout)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# sg.PopupNonBlocking("Results from Wikipedia: ",res_wiki, "Results from Wolfram: ", res_wolfram)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    try:
        res_wiki = wikipedia.summary(values[0], sentences=2)
        res_wolfram = next(client.query(values[0]).results).text
        engine.say(res_wolfram)
        sg.PopupNonBlocking("Results from Wikipedia: ", res_wiki, "Results from Wolfram: ", res_wolfram)
    except wikipedia.exceptions.DisambiguationError:
        res_wolfram = next(client.query(values[0]).results).text
        engine.say(res_wolfram)
        sg.PopupNonBlocking(res_wolfram)
    except wikipedia.exceptions.PageError:
        res_wolfram = next(client.query(values[0]).results).text
        engine.say(res_wolfram)
        sg.PopupNonBlocking(res_wolfram)
    except wikipedia.exceptions.HTTPTimeoutError:
        res_wolfram = next(client.query(values[0]).results).text
        engine.say(res_wolfram)
        sg.PopupNonBlocking(res_wolfram)
    except wikipedia.exceptions.RedirectError:
        res_wolfram = next(client.query(values[0]).results).text
        engine.say(res_wolfram)
        sg.PopupNonBlocking(res_wolfram)
    except:
        res_wiki = wikipedia.summary(values[0], sentences=2)
        engine.say(res_wolfram)
        sg.PopupNonBlocking(res_wiki)
    #res = client.query(values[0])
    #res_wolfram = next(res.results).text
    #res_wiki = wikipedia.summary(values[0], sentences=2)

    engine.runAndWait()

window.close()
