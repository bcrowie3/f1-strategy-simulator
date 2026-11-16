import flet.testing as ftt
from src.constants.drivers import DRIVERS
from src.constants.tracks import TRACKS
from src.constants.difficulty import DIFFICULTY_LEVELS
import random

#Testing the back button works
async def test_setup_back_button(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Navigating to the setup page
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking back button exists
    assert (await tester.find_by_key("back")).count == 1

    #Tapping the "back" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("back"))
    await tester.pump_and_settle()

    #Checking home page appears
    assert (await tester.find_by_text("F1 Strategy Simulator")).count == 1

#Testing all drivers are available for selection
async def test_all_drivers_available(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the "start" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checks that each driver has a corresponding button
    for key in DRIVERS.keys():
        assert (await tester.find_by_key(key)).count == 1

#Testing all tracks are available for selection
async def test_all_tracks_available(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the "start" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checks that each track has a corresponding button
    for key in TRACKS.keys():
        assert (await tester.find_by_key(key)).count == 1

#Testing all difficulties are available for selection
async def test_all_difficulties_available(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the "start" button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checks that each difficulty has a corresponding button
    for key in DIFFICULTY_LEVELS.keys():
        assert (await tester.find_by_key(key)).count == 1

#Testing qualifying button before any selections made (invalid)
async def test_qualifying_button_invalid_1(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button before a track and difficulty are selected (invalid)
async def test_qualifying_button_invalid_2(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    index = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[index]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button before a track is selected (invalid)
async def test_qualifying_button_invalid_3(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    index = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[index]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking a random difficulty button exists
    index = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[index]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button before a driver and track are selected (invalid)
async def test_qualifying_button_invalid_4(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random difficulty button exists
    index = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[index]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button before a driver and difficulty are selected (invalid)
async def test_qualifying_button_invalid_5(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    index = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)

    track = tracks[index]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button before a driver is selected (invalid)
async def test_qualifying_button_invalid_6(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    index = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)

    track = tracks[index]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking a random difficulty button exists
    index = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[index]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button before a difficulty is selected (invalid)
async def test_qualifying_button_invalid_7(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    index = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)

    track = tracks[index]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    index = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[index]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking the test does not navigate away from the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

#Testing qualifying button once all selections are made (valid)
async def test_qualifying_button_valid(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Race Setup")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    index = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)

    track = tracks[index]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    index = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[index]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking a random difficulty button exists
    index = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[index]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the qualifying button exists
    assert (await tester.find_by_key("qualifying")).count == 1

    #Tapping the qualifying button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("qualifying"))
    await tester.pump_and_settle()

    #Checking that the app has navigated to the qualifying page
    assert (await tester.find_by_key("qualis chequered flag")).count == 1

#Testing that clicking a driver button selects a driver via the instruction line response
async def test_driver_selection(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    index = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[index]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping/selecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the instruction line shows a driver selection is not needed
    assert (await tester.find_by_text("Before proceeding, please select a track and difficulty.")).count == 1

    #Generating a new random index that is different to the original index
    index2 = random.randrange(7)
    while index2 == index:
        index2 = random.randrange(7)
    driver2 = drivers[index2]

    #Tapping/selecting my second randomly selected driver button
    await tester.tap(await tester.find_by_key(driver2))
    await tester.pump_and_settle()

    #Checking the instruction line does not change as a driver is still selected
    assert (await tester.find_by_text("Before proceeding, please select a track and difficulty.")).count == 1

    #Tapping/deselecting my second randomly selected driver button
    await tester.tap(await tester.find_by_key(driver2))
    await tester.pump_and_settle()

    #Checking the instruction line shows a driver selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

#Testing that clicking a track button selects a track via the instruction line response
async def test_track_selection(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    index = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)
        
    track = tracks[index]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping/selecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking the instruction line shows a track selection is not needed
    assert (await tester.find_by_text("Before proceeding, please select a driver and difficulty.")).count == 1

    #Generating a new random index that is different to the original index
    index2 = random.randrange(len(TRACKS))
    while index2 == index:
        index2 = random.randrange(len(TRACKS))
    track2 = tracks[index2]

    #Tapping/selecting my second randomly selected track button
    await tester.tap(await tester.find_by_key(track2))
    await tester.pump_and_settle()

    #Checking the instruction line does not change as a track is still selected
    assert (await tester.find_by_text("Before proceeding, please select a driver and difficulty.")).count == 1

    #Tapping/deselecting my second randomly selected track button
    await tester.tap(await tester.find_by_key(track2))
    await tester.pump_and_settle()

    #Checking the instruction line shows a track selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

#Testing that clicking a difficulty button selects a difficulty via the instruction line response
async def test_difficulty_selection(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random difficulty button exists
    index = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[index]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping/selecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the instruction line shows a difficulty selection is not needed
    assert (await tester.find_by_text("Before proceeding, please select a driver and track.")).count == 1

    #Generating a new random index that is different to the original index
    index2 = random.randrange(len(DIFFICULTY_LEVELS))
    while index2 == index:
        index2 = random.randrange(len(DIFFICULTY_LEVELS))
    level2 = diffLevels[index2]

    #Tapping/selecting my second randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level2))
    await tester.pump_and_settle()

    #Checking the instruction line does not change as a difficulty is still selected
    assert (await tester.find_by_text("Before proceeding, please select a driver and track.")).count == 1

    #Tapping/deselecting my second randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level2))
    await tester.pump_and_settle()

    #Checking the instruction line shows a difficulty selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

#Testing that clicking difficulty and track buttons selects a difficulty and track via the instruction line response
async def test_diff_and_track_selection(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random difficulty button exists
    dIndex = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[dIndex]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping/selecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    tIndex = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)
        
    track = tracks[tIndex]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping/selecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking the instruction line shows difficulty and track selections are not needed
    assert (await tester.find_by_text("Before proceeding, please select a driver.")).count == 1

    #Tapping/deselecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Tapping/deselecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking the instruction line shows a difficulty selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

#Testing that clicking difficulty and driver buttons selects a difficulty and driver via the instruction line response
async def test_diff_and_driver_selection(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random difficulty button exists
    dIndex = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[dIndex]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping/selecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    drIndex = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[drIndex]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping/selecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the instruction line shows difficulty and driver selections are not needed
    assert (await tester.find_by_text("Before proceeding, please select a track.")).count == 1

    #Tapping/deselecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Tapping/deselecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the instruction line shows a difficulty selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

#Testing that clicking track and driver buttons selects a track and driver via the instruction line response
async def test_track_and_driver_selection(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    tIndex = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)
        
    track = tracks[tIndex]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping/selecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    drIndex = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[drIndex]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping/selecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the instruction line shows difficulty and driver selections are not needed
    assert (await tester.find_by_text("Before proceeding, please select a difficulty.")).count == 1

    #Tapping/deselecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Tapping/deselecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking the instruction line shows a difficulty selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

#Testing that clicking all buttons makes all selections via the instruction line response
async def test_all_selections(flet_app: ftt.FletTestApp):
    #Starting the app and letting it load
    tester = flet_app.tester
    await tester.pump_and_settle()

    #Tapping the start button (found by its key) and let the UI update
    await tester.tap(await tester.find_by_key("start"))
    await tester.pump_and_settle()

    #Checking the test has reached its start point, the setup page
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1

    #Checking a random track button exists - limiter will be needed in future if more tracks present
    tIndex = random.randrange(len(TRACKS))
    tracks = []
    for key in TRACKS:
        tracks.append(key)
        
    track = tracks[tIndex]
    assert (await tester.find_by_key(track)).count == 1

    #Tapping/selecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Checking a random driver (top 7) button exists - top 7 visible w/o scrolling
    drIndex = random.randrange(7)
    drivers = []
    no = 0
    for key in DRIVERS:
        if no == 7:
            break
        no += 1
        drivers.append(key)
    driver = drivers[drIndex]
    assert (await tester.find_by_key(driver)).count == 1

    #Tapping/selecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Checking a random difficulty button exists
    dIndex = random.randrange(len(DIFFICULTY_LEVELS))
    diffLevels = []
    for key in DIFFICULTY_LEVELS:
        diffLevels.append(key)

    level = diffLevels[dIndex]
    assert (await tester.find_by_key(level)).count == 1

    #Tapping/selecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the instruction line shows difficulty and driver selections are not needed
    assert (await tester.find_by_text("All necessary selections have been satisfied.")).count == 1

    #Tapping/deselecting my randomly selected track button
    await tester.tap(await tester.find_by_key(track))
    await tester.pump_and_settle()

    #Tapping/deselecting my randomly selected driver button
    await tester.tap(await tester.find_by_key(driver))
    await tester.pump_and_settle()

    #Tapping/deselecting my randomly selected difficulty button
    await tester.tap(await tester.find_by_key(level))
    await tester.pump_and_settle()

    #Checking the instruction line shows a difficulty selection is needed again
    assert (await tester.find_by_text("Before proceeding, please select a driver, track, and difficulty.")).count == 1