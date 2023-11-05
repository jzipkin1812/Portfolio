package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.ArrayList;

public class Grid
{
    private int size;
    private Paint color;
    private double smallBound;
    private double largeBound;

    public Grid(int size, Paint color)
    {
        this.size = size;
        this.color = color;
        smallBound = 400 - 85 * (size / 2.0);
        largeBound = 400 + 85 * (size / 2.0);
    }

    public void draw(GraphicsContext surface)
    {
        //set color and thickness
        surface.setStroke(color);
        surface.setLineWidth(2.0);

        //draw a grid based on the size, from X 60-740 and Y 60 - 760
        for(double x = smallBound; x <= largeBound ; x += 85.0)
        {
            surface.strokeLine(x, smallBound, x, largeBound);
        }
        //now horizontal lines
        for(double y = smallBound; y <= largeBound; y += 85.0)
        {
            surface.strokeLine(smallBound, y, largeBound, y);
        }
    }

    public void minimalDraw(GraphicsContext surface)
    {
        //set color and thickness
        surface.setStroke(color);
        surface.setLineWidth(2.0);

        surface.strokeLine(smallBound, smallBound, smallBound, largeBound);
        surface.strokeLine(largeBound, smallBound, largeBound, largeBound);
        surface.strokeLine(smallBound, smallBound, largeBound, smallBound);
        surface.strokeLine(smallBound, largeBound, largeBound, largeBound);
    }

    public int getSize()
    {
        return size;
    }

    public double getSmallBound()
    {
        return smallBound;
    }

    public double getLargeBound()
    {
        return largeBound;
    }

    public Paint getColor()
    {
        return color;
    }

    public void setColor(Paint value)
    {
        color = value;
    }



}
