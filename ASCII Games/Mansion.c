// Escape the Mansion Final C Project
// Javin Zipkin

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

typedef struct MansionRoom
{
  int north;
  int east;
  int south;
  int west;
  char mapName[30];
  char enter[500];
  char examine[800];
  char hint[700];
  int  visited;

} Room;

typedef struct MansionItem
{
  char name[12];
  int posession;
  int getItX;
  int getItY;
  int useItX;
  int useItY;
  char message[200];
} Item;

struct node {
   Item * data;
   struct node *next;
};
typedef struct node listNode;

void printList(listNode * ptr);
void append(listNode * startPtr, Item * newItemPtr);
void convertInput(char *in);
void getItem(Item * it, int x, int y, listNode * inventory);
void displayItems(listNode * startPtr);
void printMap(Room fullMansion[5][5]);

int main(void)
{
  // Initialize all rooms
  Room grandEnterance = {1, 1, 0, 1, "Entrance", "You find yourself in the Grand Enterance.", \
  "An ornate tiled floor extends forward to a grand hallway.\nAbove, you see a faded portrait of your grandmother wearing her prized amulet.\nShe sits in a velvet emerald throne beside your grandfather. He holds a brass bugle.\nThat guy always disturbed you...he never let you into his laboratory.\nThe enterance door behind you is locked! Looks like there's no way out of here!", \
  "'Golden key, to exit or enter,\nFound aside the mansion's center.\nIn a trap from ancient time,\nTo the east, the key you'll find.'"};
  Room lounge = {1, 1, 0, 0, "Lounge", "You step into the Lounge.", \
  "There's a nice, beige couch and an oak table with flowers.\nIn a locked glass case, you see your grandfather's bugle.", \
  "'At the bugle, I see you gawk.\nTo claim it you cannot just walk.\nTime is ticking, wasting away!\nYou'll have to get here another way.'"};
  Room conservatory = {0, 0, 1, 1, "Conservatory", "You advance into the Conservatory.\nTo the east is a plastic slide, too slippery to climb up. Where does it come from?", \
  "As heavy rain pummels the paneled glass you notice thick, thorned vines covering a wooden bin.\nA venus fly trap is growing in a small pot. It points slightly West and twice as much South.", \
  "'What will make a garden grow?\nA pair of gloves, that I know.\nVenus, goddess, queen of love\nGestures gaily to the glove.'"};
  Room kitchen = {0, 0, 1, 0, "Kitchen", "You stumble into the Kitchen.", \
  "Most of the house is magnificent, but everything in here is off-putting and haphazard.\nThe door to the north is locked. Where's the key?\nA boiling pot of something maroon and lumpy sits idly on the tiled counter. Yuck!", \
  "'What's for dinner?\nI always loved my cook's spaghetti, plain and simple.\nDon't get tangled up in the details that don't matter.'"};
  Room diningRoom = {1, 1, 1, 0, "Dining", "You enter the lavish Dining Room.",
  "An enormous table, its embroidered tablecloth pristine yet beige from age, occupies most of the room.\nYou remember coming here for Thanksgiving and your stomach rumbles.\nA garish chandelier seems to frown under its own weight. Looks precarious.",
  "'The dining room is the heart of every home!\nExcept this one. It's as far west as you'll get, and one space shy of the southern end.'"};
  Room grandHall = {1, 1, 1, 1, "Grand Hall", "You come to the Grand Hallway.", \
  "The hallway is fit with diamond-shaped panels, a ceiling painted with a \nbrilliant depiction of the family tree, and rooms on all four sides.\nOn the wall is an odd painting: Your grandmother's face some decades ago, eyes closed. Is she even awake?",
  "'Keep your eyes peeled! Come on, don't snore!\nWhen the time is right, input: [trapdoor]!'"};
  Room billiard = {1, 0, 1, 0, "Billiards", "You find yourself in a Billiard Room.", \
  "The green billiard table is cast in a low, ominous light from above.\nYou examine the table and, strangely, the balls are arranged in a line.\nThey are: Red, green, orange striped, yellow striped, black, burgundy.", \
  "'You seek advice? Don't look to the eight ball.\nA more complex code directs your search...'"}; // 361397
  Room chapel = {0, 0, 0, 1, "Chapel", "You reach the Chapel, feeling smited by the Gothic architecture.", \
  "Something isn't right here. The uncomfortable pews are lit only by candlelight.\nThe altar is ornate but the golden pattern on the front accidentally forms an angry expression.", \
  "'The secret of my mansion twirls around you, child.\nPlease, reconnect with my memory here, not with my amulet,\nbut through a sight more pure and true.\nOnly then may you ascend in your quest.'"};
  Room stairDown = {0, 0, 0, 1, "Stairs", "You come to the bottom of a grand Stairwell. To the east, it travels to the mansion's upper floor.", \
  "Upon closer inspection, a thin magical veil covers the space between the two levels of the house.\nWhen you try to approach, you feel a cold hand yank you back.\nWas that...no, it couldn't be...", \
  "'I don't trust children to go where they're not allowed!\nBefore you ascend, you must prove you have true sight.'"};
  Room stairUp = {1, 1, 0, 1, "Stairs", "You come to the top of the Stairwell. To the west, it travels to the mansion's ground floor.", \
  "To the north, you can enter the Study. To the east is the Music Room.", \
  "'You're halfway done, now find the rest!\nHere's what you need to continue your quest:\n Get the bugle, play a song.\nMake sure the notes aren't wrong.\nPerform an experiment in the lab.\nMy riches you will surely grab.'"};
  Room ballroom = {1, 0, 1, 0, "Ballroom", "You saunter into the palatial marble Ballroom.", \
  "Spellbound, you feel an enchanted aura around your feet,\nguiding your steps as you first walk and then dance around the room.\nWhy, you wonder, do you feel like life in this mansion was...choreographed?", \
  "'Do my riches make you dance?\nLife is more than just a glance.\nAppearances are but a trick:\nThis mansion breathes beyond the brick.\nYou my vault holds golden nuggets?\nSilly dancer! You're just a puppet.'"};
  Room coalChute = {0, 1, 1, 0, "Coal", "A smoky silence fills your ears and nose as you shuffle into a dark Coal Chute room.", \
  "To the south is the Coal Chute. It's filthy, but it's quite big. Should you...?\nNo. No, that seems crazy.", \
  "'You've reached the end of your quest, child.\nThere's only one way to go. Have courage, and be prepared...\nYou won't be able to turn back.'"};
  Room laboratory = {0, 1, 0, 0, "The Lab", "Your music unlocked the metal door! Still nervous, you trudge into the Laboratory.", \
  "Your grandfather's experiments, dusty and unused since his death long ago, are illuminated only by a single flickering lightbulb.\nYou see strange green tubes, copper bars welded to form alienlike structures, burnt and ripped papers...\nTo the west is a mysterious door, kept locked by a [keypad].", \
  "'To the west is a dark and dusty Coal Chute.\nAs for science? Astronomy's a worthwhile pursuit.'"};
  Room study = {0, 1, 1, 0, "Study", "Strolling into the well-lit Study, you feel a slight bit less anxious.",
  "On a small wooden table you see a piece of sheet music. You take a seat in a comfy recliner and examine it.\nIt's the first six notes of the Bugle scale.",
  "'If you'd like to access my Lab, you'll have to do some studying first!\nThat sheet music is your key.'"};
  Room servant = {0, 0, 1, 0, "Servant", "Dodging a filthy rag, you enter the Servant's Quarters.", \
  "Sepulchral and claustrophobic, the room is littered with clutter. A window to the north mercifully views the Garden.\nScattered relics tell this place's story: A worn ballet shoe, a sewing needle, a pair of broken glasses...\nBeneath a dirty bunk bed you notice a safe! Input [safe] to examine it.", \
  "'Locked inside, the servant's stash.\nA servant's pride is never cash\nRather their wisdom, truest sight!\nWhile you play pool, they rule the night.'"};
  Room garden = {0, 1, 0, 0, "Garden", "You wander outside into the Garden. Bitter rain batters your face but you cannot feel a breeze.", \
  "Rubescent rose bushes form a delicate circle around a broken stone fountain.\nThe base of the fountain is lined with loose soil.\nOne small patch in particular has a few eye-catching violets.", \
  "'Some things are best left forgotten.\nBut others not! Unearth, child, a dull and trite token\nThat leads to a large revelation.'"};
  Room terrace = {0, 1, 0, 1, "Terrace", "You step outside onto the grand Terrace, seeing little beyond the balcony.\nThere's a slide to the west leading down! It looks fun.", \
  "You remember how your grandmother would host gatherings, lunches, and parties on this terrace.\nWhere did the time go?", \
  "'If you take the slide with childlike zest\nThe Ballroom's one South, the Garden's one West.'"};
  Room masterBedroom = {0, 1, 0, 1, "M. Bed", "You stride into the opulent Master Bedroom.", \
  "The bed looks comfortable! But it's no time for sleeping and snoring.\nYou notice a big red [button] on a pedestal next to a portrait of your grandfather.\nGeez, you knew he was weird, but this is just ridiculous.", \
  "'Push that button, if you're frugal.\nIt is your key to his bugle!"};
  Room observatory = {0, 0, 1, 1, "Observatory", "Encased by more darkness even than before, you enter the starry Observatory.", \
  "You look through a telescope and see constellations in the night sky above the mansion!\nYou carefully count the number of stars in each constellation.\nFirst you see the Big Dipper, then Orion, then the Little Dipper, then cassiopeia.\nWow, you wonder if it is somehow significant that each constellation has a specific number of stars!\nProbably not.", \
  "'Count up the stars if you'd like to descend\nTo the innermost chamber, and to your journey's end.'"};
  Room library = {1, 0, 1, 0, "Library", "You roam into a large Library.", \
  "Finally feeling relaxed, you select a large red book from one of the shelves. and begin to read.\n'JAVAFX Guide for Beginners.\nBy: Javin Zipkin'\nHuh? You put it back on the shelf. It seems useless.\nHowever, the black book beside it is quite interesting.\n'CONSTELLATIONS OF THE NIGHT SKY\nThe next time you stargaze, keep an eye out for these constellations:\nThe big and little dippers, made of 8 and 7 stars respectively\nAquarius, made of 22 stars, but only a couple bright ones\nCancer, the majestic crab made up of 5 stars\nCassopeia, 5 stars\nOrion, made up of 7 stars\nThe constellations are not just pretty. They are the key to many scientific experiments.'", \
  "'To the west, my husband's lair.\nIt won't unlock unless you dare\nTo play his music. Fair is fair.'"};
  Room spookyHallway = {1, 0, 1, 0, "Hallway", "You shamble forward into a rickety, crickety, dark, dusty, spooky Hallway!", \
  "Actually, it's not that spooky. It's just cramped.\nActually, it's pretty spacious...\nIs that a scented candle?\nThere are doors only to the north and south.", \
  "'I mean, it's really not that scary. It's just a hallway. Don't be a baby!'"};
  Room musicRoom = {1, 0, 0, 1, "Music Room", "Hearing the ominous call of an organ, you find the Music Room, but when you enter, the sound stops.",
  "On the walls are sound-absorbing panels. Sheet music is stuffed into every drawer but it's all for the organ.\nYou try to play a few notes on the organ, but the keys won't move. Might there be another instrument?",
  "'Of course, the Bugle's in the lounge.\nBut that's not the only place you must look around.\nTo get the bugle, you'll have to use\nA secret passage, or you'll lose.'"};
  Room guestBedroom = {1, 0, 1, 1, "Guest Bed", "Feeling tired, you are glad to arrive in the Guest Bedroom.", \
  "This is the most boring room in the house!\nYou suppose that your grandparents were never...well...caring.\nPerhaps it makes sense that the guest bedroom blows.", \
  "'Oh! I forgot this room existed.\nMove along, now. Go on.'"};
  Room vault = {0, 0, 0, 0, "Vault", "To the east you notice a circular metal door with an oval slot in the middle.\nIt won't budge...But then you remember your Amulet! It fits perfectly into the door.\nThe Vault opens and you step inside.", \
  "You expect to find jewels, heaps of coins, bills, and gold bars, but the vault is completely empty.\nAt least you see a [ladder] in the center that seems to lead to somewhere outside.\nMaybe you should consult the amulet?", \
  "'Child, your journey's not for money.\nThe nectar of truth is life's sweet honey.\nYou've solved many a puzzle to reach this Vault.\nFor that, your knowledge I exalt.\nThe true inheritance, my greatest prize\nIs a zest for discovery behind thy eyes.' \
  \n\nIs she SERIOUS? This SUCKS! You went all this way for a LESSON?!\nWait, wait, she's speaking again.\n\n'Hah! JK! Got ya! That amulet is worth like four billion dollars. I gotchu covered babe.\nDid you really think I was gonna be that lame? Nah. Alright, you can leave now.\nI'm leaving this crappy mansion to your siblings BTW.'"};
  Room tomb = {0, 1, 0, 0, "Tomb", "OUCH! YEEOWCH! OOF! BANG! Sliding down the awful Coal Chute,\nyou find yourself in a dark Tomb.", \
  "Everything here is dark but strangely beautiful...\nDust falls down from the ceiling and the stone pillairs holding the mansion above are cracked.\nYou can tell that this place was never actually used as a dumpster. That Coal Chute was some kind of decoy.\nYou suppose that your Grandma wanted, most of all, for you to learn not to let appearances fool you.", \
  "But then it fades. She cannot reach you here..."};
  Room allRooms[5][5] = {{garden, conservatory, terrace, masterBedroom, observatory}, \
  {servant, ballroom, coalChute, laboratory, library}, \
  {kitchen, billiard, tomb, vault, spookyHallway}, \
  {diningRoom, grandHall, chapel, study, guestBedroom}, \
  {lounge, grandEnterance, stairDown, stairUp, musicRoom}};
  // Alternate examination messages for after rooms are changed
  char *stairDownUncovered = "The veil is gone...it seems you can pass freely.";

  // Initialize all game variables
  char input[20] = "";
  int inputCode = 0;
  int x = 1;
  int y = 4;a
  int bugleTimer = 0; // Number of moves allowed to go from the Master Bedroom to the Lounge to get the Bugle
  Room *currentRoom = &allRooms[4][1];

  // Initialize all Items
  Item shovel = {"shovel", 0, 1, 0, 0, 0, "Using the gloves, you brush aside the vines and open the toolbox.\nInside, you find a [shovel]!"};
  Item gloves = {"gloves", 0, 0, 2, 1, 0, "But you notice a pair of Gardening Gloves beside it.\nYou pick the [gloves] up. Where might these be useful?"};
  Item brassKey = {"brasskey", 0, 0, 0, 0, 1, "Trying to ignore the bitter rain, you strike the violets with the shovel.\nThe damp soil ruins your clothes but you uncover a small [brasskey]!"};
  Item mirror = {"mirror", 0, 0, 1, 2, 3, "Inside you find a small [mirror].\nYou hold it up to your face and it catches the light in such a peculiar way...\nHave your eyes turned red, or is the light playing tricks?"};
  Item bugle = {"bugle", 0, 0, 4, 4, 4, "Just before the case locks you grab the [bugle]! The button worked!\nBut where might you use this thing...?"};
  Item amulet = {"amulet", 1, 0, 0, 0, 0, ""};
  listNode * heldItems = malloc(sizeof(listNode));
  heldItems->next = NULL;
  heldItems->data = &amulet;

  // Initialize messages
  char introMessage[500] = "~ESCAPE THE MANSION~\nIf you had known this would be such an adventure you probably wouldn't have come...\n"
  "It had been a strange month filled with contradictions. Your grandmother, who you remember for her intelligence and secrecy,\nmysteriously died on her 105th "
  "birthday and granted you her entire fortune of untold riches!\nBut all you received at the funeral was her [amulet]...The rest, "
  "your mother said, would be found in her lavish estate.\nIT WAS a dark and stormy night...";
  char helpMessage[500] = "\n~HOW TO PLAY~\nEnter your input without spaces.\
  \nhelp\tDisplay this menu\nquit\tExit the game\nlook\tExamine the current room\nmap\tSee all the rooms you've visited \
  \nnorth\tMove north\nsouth\tMove south\neast\tMove east\nwest\tMove west \
  \nitem\tUse a specific item that you have collected.\n\tYou'll know you got an item when its name is displayed in [brackets.]\nitems\tDisplay all the items you have \
  \ncode\tA secret passcode OR action that you have learned from your exploration\n";
  printf("%s\n%s\n%s\n", introMessage, helpMessage, currentRoom->enter);

  // Game Loop
  while(strcmp(input, "quit") != 0)
  {
    // Make it so you've visited
    allRooms[y][x].visited = 1;
    // Collect and modify the player's input
    printf("\nEnter your next move: ");
    fgets(input, 20, stdin);
    printf("\n");
    input[strcspn(input, "\n")] = 0;
    convertInput(input);
    // Respond to the player's input
    // LOOK AROUND
    if(strcmp(input, "look") == 0)
    {
      printf("%s\n", currentRoom->examine);
      getItem(&gloves, x, y, heldItems);
      if(bugleTimer > 0)
      {
        getItem(&bugle, x, y, heldItems);
        currentRoom->examine[strcspn(currentRoom->examine, "\n")] = 0;
      }
    }
    // HELP MENU
    else if(strcmp(input, "help") == 0)
    {
      printf("%s\n", helpMessage);
    }
    // MAP
    else if(strcmp(input, "map") == 0)
    {
      printMap(allRooms);
    }
    // THE AMULET
    else if(strcmp(input, "amulet") == 0)
    {
      printf("The amulet glows with scarlet intensity as you concentrate on the memory of your grandmother.\nYou can almost hear her voice...\n\n%s\n", currentRoom->hint);
    }
    // MOVEMENT
    else if(strcmp(input, "west") == 0 || strcmp(input, "east") == 0 || strcmp(input, "north") == 0 || strcmp(input, "south") == 0)
    {
      // MOVE WEST
      if(strcmp(input, "west") == 0 && currentRoom->west)
      {
        x--;
        currentRoom = &allRooms[y][x];
        printf("%s\n", currentRoom->enter);
      }
      // MOVE EAST
      else if(strcmp(input, "east") == 0 && currentRoom->east)
      {
        x++;
        currentRoom = &allRooms[y][x];
        printf("%s\n", currentRoom->enter);
      }
      // MOVE NORTH
      else if(strcmp(input, "north") == 0 && currentRoom->north)
      {
        y--;
        currentRoom = &allRooms[y][x];
        printf("%s\n", currentRoom->enter);
      }
      // MOVE SOUTH
      else if(strcmp(input, "south") == 0 && currentRoom->south)
      {
        y++;
        currentRoom = &allRooms[y][x];
        printf("%s\n", currentRoom->enter);
      }
      else
      {
        printf("You can't move that way.\n");
      }
    }
    // ITEMS
    else if(strcmp(input, "items") == 0)
    {
      printList(heldItems);
    }
    // ITEMS
    else if(strcmp(input, "item") == 0)
    {
      printf("To use an item, input its name.\nTo check the items you have, input items.\n");
    }
    // GLOVES
    else if(gloves.posession && strcmp(input, "gloves") == 0)
    {
      getItem(&shovel, x, y, heldItems);
    }
    // SHOVEL
    else if(shovel.posession && strcmp(input, "shovel") == 0)
    {
      getItem(&brassKey, x, y, heldItems);
    }
    // BRASS KEY
    else if(brassKey.posession && strcmp(input, "brasskey") == 0 && x == 0 && y == 2 && kitchen.north == 0)
    {
      printf("The key fits into the lock and the door opens! The room behind it is messy and moldy...Your curiosity balances your disgust.\n");
      allRooms[y][x].north = 1;
    }
    // MIRROR
    else if(mirror.posession && strcmp(input, "mirror") == 0 && x == 2 && y == 3 && allRooms[4][2].east == 0)
    {
      printf("You look into the mirror, but your reflection is gone. Now you see the young face of your grandmother! AAAAH!\nHer eyes turn red "
      "and you are about to smash the mirror, but then she begins to speak:\n'You've completed the first half of your investigation. What fun!\n"
      "But the true puzzle begins when you climb that Stairwell...You're ready to ascend. Hehehe!'\nWith a wink she disappears.\n");
      allRooms[4][2].east = 1;
      strcpy(allRooms[4][2].examine, stairDownUncovered);
    }
    // BUGLE
    else if(bugle.posession && strcmp(input, "bugle") == 0 && x == 4 && y == 4 && allRooms[1][4].west == 0)
    {
      printf("You hold the bugle high and begin to play. Enter the notes you play, without spaces: ");
      fgets(input, 20, stdin);
      input[strcspn(input, "\n")] = 0;
      // CORRECT SAFE COMBINATION
      if(strcmp(input, "ccgceg") == 0 || strcmp(input, "cc1g1c2e2g2") == 0)
      {
        printf("You play the scale and something INCREDBILE happens!\nThe floor you are standing on begins to shake and quake. It spins around 360 degrees, and you nearly fall.\nYou hear a clicking sound and realized a room has unlocked...but where?\n");
        allRooms[1][4].west = 1;
      }
      else
      {
        printf("What beautiful music! But nothing happens.\n");
      }
    }
    // INTERACTING WITH SPECIAL ROOMS
    // TRAP DOOR
    else if(strcmp(input, "trapdoor") == 0 && x == 3 && y == 0)
    {
      // Teleport to the Grand Hall
      x = 1;
      y = 3;
      currentRoom = &allRooms[y][x];
      printf("You notice a loose board next to the bed and, miraculously, it's a Trap Door!\nYou enter and navigate through a dark passage.\nYou push your way out of the passage and realize you have dislodged a painting from the wall of the Grand Hallway!\n%s\n", currentRoom->enter);
    }
    // BIG RED BUTTON
    else if(strcmp(input, "button") == 0 && x == 3 && y == 0)
    {
      // Activate the bugleTimer
      bugleTimer = 5;
      printf("You push the button and hear a loud Click! From downstairs. The amulet jiggles and you hear your grandmother:\n'Quickly, now! You have a limited number of moves\nBefore that contraption's effects wear off!\nGet downstairs, now!'\n");
    }
    // SAFE
    else if(strcmp(input, "safe") == 0 && x == 0 && y == 1)
    {
      printf("You approach the safe. Enter the combo: ");
      fgets(input, 20, stdin);
      input[strcspn(input, "\n")] = 0;
      // CORRECT SAFE COMBINATION
      if(strcmp(input, "361397") == 0)
      {
        printf("The safe unlocks!\n");
        getItem(&mirror, x, y, heldItems);
      }
      else
      {
        printf("Nothing happens. The combo was incorrect.\n");
      }
    }
    // KEYPAD
    else if(strcmp(input, "keypad") == 0 && x == 3 && y == 1)
    {
      printf("You approach the keypad. Enter a four digit combo: ");
      fgets(input, 20, stdin);
      input[strcspn(input, "\n")] = 0;
      // CORRECT SAFE COMBINATION
      if(strcmp(input, "8775") == 0)
      {
        printf("The door unlocks!\n");
        allRooms[1][3].west = 1;
      }
      else
      {
        printf("Nothing happens. The combo was incorrect.\n");
      }
    }
    // EXIT LADDER
    else if(strcmp(input, "ladder") == 0 && x == 3 && y == 2)
    {
      printf("You carefully climb the ladder and find yourself...outside the enterance?\nYou recall the spatial arrangement of the mansion and conclude that this makes no sense. \
      \nHowever, with a four billion dollar amulet around your neck, you don't really care.\n~CONGRATULATIONS! You Escaped the Mansion!~\nCredits:\nStory\t\tJavin Zipkin\nCoding\t\tJavin Zipkin \
      \nAdvertising\tJavin Zipkin\nResearch\tJavin Zipkin\n3D Modeling\tJavin Zipkin\nMusic\t\tJavin Zipkin (organist)\nThanks for playing!");
      break;
    }
    // BUGLE TIMER MESSAGE
    if(bugleTimer > 0)
    {
      bugleTimer--;
      printf("%d moves left until the button's mysterious effect wears off!\n", bugleTimer);
    }
  }
  return(0);
}
void convertInput(char *p)
{
  char *source = p, *cleaned = p;

    while (*source)
    {
       if (ispunct((unsigned char)*source))
       {
          source++;
       }
       else if (isupper((unsigned char)*source))
       {
          *cleaned++ = tolower((unsigned char)*source);
          source++;
       }
       else if (source == cleaned)
       {
          source++;
          cleaned++;
       }
       else
       {
          *cleaned++ = *source++;
       }
    }

    *cleaned = 0;

}
void getItem(Item * it, int currentX, int currentY, listNode * inventory)
{
  //printf("Your x, y: %d, %d\nItem's x, y: %d, %d\n", currentX, currentY, it->getItX, it->getItY);
  if(currentX == it->getItX && currentY == it->getItY && !(it->posession))
  {
    printf("%s\n", it->message);
    it->posession = 1;
    append(inventory, it);
  }
}

//display the list
void printList(listNode * first)
{
  listNode * ptr = first;
  printf("~YOUR ITEMS~\n");

  //start from the beginning
  while(ptr != NULL) {
    printf("%s\n",ptr->data->name);
    ptr = ptr->next;
  }
}

void append(listNode * startPtr, Item * newItemPtr)
{
  // Make a new node
  struct node *newNode;
  newNode = malloc(sizeof(listNode));
  newNode->data = newItemPtr;
  newNode->next = NULL;

  // Find the very last node of the linked list you want to append to
  struct node *temp = startPtr;
  while(temp->next != NULL)
  {
    temp = temp->next;
  }
  // Make that last node point to your new last node
  temp->next = newNode;
}

void printMap(Room fullMansion[5][5])
{
  for(int my = 0; my < 5; my++)
  {
    for(int mx = 0; mx < 5; mx++)
    {

      if(fullMansion[my][mx].visited)
      {
        printf(fullMansion[my][mx].mapName);
      }
      else
      {
        printf("[");
        for(int i = 0; i < strlen(fullMansion[my][mx].mapName) - 2; i++)
        {
          printf("?");
        }
        printf("]");
      }
      printf("\t");

    }
    printf("\n\n");
  }
}
aaa