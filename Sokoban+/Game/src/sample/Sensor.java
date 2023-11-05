package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.ArrayList;

public class Sensor extends Entity
{

    public Sensor(double x, double y, String type)
    {
        super(x, y, 70, Color.BURLYWOOD);
        setType(type);
        setSensorColor();
    }

    @Override
    public void pushedBy(Entity pusher, String direction, Level level)
    {
        //yes, this method actually does nothing
        //because sensors have no collision detection
    }

    @Override
    public void drawInGrid(Grid theGrid, GraphicsContext surface)
    {
        //calculate margins (size of box is 85)
        double margin = (85 - getSize()) / 2.0;
        double centerX = theGrid.getSmallBound() + 85 * getX() + margin + getSize() / 2.0;
        double centerY = theGrid.getSmallBound() + 85 * getY() + margin + getSize() / 2.0;

        if(getType().equals("Vertical"))
        {
            double[] xPoints = {centerX, centerX + 7, centerX + 7, centerX, centerX - 7, centerX - 7};
            double[] yPoints = {centerY - 20, centerY - 10, centerY + 10, centerY + 20, centerY + 10, centerY - 10};

            surface.setFill(getColor());
            surface.fillPolygon(xPoints, yPoints, 6);

            surface.setLineWidth(2.0);
            surface.setStroke(theGrid.getColor());
            surface.strokePolygon(xPoints, yPoints, 6);

            return;
        }
        else if(getType().equals("Horizontal"))
        {
            double[] yPoints = {centerY, centerY + 7.0, centerY + 7.0, centerY, centerY - 7.0, centerY - 7.0};
            double[] xPoints = {centerX - 20, centerX - 10, centerX + 10, centerX + 20, centerX + 10, centerX - 10};

            surface.setFill(getColor());
            surface.fillPolygon(xPoints, yPoints, 6);

            surface.setLineWidth(2.0);
            surface.setStroke(theGrid.getColor());
            surface.strokePolygon(xPoints, yPoints, 6);

            return;
        }

        double[] xPoints = {centerX, centerX + 15, centerX, centerX - 15};
        double[] yPoints = {centerY - 15, centerY, centerY + 15, centerY};



        //sensor main draw
        surface.setFill(getColor());
        surface.fillPolygon(xPoints, yPoints, 4);

        surface.setLineWidth(2.0);
        surface.setStroke(theGrid.getColor());
        surface.strokePolygon(xPoints, yPoints, 4);

    }

    @Override
    public Entity copy()
    {
        return(new Sensor(getX(), getY(), getType()));
    }


}
