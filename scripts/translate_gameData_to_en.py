import json
from pathlib import Path

GAME_DATA_PATH = Path("public/data/gameData.json")

def main() -> None:
    data = json.loads(GAME_DATA_PATH.read_text(encoding="utf-8"))

    data.setdefault("meta", {})
    data["meta"]["gameTitle"] = "911 (temp)"
    data["meta"]["setting"] = "1990s Detroit, USA"
    data["meta"]["totalScenes"] = 10
    data["meta"]["note"] = "No saves. Reload restarts from Scene 1."

    scene_titles = {
        "scene1": "Morning  Missing Breakfast",
        "scene2": "Morning  The Diner and the Ring",
        "scene3": "Morning  Leaden Sky",
        "scene4": "Morning  No Badge",
        "scene5": "Noon  The Vending Machine",
        "scene6": "Evening  The Detour",
        "scene7": "Evening  Homework and Notes",
        "scene8": "Night  A Neighbor's Knock",
        "scene9": "Night  The Voice in the Noise",
        "scene10": "Night  The Fuse Box",
    }

    scene_text = {
        "scene1": (
            "Before the alarm clock could ring, the refrigerator's motor gave a low groan.\n"
            "When I opened the door, the cold air felt strangely energetic.\n"
            "No milk. The egg carton was light, too.\n"
            "Outside the window, Detroit morning smudged the street in pale exhaust.\n"
            "Mary had already left for work; only a note remained.\n"
            "Pick up groceries on your way back today, okay?\n"
            "She'd asked yesterday. It was today now.\n"
            "Lily looked like she was waiting for cocoa.\n"
            "Tommy was practicing tying his shoelaces.\n"
            "A father's day starts tilting from these small shortages.\n"
            "I patted my jacket pocket and felt how thin my wallet was."
        ),
        "scene2": (
            "The diner's doorbell always rings a beat late.\n"
            "The smell of grease and coffee loosens your shoulders before you even sit down.\n"
            "The waitress, a familiar face, guides us to a booth with a grin.\n"
            "Something's wrong with the phone this morning, she says. It keeps saying nine-one-one.\n"
            "The wall phone did ring once, short and sharp.\n"
            "Then it stopped, and the place swallowed the silence like nothing happened.\n"
            "Outside: a school bus, a newspaper kid, and the far howl of a siren.\n"
            "I picture pancakes for the family.\n"
            "And still, for some reason, someone's breathing lingers in my ear.\n"
            "Maybe the right way to start a day is not to leave a feeling like this unattended."
        ),
        "scene3": (
            "The car is old, but the engine still has grit.\n"
            "AM radio. The news repeats the same words until they turn to static.\n"
            "Emergency lines. Routing issues. Misconnections.\n"
            "My company is out in the suburbs, normally one straight shot on the highway.\n"
            "But the sky today is a heavy, leaden gray.\n"
            "At an intersection, the light seems to change a fraction of a beat too late.\n"
            "It's tiny. And tiny delays are where accidents begin.\n"
            "Speeding up is easy. Slowing down takes nerve.\n"
            "Along the edge of the windshield, a black bird keeps pace at the same height.\n"
            "I know I can't catch it."
        ),
        "scene4": (
            "The company parking lot smells like metal in the morning cold.\n"
            "At the security gate, people line up in sleepy, practiced order.\n"
            "I reach for my chest pocket and feel nothing but fabric.\n"
            "My badge is gone.\n"
            "Maybe it slipped between the couch cushions.\n"
            "Maybe I set it down while helping with homework.\n"
            "The guard's face stays blank, but his eyes are busy.\n"
            "Procedure is a hassle.\n"
            "But it's also a ritual that keeps accidents from happening.\n"
            "I say my own name silently, making sure it still fits."
        ),
        "scene5": (
            "Noon. The office air tastes of paper and fluorescent light.\n"
            "The numbers from the meeting roll through my head like coins.\n"
            "Frank claps my shoulder and laughs.\n"
            "Lunch? The vending machine's enough.\n"
            "It's old. The labels are worn down.\n"
            "C3 looks like G3.\n"
            "Press wrong, and something else drops.\n"
            "And it's not only snacks that drop like that.\n"
            "A worry falls into your gut the same way.\n"
            "I think of the kids at breakfast and listen to my stomach."
        ),
        "scene6": (
            "When work ends, the city's noise steps forward all at once.\n"
            "Horns in rush hour, a distant siren, the beep of a checkout scanner.\n"
            "In the parking lot, turning the key, I remember the empty fridge.\n"
            "Forgetting groceries stops being one person's mistake the moment you get home.\n"
            "The supermarket is a detour.\n"
            "But detours are sometimes the safest route.\n"
            "The radio insists: misdirected emergency calls are being resolved. Please remain calm.\n"
            "Staying calm is hard.\n"
            "Still, I know what I need to do."
        ),
        "scene7": (
            "I open the front door and the smell of home pushes back the smell of work.\n"
            "Evening light is thin; the curtains cast long shadows on the floor.\n"
            "Lily's poster board on the table looks like a galaxy of clutter.\n"
            "Dad, I have to build a volcano by tomorrow. I need styrofoam.\n"
            "Tommy watches TV, but the volume is too low, so low it's unsettling.\n"
            "Another note has appeared on the refrigerator.\n"
            "The word please looks darker than yesterday.\n"
            "A father's job is to help.\n"
            "Not helping is easy.\n"
            "And whenever I choose the easy way, the sirens outside feel a little closer."
        ),
        "scene8": (
            "After sunset, Detroit turns suddenly quiet.\n"
            "So quiet the house's creaks sound like conversation.\n"
            "A knock. Twice. Evenly spaced.\n"
            "Mr. Hudson from next door stands there, hat in hand.\n"
            "Sorry, David. There's a weird smell out back. Like something's burning.\n"
            "Burning is just another word for fire.\n"
            "Fire is why you call.\n"
            "Calling tonight feels unreliable.\n"
            "But fire doesn't wait.\n"
            "I feel my family's breathing behind me and look into the dark."
        ),
        "scene9": (
            "The air behind the house is cold, and the burnt smell is real.\n"
            "But I can't see flames. No smoke.\n"
            "A fire you can't see is the worst kind.\n"
            "Back inside, the phone rings again, this time clearly.\n"
            "The line is a nest of noise, and inside it a woman's voice.\n"
            "This is nine-one-one. Can you hear me?\n"
            "It says 911, but it feels far away.\n"
            "She recites my address. She knows how many people are in my house.\n"
            "My throat dries out.\n"
            "A wrong number shouldn't know that much."
        ),
        "scene10": (
            "Her voice stays calm, too calm.\n"
            "Go to the basement fuse box right now. The smell isn't fire. It's electricity.\n"
            "The basement stairs are dark, the wooden rail damp to the touch.\n"
            "My flashlight cuts old appliances and cardboard into pieces.\n"
            "At the fuse box, I find it: a run of wire blackened, but not yet burning.\n"
            "If I act now, I can stop it.\n"
            "But deeper in the basement is another door.\n"
            "Since when was that there?\n"
            "I reach out, and choose where my hand goes."
        ),
    }

    choice_texts = {
        "scene1": (
            "Go to the usual diner and grab something quick for everyone.",
            "Skip breakfast and head to work early.",
        ),
        "scene2": (
            "Ask what happened and check the phone receiver once.",
            "Ignore it, pay quickly, and step outside.",
        ),
        "scene3": ("Stay on the main road and drive carefully.", "Take a shortcut through the back streets."),
        "scene4": ("Explain and follow the proper check-in procedure.", "Slip in behind someone and get through the gate."),
        "scene5": ("Double-check the label and choose carefully.", "Just press a button  anything is fine."),
        "scene6": ("Stop by the supermarket before going home.", "Go straight home and deal with it later."),
        "scene7": ("Help Lily with the project and check on Tommy.", "Tell them you're tired and sit down for a minute."),
        "scene8": ("Go outside with Hudson and check the smell.", "Dismiss it and close the door for the night."),
        "scene9": ("Keep her talking and do exactly what she says.", "Hang up. It has to be a prank."),
        "scene10": ("Cut the power at the fuse box first.", "Open the strange door in the back first."),
    }

    for scene in data.get("scenes", []):
        scene_id = scene.get("id")
        if scene_id in scene_titles:
            scene["title"] = scene_titles[scene_id]
        if scene_id in scene_text:
            scene["storyText"] = scene_text[scene_id]

        if scene_id in choice_texts and isinstance(scene.get("choices"), list) and len(scene["choices"]) == 2:
            a, b = choice_texts[scene_id]
            scene["choices"][0]["text"] = a
            scene["choices"][1]["text"] = b

    bad_titles = {
        "bad_scene01_b": "BAD END  Early Shift",
        "bad_scene02_b": "BAD END  Ice",
        "bad_scene03_b": "BAD END  Shortcut",
        "bad_scene04_b": "BAD END  Wrong Exit",
        "bad_scene05_b": "BAD END  Wrong Button",
        "bad_scene06_b": "BAD END  Dead Batteries",
        "bad_scene07_b": "BAD END  Just a Minute",
        "bad_scene08_b": "BAD END  Smoke Alarm",
        "bad_scene09_b": "BAD END  Cut Line",
        "bad_scene10_b": "BAD END  The Phone Room",
    }

    bad_text = {
        "bad_scene01_b": (
            "David skipped breakfast and reached the company early.\n"
            "7:30 AM. The front gate wasn't even open yet.\n"
            "Hard work sometimes just spins its wheels.\n"
            "When I cut around to the service entrance, two shadows waited where no one should be.\n"
            "The moment they turned, it felt like they'd been expecting my shift.\n"
            "A blunt impact rang inside my skull. The world warped.\n"
            "The ambulance siren drifted farther and farther away.\n"
            "But somehow, the only bell that kept ringing was a phone  deep in my ear.\n"
            "As the stretcher rolled, I heard a voice like the diner waitress: the phone's been weird today.\n"
            "I never managed to answer before the dark took me."
        ),
        "bad_scene02_b": (
            "I rushed the bill and hurried the family outside.\n"
            "The doorbell rang a beat late, and in that beat, my foot slid.\n"
            "My head met frozen pavement.\n"
            "Pain came second. First came the hiss of phone noise blooming in my ear.\n"
            "Someone shouted to call an ambulance.\n"
            "But the diner phone wouldn't reach 911.\n"
            "Instead it connected to an unfamiliar voicemail.\n"
            "A woman's voice repeating: this is this is\n"
            "The bleeding shouldn't have been much, but my awareness tore like thin paper.\n"
            "The last sound I heard wasn't a bell or a siren, just metal hitting the ground."
        ),
        "bad_scene03_b": (
            "A shortcut shows you the city's underside.\n"
            "The factory walls are covered in graffiti; the windows are faces without eyes.\n"
            "The radio cuts out, replaced by sirens crawling into the car.\n"
            "Before I could locate them, the road sank.\n"
            "Hollow underneath.\n"
            "The car tipped, and my world became a slanted angle.\n"
            "No signal. The payphone was broken.\n"
            "The number that should have helped routed to someone else.\n"
            "On the other end, a woman said calmly: I thought you'd choose this way."
        ),
        "bad_scene04_b": (
            "I slipped through the gate behind a coworker. The alarm didn't sound.\n"
            "No alarm is worse.\n"
            "The hallway lights didn't flicker; they blinked, like an eye.\n"
            "The guard looked over too late.\n"
            "You're not supposed to be here today.\n"
            "Then the PA system glitched and broadcast FIRE across the whole building.\n"
            "Exit signs flipped, pointing the wrong way.\n"
            "The crowd surged to one door, and the door never opened.\n"
            "I fell. A shoe pressed into my chest.\n"
            "The last thing I heard wasn't the fire bell. It was a phone ringing."
        ),
        "bad_scene05_b": (
            "The vending machine labels were worn down. C3 looked like G3.\n"
            "What fell wasn't a snack; it was an old emergency whistle.\n"
            "Frank laughed. He couldn't stop.\n"
            "I blew the whistle. No sound came out.\n"
            "Instead, every phone in the office rang at once.\n"
            "It rang, and nobody answered.\n"
            "My stomach clenched; this wasn't hunger.\n"
            "At the edge of my vision, coworkers thinned like paper.\n"
            "As I went down, one thought stuck: I should have reached the right number."
        ),
        "bad_scene06_b": (
            "A traffic light appeared where it shouldn't exist.\n"
            "The green was too short, and the cars behind me grew angry.\n"
            "At home, my flashlight was dead, and the basement's black got thicker.\n"
            "In that dark, something flashed white behind the wiring.\n"
            "A spark ran. The burnt smell surged.\n"
            "The phone rang, and the woman said, calm as ever: if you'd bought batteries, you would have seen it.\n"
            "I couldn't see. And the burnt air slid into my throat.\n"
            "Help never reached a number that mattered."
        ),
        "bad_scene07_b": (
            "The couch takes your weight like it was made for you.\n"
            "I meant to rest just for a minute.\n"
            "But just for a minute multiplies.\n"
            "Something scraped in the kitchen.\n"
            "I turned too late.\n"
            "Late is only a beat until a beat becomes a disaster.\n"
            "Curiosity touches the word gas.\n"
            "I grabbed the phone and tried to dial 911, but the TV spoke first.\n"
            "The anchor read my address out loud.\n"
            "Calls may be misrouted\n"
            "Then the anchor looked at me and mouthed: too late."
        ),
        "bad_scene08_b": (
            "I shut the door, and the burnt smell stayed inside.\n"
            "A smell that lingers is usually real.\n"
            "At midnight, the smoke alarm went off.\n"
            "It rang politely, like a phone bell.\n"
            "Downstairs, the wiring was black and the insulation had melted.\n"
            "The fire was still small, but the exit felt far away.\n"
            "The front lock wouldn't turn.\n"
            "Something was stuffed in the keyhole  paper, jammed deep.\n"
            "On it, three digits: 911.\n"
            "Outside, Hudson said: I tried to call for help. It won't connect."
        ),
        "bad_scene09_b": (
            "When I hung up, the room's silence got heavier.\n"
            "Heavier silence has weight.\n"
            "In the basement, the back door clicked on its own.\n"
            "No receiver in my hand  yet the woman's voice was clear: you cut the line. So you'll hear it alone.\n"
            "Before I could ask what, a small flash bloomed inside the fuse box.\n"
            "Beautiful like fireworks. And then it stole the air."
        ),
        "bad_scene10_b": (
            "The back door opened too easily.\n"
            "A door that light is closer to a dream than to reality.\n"
            "Inside was a narrow room lined with old telephones.\n"
            "Every cord was cut.\n"
            "And still, they all rang at once.\n"
            "Newspaper clippings littered the floor  headlines blurred by damp ink.\n"
            "One line seemed to float up: the man who didn't cut the power was misrouted with his whole house.\n"
            "Behind me, the wiring made a sound like burning.\n"
            "It wasn't the house that was burning.\n"
            "It was the possibility of going back."
        ),
    }

    for bad_end in data.get("badEnds", []):
        bad_id = bad_end.get("id")
        if bad_id in bad_titles:
            bad_end["title"] = bad_titles[bad_id]
        if bad_id in bad_text:
            bad_end["deathText"] = bad_text[bad_id]

    if isinstance(data.get("clear"), dict):
        data["clear"]["title"] = "GAME CLEAR"
        data["clear"]["clearText"] = (
            "When I cut the fuse, the house went silent for exactly one beat.\n"
            "The refrigerator's groan, the clock's ticking, the distant sirens  everything.\n"
            "In that darkness I counted my family's breathing.\n"
            "If you can count it, you can still protect it.\n"
            "Upstairs, the phone was ringing.\n"
            "But before I could pick up, the answering machine played by itself.\n"
            "Her voice sounded more human than ever.\n"
            "This is 911. The misconnection has been resolved.\n"
            "You chose the right order today.\n"
            "The ordinary fact that tomorrow will come felt both the strangest and the most beautiful thing.\n"
            "The phone never rang again."
        )

    GAME_DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
