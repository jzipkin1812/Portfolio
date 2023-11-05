package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class Web extends Entity
{

    public Web(double x, double y)
    {
        super(x, y, 85, Color.LIGHTGRAY);
        setType("Web");
    }

    @Override
    public void pushedBy(Entity pusher, String direction, Level level)
    {
        //yes, this method actually does nothing
        //because webs have no collision detection
    }

    @Override
    public void drawInGrid(Grid theGrid, GraphicsContext surface)
    {
        //calculate margins (size of box is 85)
        double X = theGrid.getSmallBound() + getSize() * getX();
        double Y = theGrid.getSmallBound() + getSize() * getY();

        surface.setLineWidth(2.0);
        surface.setStroke(theGrid.getColor());
        surface.strokeRect(X, Y, getSize(),getSize());
        surface.strokeLine(X + 1, Y + 1, X + 84, Y + 84);
        surface.strokeLine(X + 1, Y + 84, X + 84, Y + 1);
        surface.strokeLine(X + 1, Y + 42, X + 42, Y + 84);
        surface.strokeLine(X + 1, Y + 42, X + 42, Y + 1);
        surface.strokeLine(X + 84, Y + 42, X + 42, Y + 84);
        surface.strokeLine(X + 84, Y + 42, X + 42, Y + 1);


    }

    @Override
    public Entity copy()
    {
        return(new Web(getX(), getY()));
    }
}
