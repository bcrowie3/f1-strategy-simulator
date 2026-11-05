import flet.testing as ftt


async def test_setup_back_button(flet_app: ftt.FletTestApp):
    tester = flet_app.tester

    await tester.pump_and_settle()

    #Tapping the "start" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking initial state
    assert (await tester.find_by_text("Select a driver, track, and difficulty")).count == 1

    #Checking back button exists
    assert (await tester.find_by_key("back")).count == 1

    #Tapping the "back" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("back"))
    await tester.pump_and_settle()

    #Checking home page appears
    assert (await tester.find_by_text("F1 Strategy Simulator")).count == 1