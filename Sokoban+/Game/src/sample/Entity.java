package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.*;

public class Entity
{
    private double x;
    private double y;
    private double size;
    private javafx.scene.paint.Paint color;
    private boolean controllable;
    private boolean playable;
    private String type = "Wall";

    public Entity(double x, double y, double size, Paint color)
    {
        this.x = x;
        this.y = y;
        this.size = size;
        this.color = color;
        controllable = false;
        playable = false;
    }

    public Entity(double x, double y)
    {
        this.x = x;
        this.y = y;
        this.size = 85;
        this.color = Color.SADDLEBROWN;
        controllable = false;
        playable = false;
    }

    public Entity copy()
    {
        return(new Entity(x, y, size, color));
    }

    public void draw(GraphicsContext surface)
    {
        Paint previousFill = surface.getFill();
        surface.setFill(color);
        surface.fillRect(x, y, size, size);
        //return back to whatever fill we were using before
        surface.setFill(previousFill);
    }

    public void drawInGrid(Grid theGrid, GraphicsContext surface)
    {
        //calculate margins (size of box is 85)
        double margin = (85 - size) / 2.0;
        double centerX = theGrid.getSmallBound() + 85 * x + margin + size / 2.0;
        double centerY = theGrid.getSmallBound() + 85 * y + margin + size / 2.0;

        double[] xPoints = {centerX, centerX + 10, centerX, centerX - 10};
        double[] yPoints = {centerY - 10, centerY, centerY + 10, centerY};
        surface.setFill(theGrid.getColor());
        //main rectangle
        surface.fillRect(theGrid.getSmallBound() + 85 * x + margin, theGrid.getSmallBound() + 85 * y + margin, size, size);

        //control indicator
        if(playable)
        {
            if(controllable)
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

    public double getX()
    {
        return x;
    }

    public double getY()
    {
        return y;
    }

    public double getSize()
    {
        return size;
    }

    public void setX(double value)
    {
        x = value;
    }

    public void setY(double value)
    {
        y = value;
    }

    public void moveX(double value)
    {
        x += value;
    }

    public void moveY(double value)
    {
        y += value;
    }

    public boolean isControllable()
    {
        return(controllable);
    }

    public void setControllable(boolean value)
    {
        controllable = value;
    }

    public void changeSize(double value)
    {
        size += value;
    }

    public void setColor(Paint newColor)
    {
        color = newColor;
    }

    public Paint getColor()
    {
        return color;
    }

    public boolean getPlayable()
    {
        return playable;
    }

    public void setPlayable(boolean value)
    {
        playable = value;
    }

    public static void drawCircle(double x, double y, double size, GraphicsContext surface)
    {
        double centerX = x - size;
        double centerY = y - size;
        surface.fillOval(centerX, centerY, size * 2, size * 2);
    }

    public boolean offScreen()
    {
        return(x < -1 * size|| y < -1 * size || x > 1110 + size || y > 670 + size);
    }

    public double distanceFrom(Entity other)
    {
        return Math.sqrt((other.getY() - y) * (other.getY() - y) + (other.getX() - x) * (other.getX() - x));
    }

    public boolean toTheLeftOf(Entity other)
    {
        return(x + size < other.getX());
    }

    public boolean toTheRightOf(Entity other)
    {
        return(x > other.getX() + other.getSize());
    }

    public boolean above(Entity other)
    {
        return(y + size < other.getY());
    }

    public boolean below(Entity other)
    {
        return(y > other.getY() + other.getSize());
    }

    public String getType()
    {
        return type;
    }

    public void setType(String value)
    {
        type = value;
    }

    public boolean detectCollision(Entity other)
    {
        boolean collisionDetected = true;
        //check if one is above the other
        if(y + size < other.getY())
        {
            collisionDetected = false;
        }
        //check if one is below the other
        else if(y > other.getY() + other.getSize())
        {
            collisionDetected = false;
        }
        //check if one is to the left of the other
        if(x + size < other.getX())
        {
            collisionDetected = false;
        }
        //check if one is to the right of the other
        else if(x > other.getX() + other.getSize())
        {
            collisionDetected = false;
        }

        return(collisionDetected);
    }

    public void gridKeyMovement(String code)
    {
        if(code.equals("RIGHT"))
        {
            x += 1;
        }
        if(code.equals("LEFT"))
        {
            x -= 1;
        }
        if(code.equals("UP"))
        {
            y -= 1;
        }
        if(code.equals("DOWN"))
        {
            y += 1;
        }
    }

    //big collision game mechanic system af
    public void enforcePhysics(String direction, Level level)
    {
        Grid grid = level.getLevelGrid();
        ArrayList<Entity> objects = level.getObjects();

        if(x >= grid.getSize() || x < 0 || y >= grid.getSize() || y < 0)
        {
            switch (direction) {
                case "RIGHT" -> {
                    x -= 1;
                    direction = reverse(direction);
                }
                case "LEFT" -> {
                    x += 1;
                    direction = reverse(direction);
                }
                case "UP" -> {
                    y += 1;
                    direction = reverse(direction);
                }
                case "DOWN" -> {
                    y -= 1;
                    direction = reverse(direction);
                }
            }
        }

        //now the important part, colliding with other objects in the level
        for(Entity other : objects)
        {
            if(other.getX() == x && other.getY() == y && !(other.equals(this)))
            {
                other.pushedBy(this, direction, level);
            }
        }
    }

    public void pushedBy(Entity pusher, String direction, Level level) //Grid grid, ArrayList<Entity> objects)
    {
        Grid grid = level.getLevelGrid();
        ArrayList<Entity> objects = level.getObjects();

        //by default, every object acts like an un-move-able wall
        if(direction.equals("RIGHT"))
        {
            pusher.moveX(-1);
        }
        if(direction.equals("LEFT"))
        {
            pusher.moveX(1);
        }
        if(direction.equals("UP"))
        {
            pusher.moveY(1);
        }
        if(direction.equals("DOWN"))
        {
            pusher.moveY(-1);
        }
        pusher.enforcePhysics(reverse(direction), level);
    }

    public static String reverse(String direction)
    {
        return switch (direction) {
            case "DOWN" -> ("UP");
            case "UP" -> ("DOWN");
            case "RIGHT" -> ("LEFT");
            case "LEFT" -> ("RIGHT");
            default -> ("ERROR");
        };
    }

    public boolean getActivated(Level level)
    {
        ArrayList<Entity> objs = level.getObjects();
        boolean tracker = false;

        for(Entity e: objs)
        {
            if(e.getType().equals(getType()) && e.getX() == getX() &&
                e.getY() == getY() && e != this)
            {
                //System.out.println("hey");
                setColor(Color.GOLD);
                tracker = true;
            }
        }
        if(!tracker)
        {
            setSensorColor();
        }
        return(tracker);
    }

    public void setSensorColor()
    {
        if(type.equals("BoxA"))
        {
            setColor(Color.BROWN);
        }
        else if(type.equals("BoxB"))
        {
            setColor(Color.BURLYWOOD);
        }
        else
        {
            setColor(Color.BROWN);
        }
    }


}

