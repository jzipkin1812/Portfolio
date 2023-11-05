package sample;

import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.image.Image;
import javafx.scene.paint.LinearGradient;
import javafx.scene.paint.Paint;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.security.cert.CertificateRevokedException;
import java.util.ArrayList;

import static sample.PremadeLevels.*;

public class Main extends Application {

    //defining frame counter
    int frames = 0;
    Paint desertColor = LinearGradient.valueOf("from 0% 0% to 100% 100%, Khaki 0%, Orange 100%");
    Paint springColor = LinearGradient.valueOf("from 0% 0% to 100% 100%, yellowGreen 0%, SpringGreen 100%");
    Paint spookyColor = LinearGradient.valueOf("from 100% 0% to 0% 100%, Indigo 0%, Black 100%");

    //defining global screen variables
    final int screenWidth = 800;
    final int screenHeight = 800;

    //defining global fonts
    Font defaultFont = new Font(50);
    Font smallFont = new Font(35);

    //world counter
    //world 0 is the title screen
    int currentWorld = 0;

    @Override
    public void start(Stage primaryStage)
    {
        //create test world
        World grassland = new World(springColor, l1_0, l1_1, l1_2, l1_3, l1_4, l1_5, l1_6, l1_7, l1_8, l1_9);
        World desert = new World(desertColor, l2_0, l2_1, l2_2, l2_3, l2_4, l2_5, l2_6, l2_7, l2_8, l2_9);
        World spookyWorld = new World(spookyColor, l3_0, l3_1, l3_2, l3_3, l3_4, l3_5, l3_6, l3_7, l3_8, l3_9);
        ArrayList<World> worlds = new ArrayList<>();
        worlds.add(grassland);
        worlds.add(grassland);
        worlds.add(desert);
        worlds.add(spookyWorld);

        //creating a Group object and a canvas
        Group root = new Group();
        Canvas canvas = new Canvas(screenWidth, screenHeight);
        root.getChildren().add( canvas );
        GraphicsContext gc = canvas.getGraphicsContext2D();
        //Creating a Scene by passing the group object, height and width
        Scene scene = new Scene(root,screenWidth, screenHeight);

        //create title screen image
        Image titleScreen = new Image("SokobanTitleScreen.png", 800, 800, true, false);

        //setting a mouse listener to the scene
        scene.setOnMousePressed(mouseEvent -> {
            //System.out.println(mouseEvent.getX() + ", " + mouseEvent.getY());
            if(currentWorld == 0)
            {
                currentWorld = clickWorld(mouseEvent.getX(), mouseEvent.getY());
            }
            else if(currentWorld > 0)
            {
                worlds.get(currentWorld).getCurrentLevel().setControllable(mouseEvent.getX(), mouseEvent.getY());
            }
        });

        //setting a key listener to the scene
        //list of keys pressed
        ArrayList<String> keysPressed = new ArrayList<>();

        scene.setOnKeyPressed(keyEvent -> {
            String code = keyEvent.getCode().toString();
            //only add once to prevent duplicates
            if (!keysPressed.contains(code))
            {
                keysPressed.add(code);
            }
            if(currentWorld > 0)
            {
                //ENFORCE INPUT
                worlds.get(currentWorld).getCurrentLevel().enforceInput(code);
                if(code.equals("R"))
                {
                    worlds.get(currentWorld).getCurrentLevel().reset();
                }
                if(code.equals("M"))
                {
                    currentWorld = 0;
                }
            }


        });

        scene.setOnKeyReleased(keyEvent -> {
            String removeCode = keyEvent.getCode().toString();
            keysPressed.remove(removeCode);
        });

        //Setting the title to Stage.
        primaryStage.setTitle("Sokoban+");

        //Adding the scene to Stage
        primaryStage.setScene(scene);

        //GAME LOOP
        new AnimationTimer()
        {
            public void handle(long currentNanoTime)
            {
                //increment frames
                frames += 1;

                //title screen
                if(currentWorld == 0)
                {
                    gc.drawImage(titleScreen, 0, 0);
                }

                //main gameplay
                else if(currentWorld > 0)
                {
                    //clear the screen
                    worlds.get(currentWorld).display(gc);

                    //display instructional text
                    gc.setFont(smallFont);
                    gc.setFill(worlds.get(currentWorld).getCurrentLevel().getLevelGrid().getColor());
                    gc.fillText("R to restart", 10, 35);
                    gc.fillText("M to return to menu", 10, 70);
                    if(worlds.get(currentWorld).getNumber() == 9)
                    {
                        gc.fillText("" + currentWorld + " - " + (worlds.get(currentWorld).getNumber() + 1), 705, 35);
                    }
                    else
                    {
                        gc.fillText("" + currentWorld + " - " + (worlds.get(currentWorld).getNumber() + 1), 720, 35);
                    }

                    //sensors and completion & completion message
                    if(worlds.get(currentWorld).getCurrentLevel().isCompleted())
                    {
                        //display continue text
                        gc.setFill(worlds.get(currentWorld).getCurrentLevel().getLevelGrid().getColor());
                        gc.setFont(defaultFont);
                        if(worlds.get(currentWorld).getNumber() == 9)
                        {
                            gc.fillText("World " + currentWorld + " Complete!", 193, 750);
                        }
                        else
                        {
                            gc.fillText("Space to continue", 200, 750);
                        }


                        //level ascension
                        if(keysPressed.contains("SPACE"))
                        {
                            worlds.get(currentWorld).ascend();
                        }
                    }


                    //display everything in the level
                    worlds.get(currentWorld).getCurrentLevel().display(gc);
                }


            }
        }.start();



        //Displaying the contents of the stage
        primaryStage.show();

    }

    public static void main(String[] args)
    {
        launch(args);
    }

    public static int clickWorld(double mouseX, double mouseY)
    {
        if(mouseY >= 375 && mouseY <= 475)
        {
            if(mouseX >= 290 && mouseX <= 390)
            {
                return(1);
            }
            if(mouseX >= 450 && mouseX <= 550)
            {
                return(2);
            }
            if(mouseX >= 610 && mouseX <= 710)
            {
                return(3);
            }
        }
        return(0);
    }
}
