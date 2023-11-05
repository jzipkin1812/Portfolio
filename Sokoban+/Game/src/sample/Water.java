package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.ArrayList;

public class Water extends Entity
{
    public Water(double x, double y)
    {
        super(x, y, 70, Color.LIGHTBLUE);
        setPlayable(false);
    }

    @Override
    public void pushedBy(Entity pusher, String direction, Level level)
    {
        level.addDeadObject(this);
        level.addDeadObject(pusher);
    }

    @Override
    public Entity copy()
    {
        return(new Water(getX(), getY()));
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
