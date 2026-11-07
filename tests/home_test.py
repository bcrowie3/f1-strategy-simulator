import flet.testing as ftt


async def test_start_button(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester

    await tester.pump_and_settle()

    #Checking initial state
    assert (await tester.find_by_text("F1 Strategy Simulator")).count == 1

    #Checking Start button exists
    assert (await tester.find_by_key("start")).count == 1

    #Tapping the "start" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking setup page appears
    assert (await tester.find_by_text("Race Setup")).count == 1