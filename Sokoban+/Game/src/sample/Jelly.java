package sample;

import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.ArrayList;

public class Jelly extends Entity
{
    private String type = "Jelly";
    public Jelly(double x, double y)
    {
        super(x, y, 30, Color.PURPLE);

    }

    @Override
    public void pushedBy(Entity pusher, String direction, Level level)
    {
        Grid grid = level.getLevelGrid();
        ArrayList<Entity> objects = level.getObjects();
        //by default, every object acts like an un-move-able wall
        switch (direction) {
            case "RIGHT" -> moveX(-1);
            case "LEFT" -> moveX(1);
            case "UP" -> moveY(1);
            case "DOWN" -> moveY(-1);
        }
        direction = reverse(direction);
        //enforcePhysics((direction), grid, objects);
    }
}
