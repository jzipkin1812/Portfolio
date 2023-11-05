package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.ArrayList;

public class Box extends Entity
{
    public Box(double x, double y)
    {
        super(x, y, 70, Color.BROWN);
        setPlayable(true);
        setType("BoxA");
    }

    public Box(double x, double y, boolean play)
    {
        super(x, y, 70, Color.BROWN);
        setPlayable(play);
        setType("BoxA");
    }

    public Box(double x, double y, boolean play, Paint color)
    {
        super(x, y, 70, color);
        setPlayable(play);
        setType("BoxB");
    }


    public Box(double x, double y, boolean play, Paint color, String theType)
    {
        super(x, y, 70, color);
        setPlayable(play);
        setType(theType);
    }

    @Override
    public void pushedBy(Entity pusher, String direction, Level level)
    {
        Grid grid = level.getLevelGrid();
        ArrayList<Entity> objects = level.getObjects();
        //by default, every object acts like an un-move-able wall
        switch (direction) {
            case "RIGHT" -> moveX(1);
            case "LEFT" -> moveX(-1);
            case "UP" -> moveY(-1);
            case "DOWN" -> moveY(1);
        }
        enforcePhysics((direction), level);
    }

    @Override
    public Entity copy()
    {
        return(new Box(getX(), getY(), getPlayable(), getColor(), getType()));
    }

    @Override
    public void drawInGrid(Grid theGrid, GraphicsContext surface)
    {
        //calculate margins (size of box is 85)
        double margin = (85 - getSize()) / 2.0;
        double centerX = theGrid.getSmallBound() + 85 * getX() + margin + getSize() / 2.0;
        double centerY = theGrid.getSmallBound() + 85 * getY() + margin + getSize() / 2.0;

        double[] xPoints = {centerX, centerX + 10, centerX, centerX - 10};
        double[] yPoints = {centerY - 10, centerY, centerY + 10, centerY};
        surface.setFill(getColor());
        //main rectangle
        surface.fillRect(theGrid.getSmallBound() + 85 * getX() + margin, theGrid.getSmallBound() + 85 * getY() + margin, getSize(), getSize());

        //control indicator
        if(getPlayable())
        {
            if(isControllable())
            {
                surface.setFill(Color.GOLD);
                surface.fillPolygon(xPoints, yPoints, 4);
            }
            else
            {
                surface.setFill(Color.GRAY);
                surface.fillPolygon(xPoints, yPoints, 4);
            }
        }
    }

}
